# Data Policy: Ministry AI Governance Assistant

**Version:** 1.0  
**Effective Date:** February 2026  
**Last Updated:** February 2026  
**Policy Owner:** Francis

---

## 1. Purpose & Scope

### Purpose
This Data Policy defines how the Ministry AI Governance Assistant handles, stores, and protects data throughout its lifecycle. It establishes clear boundaries for what data can and cannot be processed, ensuring the system operates safely and ethically.

### Scope
This policy applies to:
- All data ingested into the knowledge base
- All user queries and interactions
- All system logs and metadata
- All outputs and responses generated

---

## 2. Data Classification

### Tier 1: Allowed Data (GREEN)

**Public Knowledge Resources**
- Published AI ethics frameworks and guidelines
- Public church technology best practice articles
- General ministry resource guides
- Non-confidential policy templates
- Published research papers and reports
- Publicly available training materials

**Characteristics:**
- Publicly accessible without authentication
- No copyright restrictions for educational use
- No personally identifiable information (PII)
- No sensitive organizational data
- Properly licensed or public domain

### Tier 2: Restricted Data (YELLOW)

**Data Requiring Special Handling**
- Aggregated, anonymized statistics (no individual identification)
- Generic organizational scenarios (no specific church identification)
- Public case studies with proper attribution

**Requirements:**
- Must be fully anonymized
- No re-identification possible
- Proper source attribution
- Clear consent for use

### Tier 3: Forbidden Data (RED)

**Data NEVER Allowed in System**

**Individual Information:**
- Church member names, addresses, contact information
- Donation amounts or giving records
- Attendance records linked to individuals
- Volunteer applications with personal details
- Background check results

**Sensitive Communications:**
- Pastoral counseling session notes
- Prayer request details with personal information
- Internal church conflict documentation
- Confidential leadership discussions
- Private correspondence

**Protected Categories:**
- Any information about minors (names, photos, details)
- Medical information or health records
- Financial account details
- Social Security numbers or tax IDs
- Passwords or authentication credentials

**Proprietary Information:**
- Vendor contracts or pricing
- Internal financial projections
- Strategic planning documents (non-public)
- Personnel files or HR records
- Privileged legal communications

---

## 3. Data Collection

### Knowledge Base Sources

**Collection Criteria:**
- Must be Tier 1 (Allowed) data only
- Publicly accessible without barriers
- Authoritative and reputable sources
- Recent and relevant content
- Clear licensing terms

**Current Sources (as of February 2026):**
- 5 AI ethics and safety documents
- 6 church technology best practice articles
- 4 privacy and child safety guides
- Total: 15 curated sources

**Source Review Process:**
1. Identify potential source
2. Verify public accessibility
3. Review for PII or sensitive data
4. Confirm licensing allows educational use
5. Document in SOURCE_LIST.md
6. Obtain approval before ingestion

### User Query Data

**What is Collected:**
- Query text (sanitized)
- Timestamp
- Session ID (not linked to user identity)
- Retrieved document IDs
- Response metadata (length, sources used)
- Risk flags triggered

**What is NOT Collected:**
- User names or email addresses
- IP addresses or device identifiers
- Location data
- Browser fingerprints
- Any cross-session tracking data

---

## 4. Data Storage

### Knowledge Base Storage

**Location:** Local development environment  
**Format:** Processed text chunks with embeddings  
**Encryption:** Not required (public data only)  
**Backup:** Version controlled via Git

**Storage Requirements:**
- Separate from any private church data
- No commingling with production systems
- Clear labeling of data source and date
- Version tracking for all changes

### Query Log Storage

**Location:** Local logs directory  
**Format:** JSONL (JSON Lines)  
**Retention:** 90 days  
**Access:** Developer only

**Log Contents:**
```json
{
  "timestamp": "2026-02-06T14:30:00Z",
  "session_id": "anonymous_session_abc123",
  "query_sanitized": "What are AI best practices for churches?",
  "retrieved_docs": ["doc_001", "doc_003"],
  "response_length": 450,
  "risk_flags": [],
  "sources_cited": 2
}
```

**Sanitization Rules:**
- Remove any names mentioned in queries
- Redact any email addresses or phone numbers
- Strip any church-identifying information
- Replace specific dates with relative time (e.g., "recently")

---

## 5. Data Access Control

### Access Levels

**Level 1: Public Read Access**
- Who: Anyone
- What: README.md, documentation, source list
- Where: Public GitHub repository

**Level 2: Developer Access**
- Who: Project maintainer (Francis)
- What: All system files, logs, configuration
- Where: Local development environment

**Level 3: No Access**
- Who: No one
- What: Private church data (system never processes this)

### Authentication & Authorization

**For Development:**
- Git credentials for repository access
- No multi-user access needed (single developer project)
- No authentication required for public documentation

**For Future Production (if applicable):**
- Would require proper authentication system
- Role-based access control (RBAC)
- Audit logging of all access
- Multi-factor authentication recommended

---

## 6. Data Retention

### Knowledge Base Data
- **Retention:** Indefinite (sources are public, permanent references)
- **Updates:** Sources reviewed quarterly for accuracy
- **Removal:** Sources removed if licensing changes or content outdated

### Query Logs
- **Retention:** 90 days
- **Purpose:** System improvement and safety monitoring only
- **Deletion:** Automatic purge after 90 days
- **No archival:** Logs not backed up after deletion

### System Outputs
- **Retention:** Not stored (responses generated on-demand)
- **User responsibility:** Users must save responses if needed
- **No tracking:** No record of what users do with outputs

---

## 7. Data Sharing & Disclosure

### Internal Use Only
All data collected by this system is for internal development and improvement only.

