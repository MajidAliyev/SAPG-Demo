# 🧪 Testing Guide

## Test Suite Overview

The Self-Auditing Prompt Generator includes a comprehensive test suite to ensure code quality and reliability.

## 📁 Test Structure

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Pytest fixtures and configuration
├── test_protocol.py         # Tests for Self-Auditing Protocol
├── test_agents.py           # Tests for agent classes
├── test_llm_factory.py      # Tests for LLM factory
└── test_integration.py      # Integration tests (requires Ollama)
```

## 🚀 Running Tests

### Install Test Dependencies

```bash
pip install -r requirements.txt
```

This installs:

- `pytest` - Test framework
- `pytest-cov` - Coverage reporting
- `pytest-mock` - Mocking utilities

### Run All Tests

```bash
pytest
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Coverage Report

```bash
pytest --cov=. --cov-report=html
```

Open `htmlcov/index.html` in your browser to see detailed coverage.

### Run Specific Test File

```bash
pytest tests/test_agents.py
pytest tests/test_protocol.py
pytest tests/test_llm_factory.py
```

### Run Only Fast Tests (Skip Integration Tests)

```bash
pytest -m "not slow"
```

Integration tests are marked with `@pytest.mark.slow` and `@pytest.mark.requires_ollama`

## 📊 Test Coverage

Current test coverage includes:

- ✅ **Protocol Tests** - Verify protocol template exists and contains key concepts
- ✅ **Agent Tests** - Test agent instantiation and basic structure
- ✅ **LLM Factory Tests** - Test LLM creation and error handling
- ✅ **Integration Tests** - Full workflow with real LLM (requires Ollama)

## 🎯 Writing New Tests

### Example Test Structure

```python
def test_feature_name():
    """Test description."""
    # Arrange - Set up test data
    test_input = "example"

    # Act - Execute code being tested
    result = function_to_test(test_input)

    # Assert - Verify results
    assert result is not None
    assert len(result) > 0
```

### Using Fixtures

Tests can use fixtures defined in `conftest.py`:

```python
def test_with_mock_llm(mock_llm):
    """Test using mock LLM."""
    # Use mock_llm fixture
    pass

def test_with_protocol(sample_protocol):
    """Test using sample protocol."""
    # Use sample_protocol fixture
    pass
```

## 🔍 Test Markers

Tests use markers to categorize them:

- `@pytest.mark.unit` - Unit tests (fast, no dependencies)
- `@pytest.mark.integration` - Integration tests (require external services)
- `@pytest.mark.slow` - Slow-running tests
- `@pytest.mark.requires_ollama` - Require Ollama to be running
- `@pytest.mark.requires_openai` - Require OpenAI API key
- `@pytest.mark.requires_anthropic` - Require Anthropic API key

## 🚫 Skipped Tests

Some tests are intentionally skipped:

- Integration tests require Ollama to be running
- API tests require valid API keys

To run integration tests:

```bash
pytest -m integration  # Run integration tests
pytest -m "requires_ollama"  # Run Ollama-requiring tests
```

## ✅ Continuous Integration

For CI/CD pipelines, run:

```bash
pytest --cov=. --cov-report=xml --junitxml=test-results.xml
```

This generates coverage and test result files suitable for CI systems.

## 🐛 Debugging Tests

### Run with PDB (Debugger)

```bash
pytest --pdb  # Drop into debugger on failure
```

### Print Output During Tests

```bash
pytest -s  # Show print statements
```

### Run Last Failed Test

```bash
pytest --lf  # Run only last failed tests
```

## 📈 Best Practices

1. **One assertion per test** (when possible)
2. **Descriptive test names** that explain what is being tested
3. **Use fixtures** for common setup code
4. **Mock external dependencies** for unit tests
5. **Keep tests fast** - mock slow operations
6. **Test edge cases** and error conditions
7. **Document complex tests** with comments

## 🎓 Need Help?

- See pytest documentation: https://docs.pytest.org/
- Check test files for examples
- Open an issue on GitHub

Happy Testing! 🧪
