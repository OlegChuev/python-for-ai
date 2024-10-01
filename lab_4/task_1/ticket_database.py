import json
import os
from typing import Optional, Union
from ticket import Ticket, TicketType


class TicketDatabase:
    def __init__(self, file_path: str):
        """
        Initialize the TicketDatabase with the given file path.
        Loads existing tickets from the file and calculates the next available ID.
        """
        self.file_path = file_path
        self.tickets = self.load_tickets()
        self._id_counter = self.__calculate_next_id()

    def load_tickets(self) -> list:
        """
        Load tickets from the file. If the file does not exist or contains invalid JSON,
        initialize with an empty list of tickets.
        """
        if not os.path.exists(self.file_path):
            print("Ticket database file not found. Creating a new file...")
            # Create an empty file with an empty JSON array
            with open(self.file_path, "w") as file:
                json.dump([], file)
            return []

        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                # Convert JSON data to Ticket objects
                return [Ticket(**ticket) for ticket in data]
        except json.JSONDecodeError:
            print(
                "Error decoding JSON from the ticket database file. Initializing with an empty database."
            )
            return []

    def __calculate_next_id(self) -> int:
        """
        Calculate the next available ticket ID based on the existing tickets.
        """
        if self.tickets:
            last_ticket_number = max(ticket.ticket_number for ticket in self.tickets)
            return int(last_ticket_number) + 1
        return 1

    def save_tickets(self) -> None:
        """
        Save the current list of tickets to the file as a formatted JSON array.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(
                    [ticket.__dict__ for ticket in self.tickets],
                    file,
                    default=str,
                    indent=4,
                )
        except IOError as e:
            print(f"Error saving tickets to file: {e}")

    def find_ticket_by_number(self, ticket_number: str) -> Optional["Ticket"]:
        """
        Find and return a ticket by its number. Returns None if not found.
        """
        return next(
            (
                ticket
                for ticket in self.tickets
                if str(ticket.ticket_number) == ticket_number
            ),
            None,
        )

    def add_ticket(
        self,
        ticket_type: TicketType,
        purchase_date: str,
        event_date: str,
        regular_price: float,
    ) -> "Ticket":
        """
        Create and add a new ticket to the database.
        Generates a new ticket number and saves the updated list of tickets to the file.
        """
        ticket_number = Ticket.generate_ticket_number(self._id_counter)
        new_ticket = Ticket(
            ticket_number=ticket_number,
            ticket_type=ticket_type,
            purchase_date=purchase_date,
            event_date=event_date,
            regular_price=regular_price,
        )
        self.tickets.append(new_ticket)
        self._id_counter += 1
        self.save_tickets()
        return new_ticket
