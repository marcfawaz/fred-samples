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

"""
State models for the postal tracking graph sample.

Why this module exists:
- keep the graph input/state schema explicit and typed
- capture map, pickup point, and tracking fields in one place so steps stay small

How to use it:
- reference PostalTrackingInput as the GraphAgent input schema
- reference PostalTrackingState as the GraphAgent state schema

Conversation continuity:
- tracking_id is carried across turns by PostalTrackingGraphAgent.build_turn_state
- this means "Track that parcel" on a second turn works without re-providing the id
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class PostalTrackingInput(BaseModel):
    """
    User input for the postal tracking graph.

    Why this exists:
    - the graph runtime needs a stable input schema for validation
    - a single message field keeps the sample minimal and easy to test

    How to use it:
    - send the user message via the `message` field
    """

    message: str = Field(..., description="Latest user message.")


class PostalTrackingState(BaseModel):
    """
    Workflow state for the postal tracking sample.

    Why this exists:
    - keep cross-step data (tracking id, map inputs, pickup points) centralized
    - let the graph output include optional GeoPart data when available

    Conversation continuity:
    - tracking_id is the key field carried across turns via build_turn_state
    - steps should write only the fields they own via StepResult.state_update

    How to use it:
    - mutate only the fields your step owns via StepResult.state_update
    """

    latest_user_text: str = Field(..., description="Latest user message.")
    final_text: str | None = Field(default=None, description="Final user response.")
    done_reason: str | None = Field(default=None, description="Terminal reason tag.")

    # Carried across turns by build_turn_state — the agent remembers which parcel
    # the user was talking about without requiring them to repeat the tracking id.
    tracking_id: str | None = Field(default=None, description="Parcel tracking id.")

    wants_map: bool = Field(default=False, description="Whether a map was requested.")
    wants_pickup_points: bool = Field(
        default=False, description="Whether pickup points were requested."
    )
    wants_reroute: bool = Field(
        default=False, description="Whether the user asked to reroute to pickup."
    )

    business_track: dict[str, Any] | None = Field(
        default=None, description="Response from track_package (postal MCP)."
    )
    iot_snapshot: dict[str, Any] | None = Field(
        default=None, description="Response from get_live_tracking_snapshot (IoT MCP)."
    )
    route_geometry: dict[str, Any] | None = Field(
        default=None, description="Route geometry from get_route_geometry (IoT MCP)."
    )
    route_markers: list[dict[str, Any]] = Field(
        default_factory=list, description="Markers from the IoT route geometry call."
    )
    pickup_points: list[dict[str, Any]] = Field(
        default_factory=list, description="Nearby pickup points from postal MCP."
    )

    chosen_pickup_point_id: str | None = Field(
        default=None, description="Pickup point selected during reroute confirmation."
    )
    ui_geojson: dict[str, Any] | None = Field(
        default=None, description="GeoJSON payload for GeoPart rendering."
    )
