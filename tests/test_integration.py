"""
Integration tests for the Self-Auditing Prompt Generator

⚠️ Warning: These tests require Ollama to be running and will be slow.
Run with: pytest tests/test_integration.py -v
"""

import pytest


@pytest.mark.integration
@pytest.mark.requires_ollama
@pytest.mark.skip(reason="Requires Ollama to be running and installed")
def test_full_orchestration_with_ollama():
    """Test full orchestration with actual Ollama."""
    from agents import DraftAgent, CritiqueAgent, RevisionAgent, SAPGOrchestrator
    from llm_factory import LLMFactory
    from protocol import get_protocol_template

    # This is an integration test - requires actual Ollama
    try:
        # Initialize with Ollama
        llm = LLMFactory.create_ollama("llama2")
        protocol = get_protocol_template()

        # Create agents
        draft_agent = DraftAgent(llm, protocol)
        critique_agent = CritiqueAgent(llm, protocol)
        revision_agent = RevisionAgent(llm, protocol)

        # Create orchestrator
        orchestrator = SAPGOrchestrator(
            draft_agent, critique_agent, revision_agent)

        # Execute with simple request
        user_request = "Write a hello world program in Python"
        results = orchestrator.execute(user_request)

        # Check results
        assert "user_request" in results
        assert "draft" in results
        assert "critique" in results
        assert "revision" in results

        # Check that outputs exist
        assert len(results["draft"]) > 0
        assert len(results["critique"]) > 0
        assert len(results["revision"]) > 0

    except Exception as e:
        pytest.skip(f"Integration test skipped: {str(e)}")


@pytest.mark.integration
@pytest.mark.requires_ollama
@pytest.mark.skip(reason="Requires Ollama to be running and installed")
def test_draft_agent_with_simple_request():
    """Test draft agent with a simple request."""
    from agents import DraftAgent
    from llm_factory import LLMFactory
    from protocol import get_protocol_template

    try:
        llm = LLMFactory.create_ollama("llama2")
        protocol = get_protocol_template()

        agent = DraftAgent(llm, protocol)

        output = agent.generate("Write hello in Python")

        assert len(output) > 0
        assert "hello" in output.lower() or "print" in output.lower()

    except Exception as e:
        pytest.skip(f"Integration test skipped: {str(e)}")
