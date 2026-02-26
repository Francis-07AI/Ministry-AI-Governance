"""RAG query system for the Ministry AI Governance Assistant."""

import json
import numpy as np
from typing import List, Dict, Any
from openai import OpenAI
from anthropic import Anthropic
from src.utils import (
    get_api_key, 
    detect_risk_flags, 
    sanitize_query, 
    format_sources, 
    add_disclaimers
)

class RAGQuerySystem:
    """Handles query processing and response generation."""
    
    def __init__(self, knowledge_base_file: str = "data/processed/knowledge_base.json"):
        """Initialize the query system."""
        self.openai_client = OpenAI(api_key=get_api_key("openai"))
        self.anthropic_client = Anthropic(api_key=get_api_key("anthropic"))
        self.knowledge_base = self.load_knowledge_base(knowledge_base_file)
        
    def load_knowledge_base(self, file_path: str) -> List[Dict[str, Any]]:
        """Load the processed knowledge base."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Knowledge base not found at {file_path}")
            print("Run ingestion first: python src/ingest.py")
            return []
    
    def create_query_embedding(self, query: str) -> List[float]:
        """Create embedding for the query."""
        response = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )
        return response.data[0].embedding
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve most relevant chunks for the query."""
        if not self.knowledge_base:
            return []
        
        # Create query embedding
        query_embedding = self.create_query_embedding(query)
        
        # Calculate similarities
        scored_chunks = []
        for chunk in self.knowledge_base:
            similarity = self.cosine_similarity(query_embedding, chunk['embedding'])
            scored_chunks.append({
                'chunk': chunk,
                'score': similarity
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
IMPORTANT: This query is outside the system's scope. Politely refuse and explain why, 
then suggest appropriate alternatives (consulting pastors, counselors, or denominational resources).
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
- Cite sources for all claims using format: [Source N]
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
        sources = [
            {
                'title': chunk['title'],
                'url': chunk['url']
            }
            for chunk in relevant_chunks
        ]
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
    print("Ministry AI Governance Assistant - Query System")
    print("=" * 50)
    
    # Initialize system
    rag = RAGQuerySystem()
    
    if not rag.knowledge_base:
        print("\nNo knowledge base found. Please run ingestion first.")
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
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()