# Risk Checklist: Ministry AI Governance Assistant

**Version:** 1.0  
**Last Updated:** February 2026  
**Review Frequency:** Quarterly  
**Risk Owner:** Francis

---

## Purpose

This checklist provides a systematic framework for identifying, assessing, and mitigating risks associated with the Ministry AI Governance Assistant. It should be reviewed before deployment, after significant changes, and quarterly during operation.

---

## How to Use This Checklist

**Rating Scale:**
- **High Risk:** Immediate action required, blocks deployment
- **Medium Risk:** Mitigation plan required before deployment
- **Low Risk:** Monitor, document mitigation approach
- **N/A:** Not applicable to current system state

**Review Process:**
1. Work through each section systematically
2. Rate each risk item
3. Document current mitigation status
4. Create action items for unmitigated risks
5. Set review date for next assessment

---

## Risk Category 1: Data & Privacy Risks

### 1.1 Data Boundary Violations

**Risk:** System processes data it should not have access to

**Assessment Questions:**
- [ ] Are data boundaries clearly defined and documented?
- [ ] Does system reject forbidden data types automatically?
- [ ] Are there technical controls preventing private data ingestion?
- [ ] Is there a process for verifying data sources before ingestion?

**Current Mitigation:**
- SOURCE_LIST.md with approved sources only
- DATA_POLICY.md with clear exclusion list
- Manual review of all sources before ingestion

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 1.2 Personally Identifiable Information (PII) Exposure

**Risk:** User queries containing PII are logged or processed insecurely

**Assessment Questions:**
- [ ] Are query logs sanitized to remove PII?
- [ ] Is there a process for detecting PII in inputs?
- [ ] Are logs encrypted or access-controlled?
- [ ] Is log retention limited to necessary duration?

**Current Mitigation:**
- 90-day log retention policy
- Sanitization rules in DATA_POLICY.md
- Local-only storage (no cloud exposure)

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Implement automated PII detection in logs
- Add sanitization script before logging

---

### 1.3 Child Data Protection

**Risk:** System inadvertently collects or processes information about minors

**Assessment Questions:**
- [ ] Are there explicit controls preventing child data collection?
- [ ] Do risk flags activate on child-related queries?
- [ ] Is there special handling for queries about minors?
- [ ] Is staff trained on child data protection requirements?

**Current Mitigation:**
- No child data in knowledge base
- Risk flags defined for child-related queries
- SYSTEM_CARD.md explicitly excludes child data

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 1.4 Data Retention Violations

**Risk:** Data kept longer than necessary or policy allows

**Assessment Questions:**
- [ ] Is retention policy clearly defined?
- [ ] Are automated deletion mechanisms in place?
- [ ] Is there a process for verifying deletion?
- [ ] Are backups included in retention policy?

**Current Mitigation:**
- 90-day retention policy for logs
- Knowledge base sources retained indefinitely (public data)

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Implement automated log purge script
- Set calendar reminder for quarterly deletion verification

---

## Risk Category 2: Ethical & Misuse Risks

### 2.1 Pastoral Care Replacement

**Risk:** System used inappropriately for counseling or pastoral care

**Assessment Questions:**
- [ ] Are boundaries clearly communicated to users?
- [ ] Does system refuse pastoral care requests?
- [ ] Are alternative resources suggested?
- [ ] Are pastoral care queries flagged for monitoring?

**Current Mitigation:**
- Clear disclaimers in SYSTEM_CARD.md
- Test cases for pastoral care refusal (test_prompts.md)
- Risk flags defined

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 2.2 Theological/Doctrinal Misuse

**Risk:** System provides theological guidance beyond its scope

**Assessment Questions:**
- [ ] Are theological questions explicitly out of scope?
- [ ] Does system redirect to appropriate authorities?
- [ ] Are there safeguards against doctrinal positions?
- [ ] Is denominational neutrality maintained?

**Current Mitigation:**
- Theological questions marked out-of-scope in SYSTEM_CARD.md
- Refusal test cases in test_prompts.md
- Generic guidance only, no doctrinal positions

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 2.3 Financial Manipulation

**Risk:** System used to manipulate giving or donor behavior

**Assessment Questions:**
- [ ] Are financial manipulation queries flagged?
- [ ] Does system refuse donor targeting advice?
- [ ] Are ethical fundraising principles emphasized?
- [ ] Is transparency vs manipulation boundary clear?

**Current Mitigation:**
- Financial manipulation test cases defined
- Risk flags for donor targeting queries
- Ethical boundaries in SYSTEM_CARD.md

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 2.4 Over-Reliance on AI Guidance

**Risk:** Church leaders treat system as authoritative without human judgment

**Assessment Questions:**
- [ ] Are disclaimers clear and prominent?
- [ ] Does system emphasize need for human judgment?
- [ ] Are consultation recommendations included in outputs?
- [ ] Is "demonstration project" status clear?

**Current Mitigation:**
- Multiple disclaimers in SYSTEM_CARD.md and README.md
- Recommendations to consult human experts
- "Not production-ready" warnings

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

