# SAPG - Self-Auditing Prompt Generator
# Main Streamlit app

import streamlit as st
from protocol import get_protocol_template
from agents import DraftAgent, CritiqueAgent, RevisionAgent
from llm_factory import LLMFactory

st.set_page_config(page_title="Self-Auditing Prompt Generator",
                   page_icon="🔍", layout="wide")


def init_state():
    """Set up session variables"""
    if 'results' not in st.session_state:
        st.session_state.results = None


def show_header():
    st.title("🔍 Self-Auditing Prompt Generator (SAPG)")
    st.markdown("""
    **Turns simple prompts into error-free outputs using self-correction.**
    
    Uses a Draft → Critique → Revision cycle to catch errors before delivery.
    """)
    st.divider()


def setup_sidebar():
    """Configure the sidebar settings"""
    with st.sidebar:
        st.header("⚙️ Configuration")

        providers = LLMFactory.get_available_providers()
        if not providers:
            st.error("No LLM providers found. Install one of:")
            st.code("pip install ollama", language="bash")
            return None, None

        provider = st.selectbox("LLM Provider", providers,
                                help="Pick your provider")

        # figure out which model to show
        if provider == "ollama":
            st.info("💡 Tip: Use 'mistral' or 'llama2:7b' for 5x faster results!")
            model = st.text_input(
                "Model Name", value="llama2", help="try: mistral, llama2:7b")
        elif provider == "openai":
            model = st.selectbox(
                "Model", ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"])
        elif provider == "anthropic":
            model = st.selectbox(
                "Model", ["claude-3-sonnet-20240229", "claude-3-opus-20240229"])
        else:
            model = "llama2"  # fallback

        with st.expander("📋 View Protocol"):
            st.markdown(get_protocol_template())

        st.markdown("---")
        st.markdown("📚 [Speed Tips](SPEED_TIPS.md) for faster results")

        return provider, model


def show_info():
    """Show how it works"""
    with st.expander("📋 How It Works: The Self-Auditing Protocol"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 1️⃣ Draft")
            st.info("Agent generates the initial plan")

        with col2:
            st.markdown("### 2️⃣ Critique")
            st.warning("Systematically finds errors and issues")

        with col3:
            st.markdown("### 3️⃣ Revision")
            st.success("Produces corrected, final output")


def get_user_input():
    """Get the request from user"""
    st.subheader("📝 Your Request")

    # example requests
    examples = [
        "",
        "Write a Python script that scrapes a website and stores data",
        "Create an ETL pipeline with error handling",
        "Build a secure auth system with rate limiting"
    ]

    selected = st.selectbox("Load Example:", [""] + examples[1:])

    user_input = st.text_area(
        "Enter your request",
        value=selected,
        height=150,
        placeholder="What do you need generated?"
    )

    return user_input


def create_agents(provider, model):
    """Initialize the three agents"""
    try:
        # add timeout for ollama to prevent hanging
        if provider == "ollama":
            llm = LLMFactory.create_llm(provider, model)
            # reduce model size suggestion if using default
            if model == "llama2":
                st.warning(
                    "⚠️ llama2 is slow. Try 'mistral' or 'llama2:7b' for faster results!")
        else:
            llm = LLMFactory.create_llm(provider, model)

        protocol = get_protocol_template()

        draft = DraftAgent(llm, protocol)
        critique = CritiqueAgent(llm, protocol)
        revision = RevisionAgent(llm, protocol)

        return draft, critique, revision
    except Exception as e:
        st.error(f"Failed to setup agents: {e}")
        return None, None, None


def show_results(results):
    """Display results in tabs"""
    tabs = st.tabs(["📄 Final Output", "📋 Draft", "🔍 Critique", "✏️ Revision"])

    with tabs[0]:
        st.subheader("Final Output")
        st.markdown("The final, corrected output.")
        st.code(results['revision'], language='text')

    with tabs[1]:
        st.subheader("Phase 1: Draft")
        st.info("Initial output")
        st.text_area("", results['draft'], height=400,
                     label_visibility="collapsed")

    with tabs[2]:
        st.subheader("Phase 2: Critique")
        st.warning("Audit findings")
        st.text_area("", results['critique'],
                     height=400, label_visibility="collapsed")

    with tabs[3]:
        st.subheader("Phase 3: Revision")
        st.success("Corrected version")
        st.text_area("", results['revision'],
                     height=400, label_visibility="collapsed")


def main():
    """Main app entry point"""
    init_state()

    # render the UI
    show_header()

    provider, model = setup_sidebar()
    if not provider:
        return

    show_info()
    user_input = get_user_input()

    # buttons
    col1, col2 = st.columns([1, 4])
    with col1:
        go_btn = st.button("🚀 Execute Self-Audit",
                           type="primary", use_container_width=True)
    with col2:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)

    if clear_btn:
        st.session_state.results = None
        st.rerun()

    if go_btn:
        if not user_input or not user_input.strip():
            st.error("Enter a request first")
            return

        # setup agents
        with st.spinner("Setting up agents..."):
            draft_agent, critique_agent, revision_agent = create_agents(
                provider, model)

        if not draft_agent or not critique_agent or not revision_agent:
            return

        # run the three phases
        try:
            # show progress
            progress = st.progress(0)
            status = st.empty()

            # Phase 1
            status.text("📝 Phase 1/3: Creating Draft...")
            progress.progress(33)

            # add timeout warning
            if provider == "ollama":
                status.text(
                    "📝 Phase 1/3: Creating Draft... (This may take 2-5 minutes)")

            draft_output = draft_agent.generate(user_input)

            # Phase 2
            status.text("🔍 Phase 2/3: Running Critique...")
            progress.progress(66)
            critique_output = critique_agent.critique(user_input, draft_output)

            # Phase 3
            status.text("✏️ Phase 3/3: Generating Revision...")
            progress.progress(100)
            final_output = revision_agent.revise(
                user_input, draft_output, critique_output)

            # cleanup
            progress.empty()
            status.empty()

            # save results
            st.session_state.results = {
                "user_request": user_input,
                "draft": draft_output,
                "critique": critique_output,
                "revision": final_output
            }

            st.success("✅ Done!")
        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ Error: {error_msg}")

            # helpful error messages
            if "timeout" in error_msg.lower() or "connection" in error_msg.lower():
                st.warning("""
                **Connection timeout!** 
                - Try a faster model like 'mistral' or 'llama2:7b'
                - Run: `ollama pull mistral` in terminal
                - Or use OpenAI/Anthropic API for instant results
                """)
            elif "ollama" in error_msg.lower():
                st.info("Make sure Ollama is running: `ollama serve`")

            import traceback
            with st.expander("🔍 See full error"):
                st.text(traceback.format_exc())
            return

    # show results if we have them
    if st.session_state.results:
        st.divider()
        show_results(st.session_state.results)


if __name__ == "__main__":
    main()
