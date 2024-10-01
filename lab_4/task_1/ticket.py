from enum import Enum
from datetime import datetime
from typing import Dict, Callable
from tabulate import tabulate


# Enumeration for different types of tickets
class TicketType(str, Enum):
    REGULAR = "regular"
    ADVANCE = "advance"
    STUDENT = "student"
    LATER = "later"

    @classmethod
    def has_value(cls, value):
        """Check if the given value is a valid ticket type."""
        return value in cls._value2member_map_


# Enumeration for ticket price modifiers based on type
class TicketTypeModifier(float, Enum):
    REGULAR = 1
    ADVANCE = 1 - 0.7
    STUDENT = 1 - 0.5
    LATER = 1 + 0.2


# Class representing a ticket
class Ticket:
    # Constants for ticket pricing and purchase requirements
    REGULAR_MULTIPLIER = 100
    ADVANCE_DAYS_REQUIRED = 90
    LATER_DAYS_LIMIT = 7
    DEFAULT_DATE_FORMAT = "%Y-%m-%d"

    def __validate_ticket_type(self, ticket_type) -> TicketType:
        """Validate and return a TicketType instance from a given ticket_type value."""
        if isinstance(ticket_type, TicketType) or TicketType.has_value(ticket_type):
            return (
                ticket_type
                if isinstance(ticket_type, TicketType)
                else TicketType(ticket_type)
            )
        else:
            raise ValueError("Invalid ticket type.")

    def __validate_advance_ticket(self, days_before_event: int) -> None:
        """Ensure advance tickets are purchased at least 90 days before the event."""
        if days_before_event < Ticket.ADVANCE_DAYS_REQUIRED:
            raise ValueError(
                "Advance tickets must be purchased 90 days or more before the event."
            )

    def __validate_later_ticket(self, days_before_event: int) -> float:
        """Ensure later tickets are purchased less than 7 days before the event."""
        if days_before_event >= Ticket.LATER_DAYS_LIMIT:
            raise ValueError(
                "Later purchased tickets must be purchased less than 7 days before the event."
            )

    def __convert_time(self, time: str) -> datetime:
        """Convert a string date to a datetime object."""
        return datetime.strptime(time[:10], Ticket.DEFAULT_DATE_FORMAT)

    def __init__(
        self, ticket_number, ticket_type, purchase_date, event_date, regular_price
    ):
        # Initialize ticket with validation
        ticket_type = self.__validate_ticket_type(ticket_type)
        purchase_date = self.__convert_time(purchase_date)
        event_date = self.__convert_time(event_date)
        days_before_event = (event_date - purchase_date).days

        # Validate ticket based on type and purchase date
        if ticket_type == TicketType.ADVANCE:
            self.__validate_advance_ticket(days_before_event)
        elif ticket_type == TicketType.LATER:
            self.__validate_later_ticket(days_before_event)

        self.ticket_number = ticket_number
        self.ticket_type = ticket_type
        self.purchase_date = purchase_date
        self.event_date = event_date
        self.regular_price = regular_price

    def get_price(self) -> float:
        """Calculate and return the ticket price based on its type and the regular price."""
        base_price = self.regular_price * Ticket.REGULAR_MULTIPLIER

        # Dictionary to map ticket types to their respective modifiers
        modifiers = {
            TicketType.REGULAR: TicketTypeModifier.REGULAR.value,
            TicketType.ADVANCE: TicketTypeModifier.ADVANCE.value,
            TicketType.STUDENT: TicketTypeModifier.STUDENT.value,
            TicketType.LATER: TicketTypeModifier.LATER.value,
        }

        # Retrieve the modifier based on the ticket type
        modifier = modifiers.get(self.ticket_type)

        if modifier is None:
            raise ValueError("Invalid ticket type.")

        return base_price * modifier

    def print(self) -> None:
        """Print ticket details in a tabulated format."""
        table = [
            ["Ticket Number", self.ticket_number],
            ["Ticket Type", self.ticket_type.value.capitalize()],
            ["Purchase Date", self.purchase_date.strftime(self.DEFAULT_DATE_FORMAT)],
            ["Event Date", self.event_date.strftime(self.DEFAULT_DATE_FORMAT)],
            ["Price", f"${self.get_price():.2f}"],
        ]
        print(tabulate(table))

    @classmethod
    def generate_ticket_number(cls, counter):
        """Generate a formatted ticket number based on the given counter."""
        return counter
