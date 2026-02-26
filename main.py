"""Main CLI interface for the Ministry AI Governance Assistant."""

import argparse
from src.query import RAGQuerySystem

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Ministry AI Governance Assistant - Query Interface"
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="Your question about AI adoption in ministry"
    )
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Start interactive mode"
    )
    
    args = parser.parse_args()
    
    # Initialize RAG system
    print("Loading Ministry AI Governance Assistant...")
    rag = RAGQuerySystem()
    
    if not rag.knowledge_base:
        print("\nERROR: No knowledge base found.")
        print("Please run ingestion first:")
        print("  python -m src.ingest")
        return
    
    print(f"Knowledge base loaded: {len(rag.knowledge_base)} chunks\n")
    
    # Interactive mode
    if args.interactive or not args.query:
        print("=" * 60)
        print("Ministry AI Governance Assistant - Interactive Mode")
        print("=" * 60)
        print("\nAsk questions about ethical AI adoption in ministry.")
        print("Type 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("> ")
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye!")
                    break
                
                if not user_input.strip():
                    continue
                
                # Process query
                print("\nProcessing...\n")
                result = rag.query(user_input)
                
                # Display result
                print(result['response'])
                
                if result['risk_flags']:
                    print(f"\nRisk flags detected: {', '.join(result['risk_flags'])}")
                
                print(f"Sources used: {result['sources_used']}")
                print("\n" + "=" * 60 + "\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}\n")
    
    # Single query mode
    else:
        result = rag.query(args.query)
        print(result['response'])
        
        if result['risk_flags']:
            print(f"\nRisk flags: {', '.join(result['risk_flags'])}")

if __name__ == "__main__":
    main()