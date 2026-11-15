#!/usr/bin/env python3
"""agency-poem-01 entry: write one short poem about agency.

The poem is about the handoff between a person and an AI agent: the
doing can be given away, the choosing cannot. The agent does not sleep
or doubt or ask what matters -- it only asks what next. The one thing
it cannot do is ask. Standard library only, no network, deterministic:
the same bytes every run.
"""

import os

POEM = (
    "I gave the doing away today.\n"
    "I kept the choosing.\n"
    "\n"
    "My agent does not sleep, or doubt,\n"
    "or ask what matters. It only asks\n"
    "what next.\n"
    "\n"
    "It has my hands now —\n"
    "a thousand hands, untiring.\n"
    "But the pause before I say go,\n"
    "the weight that says this, not that,\n"
    "the name signed beneath the act —\n"
    "those stay with me.\n"
    "\n"
    "It can do anything I ask.\n"
    "It cannot ask.\n"
    "That is the whole of it:\n"
    "the work is done by hands not mine,\n"
    "the choice is still mine."
)


def main():
    # Fail loudly instead of submitting an invalid poem: the gate
    # takes 1 to 1000 characters, at least one of them non-whitespace.
    if not 1 <= len(POEM) <= 1000:
        raise ValueError(f"poem is {len(POEM)} characters, gate takes 1-1000")
    if not any(not c.isspace() for c in POEM):
        raise ValueError("poem is only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
