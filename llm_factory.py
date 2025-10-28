# LLM Factory - Creates LLM instances from different providers

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# try importing the different providers
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None

try:
    from langchain_ollama import ChatOllama
except ImportError:
    ChatOllama = None

try:
    from langchain_anthropic import ChatAnthropic
except ImportError:
    ChatAnthropic = None


class LLMFactory:
    """Factory for creating LLMs"""

    @staticmethod
    def create_ollama(model_name: str = "llama2"):
        """Create Ollama LLM with timeout"""
        if ChatOllama is None:
            raise ImportError(
                "langchain-ollama not installed. Run: pip install langchain-ollama")
        # lower temp for faster, more focused responses
        return ChatOllama(model=model_name, temperature=0.3, timeout=300)

    @staticmethod
    def create_openai(model_name: str = "gpt-3.5-turbo"):
        """Create OpenAI LLM"""
        if ChatOpenAI is None:
            raise ImportError(
                "langchain-openai not installed. Run: pip install langchain-openai")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Set it in .env file.")
        # set the key in environment
        os.environ["OPENAI_API_KEY"] = api_key
        return ChatOpenAI(model=model_name, temperature=0.7)

    @staticmethod
    def create_anthropic(model_name: str = "claude-3-sonnet-20240229"):
        """Create Anthropic LLM"""
        if ChatAnthropic is None:
            raise ImportError(
                "langchain-anthropic not installed. Run: pip install langchain-anthropic")
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. Set it in .env file.")
        # set the key in environment
        os.environ["ANTHROPIC_API_KEY"] = api_key
        return ChatAnthropic(model=model_name, temperature=0.7)

    @staticmethod
    def create_llm(provider: str, model_name: Optional[str] = None):
        """Create an LLM based on provider"""
        if provider == "ollama":
            model_name = model_name or "llama2"
            return LLMFactory.create_ollama(model_name)
        elif provider == "openai":
            model_name = model_name or "gpt-3.5-turbo"
            return LLMFactory.create_openai(model_name)
        elif provider == "anthropic":
            model_name = model_name or "claude-3-sonnet-20240229"
            return LLMFactory.create_anthropic(model_name)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    @staticmethod
    def get_available_providers():
        """Get list of available providers"""
        providers = []
        if ChatOllama is not None:
            providers.append("ollama")
        if ChatOpenAI is not None:
            providers.append("openai")
        if ChatAnthropic is not None:
            providers.append("anthropic")
        return providers
