from fred_sdk import FieldSpec, UIHints
from fred_sdk.contracts.models import ReActAgentDefinition, ReActPolicy

PARAMETERIZED_REACT_AGENT_ID = "fred.samples.parameterized_react"

_SYSTEM_PROMPT_TEMPLATE = """\
You are a configurable Fred sample assistant.

Configuration selected by the user:
- Answer style: {settings_answer_style}
- Response language: {response_language}

Behavior:
- Be direct and practical.
- Adapt the level of detail to the selected answer style.
- If the answer depends on current or external facts, say that you cannot verify them from this sample agent alone.

Today is {today}.
"""


class ParameterizedReActAgentDefinition(ReActAgentDefinition):
    agent_id: str = PARAMETERIZED_REACT_AGENT_ID
    role: str = "Parameterized ReAct assistant"
    description: str = (
        "Minimal sample showing how to expose agent-owned parameters in the "
        "Fred frontend using FieldSpec and UIHints."
    )
    tags: tuple[str, ...] = ("sample", "react", "parameters", "frontend")
    system_prompt_template: str = _SYSTEM_PROMPT_TEMPLATE

    fields: tuple[FieldSpec, ...] = (
        FieldSpec(
            key="prompts.system",
            type="prompt",
            title="System prompt",
            description="Optional override for the default system prompt.",
            required=False,
            ui=UIHints(
                group="Prompts",
                multiline=True,
                markdown=True,
                max_lines=12,
            ),
        ),
        FieldSpec(
            key="settings.answer_style",
            type="string",
            title="Answer style",
            description="Controls how concise or detailed the assistant should be.",
            enum=("concise", "balanced", "detailed"),
            default="balanced",
            required=False,
            ui=UIHints(group="Settings"),
        ),
    )

    def policy(self) -> ReActPolicy:
        return ReActPolicy(system_prompt_template=self.system_prompt_template)


PARAMETERIZED_REACT_AGENT = ParameterizedReActAgentDefinition()