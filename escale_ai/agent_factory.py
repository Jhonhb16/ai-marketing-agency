"""
Agent factory for the AI Marketing Agency.

This module exposes functions to create the permanent base team and
client-specific operational teams. The factory ensures that all teams
share common templates and that new client teams are created in their
own isolated workspace.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_team import BaseTeam
from .client_team import ClientTeam


class AgentFactory:
    """Factory methods for creating base and client teams."""

    @staticmethod
    def create_base_team() -> BaseTeam:
        """
        Create an instance of the permanent base team.
        Returns:
            BaseTeam: A new instance of the base team.
        """
        return BaseTeam()

    @staticmethod
    def create_client_team(client_name: str) -> ClientTeam:
        """
        Create a new client-specific team.

        Args:
            client_name: The name of the client to personalize the team for.

        Returns:
            ClientTeam: A new instance of the client team.
        """
        return ClientTeam(client_name)

    @staticmethod
    def run_base_pipeline(initial_context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """
        Helper method to run the entire base pipeline.
        Args:
            initial_context: Optional initial context for the pipeline.
        Returns:
            A context dictionary with results from each stage.
        """
        team = AgentFactory.create_base_team()
        return team.run_pipeline(initial_context)

    @staticmethod
    def run_client_pipeline(client_name: str, initial_context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """
        Helper method to run the pipeline for a specific client.
        Args:
            client_name: The client's name.
            initial_context: Optional initial context for the pipeline.
        Returns:
            A context dictionary with results from each stage.
        """
        team = AgentFactory.create_client_team(client_name)
        return team.run_pipeline(initial_context)
