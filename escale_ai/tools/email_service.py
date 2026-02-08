"""
Email service interfaces and mock implementation.

This module defines an abstract base class representing an email sending service
and a mock implementation that simply logs the email contents. The outreach
agent uses this service to send cold emails to leads or to schedule follow-ups.

Usage:
    from escale_ai.tools.email_service import MockEmailService
    email_service = MockEmailService()
    email_service.send_email(to_address="example@example.com", subject="Hello", body="Hi there!")
"""

from abc import ABC, abstractmethod


class BaseEmailService(ABC):
    """Abstract base class for sending emails."""

    @abstractmethod
    def send_email(self, to_address: str, subject: str, body: str) -> None:
        """Send an email to the given address.

        Args:
            to_address: recipient's email address
            subject: subject line of the email
            body: body text of the email
        """
        raise NotImplementedError


class MockEmailService(BaseEmailService):
    """Mock email service that prints email contents instead of sending them."""

    def send_email(self, to_address: str, subject: str, body: str) -> None:
        """Pretend to send an email by printing its contents.

        Args:
            to_address: recipient's email address
            subject: subject line of the email
            body: body text of the email
        """
        print(f"Sending email to {to_address}:")
        print(f"Subject: {subject}")
        print(f"Body: {body}")


__all__ = ["BaseEmailService", "MockEmailService"]
