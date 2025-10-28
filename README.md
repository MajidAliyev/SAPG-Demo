# Self-Auditing Prompt Generator (SAPG)

> **Transform simple prompts into auditable, error-free outputs through systematic self-correction.**

The SAPG implements a practical **Draft → Critique → Revision** cycle to address the fundamental flaw that AI agents often fail due to systemic, non-auditable errors.

## 📖 For Beginners

**New to programming?** Check out [QUICKSTART.md](QUICKSTART.md) for step-by-step installation instructions!

## 🎯 What It Solves

**The Core Gap**: AI agents often produce outputs with logical flaws, infinite loops, missing exception handling, and compliance risks that go undetected.

**The Solution**: Instead of running an LLM prompt once, the SAPG uses a three-phase self-correction cycle:

1. **Draft**: An agent generates a complex execution plan
2. **Critique**: A secondary agent systematically checks for errors, infinite loops, missing exception handling, and compliance risks
3. **Revision**: The first agent uses the critique to generate a corrected, auditable final output

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│         SELF-AUDITING PROTOCOL (SAP)            │
├─────────────────────────────────────────────────┤
│  Phase 1: DRAFT AGENT                           │
│  → Generates initial solution                   │
│                                                  │
│  Phase 2: CRITIQUE AGENT                        │
│  → Audits for:                                  │
│     - Logical flaws                             │
│     - Infinite loops                            │
│     - Missing exception handling                │
│     - Compliance risks                          │
│                                                  │
│  Phase 3: REVISION AGENT                        │
│  → Incorporates feedback                        │
│     → Produces corrected output                 │
└─────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Git (optional, for cloning)

### Installation

1. **Clone this repository from GitHub**

   ```bash
   git clone https://github.com/yourusername/SACC.git
   cd SACC
   ```

   Or download as ZIP and extract it.

   **Note**: Replace `yourusername` with your actual GitHub username!

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama (or use cloud APIs):**

   **Option A: Ollama (Local - Recommended for Free Use)**

   ```bash
   # Install Ollama from https://ollama.ai
   # Then pull a model:
   ollama pull llama2
   # or
   ollama pull mistral
   ```

   **Option B: OpenAI API**

   ```bash
   pip install langchain-openai
   ```

   **Option C: Anthropic API**

   ```bash
   pip install langchain-anthropic
   ```

4. **Configure environment (for API providers, optional)**

   Create a `.env` file in the project folder:

   ```bash
   # For OpenAI
   OPENAI_API_KEY=your_api_key_here

   # OR for Anthropic
   ANTHROPIC_API_KEY=your_api_key_here
   ```

5. **Run the application**

   ```bash
   streamlit run app.py
   ```

6. **Open your browser**

   The app will automatically open at `http://localhost:8501`

## 💻 Usage

1. **Configure LLM Provider**

   - Select your provider (Ollama, OpenAI, or Anthropic) in the sidebar
   - Choose a model (e.g., `llama2`, `gpt-3.5-turbo`, `claude-3-sonnet`)

2. **Enter Your Request**

   - Type or select an example request (e.g., "Create a secure authentication system")
   - Be specific about what you need generated

3. **Execute Self-Audit**

   - Click "Execute Self-Audit" to run the Draft → Critique → Revision cycle
   - Watch as the system generates, critiques, and revises the output

4. **Review Results**
   - **Final Output**: The corrected, production-ready result
   - **Draft**: See the initial output
   - **Critique**: View the systematic audit findings
   - **Revision**: See how the feedback was incorporated

## 📋 Example Use Cases

- **Code Generation**: Generate Python scripts with proper error handling
- **ETL Pipelines**: Design data pipelines with validation and compliance checks
- **Security Systems**: Build authentication systems with rate limiting and security best practices
- **Data Analysis**: Create analysis scripts with privacy safeguards
- **Business Plans**: Generate multi-step plans with risk assessment

## 🛠️ Technology Stack

- **Python**: Core language
- **Streamlit**: Web UI framework
- **LangChain**: Agent orchestration
- **Ollama**: Local LLM server (or OpenAI/Anthropic APIs)
- **LangChain Community**: Provider integrations

## 📁 Project Structure

```
SACC/
├── app.py              # Main Streamlit application
├── agents.py           # Agent definitions (Draft, Critique, Revision)
├── protocol.py         # Self-Auditing Protocol template
├── llm_factory.py     # LLM provider factory
├── requirements.txt    # Python dependencies
├── pytest.ini         # Pytest configuration
├── README.md          # This file
├── tests/             # Test suite
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_llm_factory.py
│   ├── test_protocol.py
│   ├── test_integration.py
│   └── conftest.py
└── .env               # Environment variables (create this)
```

## 🎓 How It Works

### The Self-Auditing Protocol

The SAPG implements a formal protocol that defines:

1. **Agent Roles**: Distinct agents for Draft, Critique, and Revision
2. **Systematic Auditing**: Checklist-based review (logical flaws, loops, security, etc.)
3. **Recursive Nature**: The protocol applies to itself (meta-critical thinking)
4. **Bounded Self-Correction**: Prevents "hallucination cascades"

### The Intelligent Gap

Traditional AI tools run a prompt once and return the output. The SAPG adds an intelligent layer:

- **Single-shot systems** fail due to undetected errors
- **Self-auditing systems** catch errors before delivery
- This creates **provable safety** through systematic verification

## 🎯 Hiring Leverage

This project demonstrates:

- **Agent-native design**: Systems built specifically for LLM agents
- **Provable safety**: Formal methods for AI reliability
- **Recursive architectures**: Self-correcting AI systems
- **Production AI**: Moving beyond single-shot "copilot" responses

## 🔧 Customization

### Add Custom Audit Criteria

Edit `protocol.py` to add domain-specific audit checks:

```python
CUSTOM_CRITERIA = """
□ DATABASE: Proper connection pooling and transaction handling
□ API: Rate limiting and authentication checks
□ UI: Accessibility and cross-browser compatibility
"""
```

### Use Different LLMs

Modify `llm_factory.py` to add support for additional providers (Cohere, HuggingFace, etc.)

### Extend the Cycle

Add more phases (e.g., "Validation" phase after Revision) by extending the orchestrator in `agents.py`

## 📝 License

Open source - MIT License (or as specified)

## 🧪 Testing

For detailed testing instructions, see [TESTING.md](TESTING.md).

**Quick start:**

```bash
# Install test dependencies
pip install pytest pytest-cov pytest-mock

# Run all tests
pytest

# Run with coverage report
pytest --cov=. --cov-report=html

# View coverage: open htmlcov/index.html
```

See TESTING.md for comprehensive testing guide.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas for improvement:**

- Additional LLM providers
- Custom audit criteria templates
- Batch processing for multiple requests
- Export functionality (PDF, Markdown, etc.)

## 🌐 Deployment

Want to share this with others online? Deploy to:

- **Streamlit Cloud**: https://streamlit.io/cloud
- **Heroku**: Use a Procfile and deploy via Heroku CLI
- **AWS/Azure/GCP**: Deploy as a containerized app

See the deployment guides in the `docs/` folder (create as needed).

## 🙏 Credits

Inspired by research on AI failure modes and recursive self-correction systems.
