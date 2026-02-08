"""
Lead source service interfaces and mock implementation.

This module defines the base class for a lead source service used by the prospector.
A lead source service is responsible for retrieving potential client leads from
external databases or APIs. It also includes a simple mock implementation for development
and testing purposes.

Usage:
    from escale_ai.tools.lead_source import MockLeadSource
    leads = MockLeadSource().fetch_leads(limit=10)
"""

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseLeadSource(ABC):
    """Abstract base class for lead source services."""

    @abstractmethod
    def fetch_leads(self, limit: int = 10) -> List[Dict[str, str]]:
        """Fetch a list of lead dictionaries.

        Each lead dictionary should include at least 'name' and 'contact' keys.

        Args:
            limit: maximum number of leads to return.

        Returns:
            A list of dictionaries representing potential leads.
        """
        raise NotImplementedError


class MockLeadSource(BaseLeadSource):
    """A simple mock lead source used for testing and development."""

    def fetch_leads(self, limit: int = 10) -> List[Dict[str, str]]:
        """Return dummy leads for demonstration.

        Args:
            limit: maximum number of leads to return.

        Returns:
            List of dictionaries with 'name' and 'contact' fields.
        """
        return [
            {"name": f"Lead {i+1}", "contact": f"lead{i+1}@example.com"}
            for i in range(limit)
        ]


__all__ = ["BaseLeadSource", "MockLeadSource"]
