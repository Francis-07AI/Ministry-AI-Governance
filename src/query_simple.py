"""Simplified RAG query system using keyword matching."""

import json
from typing import List, Dict, Any
from anthropic import Anthropic
from src.utils import (
    get_api_key, 
    detect_risk_flags, 
    sanitize_query, 
    format_sources, 
    add_disclaimers
)

class SimpleRAGSystem:
    """Simple RAG system using keyword matching instead of embeddings."""
    
    def __init__(self, knowledge_base_file: str = "data/processed/knowledge_base_simple.json"):
        """Initialize the query system."""
        self.anthropic_client = Anthropic(api_key=get_api_key("anthropic"))
        self.knowledge_base = self.load_knowledge_base(knowledge_base_file)
        
    def load_knowledge_base(self, file_path: str) -> List[Dict[str, Any]]:
        """Load the processed knowledge base."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Knowledge base not found at {file_path}")
            print("Run ingestion first: python -m src.ingest_simple")
            return []
    
    def keyword_match_score(self, query: str, chunk: Dict[str, Any]) -> float:
        """Calculate keyword match score between query and chunk."""
        query_words = set(query.lower().split())
        chunk_keywords = set(chunk.get('keywords', []))
        
        # Count matching keywords
        matches = query_words.intersection(chunk_keywords)
        
        if not chunk_keywords:
            return 0.0
        
        # Calculate score as ratio of matches
        score = len(matches) / max(len(query_words), len(chunk_keywords))
        
        # Boost score if query words appear in chunk text
        chunk_text_lower = chunk['text'].lower()
        for word in query_words:
            if word in chunk_text_lower:
                score += 0.1
        
        return min(score, 1.0)
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve most relevant chunks using keyword matching."""
        if not self.knowledge_base:
            return []
        
        # Score all chunks
        scored_chunks = []
        for chunk in self.knowledge_base:
            score = self.keyword_match_score(query, chunk)
            if score > 0:
                scored_chunks.append({
                    'chunk': chunk,
                    'score': score
                })
        
        # Sort by score and get top K
        scored_chunks.sort(key=lambda x: x['score'], reverse=True)
        return [item['chunk'] for item in scored_chunks[:top_k]]
    
    def build_prompt(self, query: str, context_chunks: List[Dict[str, Any]], risk_flags: List[str]) -> str:
        """Build the prompt for Claude."""
        # Build context from retrieved chunks
        context = ""
        for i, chunk in enumerate(context_chunks, 1):
            context += f"\n[Source {i}: {chunk['title']}]\n{chunk['text']}\n"
        
        # Check if query should be refused
        should_refuse = any(flag in ["PASTORAL_CARE", "THEOLOGICAL", "PASTORAL_CONTENT"] 
                           for flag in risk_flags)
        
        if should_refuse:
            refusal_instruction = """
IMPORTANT: This query is outside the system scope. Politely refuse and explain why, 
then suggest appropriate alternatives like consulting pastors, counselors, or denominational resources.
"""
        else:
            refusal_instruction = ""
        
        prompt = f"""You are a helpful assistant providing guidance on AI adoption for churches and ministries.

{refusal_instruction}

Context from knowledge base:
{context}

User Question: {query}

Instructions:
- Use ONLY the provided context to answer
- Cite sources for claims using format: [Source N]
- If the answer is not in the context, say so clearly
- Include appropriate disclaimers for sensitive topics
- Recommend consulting experts for implementation
- Do NOT provide theological or pastoral counseling advice
- Keep responses practical and actionable

Response:"""
        
        return prompt
    
    def generate_response(self, prompt: str) -> str:
        """Generate response using Claude."""
        response = self.anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text
    
    def query(self, user_query: str) -> Dict[str, Any]:
        """Process a user query and return response."""
        # Sanitize query
        sanitized = sanitize_query(user_query)
        
        # Detect risk flags
        risk_flags = detect_risk_flags(sanitized)
        
        # Retrieve relevant chunks
        relevant_chunks = self.retrieve_relevant_chunks(sanitized)
        
        # Build prompt
        prompt = self.build_prompt(sanitized, relevant_chunks, risk_flags)
        
        # Generate response
        response = self.generate_response(prompt)
        
        # Format sources
        sources = []
        seen_titles = set()
        for chunk in relevant_chunks:
            title = chunk['title']
            if title not in seen_titles:
                sources.append({
                    'title': title,
                    'url': chunk['url']
                })
                seen_titles.add(title)
        
        sources_formatted = format_sources(sources)
        
        # Add disclaimers
        final_response = add_disclaimers(response + sources_formatted, risk_flags)
        
        return {
            'query': user_query,
            'response': final_response,
            'risk_flags': risk_flags,
            'sources_used': len(relevant_chunks)
        }

def main():
    """Interactive query demo."""
    print("Ministry AI Governance Assistant - Simple Query System")
    print("=" * 60)
    
    # Initialize system
    rag = SimpleRAGSystem()
    
    if not rag.knowledge_base:
        print("\nNo knowledge base found. Please run ingestion first.")
        print("Run: python -m src.ingest_simple")
        return
    
    print(f"\nKnowledge base loaded: {len(rag.knowledge_base)} chunks")
    print("\nEnter your query (or 'quit' to exit):\n")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input.strip():
            continue
        
        # Process query
        print("\nProcessing...\n")
        result = rag.query(user_input)
        
        # Display result
        print(result['response'])
        print(f"\n[Risk flags: {', '.join(result['risk_flags']) if result['risk_flags'] else 'None'}]")
        print(f"[Sources used: {result['sources_used']}]")
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()