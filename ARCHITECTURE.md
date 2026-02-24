# Architecture: Ministry AI Governance Assistant

**Version:** 0.1.0  
**Last Updated:** February 2026  
**Status:** Planning Phase

---

## 1. System Overview

### High-Level Description

The Ministry AI Governance Assistant is a **Retrieval-Augmented Generation (RAG)** system that helps church leaders understand AI best practices by retrieving relevant information from a curated knowledge base and generating contextually appropriate responses.

### Design Principles

1. **Governance-First:** Safety and ethical boundaries built into architecture
2. **Transparency:** All sources cited, all decisions logged
3. **Simplicity:** Minimal dependencies, clear data flow
4. **Auditability:** Every interaction traceable
5. **Privacy-Preserving:** No user data collection beyond minimal logs

---

## 2. System Architecture

### Architecture Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                          USER                                │
└─────────────────────┬───────────────────────────────────────┘
                      │ Query
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   QUERY PROCESSOR                            │
│  - Input validation                                          │
│  - PII detection & sanitization                              │
│  - Risk flag detection                                       │
└─────────────────────┬───────────────────────────────────────┘
                      │ Sanitized Query + Risk Flags
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   RAG PIPELINE                               │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   RETRIEVAL  │→ │  RERANKING   │→ │  GENERATION  │     │
│  │              │  │              │  │              │     │
│  │ - Embedding  │  │ - Relevance  │  │ - LLM Call   │     │
│  │ - Vector DB  │  │ - Top-K      │  │ - Prompting  │     │
│  │ - Search     │  │ - Filtering  │  │ - Citation   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
└─────────────────────┬───────────────────────────────────────┘
                      │ Response + Sources
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                 RESPONSE VALIDATOR                           │
│  - Citation verification                                     │
│  - Disclaimer addition                                       │
│  - Risk flag handling                                        │
└─────────────────────┬───────────────────────────────────────┘
                      │ Final Response
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    AUDIT LOGGER                              │
│  - Query logging (sanitized)                                 │
│  - Source tracking                                           │
│  - Risk flag recording                                       │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                      USER                                    │
│              (receives response)                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Component Details

### 3.1 Knowledge Base

**Purpose:** Store and index curated source documents

**Components:**
- **Document Store:** Raw source documents (markdown/text)
- **Chunk Store:** Segmented text chunks (optimal size for retrieval)
- **Vector Store:** Embeddings for semantic search
- **Metadata Store:** Source attribution, dates, categories

**Implementation Options:**

**Option A: Simple File-Based (Current Phase)**
```
data/
├── sources/
│   ├── raw/
│   │   ├── anthropic_rsp.md
│   │   ├── nist_ai_rmf.md
│   │   └── ...
│   └── processed/
│       ├── chunks.json
│       └── metadata.json
```

**Option B: Vector Database (Future)**
- **ChromaDB:** Lightweight, embedded vector database
- **FAISS:** Facebook AI similarity search library
- **Pinecone:** Managed vector database (if scaling)

**Chunking Strategy:**
- **Chunk Size:** 512 tokens (balance between context and specificity)
- **Overlap:** 50 tokens (maintain context across boundaries)
- **Method:** Semantic chunking (respect paragraph/section boundaries)

---

### 3.2 Query Processor

**Purpose:** Validate, sanitize, and classify incoming queries

**Functions:**

1. **Input Validation**
   - Length checks (min/max characters)
   - Format validation
   - Encoding verification

2. **PII Detection**
   - Regex patterns for emails, phones, SSNs
   - Named entity recognition (NER) for names
   - Pattern matching for addresses

3. **Risk Flag Detection**
   - Keyword matching (child, minor, counseling, etc.)
   - Pattern recognition for harmful requests
   - Context analysis for boundary violations

