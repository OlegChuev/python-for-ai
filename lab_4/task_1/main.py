from ticket_database import TicketDatabase
from ticket import TicketType


def main():
    # Initialize the ticket database
    ticket_db = TicketDatabase("db/tickets.json")

    try:
        # Add and display an advance ticket with a valid time range
        advance_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.ADVANCE,
            purchase_date="2024-06-01",
            event_date="2024-09-01",
            regular_price=50,
        )
        advance_ticket.get_price()
        advance_ticket.print()
    except ValueError as e:
        print(f"Error adding advance ticket: {e}")

    try:
        # Add and display a student ticket
        student_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.STUDENT,
            purchase_date="2024-06-01",
            event_date="2024-09-01",
            regular_price=50,
        )
        student_ticket.get_price()
        student_ticket.print()
    except ValueError as e:
        print(f"Error adding student ticket: {e}")

    try:
        # Add and display a regular ticket
        regular_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.REGULAR,
            purchase_date="2024-06-01",
            event_date="2024-09-01",
            regular_price=50,
        )
        regular_ticket.get_price()
        regular_ticket.print()
    except ValueError as e:
        print(f"Error adding regular ticket: {e}")

    try:
        # Add and display a later ticket with a valid time range
        later_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.LATER,
            purchase_date="2024-06-01",
            event_date="2024-06-05",
            regular_price=50,
        )
        later_ticket.get_price()
        later_ticket.print()
    except ValueError as e:
        print(f"Error adding later ticket: {e}")

    # Search for an existing ticket
    ticket = ticket_db.find_ticket_by_number("1")
    if ticket:
        print("Ticket found:")
        ticket.print()
    else:
        print("Ticket not found.")

    # Search for a non-existent ticket
    ticket = ticket_db.find_ticket_by_number("99")
    if ticket:
        print("Ticket found:")
        ticket.print()
    else:
        print("Ticket not found.")

    try:
        # Attempt to add and display an advance ticket with an invalid time range
        advance_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.ADVANCE,
            purchase_date="2024-06-01",
            event_date="2024-06-02",
            regular_price=50,
        )
        advance_ticket.get_price()
        advance_ticket.print()
    except ValueError as e:
        print(f"Error adding advance ticket with invalid time range: {e}")

    try:
        # Attempt to add and display a later ticket with an invalid time range
        later_ticket = ticket_db.add_ticket(
            ticket_type=TicketType.LATER,
            purchase_date="2024-06-01",
            event_date="2024-09-01",
            regular_price=50,
        )
        later_ticket.get_price()
        later_ticket.print()
    except ValueError as e:
        print(f"Error adding later ticket with invalid time range: {e}")


if __name__ == "__main__":
    main()
