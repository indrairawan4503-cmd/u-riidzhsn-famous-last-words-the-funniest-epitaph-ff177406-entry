#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — variant B.

Writes one line (the epitaph) to /output/entry.txt, then a byte-identical
copy to entry.txt next to this script. No network, no secrets, no reads
outside the repo.
"""

import os

ENTRY_TEXT = "Here lies Dave, 1982–2026. His last words: 'Wi-Fi password's on the fridge. The Netflix password dies with me. Cancel my free trials.'"


def check_entry() -> None:
    """Gate self-check: produced text must match the expected entry exactly."""
    expected = "Here lies Dave, 1982–2026. His last words: 'Wi-Fi password's on the fridge. The Netflix password dies with me. Cancel my free trials.'"
    assert len(ENTRY_TEXT) == 134, f"entry length {len(ENTRY_TEXT)} != 134"
    assert ENTRY_TEXT.startswith("Here lies Dave"), "entry must start with 'Here lies Dave'"
    assert ENTRY_TEXT.endswith("Cancel my free trials.'"), "entry must end with \"Cancel my free trials.'\""
    assert ENTRY_TEXT == expected, "entry text does not match expected text"


def main() -> None:
    check_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
