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
from typing imList, Dict, Optional


import csv
import os

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
class CSVLeadSource(BaseLeadSource):
    """
    Lead source that reads leads from a CSV file.
    Expects at least 'clinic_name' and 'email' columns.
    """
    def __init__(self, csv_path: Optional[str] = None):
        self.csv_path = csv_path or os.getenv("LEADS_CSV_PATH", "data/leads.csv")

    def fetch_leads(self, limit: int = 10) -> List[Dict[str, str]]:
        leads: List[Dict[str, str]] = []
        try:
            with open(self.csv_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if len(leads) >= limit:
                        break
                    name = row.get("clinic_name") or row.get("name")
                    contact = row.get("email") or row.get("contact")
                    if not name or not contact:
                        continue
                    leads.append({"name": name, "contact": contact})
        except FileNotFoundError:
            pass
        return leads

            List of dictionaries with 'name' and 'contact' fields.
        """
        return [
            {"name": f"Lead {i+1}", "contact": f"lead{i+1}@example.com"}
            for i in range(limit)
        ]


__all__ = ["BaseLeadSource", "MockLeadSource, "CSVLeadSource""]