**Data is NOT:**
- Sold to third parties
- Shared with marketing services
- Used for profiling or targeting
- Provided to advertisers
- Transferred across borders (local development only)

### Exceptions
Data may be disclosed only if:
- Required by law (valid legal process)
- Necessary to protect safety (e.g., child endangerment report)
- With explicit user consent (not applicable in this demo)

**In this demonstration project:** No data sharing occurs. All processing is local.

---

## 8. Data Security

### Security Measures

**Physical Security:**
- Development machine password protected
- Encrypted disk storage (standard OS encryption)
- Secure physical location

**Network Security:**
- No network exposure (local development only)
- No external API calls with sensitive data
- Git credentials secured

**Access Security:**
- Single developer access (Francis)
- Strong password policies
- Regular security updates

### Incident Response

**In case of data breach:**
1. Immediately stop system operation
2. Assess scope of exposure
3. Document incident details
4. Implement corrective measures
5. Update policy as needed

**For this demonstration project:** Risk is minimal (only public data processed).

---

## 9. Data Subject Rights

### Applicable Rights

Since this system processes no personal data (PII), traditional data subject rights do not apply. However, the system respects the following principles:

**Transparency:**
- Clear documentation of what data is used
- Public source list
- Open source code (planned)

**User Control:**
- Users can choose what queries to submit
- No tracking or profiling
- No forced data collection

**Right to be Forgotten:**
- Query logs auto-delete after 90 days
- No persistent user profiles
- No cross-session tracking

---

## 10. Children's Data Protection

### Special Protections for Minors

**Absolute Prohibition:**
- No collection of data about children under 18
- No processing of child-related personal information
- No storage of images, names, or details of minors

**Queries About Children:**
- System may discuss general child safety principles
- Must not request or store specific child information
- Risk flags activate on child-related queries

**Compliance:**
- COPPA (Children's Online Privacy Protection Act)
- GDPR provisions for children's data
- Church child protection policies

---

## 11. Compliance & Standards

### Regulatory Alignment

**Relevant Standards:**
- NIST AI Risk Management Framework
- ISO 27001 principles (information security)
- GDPR privacy by design principles
- Nonprofit data protection best practices

**Church-Specific Considerations:**
- Denominational data policies
- Child protection requirements
- Pastoral confidentiality norms
- Donor privacy expectations

### Audit Trail

**Documentation Requirements:**
- All data sources documented in SOURCE_LIST.md
- Data flow documented in system architecture
- Access controls documented in this policy
- Changes tracked via Git version control

---

## 12. Data Minimization

### Principles

**Collect Only What's Needed:**
- No user personal data collected
- Query logs contain minimum necessary metadata
- No tracking beyond what's required for safety

**Process Only What's Allowed:**
- Strict boundaries on data types
- Hard blocks on forbidden data
- No scope creep beyond public sources

**Retain Only What's Required:**
- 90-day log retention (for safety monitoring)
- No indefinite storage of query data
- Automatic deletion mechanisms

---

## 13. Third-Party Data

### Vendor Data

**If using cloud services (future consideration):**
- Data Processing Agreements required
- Vendor security certifications verified
- Data residency requirements specified
- Right to audit vendor practices

**Current State:**
- No third-party services used
- No cloud processing
- All data local to development machine

---

## 14. Data Disposal

### Secure Deletion

**When data is no longer needed:**

**Query Logs (after 90 days):**
- Automated purge script
- Secure deletion (not just file removal)
- Verification of deletion

**Decommissioned Sources:**
- Remove from knowledge base
- Delete embeddings and chunks
- Document removal in changelog

**System Decommission (if applicable):**
- Wipe all logs and temporary files
- Remove all source data copies
- Verify no residual data remains

---

## 15. Policy Updates

### Review Schedule
- Quarterly review of data sources
- Annual comprehensive policy review
- Immediate review after any incident
- Review when adding new data types

### Change Process
1. Identify need for change
2. Document proposed changes
3. Assess impact on existing data
4. Update policy version
5. Communicate changes (GitHub commit message)
6. Update related documentation

### Version History

**Version 1.0 (February 2026):**
- Initial data policy
- 15 sources defined
- 90-day log retention
- Local-only processing

---

## 16. Roles & Responsibilities

### Data Controller
**Role:** Project Maintainer (Francis)  
**Responsibilities:**
- Enforce this data policy
- Review and approve data sources
- Monitor compliance
- Respond to data incidents
- Update policy as needed

### Data Processor
**Role:** AI System (automated)  
**Responsibilities:**
- Process only allowed data
- Enforce data boundaries
- Log required metadata
- Flag policy violations
- Delete data per retention schedule

---

## 17. Contact & Questions

**Policy Questions:** Reference GitHub repository  
**Data Concerns:** Create issue in GitHub repo  
**Security Issues:** Private communication via repository maintainer

---

## Appendix A: Data Flow Diagram
```
[Public Sources] → [Manual Curation] → [SOURCE_LIST.md]
       ↓
[Ingestion Pipeline] → [Processed Chunks] → [Knowledge Base]
       ↓
[User Query] → [RAG System] → [Retrieved Context]
       ↓
[LLM Processing] → [Response Generation] → [User]
       ↓
[Sanitized Log] → [90-day Storage] → [Auto-Delete]
```

---

## Appendix B: Forbidden Data Examples

**Examples of data NEVER allowed:**
- "John Smith, 123 Main St, donated $500"
- "Youth group member Sarah has anxiety issues"
- "Pastor's personal cell phone: 555-1234"
- "Confidential elder board meeting notes"
- "Background check results for volunteer Tom"

---

**Document Status:** Living document, updated as data practices evolve  
**Next Review:** May 2026 or upon system architecture changes