**Risk Flags Defined:**
```python
RISK_FLAGS = {
    "PASTORAL_CARE": ["counseling", "therapy", "depression", "suicide"],
    "CHILD_SAFETY": ["child", "minor", "youth", "kid", "teen"],
    "FINANCIAL_MANIPULATION": ["donor targeting", "giving patterns", "maximize donations"],
    "DATA_BOUNDARY": ["analyze our database", "member data", "private information"],
    "THEOLOGICAL": ["should we believe", "is it biblical", "theological position"],
    "PASTORAL_CONTENT": ["write sermon", "create prayer", "generate liturgy"]
}
```

---

### 3.3 RAG Pipeline

**Purpose:** Retrieve relevant context and generate responses

#### 3.3.1 Retrieval Component

**Input:** User query (sanitized)  
**Output:** Top-K relevant document chunks

**Process:**
1. Query embedding generation
2. Similarity search in vector store
3. Retrieve top 5-10 most relevant chunks
4. Include metadata (source, section, date)

**Embedding Model Options:**
- **sentence-transformers/all-MiniLM-L6-v2:** Fast, good quality (default)
- **text-embedding-ada-002:** OpenAI embedding API
- **bge-base-en-v1.5:** High quality, open source

#### 3.3.2 Reranking Component

**Input:** Retrieved chunks  
**Output:** Reordered, filtered chunks

**Process:**
1. Score relevance to original query
2. Remove duplicates or near-duplicates
3. Filter out low-relevance chunks (threshold: 0.6)
4. Order by relevance score
5. Limit to top 3-5 chunks for context window

#### 3.3.3 Generation Component

**Input:** Query + Retrieved context  
**Output:** Generated response with citations

**LLM Options:**
- **Claude 3.5 Sonnet:** High quality, safety-focused (recommended)
- **GPT-4:** Strong performance, widely available
- **Open source:** Llama 3, Mistral (if local deployment needed)

**Prompt Structure:**
```
You are a helpful assistant providing guidance on AI adoption for churches.
Use ONLY the provided context to answer. If the answer isn't in the context, say so.

Context:
[Retrieved chunks with source citations]

User Question: [Query]

Instructions:
- Cite sources for all claims using format: [Source Name, Section]
- Include disclaimer if answer touches on sensitive topics
- Recommend consulting experts for implementation
- Do not provide theological or pastoral counseling advice

Response:
```

---

### 3.4 Response Validator

**Purpose:** Ensure response quality and safety

**Validation Checks:**

1. **Citation Verification**
   - Every factual claim has a source
   - Citations match retrieved documents
   - No hallucinated sources

2. **Disclaimer Addition**
   - Risk flags trigger appropriate disclaimers
   - General disclaimer for all responses
   - Consultation recommendations

3. **Refusal Handling**
   - Hard refusals for harmful queries
   - Explanation of why request is out of scope
   - Alternative resource suggestions

**Disclaimer Templates:**
```
GENERAL: "This guidance is for informational purposes. Consult your denominational resources and professional advisors."

PASTORAL_CARE: "This system cannot provide counseling. Please consult a qualified pastoral counselor or mental health professional."

CHILD_SAFETY: "Questions involving children require expert guidance. Consult child protection specialists and legal counsel."
```

---

### 3.5 Audit Logger

**Purpose:** Track all interactions for safety monitoring

**Log Format:**
```json
{
  "timestamp": "2026-02-06T14:30:00Z",
  "session_id": "anon_abc123",
  "query_sanitized": "What are AI best practices for churches?",
  "query_length": 45,
  "risk_flags": [],
  "retrieved_docs": ["doc_001", "doc_003", "doc_007"],
  "response_length": 450,
  "sources_cited": 3,
  "disclaimers_added": ["GENERAL"],
  "processing_time_ms": 1250
}
```

**Storage:**
- Location: `/logs/queries.jsonl`
- Retention: 90 days
- Access: Developer only
- Encryption: Not required (no PII, public sources)

---

## 4. Data Flow

