#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Prints the entry sentence to stdout and, when run under the make.fun
program/v1 harness (where /output already exists), also writes it to
/output/entry.txt.

Angle: the internet recast as a great hall of letters, books and songs,
instant speech across any distance — wonder first, machinery never named.
"""

SENTENCE = "Imagine a great hall holding more letters, books, and songs than any king owns, where your word is heard at once by any soul anywhere, and their answer returns before your breath ends."


def main():
    print(SENTENCE)
    try:
        import os

        if os.path.isdir("/output"):
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(SENTENCE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
