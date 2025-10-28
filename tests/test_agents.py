"""
Tests for Agent classes
"""

import pytest
from unittest.mock import Mock, MagicMock


def test_agent_base_class():
    """Test that base Agent class can be instantiated."""
    from agents import Agent

    # Create a mock LLM
    mock_llm = Mock()

    agent = Agent(mock_llm, "Test Agent")
    assert agent.name == "Test Agent"
    assert agent.llm is not None


def test_draft_agent_creation():
    """Test DraftAgent can be created."""
    from agents import DraftAgent

    mock_llm = Mock()
    protocol = "Test Protocol"

    agent = DraftAgent(mock_llm, protocol)
    assert agent.name == "Draft Agent"
    assert agent.protocol_template == protocol


def test_critique_agent_creation():
    """Test CritiqueAgent can be created."""
    from agents import CritiqueAgent

    mock_llm = Mock()
    protocol = "Test Protocol"

    agent = CritiqueAgent(mock_llm, protocol)
    assert agent.name == "Critique Agent"
    assert agent.protocol_template == protocol


def test_revision_agent_creation():
    """Test RevisionAgent can be created."""
    from agents import RevisionAgent

    mock_llm = Mock()
    protocol = "Test Protocol"

    agent = RevisionAgent(mock_llm, protocol)
    assert agent.name == "Revision Agent"
    assert agent.protocol_template == protocol


def test_orchestrator_creation():
    """Test SAPGOrchestrator can be created."""
    from agents import DraftAgent, CritiqueAgent, RevisionAgent, SAPGOrchestrator

    mock_llm = Mock()
    protocol = "Test Protocol"

    draft = DraftAgent(mock_llm, protocol)
    critique = CritiqueAgent(mock_llm, protocol)
    revision = RevisionAgent(mock_llm, protocol)

    orchestrator = SAPGOrchestrator(draft, critique, revision)
    assert orchestrator.draft_agent is not None
    assert orchestrator.critique_agent is not None
    assert orchestrator.revision_agent is not None


@pytest.mark.skip(reason="Requires actual LLM connection")
def test_draft_agent_generate():
    """Test DraftAgent can generate output."""
    from agents import DraftAgent

    # This would require actual LLM
    # For now, just check the method exists
    assert hasattr(DraftAgent, 'generate')


@pytest.mark.skip(reason="Requires actual LLM connection")
def test_critique_agent_critique():
    """Test CritiqueAgent can critique output."""
    from agents import CritiqueAgent

    # This would require actual LLM
    # For now, just check the method exists
    assert hasattr(CritiqueAgent, 'critique')


@pytest.mark.skip(reason="Requires actual LLM connection")
def test_revision_agent_revise():
    """Test RevisionAgent can revise output."""
    from agents import RevisionAgent

    # This would require actual LLM
    # For now, just check the method exists
    assert hasattr(RevisionAgent, 'revise')


@pytest.mark.skip(reason="Requires actual LLM connection")
def test_orchestrator_execute():
    """Test SAPGOrchestrator can execute full cycle."""
    from agents import SAPGOrchestrator

    # This would require actual LLM
    # For now, just check the method exists
    assert hasattr(SAPGOrchestrator, 'execute')
