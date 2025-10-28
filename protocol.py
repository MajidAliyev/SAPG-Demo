# Self-Auditing Protocol Template

PROTOCOL_TEMPLATE = """SELF-AUDITING PROTOCOL (SAP)

PRINCIPLE: All AI outputs must go through systematic self-correction before delivery.

ARCHITECTURE:
1. DRAFT: Agent generates the solution
2. CRITIQUE: Separate agent reviews for errors
3. REVISION: Agent incorporates feedback to produce final output

AUDIT CHECKLIST (for Critique):
□ LOGICAL ERRORS: Any contradictions or mistakes
□ TERMINATION: No infinite loops; all loops have exits
□ ERROR HANDLING: Handles all failure modes
□ COMPLETENESS: Addresses all requirements
□ SECURITY: No vulnerabilities (SQL injection, XSS, etc.)
□ PRIVACY: Handles sensitive data properly
□ EDGE CASES: Handles nulls, empty inputs, boundaries
□ PERFORMANCE: No unnecessary operations
□ MAINTAINABILITY: Clear, readable code

RECURSIVE NATURE:
- Protocol applies to itself
- Creates bounded self-correction
- Prevents compounding errors

EXECUTION:
When generating, consider:
1. What could go wrong?
2. What are edge cases?
3. What security risks exist?
4. How will this fail gracefully?
5. Is this auditable?

Remember: Single-shot AI is unreliable. SAP ensures safety through systematic audit."""


def get_protocol_template():
    """Returns the protocol"""
    return PROTOCOL_TEMPLATE
