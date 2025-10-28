"""
Tests for the Self-Auditing Protocol
"""

import pytest
from protocol import get_protocol_template


def test_protocol_template_exists():
    """Test that protocol template is not empty."""
    protocol = get_protocol_template()
    assert protocol is not None
    assert len(protocol) > 0


def test_protocol_contains_key_terms():
    """Test that protocol contains key self-auditing terms."""
    protocol = get_protocol_template()

    # Check for key concepts
    assert "DRAFT" in protocol or "Draft" in protocol
    assert "CRITIQUE" in protocol or "Critique" in protocol
    assert "REVISION" in protocol or "Revision" in protocol
    assert "AUDIT" in protocol or "audit" in protocol


def test_protocol_is_string():
    """Test that protocol returns a string."""
    protocol = get_protocol_template()
    assert isinstance(protocol, str)


def test_protocol_is_readable():
    """Test that protocol is human-readable."""
    protocol = get_protocol_template()
    # Should not be too short (basic check)
    assert len(protocol) > 100
