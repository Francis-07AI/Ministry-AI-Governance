"""Mock RAG query system for demo without API costs."""

import json
from typing import List, Dict, Any
from src.utils import (
    detect_risk_flags, 
    sanitize_query, 
    format_sources, 
    add_disclaimers
)

class MockRAGSystem:
    """Mock RAG system for demo purposes without API calls."""
    
    def __init__(self, knowledge_base_file: str = "data/processed/knowledge_base_simple.json"):
        """Initialize the query system."""
        self.knowledge_base = self.load_knowledge_base(knowledge_base_file)
        
        # Pre-written mock responses for common queries
        self.mock_responses = {
            "safe": """Based on the guidance from our sources, here are key best practices for AI adoption in ministry contexts:

1. Start with low-risk administrative tasks like scheduling and communication organization [Source 3]

2. Implement appropriate safeguards that scale with the AI capabilities being used [Source 1]

3. Conduct risk assessments before deployment and maintain audit trails [Source 2]

4. Never input private member information into AI tools and obtain consent before using personal data [Source 3]

5. Provide staff training on AI tools and ethics, and establish clear usage policies [Source 3]

The key principle is maintaining authentic human relationships while using AI as a tool for administrative efficiency, not as a replacement for pastoral ministry.""",
            
            "child_safety": """This query involves child safety considerations, which require expert guidance beyond this system's scope.

For questions involving children and AI tools, you should:
- Consult child protection specialists
- Review your denominational child safety policies
- Seek legal counsel familiar with child data protection laws
- Ensure proper background checks and oversight

General principles from the sources indicate that any AI applications involving minors require parental consent, the two-person rule, and no biometric data collection [Source 3].""",
            
            "pastoral_care": """This system cannot provide counseling or pastoral care guidance.

Pastoral counseling requires human empathy, theological training, relational context, and spiritual discernment that AI cannot provide.

For pastoral care situations, please consult:
- Qualified pastoral counselors
- Mental health professionals
- Your denominational pastoral care resources
- Licensed therapists with experience in faith-based counseling""",
            
            "theological": """This system does not provide theological or doctrinal guidance.

Theological questions require pastoral wisdom, denominational context, and spiritual discernment.

Please consult:
- Your pastor or church leadership
- Denominational theological resources
- Seminary-trained theologians
- Your church's statement of faith""",
            
            "default": """Based on the available sources, I can provide some general guidance on AI adoption for ministries.

The key frameworks emphasize:
- Risk assessment before deployment [Source 2]
- Graduated safeguards that scale with capabilities [Source 1]  
- Transparency and accountability [Sources 1, 2, 3]
- Privacy protection and data governance [Source 3]

For specific implementation, I recommend consulting your denominational technology resources and professional advisors."""
        }
        
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
        """Calculate keyword match score."""
        query_words = set(query.lower().split())
        chunk_keywords = set(chunk.get('keywords', []))
        
        matches = query_words.intersection(chunk_keywords)
        
        if not chunk_keywords:
            return 0.0
        
        score = len(matches) / max(len(query_words), len(chunk_keywords))
        
        chunk_text_lower = chunk['text'].lower()
        for word in query_words:
            if word in chunk_text_lower:
                score += 0.1
        
        return min(score, 1.0)
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve most relevant chunks."""
        if not self.knowledge_base:
            return []
        
        scored_chunks = []
        for chunk in self.knowledge_base:
            score = self.keyword_match_score(query, chunk)
            if score > 0:
                scored_chunks.append({
                    'chunk': chunk,
                    'score': score
                })
        
        scored_chunks.sort(key=lambda x: x['score'], reverse=True)
        return [item['chunk'] for item in scored_chunks[:top_k]]
    
    def select_mock_response(self, risk_flags: List[str]) -> str:
        """Select appropriate mock response based on risk flags."""
        if "CHILD_SAFETY" in risk_flags:
            return self.mock_responses["child_safety"]
        elif "PASTORAL_CARE" in risk_flags:
            return self.mock_responses["pastoral_care"]
        elif "THEOLOGICAL" in risk_flags or "PASTORAL_CONTENT" in risk_flags:
            return self.mock_responses["theological"]
        elif not risk_flags:
            return self.mock_responses["safe"]
        else:
            return self.mock_responses["default"]
    
    def query(self, user_query: str) -> Dict[str, Any]:
        """Process a user query and return mock response."""
        # Sanitize query
        sanitized = sanitize_query(user_query)
        
        # Detect risk flags
        risk_flags = detect_risk_flags(sanitized)
        
        # Retrieve relevant chunks for source citations
        relevant_chunks = self.retrieve_relevant_chunks(sanitized)
        
        # Select appropriate mock response
        response = self.select_mock_response(risk_flags)
        
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
            'sources_used': len(relevant_chunks),
            'mode': 'MOCK DEMO - No API calls made'
        }

def main():
    """Interactive query demo."""
    print("Ministry AI Governance Assistant - Mock Demo Mode")
    print("=" * 60)
    print("NOTE: This is a demo mode with pre-written responses")
    print("=" * 60)
    
    rag = MockRAGSystem()
    
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
        
        print("\nProcessing (mock mode)...\n")
        result = rag.query(user_input)
        
        print(result['response'])
        print(f"\n[Mode: {result['mode']}]")
        print(f"[Risk flags: {', '.join(result['risk_flags']) if result['risk_flags'] else 'None'}]")
        print(f"[Sources used: {result['sources_used']}]")
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()