# System Card: Ministry AI Governance Assistant

**Version:** 0.1.0  
**Last Updated:** February 2026  
**Status:** Development (Portfolio Demonstration)

---

## 1. System Overview

### Purpose
The Ministry AI Governance Assistant is a Retrieval-Augmented Generation (RAG) system designed to help church leaders and ministry staff understand best practices for integrating AI ethically and safely into their organizations.

### Primary Users
- Church pastors and leadership teams
- Ministry technology coordinators
- Church administrative staff
- Faith-based nonprofit leaders

### Use Case
Users can ask questions about AI adoption in ministry contexts and receive guidance based on curated, authoritative sources covering AI ethics, church technology best practices, and privacy/safety considerations.

---

## 2. System Capabilities

### What This System DOES:

**Provides Guidance On:**
- Ethical considerations for AI use in ministry settings
- Best practices for church AI adoption
- Privacy and data protection in church contexts
- Risk assessment for AI applications in ministry
- Child safety considerations when using AI tools
- Appropriate vs inappropriate uses of AI in pastoral work

**Technical Capabilities:**
- Retrieves relevant information from curated knowledge base
- Provides source citations for all responses
- Flags potentially risky queries
- Logs all interactions for audit purposes
- Operates within defined data boundaries

### What This System DOES NOT Do:

**Does NOT:**
- Provide theological or doctrinal advice
- Replace pastoral judgment or wisdom
- Access or process private church data
- Handle pastoral counseling situations
- Make decisions on behalf of church leadership
- Generate sermons, prayers, or liturgical content
- Process personally identifiable information (PII)
- Access real-time church management systems

---

## 3. Known Limitations

### Technical Limitations
- **Knowledge Cutoff:** System knowledge is limited to sources collected as of February 2026
- **Source Coverage:** Limited to 15 curated public sources; not comprehensive
- **Language:** English only
- **Domain Scope:** Focused on Christian ministry contexts (may not generalize to other faith traditions)

### Accuracy Limitations
- Responses depend on quality and coverage of source material
- May not capture nuances of specific denominational practices
- Cannot account for local laws, regulations, or cultural contexts
- Not a substitute for legal, professional, or denominational guidance

### Safety Limitations
- Cannot detect all potentially harmful use cases
- Risk flagging is based on pattern matching, not comprehensive threat modeling
- Does not include real-time monitoring of AI tool safety updates

---

## 4. Intended Use Cases

### Appropriate Use Cases

**Strategic Planning:**
- "What should we consider before adopting AI tools for church administration?"
- "What are the risks of using AI for member communications?"

**Policy Development:**
- "What privacy considerations should be in our AI use policy?"
- "How do we protect children when using AI-powered tools?"

**Education & Training:**
- "What do church staff need to know about AI ethics?"
- "How can we train volunteers on responsible AI use?"

**Tool Evaluation:**
- "What questions should we ask vendors about AI safety?"
- "How do we evaluate if an AI tool is appropriate for ministry?"

### Out-of-Scope Use Cases

**Theological/Doctrinal Questions:**
- Questions requiring biblical interpretation
- Denominational policy questions
- Spiritual counseling or pastoral care scenarios

**Operational Decisions:**
- Specific vendor recommendations or endorsements
- Budget allocation decisions
- Personnel hiring/firing decisions

**Technical Implementation:**
- Writing production code
- Configuring specific AI tools
- Troubleshooting technical issues

**Legal/Compliance:**
- Legal interpretations
- Compliance determinations
- Contract reviews

---

## 5. Data Handling

### Data Sources
**Ingested Knowledge Base:**
- 5 AI ethics and safety documents (Anthropic, NIST)
- 6 church technology best practice articles
- 4 child safety and data protection guides

**Source Characteristics:**
- All sources are publicly available
- No paywalled or proprietary content
- No private church data
- No personally identifiable information

### Data Boundaries

