"""Simplified document ingestion without embeddings."""

import os
import json
from typing import List, Dict, Any

class SimpleIngester:
    """Simple text-based ingestion without embeddings."""
    
    def __init__(self):
        """Initialize the ingester."""
        self.chunks = []
        
    def load_text_file(self, filepath: str) -> str:
        """Load content from a text file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        """Split text into chunks by words."""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)
        
        return chunks
    
    def extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords from text."""
        # Convert to lowercase and split
        words = text.lower().split()
        
        # Remove common stopwords
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'by', 'from', 'as', 'is', 'are', 'was', 'were', 'be', 
                     'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                     'would', 'should', 'could', 'may', 'might', 'must', 'can', 'this',
                     'that', 'these', 'those', 'it', 'its', 'they', 'their', 'them'}
        
        # Filter out stopwords and short words
        keywords = [w for w in words if w not in stopwords and len(w) > 3]
        
        # Get unique keywords
        return list(set(keywords))
    
    def ingest_document(self, title: str, filepath: str, url: str = ""):
        """Ingest a single document."""
        print(f"Ingesting: {title}")
        
        # Load content
        content = self.load_text_file(filepath)
        
        # Chunk text
        text_chunks = self.chunk_text(content)
        print(f"  Created {len(text_chunks)} chunks")
        
        # Store chunks with metadata
        for i, chunk in enumerate(text_chunks):
            keywords = self.extract_keywords(chunk)
            
            self.chunks.append({
                'title': title,
                'url': url,
                'chunk_id': i,
                'text': chunk,
                'keywords': keywords
            })
        
        print(f"  Completed")
    
    def save_knowledge_base(self, output_file: str = "data/processed/knowledge_base_simple.json"):
        """Save processed chunks to JSON."""
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.chunks, f, indent=2)
        
        print(f"\nKnowledge base saved: {len(self.chunks)} chunks")
        print(f"Location: {output_file}")

def main():
    """Main ingestion pipeline."""
    print("Starting simplified document ingestion...\n")
    
    ingester = SimpleIngester()
    
    # Define sources
    sources = [
        {
            'title': 'Anthropic Responsible Scaling Policy',
            'filepath': 'data/sources/raw/anthropic_rsp.txt',
            'url': 'https://www.anthropic.com/news/anthropics-responsible-scaling-policy'
        },
        {
            'title': 'NIST AI Risk Management Framework',
            'filepath': 'data/sources/raw/nist_ai_rmf.txt',
            'url': 'https://www.nist.gov/itl/ai-risk-management-framework'
        },
        {
            'title': 'Church AI Best Practices',
            'filepath': 'data/sources/raw/church_ai_best_practices.txt',
            'url': 'Various denominational guidelines'
        }
    ]
    
    # Ingest each source
    for source in sources:
        ingester.ingest_document(
            title=source['title'],
            filepath=source['filepath'],
            url=source['url']
        )
    
    # Save knowledge base
    ingester.save_knowledge_base()
    
    print("\nIngestion complete!")
    print("You can now run queries: python main_simple.py")

if __name__ == "__main__":
    main()