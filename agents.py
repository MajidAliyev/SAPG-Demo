# SAPG Agents - Draft, Critique, and Revision agents

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from typing import Dict, Any


class Agent:
    """Base class for all agents"""

    def __init__(self, llm, name: str):
        self.llm = llm
        self.name = name

    def get_chain(self, template: PromptTemplate):
        # build the chain for processing
        return (
            RunnablePassthrough()
            | template
            | self.llm
            | StrOutputParser()
        )


class DraftAgent(Agent):
    """Generates the initial draft/solution"""

    def __init__(self, llm, protocol_template: str):
        super().__init__(llm, "Draft Agent")
        self.protocol_template = protocol_template

    def create_prompt_template(self) -> PromptTemplate:
        return PromptTemplate(
            input_variables=["user_request"],
            template=f"""You are {self.name}.

PROTOCOL: {self.protocol_template}

TASK:
{{user_request}}

Provide a concise, step-by-step plan. Be specific and actionable.""",
        )

    def generate(self, user_request: str) -> str:
        """Generate the initial draft"""
        template = self.create_prompt_template()
        chain = self.get_chain(template)
        return chain.invoke({"user_request": user_request})


class CritiqueAgent(Agent):
    """Reviews the draft for errors and issues"""

    def __init__(self, llm, protocol_template: str):
        super().__init__(llm, "Critique Agent")
        self.protocol_template = protocol_template

    def create_prompt_template(self) -> PromptTemplate:
        return PromptTemplate(
            input_variables=["user_request", "draft_output"],
            template=f"""You are {self.name}.

PROTOCOL: {self.protocol_template}

REQUEST: {{user_request}}

DRAFT: {{draft_output}}

Find these issues:
1. Logic errors or contradictions
2. Infinite loops
3. Missing error handling
4. Security issues
5. Incomplete parts

List specific issues and fixes.""",
        )

    def critique(self, user_request: str, draft_output: str) -> str:
        """Review the draft"""
        template = self.create_prompt_template()
        chain = self.get_chain(template)
        return chain.invoke({
            "user_request": user_request,
            "draft_output": draft_output
        })


class RevisionAgent(Agent):
    """Incorporates critique feedback into final output"""

    def __init__(self, llm, protocol_template: str):
        super().__init__(llm, "Revision Agent")
        self.protocol_template = protocol_template

    def create_prompt_template(self) -> PromptTemplate:
        return PromptTemplate(
            input_variables=["user_request", "draft_output", "critique"],
            template=f"""You are {self.name}.

PROTOCOL: {self.protocol_template}

REQUEST: {{user_request}}

DRAFT: {{draft_output}}

ISSUES: {{critique}}

Create the final output that:
1. Fixes all issues
2. Implements improvements
3. Is production-ready

Provide the complete corrected version.""",
        )

    def revise(self, user_request: str, draft_output: str, critique: str) -> str:
        """Generate the revised final output"""
        template = self.create_prompt_template()
        chain = self.get_chain(template)
        return chain.invoke({
            "user_request": user_request,
            "draft_output": draft_output,
            "critique": critique
        })