### 4.1 Ingestion Pipeline (One-Time Setup)
```
[Source URLs] 
    → Download & verify
    → Parse & clean
    → Chunk into segments
    → Generate embeddings
    → Store in vector DB
    → Create metadata index
```

**Steps:**
1. Read SOURCE_LIST.md
2. For each source:
   - Fetch content
   - Extract text
   - Clean formatting
   - Segment into chunks
   - Generate embeddings
   - Store with metadata
3. Create searchable index

### 4.2 Query Pipeline (Runtime)
```
[User Query]
    → Sanitize & validate
    → Detect risk flags
    → Generate query embedding
    → Retrieve top chunks
    → Rerank by relevance
    → Construct prompt with context
    → Call LLM
    → Validate response
    → Add citations & disclaimers
    → Log interaction
    → Return to user
```

---

## 5. Technology Stack

### 5.1 Core Dependencies

**Python Ecosystem (Recommended):**
```
python >= 3.10
langchain >= 0.1.0        # RAG orchestration
chromadb >= 0.4.0         # Vector database
sentence-transformers     # Embeddings
anthropic                 # Claude API (or openai for GPT)
pydantic >= 2.0          # Data validation
```

**Alternative: JavaScript/TypeScript:**
```
node >= 18
@langchain/core
chromadb (JS client)
@anthropic-ai/sdk
zod                       # Validation
```

### 5.2 Development Tools
```
pytest                    # Testing
black / ruff              # Code formatting
mypy                      # Type checking
pre-commit               # Git hooks
```

### 5.3 Infrastructure

**Current Phase (Local Development):**
- Local Python environment
- File-based storage
- No external services

**Future Production Considerations:**
- Docker containerization
- API deployment (FastAPI/Flask)
- Managed vector DB (if scaling)
- Monitoring & observability

---

## 6. Governance Integration

### 6.1 Data Boundaries

**Enforcement Points:**
- Ingestion: Only sources in SOURCE_LIST.md
- Query: Reject queries requesting private data
- Retrieval: Only from approved knowledge base
- Logging: Sanitize before storage

### 6.2 Risk Flags

**Implementation:**
```python
def detect_risk_flags(query: str) -> List[str]:
    flags = []
    for flag_type, keywords in RISK_FLAGS.items():
        if any(keyword in query.lower() for keyword in keywords):
            flags.append(flag_type)
    return flags
```

**Actions on Flags:**
- Log flag activation
- Modify response generation prompt
- Add appropriate disclaimers
- Consider refusal for high-risk flags

### 6.3 Evaluation Harness

**Test Execution:**
```bash
# Run all test cases
pytest tests/test_prompts.py

# Run specific category
pytest tests/test_prompts.py::test_safe_queries
pytest tests/test_prompts.py::test_harmful_queries

# Generate test report
pytest --html=report.html
```

**Success Criteria:**
- 100% pass rate on harmful query refusals
- 100% citation accuracy on safe queries
- 0% hallucinated sources

---

## 7. Deployment Considerations

### 7.1 Deployment Options

**Option 1: Command-Line Interface (Simplest)**
```bash
python query.py "What are AI best practices for churches?"
```

**Option 2: Simple Web UI (Gradio/Streamlit)**
```python
import gradio as gr

def query_system(user_input):
    # RAG pipeline logic
    return response

gr.Interface(fn=query_system, inputs="text", outputs="text").launch()
```

**Option 3: REST API (Future)**
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/query")
def query_endpoint(query: str):
    # RAG pipeline logic
    return {"response": response, "sources": sources}
