"""
Pytest configuration and fixtures for test suite
"""

import pytest
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def mock_llm():
    """Create a mock LLM for testing."""
    from unittest.mock import Mock

    llm = Mock()
    llm.invoke.return_value = "Mock LLM Response"
    return llm


@pytest.fixture
def sample_protocol():
    """Return sample protocol for testing."""
    return """
    TEST PROTOCOL
    
    This is a test protocol for unit testing.
    
    Principles:
    - Test everything
    - Mock external dependencies
    - Keep tests fast
    """


@pytest.fixture
def sample_user_request():
    """Return sample user request for testing."""
    return "Create a simple login system"


@pytest.fixture
def sample_draft_output():
    """Return sample draft output for testing."""
    return """
    DRAFT: Login System
    
    1. Create login form
    2. Add authentication
    3. Redirect after login
    """


@pytest.fixture
def sample_critique_output():
    """Return sample critique output for testing."""
    return """
    CRITIQUE: Login System
    
    Issues found:
    1. Missing password hashing
    2. No rate limiting
    3. Missing error handling
    """
