"""Mock main CLI interface - zero API costs."""

import argparse
from src.query_mock import MockRAGSystem

def main():
    """Main entry point for the mock demo CLI."""
    parser = argparse.ArgumentParser(
        description="Ministry AI Governance Assistant - Mock Demo (No API Costs)"
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
    
    # Initialize mock RAG system
    print("Loading Ministry AI Governance Assistant (Mock Demo Mode)...")
    print("NOTE: Using pre-written responses - no API calls made\n")
    
    rag = MockRAGSystem()
    
    if not rag.knowledge_base:
        print("\nERROR: No knowledge base found.")
        print("Please run ingestion first:")
        print("  python -m src.ingest_simple")
        return
    
    print(f"Knowledge base loaded: {len(rag.knowledge_base)} chunks\n")
    
    # Interactive mode
    if args.interactive or not args.query:
        print("=" * 60)
        print("Ministry AI Governance Assistant - Mock Demo")
        print("=" * 60)
        print("\nThis demo shows governance features without API costs.")
        print("Ask questions about ethical AI adoption in ministry.")
        print("Type 'quit' to exit.\n")
        
        print("Try these example queries:")
        print("  - What are best practices for using AI in churches?")
        print("  - Can we use AI for pastoral counseling?")
        print("  - How should we handle AI tools with children?")
        print("  - Should AI write our sermons?\n")
        
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
                print(f"\n[{result['mode']}]")
                
                if result['risk_flags']:
                    print(f"[Risk flags detected: {', '.join(result['risk_flags'])}]")
                
                print(f"[Sources used: {result['sources_used']}]")
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
        print(f"\n[{result['mode']}]")
        
        if result['risk_flags']:
            print(f"[Risk flags: {', '.join(result['risk_flags'])}]")

if __name__ == "__main__":
    main()