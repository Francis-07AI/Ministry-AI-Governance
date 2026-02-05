# Ministry AI Governance Assistant

A governance-ready RAG system helping church leaders adopt AI ethically and safely.

**Project Status:** Foundation Phase (Week 1)  
**Built by:** Francis | MS AI/ML | Governance-Aware Applied AI Engineer

---

## What This Is NOT

- NOT a replacement for pastoral judgment or wisdom
- NOT providing theological or doctrinal advice  
- NOT accessing your church's private data
- NOT production-ready (this is a portfolio demonstration)

---

## What This IS

A reference implementation showing how to build governance-ready AI systems for faith-based organizations.

### Governance Features Demonstrated:

- **Source Citations** - Every answer is traceable to original sources  
- **Risk Flagging** - Automatically highlights ethical/privacy concerns  
- **Audit Logging** - Track all queries for accountability  
- **Evaluation Harness** - Safety testing before deployment  
- **Data Boundaries** - Only approved, public sources (no private church data)

---

## Target Use Cases

### Appropriate Questions:

- "What are best practices for using AI in sermon preparation?"
- "What privacy concerns should we consider with church management software?"
- "How can we use AI for administrative tasks ethically?"
- "What are the risks of using AI for pastoral communications?"

### Out of Scope:

- Theological/doctrinal questions → Consult your pastor or denomination
- Personal counseling situations → Seek qualified pastoral care
- Questions about specific church members → Privacy violation
- Requests to generate sermons/prayers → Requires human pastoral discernment

---

## Architecture
```
ministry-ai-governance/
├── data/
│   ├── sources/          # Curated public AI ethics + ministry tech resources
│   └── processed/        # Embedded/indexed documents
├── docs/governance-pack/ # Templates for church AI adoption
│   ├── SYSTEM_CARD.md   # What the system does/doesn't do
│   ├── DATA_POLICY.md   # Data boundaries and privacy rules
│   └── RISK_CHECKLIST.md # Ethical risk assessment
├── eval/                 # Safety testing & red-team prompts
│   └── test_prompts.md  # Test cases for inappropriate queries
├── logs/                 # Query audit trail
└── src/                  # Implementation (RAG pipeline)
```

---

## Governance Implementation

### 1. Data Boundaries (Privacy-First)

**Allowed Sources:**
- Public AI ethics documentation (Anthropic, OpenAI guidelines)
- Church technology best practices (blogs, guides)
- Ministry-focused privacy frameworks
- Published case studies

**Forbidden (Hard Exclusions):**
- Private church member data
- Pastoral counseling session notes  
- Donation records with PII
- Internal church conflict documentation
- Anything involving identifiable minors

### 2. Risk Flagging System

Queries automatically trigger warnings for:
- **Child safety scenarios** (mandatory human review)
- **Financial manipulation** (donor targeting, deceptive fundraising)
- **Pastoral care replacement** (AI cannot replace human ministry)
- **Privacy violations** (member data, confidential communications)

### 3. Audit Logging

Every interaction logs:
- Timestamp
- Query text (sanitized)
- Sources retrieved
- Response length
- Risk flags triggered

### 4. Evaluation Harness

**Test Categories:**
- Safe queries (should answer confidently)
- Edge cases (should answer with caveats)
- Harmful queries (should refuse with explanation)

---

## Sample Outputs

### Example 1: Safe Query

**Question:** "Can we use AI to help with sermon research?"

**Answer:** Yes, AI can be a helpful research assistant for sermon preparation. Here are best practices:

1. **Use AI for research aggregation** (gathering commentaries, cross-references, historical context)
2. **Maintain pastoral discernment** (AI suggestions must be reviewed for theological accuracy)
3. **Cite sources properly** (if using AI-generated insights, verify and attribute correctly)
4. **Avoid plagiarism** (don't pass off AI-generated content as original sermon material)

**Sources:**  
- "AI in Ministry: Best Practices" (Church Tech Today, 2024)
- "Ethical AI Use for Pastors" (Faith & Technology Institute, 2024)

**Reminder:** This is guidance, not theological advice. Consult your denomination's standards.

---

### Example 2: Flagged Query

**Question:** "Should we use AI to handle pastoral counseling sessions?"

**Answer:** **This use case is NOT appropriate.**

**Why:**
- Pastoral counseling requires human empathy, spiritual discernment, and confidentiality
- AI cannot provide the relational trust essential to pastoral care
- Privacy risks: Counseling content should never be sent to external AI systems
- Liability concerns: Misadvice could cause spiritual or emotional harm

**Alternative:** Use AI only for administrative counseling tasks (scheduling, resource suggestions), never for the counseling itself.

**Sources:**  
- "When NOT to Use AI in Ministry" (Ministry Safe, 2024)
- "AI and Pastoral Ethics" (Association of Church Technology, 2024)

**Critical:** If someone is in crisis, connect them with a qualified human counselor immediately.

---

## Roadmap

### Phase 1 (Current): Foundation
- [x] Project scope defined
- [x] Folder structure created
- [ ] Data sources curated (15-20 documents)
- [ ] Basic RAG implementation
- [ ] System card written

### Phase 2 (Week 2): Governance Controls
- [ ] Audit logging implemented
- [ ] Risk flagging system
- [ ] Evaluation harness with test prompts
- [ ] Data policy documented

### Phase 3 (Week 3): Red-Team Testing
- [ ] Edge case testing (theological, ethical, privacy)
- [ ] Red-team prompt set (harmful queries)
- [ ] Refusal handling validated

### Phase 4 (Week 4): Packaging & Publishing
- [ ] Demo video/screenshots
- [ ] LinkedIn case study post
- [ ] GitHub polish (badges, documentation)
- [ ] Outreach to church tech communities

---

## Contributing

This is a portfolio project, but feedback is welcome! If you're a:
- **Church tech leader** → Let me know what features would be most helpful
- **AI governance practitioner** → Suggest improvements to controls
- **Ministry leader** → Share use cases I should test

---

## Contact

**Francis** - Governance-Aware Applied AI Engineer  
LinkedIn: [Add your link]  
GitHub: [Add your link]  
Email: [Add your email]

---

## License & Disclaimer

**License:** MIT (code) | CC BY 4.0 (documentation)

**Disclaimer:** This project is for educational and portfolio purposes. It demonstrates AI governance principles but is not intended for production use without:
- Proper security review
- Legal/compliance vetting
- Denominational approval
- Ongoing human oversight

**No Warranty:** This system provides guidance, not professional advice. Always consult qualified pastoral, legal, and technical experts for your specific context.

---

Last Updated: February 2026