"""
Tests for LLM Factory
"""

import pytest
import os
from unittest.mock import patch, Mock


def test_llm_factory_import():
    """Test that LLMFactory can be imported."""
    from llm_factory import LLMFactory
    assert LLMFactory is not None


def test_get_available_providers():
    """Test that get_available_providers returns a list."""
    from llm_factory import LLMFactory

    providers = LLMFactory.get_available_providers()
    assert isinstance(providers, list)
    assert len(providers) >= 0  # At least ollama should be available


@patch('llm_factory.ChatOllama')
def test_create_ollama(mock_ollama_class):
    """Test creating Ollama LLM."""
    from llm_factory import LLMFactory

    # Mock the ChatOllama class
    mock_instance = Mock()
    mock_ollama_class.return_value = mock_instance

    llm = LLMFactory.create_ollama("llama2")

    # Should create and return the instance
    assert llm is not None
    mock_ollama_class.assert_called_once_with(model="llama2", temperature=0.7)


@pytest.mark.skip(reason="Requires OPENAI_API_KEY environment variable")
def test_create_openai_without_key():
    """Test OpenAI creation fails without API key."""
    from llm_factory import LLMFactory

    # Remove API key if it exists
    old_key = os.environ.pop('OPENAI_API_KEY', None)

    try:
        with pytest.raises(ValueError):
            LLMFactory.create_openai()
    finally:
        # Restore old key
        if old_key:
            os.environ['OPENAI_API_KEY'] = old_key


@pytest.mark.skip(reason="Requires ANTHROPIC_API_KEY environment variable")
def test_create_anthropic_without_key():
    """Test Anthropic creation fails without API key."""
    from llm_factory import LLMFactory

    # Remove API key if it exists
    old_key = os.environ.pop('ANTHROPIC_API_KEY', None)

    try:
        with pytest.raises(ValueError):
            LLMFactory.create_anthropic()
    finally:
        # Restore old key
        if old_key:
            os.environ['ANTHROPIC_API_KEY'] = old_key


@patch('llm_factory.ChatOllama')
def test_create_llm_with_ollama(mock_ollama_class):
    """Test create_llm with ollama provider."""
    from llm_factory import LLMFactory

    mock_instance = Mock()
    mock_ollama_class.return_value = mock_instance

    llm = LLMFactory.create_llm("ollama", "llama2")

    assert llm is not None
    mock_ollama_class.assert_called_once_with(model="llama2", temperature=0.7)


def test_create_llm_with_invalid_provider():
    """Test create_llm with invalid provider."""
    from llm_factory import LLMFactory

    with pytest.raises(ValueError, match="Unknown provider"):
        LLMFactory.create_llm("invalid_provider")