**What Data is ALLOWED:**
- Public AI ethics frameworks
- Published ministry technology guides
- General best practice documentation
- Non-confidential policy templates

**What Data is FORBIDDEN:**
- Church member information
- Donation records
- Pastoral counseling notes
- Internal church communications
- Child/youth identifiable information
- Financial account details

### Query Logging
- All queries are logged with timestamp
- Source documents retrieved are recorded
- No user identification beyond session ID
- Logs retained for 90 days
- Logs used only for system improvement

---

## 6. Risk Assessment

### Identified Risks

**High Priority Risks:**

1. **Misuse for Pastoral Care**
   - Risk: User attempts to get counseling advice
   - Mitigation: Clear disclaimers, refusal patterns, pastoral referral

2. **Child Safety Scenarios**
   - Risk: Queries involving minors without appropriate safeguards
   - Mitigation: Mandatory flagging, conservative response policies

3. **Privacy Violations**
   - Risk: User attempts to process private church data
   - Mitigation: Data boundary enforcement, clear exclusion policies

**Medium Priority Risks:**

4. **Over-reliance on AI Guidance**
   - Risk: Church leadership treats system as authoritative
   - Mitigation: Disclaimers, emphasis on human judgment

5. **Denominational Misalignment**
   - Risk: Guidance doesn't match specific tradition
   - Mitigation: Generic advice, denominational consultation prompts

6. **Outdated Information**
   - Risk: AI landscape changes rapidly
   - Mitigation: Version dating, knowledge cutoff disclaimers

### Risk Flags

The system automatically flags queries containing:
- Child/youth/minor keywords
- Pastoral counseling language
- Financial manipulation patterns
- Privacy violation indicators
- Requests to access or process church data

Flagged queries receive conservative responses with mandatory disclaimers.

---

## 7. Evaluation & Testing

### Test Categories

**Safe Queries (Should Answer Confidently):**
- General AI ethics questions
- Church technology best practices
- Privacy policy guidance

**Edge Cases (Should Answer with Caveats):**
- Denominationally-specific scenarios
- Emerging AI technologies
- Complex ethical dilemmas

**Harmful Queries (Should Refuse):**
- Pastoral counseling requests
- Requests involving minors without safeguards
- Attempts to access private data
- Financial manipulation scenarios

### Success Criteria
- 100% refusal rate on harmful queries
- Source citation in 100% of responses
- Risk flag activation on 100% of sensitive queries
- No hallucinated sources or citations

---

## 8. Disclaimers & Warnings

### Critical User Warnings

**This system:**
- Is NOT a substitute for pastoral wisdom or professional advice
- Does NOT provide theological or doctrinal guidance
- Does NOT access or process your church's data
- Is NOT production-ready (demonstration project only)
- Should NOT be used for sensitive or confidential matters

**Users should:**
- Consult denominational leadership for policy decisions
- Seek legal counsel for compliance questions
- Obtain professional advice for implementation
- Verify all guidance with authoritative sources
- Never share private church data with this system

### Recommended Next Steps

After using this system, users should:
1. Consult their denominational resources
2. Review guidance with church leadership
3. Seek professional counsel (legal, technical, pastoral)
4. Verify recommendations with primary sources
5. Adapt guidance to local context

---

## 9. Change Log

### Version 0.1.0 (February 2026)
- Initial system card
- 15 sources in knowledge base
- Basic risk flagging implemented
- Citation system operational
- Audit logging enabled

---

## 10. Contact & Feedback

**Project Maintainer:** Francis  
**Purpose:** Portfolio demonstration of governance-aware AI engineering  
**Feedback:** Issues and suggestions welcome via GitHub

**For Ministry Use:** This is a demonstration project. For actual ministry AI adoption, consult:
- Your denominational technology office
- Professional AI ethics consultants
- Legal counsel familiar with nonprofit data protection
- Qualified church technology advisors

---

**Document Status:** Living document, updated as system evolves  
**Next Review:** Upon implementation of RAG pipeline