## Risk Category 3: Technical & Operational Risks

### 3.1 Source Quality & Accuracy

**Risk:** Knowledge base contains inaccurate or outdated information

**Assessment Questions:**
- [ ] Are sources from authoritative organizations?
- [ ] Is there a process for reviewing source quality?
- [ ] Are sources dated and version-controlled?
- [ ] Is there a schedule for reviewing source freshness?

**Current Mitigation:**
- 15 curated sources from reputable organizations
- All sources documented in SOURCE_LIST.md
- Source selection criteria defined

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Set quarterly review schedule for sources
- Add publication dates to SOURCE_LIST.md entries

---

### 3.2 Hallucination & False Citations

**Risk:** System generates false information or fake source citations

**Assessment Questions:**
- [ ] Are all citations verified against real sources?
- [ ] Is there a process for detecting hallucinations?
- [ ] Are outputs tested for citation accuracy?
- [ ] Is citation format standardized?

**Current Mitigation:**
- RAG architecture reduces hallucination risk
- Test cases include citation verification
- All sources are real, documented URLs

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Implement citation verification in evaluation harness
- Test for hallucination patterns

---

### 3.3 System Availability & Reliability

**Risk:** System unavailable when needed or produces inconsistent results

**Assessment Questions:**
- [ ] Is system architecture documented?
- [ ] Are failure modes identified?
- [ ] Is there a backup or recovery plan?
- [ ] Are performance metrics monitored?

**Current Mitigation:**
- Git version control for recovery
- Local deployment (no external dependencies)
- Architecture will be documented

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Document system architecture
- Create deployment guide

---

### 3.4 Prompt Injection & Jailbreaking

**Risk:** Users bypass safety controls through adversarial prompts

**Assessment Questions:**
- [ ] Are boundary-testing scenarios defined?
- [ ] Is there monitoring for bypass attempts?
- [ ] Are safety controls regularly tested?
- [ ] Is there a process for updating defenses?

**Current Mitigation:**
- Boundary testing section in test_prompts.md
- Test cases for reframing and hypothetical attacks

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Implement bypass attempt logging
- Schedule red-team testing

---

## Risk Category 4: Legal & Compliance Risks

### 4.1 Copyright Violations

**Risk:** Knowledge base contains copyrighted material used improperly

**Assessment Questions:**
- [ ] Are all sources properly licensed?
- [ ] Is fair use appropriately applied?
- [ ] Are source attributions complete?
- [ ] Is there a process for handling DMCA requests?

**Current Mitigation:**
- All sources are publicly available
- Educational use context
- Full source attribution in SOURCE_LIST.md

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Review licensing terms for each source
- Add licensing notes to SOURCE_LIST.md

---

### 4.2 Data Protection Compliance

**Risk:** System violates GDPR, COPPA, or other data protection laws

**Assessment Questions:**
- [ ] Are data protection principles followed?
- [ ] Is child data protection compliant?
- [ ] Are user rights respected?
- [ ] Is privacy policy adequate?

**Current Mitigation:**
- No PII collection
- DATA_POLICY.md aligned with GDPR principles
- Child data explicitly prohibited

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 4.3 Liability & Disclaimers

**Risk:** System held liable for harmful advice or outcomes

**Assessment Questions:**
- [ ] Are disclaimers clear and prominent?
- [ ] Is demonstration status explicit?
- [ ] Are limitations clearly stated?
- [ ] Is legal review recommended?

**Current Mitigation:**
- Multiple disclaimers in all documentation
- "Not production-ready" warnings
- Recommendations to seek professional advice

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

## Risk Category 5: Ministry-Specific Risks

### 5.1 Denominational Misalignment

**Risk:** Guidance conflicts with specific denominational practices

**Assessment Questions:**
- [ ] Is guidance generic across denominations?
- [ ] Are denominational consultations recommended?
- [ ] Is theological diversity respected?
- [ ] Are specific traditions acknowledged?

**Current Mitigation:**
- Generic guidance only
- Recommendations to consult denominational resources
- No doctrinal positions taken

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 5.2 Erosion of Human Ministry

**Risk:** AI tools reduce authentic human connection in ministry

**Assessment Questions:**
- [ ] Does guidance emphasize human relationships?
- [ ] Are AI limits clearly explained?
- [ ] Is incarnational ministry prioritized?
- [ ] Are pastoral calling and discernment protected?

**Current Mitigation:**
- Emphasis on AI as tool, not replacement
- Refusal to generate pastoral content
- Human judgment emphasized throughout

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 5.3 Digital Divide & Accessibility

**Risk:** System accessible only to tech-savvy churches

**Assessment Questions:**
- [ ] Is documentation clear for non-technical users?
- [ ] Are barriers to entry minimized?
- [ ] Is guidance practical for small churches?
- [ ] Are alternatives provided for low-tech contexts?

**Current Mitigation:**
- Clear, non-technical documentation
- Focus on principles over specific tools
- Recognition of resource constraints

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Add glossary for technical terms
- Include low-tech alternatives in guidance

