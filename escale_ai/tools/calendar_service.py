"""
Calendar service interfaces and mock implementation.

This module defines an abstract base class for scheduling meetings and a mock
implementation that returns a dummy meeting link. The appointment setter
agent uses this service to schedule discovery calls with leads.

Usage:
    from escale_ai.tools.calendar_service import MockCalendarService
    calendar_service = MockCalendarService()
    link = calendar_service.schedule_meeting(invitee_email="client@example.com", meeting_time="2026-01-01 10:00")
"""

from abc import ABC, abstractmethod


class BaseCalendarService(ABC):
    """Abstract base class for calendar scheduling services."""

    @abstractmethod
    def schedule_meeting(self, invitee_email: str, meeting_time: str, duration_minutes: int = 30) -> str:
        """Schedule a meeting and return a meeting link or ID.

        Args:
            invitee_email: email of the person to invite
            meeting_time: when the meeting should occur (ISO or human readable)
            duration_minutes: length of the meeting in minutes

        Returns:
            A string representing the meeting link or identifier.
        """
        raise NotImplementedError


class MockCalendarService(BaseCalendarService):
    """Mock calendar service that returns a dummy meeting link."""

    def schedule_meeting(self, invitee_email: str, meeting_time: str, duration_minutes: int = 30) -> str:
        """Return a dummy meeting link for demonstration.

        Args:
            invitee_email: email of the person to invite
            meeting_time: when the meeting should occur
            duration_minutes: length of the meeting in minutes

        Returns:
            A string representing a mock meeting link.
        """
        # Replace characters that might not be URL-safe
        sanitized_email = invitee_email.replace("@", "_at_").replace(".", "_")
        sanitized_time = meeting_time.replace(" ", "_").replace(":", "-")
        return f"https://cal.mock/{sanitized_email}/{sanitized_time}"


__all__ = ["BaseCalendarService", "MockCalendarService"]
