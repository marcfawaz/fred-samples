# Copyright Thales 2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fred_sdk.contracts.models import ReActAgentDefinition

from fred_samples_agents.bank_transfer.graph_agent import BANK_TRANSFER_AGENT
from fred_samples_agents.postal_tracking.graph_agent import POSTAL_TRACKING_AGENT
from fred_samples_agents.general_assistant import GENERAL_ASSISTANT_AGENT

def build_registry() -> dict[str, ReActAgentDefinition]:
    return {
        GENERAL_ASSISTANT_AGENT.agent_id: GENERAL_ASSISTANT_AGENT,  
        BANK_TRANSFER_AGENT.agent_id: BANK_TRANSFER_AGENT,
        POSTAL_TRACKING_AGENT.agent_id: POSTAL_TRACKING_AGENT,
    }


REGISTRY: dict[str, ReActAgentDefinition] = build_registry()