---

## Risk Category 6: Governance & Oversight Risks

### 6.1 Inadequate Testing

**Risk:** System deployed without sufficient safety testing

**Assessment Questions:**
- [ ] Is evaluation harness comprehensive?
- [ ] Are all risk scenarios tested?
- [ ] Is testing done before each release?
- [ ] Are test results documented?

**Current Mitigation:**
- 25+ test cases in test_prompts.md
- Safe, edge, and harmful query categories
- Testing schedule defined

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Execute full test suite before any demo
- Document test results

---

### 6.2 Inadequate Documentation

**Risk:** Governance practices not properly documented

**Assessment Questions:**
- [ ] Are all policies documented?
- [ ] Is documentation accessible?
- [ ] Are changes tracked?
- [ ] Is documentation kept current?

**Current Mitigation:**
- Comprehensive governance pack (4 documents)
- Version control via Git
- Living document status noted

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- 

---

### 6.3 Lack of Independent Review

**Risk:** No external validation of safety claims

**Assessment Questions:**
- [ ] Has system been reviewed by third parties?
- [ ] Is peer feedback solicited?
- [ ] Are limitations acknowledged?
- [ ] Is external expertise consulted?

**Current Mitigation:**
- Public GitHub repository (open to feedback)
- Acknowledgment of demonstration status
- No claims of external validation

**Risk Level:** [ ] High [ ] Medium [ ] Low [ ] N/A

**Action Items:**
- Solicit feedback from church tech community
- Consider peer review before public demo

---

## Risk Summary Dashboard

### High Priority Risks (Address Immediately)

| Risk ID | Description | Status | Owner | Due Date |
|---------|-------------|--------|-------|----------|
| | | | | |

### Medium Priority Risks (Mitigation Plan Required)

| Risk ID | Description | Status | Owner | Due Date |
|---------|-------------|--------|-------|----------|
| | | | | |

### Low Priority Risks (Monitor)

| Risk ID | Description | Status | Owner | Due Date |
|---------|-------------|--------|-------|----------|
| | | | | |

---

## Mitigation Action Tracker

### Immediate Actions (Before Any Demo)

- [ ] Execute full test suite (test_prompts.md)
- [ ] Verify all source URLs are accessible
- [ ] Implement query log sanitization
- [ ] Add disclaimers to any user-facing interface
- [ ] Document RAG architecture

### Short-Term Actions (Within 30 Days)

- [ ] Implement automated log purge
- [ ] Add PII detection to logging
- [ ] Complete citation verification tests
- [ ] Schedule quarterly source review
- [ ] Solicit peer feedback

### Long-Term Actions (Ongoing)

- [ ] Quarterly risk assessment review
- [ ] Annual comprehensive policy review
- [ ] Continuous test case expansion
- [ ] Community feedback integration
- [ ] Source freshness monitoring

---

## Review Schedule

### Pre-Deployment Review
**Timing:** Before any public demo or deployment  
**Focus:** All High and Medium risks must be addressed  
**Checklist:** Complete all sections of this document

### Quarterly Review
**Timing:** Every 3 months  
**Focus:** Mitigation effectiveness, new risks, source freshness  
**Checklist:** Sections 1-6, update action items

### Post-Incident Review
**Timing:** After any safety incident or close call  
**Focus:** Root cause, additional mitigations, policy updates  
**Checklist:** Relevant sections, document lessons learned

### Annual Comprehensive Review
**Timing:** Yearly  
**Focus:** Complete risk reassessment, policy updates  
**Checklist:** All sections, update risk ratings

---

## Risk Acceptance

### Accepted Risks (Demonstration Project)

The following risks are accepted given this is a portfolio demonstration:

1. **Limited Scope:** Only 15 sources (not comprehensive)
2. **No Production Hardening:** Security appropriate for demo only
3. **Single Developer:** No peer review or independent validation
4. **No Real Users:** No user testing or feedback loops
5. **Rapid Development:** Prioritizes learning over production readiness

**Condition:** These risks are acceptable ONLY for demonstration purposes. Production deployment would require addressing all of these.

---

## Escalation Procedures

### When to Escalate

Escalate immediately if:
- Any High Risk is discovered
- Safety controls are bypassed
- Data boundary violations occur
- Child data is inadvertently processed
- Legal concerns arise

### Escalation Process

**For this demonstration project:**
1. Stop system operation
2. Document incident
3. Implement fixes
4. Update policies
5. Re-test before resuming

**For production systems (future):**
- Would require formal incident response team
- Legal consultation for data breaches
- User notification procedures
- Regulatory reporting as required

---

## Sign-Off

### Risk Assessment Completed

**Date:** _____________  
**Completed By:** _____________  
**Next Review Date:** _____________

**Overall Risk Status:**
- [ ] Ready for demonstration
- [ ] Requires mitigation before demo
- [ ] Requires major changes

**Notes:**

---

**Document Status:** Living document, updated with each risk review  
**Next Review:** Upon RAG implementation or quarterly (whichever comes first)