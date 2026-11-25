#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings to /output/entry.txt (1-200
characters, UTF-8, not only whitespace). Standard library only, no
network, no input.

The joke is built from three fragments: the setup (the weekend files
a complaint about Monday morning), the turn (Monday itself answers),
and the punch (Monday closes its own ticket and promises to be back
next week). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My weekend filed a complaint about Monday morning."
TURN = "Monday answered:"
PUNCH = "'Ticket closed \u2014 see you next week.'"
SEPARATOR = " "  # single space joins setup, turn and punch

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, turn: str, punch: str, separator: str) -> str:
    """Join the three fragments into one joke line."""
    return separator.join([setup, turn, punch])


def validate(joke: str) -> str:
    """Check the joke meets the entry gate before it is written.

    Must be 1-200 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    joke.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return joke


def main() -> None:
    joke = validate(assemble(SETUP, TURN, PUNCH, SEPARATOR))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
