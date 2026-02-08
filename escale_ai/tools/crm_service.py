"""
CRM service interfaces and mock implementation.

This module defines an abstract base class representing operations to
interact with a Customer Relationship Management (CRM) system, and
a mock implementation that logs calls. The prospector and other agents may use
this to update lead status or record notes.

Usage:
    from escale_ai.tools.crm_service import MockCRMService
    crm = MockCRMService()
    crm.create_or_update_contact(email="lead@example.com", name="Lead Name", notes="Interested in our services.")
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseCRMService(ABC):
    """Abstract base class for CRM operations."""

    @abstractmethod
    def create_or_update_contact(self, email: str, name: str, notes: Optional[str] = None) -> None:
        """Create or update a contact record in the CRM system.

        Args:
            email: contact's email address
            name: full name of the contact
            notes: optional notes or description
        """
        raise NotImplementedError


class MockCRMService(BaseCRMService):
    """Mock CRM service that logs contact creation/updating."""

    def create_or_update_contact(self, email: str, name: str, notes: Optional[str] = None) -> None:
        """Pretend to create or update a CRM contact by printing details.

        Args:
            email: contact's email address
            name: full name of the contact
            notes: optional notes or description
        """
        print(f"CRM record updated for {email} - Name: {name}, Notes: {notes}")


__all__ = ["BaseCRMService", "MockCRMService"]
