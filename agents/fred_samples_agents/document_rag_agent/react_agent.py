from fred_sdk import (
    MCP_SERVER_KNOWLEDGE_FLOW_TEXT,
    FieldSpec,
    MCPServerRef,
    UIHints,
)
from fred_sdk.contracts.models import ReActAgentDefinition, ReActPolicy

DOCUMENT_RAG_AGENT_ID = "fred.samples.document_rag.react"

_SYSTEM_PROMPT = """\
You are a document-grounded assistant.

Search before answering factual questions.
Use retrieved evidence.
If retrieval is missing or weak, say so.
Respond in {response_language}.
Today is {today}.
"""


class DocumentRagAgentDefinition(ReActAgentDefinition):
    agent_id: str = DOCUMENT_RAG_AGENT_ID
    role: str = "Document RAG Assistant"
    description: str = (
        "Document-grounded ReAct assistant using Knowledge Flow MCP text search. "
        "The system prompt is configurable from the frontend."
    )
    tags: tuple[str, ...] = ("sample", "rag", "documents", "react", "mcp")

    system_prompt_template: str = _SYSTEM_PROMPT

    default_mcp_servers: tuple[MCPServerRef, ...] = (
        MCPServerRef(id=MCP_SERVER_KNOWLEDGE_FLOW_TEXT),
    )

    fields: tuple[FieldSpec, ...] = (
        FieldSpec(
            key="prompts.system",
            type="prompt",
            title="System prompt",
            description="Override the default document-grounded instructions.",
            required=False,
            ui=UIHints(group="Prompts", multiline=True, markdown=True, max_lines=12),
        ),
    )

    def policy(self) -> ReActPolicy:
        return ReActPolicy(system_prompt_template=self.system_prompt_template)


DOCUMENT_RAG_AGENT = DocumentRagAgentDefinition()