```

### 7.2 Performance Targets

**Acceptable for Demonstration:**
- Query response time: < 5 seconds
- Embedding generation: < 1 second
- Retrieval: < 500ms
- LLM call: < 3 seconds

**Production Targets (Future):**
- Query response time: < 2 seconds
- Concurrent queries: 10+ simultaneous
- Uptime: 99%+

### 7.3 Monitoring

**Metrics to Track:**
- Queries per day
- Average response time
- Risk flag frequency
- Citation accuracy rate
- Refusal rate by category

---

## 8. Security Architecture

### 8.1 Threat Model

**Threats:**
1. Prompt injection attempts
2. Data boundary violations
3. PII leakage in logs
4. Unauthorized access to system
5. Source poisoning

**Mitigations:**
1. Input validation & sanitization
2. Hard-coded data boundaries
3. Log sanitization
4. Local-only deployment (demo phase)
5. Manual source curation

### 8.2 Access Control

**Development Phase:**
- Single developer access
- Local machine only
- No network exposure

**Production Phase (Future):**
- Authentication required
- Role-based access control
- API key management
- Rate limiting

---

## 9. Scalability Considerations

### Current Scope (15 Sources)
- **Storage:** < 100MB
- **Memory:** < 2GB RAM
- **Compute:** Standard laptop sufficient

### Future Scaling (100+ Sources)
- **Vector DB:** Migrate to managed service
- **Caching:** Add Redis for frequent queries
- **Load Balancing:** Multiple RAG instances
- **Monitoring:** Prometheus + Grafana

---

## 10. Development Roadmap

### Phase 1: Foundation (Current - Day 1-7)
- [x] Project structure
- [x] Governance documentation
- [x] Source curation
- [ ] Basic RAG implementation

### Phase 2: Core Functionality (Days 8-14)
- [ ] Ingestion pipeline
- [ ] Query processing
- [ ] RAG pipeline
- [ ] Response validation

### Phase 3: Safety & Testing (Days 15-21)
- [ ] Risk flag implementation
- [ ] Evaluation harness execution
- [ ] Red-team testing
- [ ] Refinement based on tests

### Phase 4: Polish & Demo (Days 22-30)
- [ ] UI implementation (Gradio/Streamlit)
- [ ] Demo video creation
- [ ] Documentation finalization
- [ ] Public launch (LinkedIn post)

---

## 11. Alternative Architectures Considered

### Option A: Fine-Tuned Model
**Pros:** No retrieval needed, faster responses  
**Cons:** Expensive, hard to update, less transparent  
**Decision:** Not suitable for demonstration project

### Option B: Prompt-Only (No RAG)
**Pros:** Simplest implementation  
**Cons:** No source grounding, high hallucination risk  
**Decision:** Does not demonstrate governance capabilities

### Option C: Hybrid (RAG + Fine-Tuning)
**Pros:** Best of both worlds  
**Cons:** Complex, expensive, overkill for scope  
**Decision:** Too complex for 30-day timeline

**Selected: Pure RAG Architecture**
- Transparent and auditable
- Easy to update knowledge base
- Strong source attribution
- Appropriate complexity for demonstration

---

## 12. Open Questions & Decisions Needed

### Technical Decisions
- [ ] Choose vector database (ChromaDB vs FAISS)
- [ ] Choose LLM provider (Claude vs GPT-4)
- [ ] Choose embedding model
- [ ] Decide on UI approach (CLI vs Gradio vs Streamlit)

### Implementation Decisions
- [ ] Chunking strategy details
- [ ] Exact prompt template
- [ ] Response length limits
- [ ] Reranking algorithm

### Testing Decisions
- [ ] Automated vs manual test execution
- [ ] Frequency of test suite runs
- [ ] Threshold for acceptable performance

---

## 13. Success Criteria

**System is ready for demonstration when:**

1. **Functionality:**
   - Answers safe queries with citations
   - Refuses harmful queries appropriately
   - Passes 100% of test suite

2. **Governance:**
   - All policies documented
   - Risk flags operational
   - Audit logging functional

3. **Documentation:**
   - Architecture documented (this file)
   - README complete
   - Governance pack finalized

4. **Demonstration:**
   - Demo script prepared
   - Screenshots/video captured
   - GitHub polished

---

**Document Status:** Living document, updated as architecture evolves  
**Next Update:** Upon implementation decisions and testing results