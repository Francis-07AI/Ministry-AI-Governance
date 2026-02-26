"""Document ingestion pipeline for the Ministry AI Governance Assistant."""

import os
import json
import requests
from typing import List, Dict, Any
from bs4 import BeautifulSoup
from openai import OpenAI
from src.utils import get_api_key

class DocumentIngester:
    """Handles document ingestion, chunking, and embedding."""
    
    def __init__(self):
        """Initialize the ingester."""
        self.client = OpenAI(api_key=get_api_key("openai"))
        self.chunks = []
        self.embeddings = []
        
    def load_sources(self, source_file: str = "data/sources/SOURCE_LIST.md") -> List[Dict[str, str]]:
        """Parse SOURCE_LIST.md to extract source URLs."""
        sources = []
        
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Simple parsing - look for URL patterns
        lines = content.split('\n')
        current_source = {}
        
        for line in lines:
            if line.startswith('###'):
                # New source entry
                if current_source:
                    sources.append(current_source)
                current_source = {'title': line.replace('###', '').strip()}
                
            elif '**URL:**' in line:
                url = line.split('**URL:**')[1].strip()
                current_source['url'] = url
                
            elif '**Type:**' in line:
                source_type = line.split('**Type:**')[1].strip()
                current_source['type'] = source_type
        
        # Add last source
        if current_source:
            sources.append(current_source)
        
        return sources
    
    def fetch_content(self, url: str) -> str:
        """Fetch content from URL."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
            
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""
    
    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """Split text into overlapping chunks."""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            if chunk:
                chunks.append(chunk)
        
        return chunks
    
    def create_embedding(self, text: str) -> List[float]:
        """Create embedding for text using OpenAI."""
        try:
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error creating embedding: {e}")
            return []
    
    def ingest_document(self, title: str, url: str, doc_type: str = "article"):
        """Ingest a single document."""
        print(f"Ingesting: {title}")
        
        # Fetch content
        content = self.fetch_content(url)
        if not content:
            print(f"  Skipped - no content")
            return
        
        # Chunk text
        text_chunks = self.chunk_text(content)
        print(f"  Created {len(text_chunks)} chunks")
        
        # Create embeddings and store
        for i, chunk in enumerate(text_chunks):
            embedding = self.create_embedding(chunk)
            if embedding:
                self.chunks.append({
                    'title': title,
                    'url': url,
                    'type': doc_type,
                    'chunk_id': i,
                    'text': chunk,
                    'embedding': embedding
                })
        
        print(f"  Completed")
    
    def save_knowledge_base(self, output_file: str = "data/processed/knowledge_base.json"):
        """Save processed chunks and embeddings to JSON."""
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.chunks, f, indent=2)
        
        print(f"\nKnowledge base saved: {len(self.chunks)} chunks")
        print(f"Location: {output_file}")

def main():
    """Main ingestion pipeline."""
    print("Starting document ingestion...")
    
    ingester = DocumentIngester()
    
    # Load sources from SOURCE_LIST.md
    sources = ingester.load_sources()
    print(f"Found {len(sources)} sources to ingest\n")
    
    # For demo, limit to first 3 sources to save API costs
    # Remove [:3] to process all sources
    for source in sources[:3]:
        if 'url' in source:
            ingester.ingest_document(
                title=source.get('title', 'Unknown'),
                url=source['url'],
                doc_type=source.get('type', 'article')
            )
    
    # Save knowledge base
    ingester.save_knowledge_base()
    
    print("\nIngestion complete!")

if __name__ == "__main__":
    main()