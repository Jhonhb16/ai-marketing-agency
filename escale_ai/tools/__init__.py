"""Interfaces and mock implementations for external services used by the AI Marketing Agency.

This package defines base interfaces for services such as lead sourcing,
email sending, calendar scheduling, and CRM interactions. Concrete
implementations can subclass these interfaces to integrate with
real providers.
"""
from .lead_source import BaseLeadSource, MockLeadSource
from .email_service import BaseEmailService, MockEmailService
from .calendar_service import BaseCalendarService, MockCalendarService
from .crm_service import BaseCRMService, MockCRMService


__all__ = [
    "BaseLeadSource",
    "BaseEmailService",
    "BaseCalendarService",
    "BaseCRMService",
        "MockLeadSource",
    "MockEmailService",
    "MockCalendarService",
    "MockCRMService",
]
