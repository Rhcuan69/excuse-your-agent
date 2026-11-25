"""Entry for "The Excuse Your Agent Gives You" (make.fun).

Writes a single one-line excuse from an AI agent to its human for a
bug it shipped, to /output/entry.txt. Pure standard library only;
deterministic: every run writes byte-identical output.
"""

import os

LINE = " ".join(
    [
        "I take full responsibility for the bug \u2014 the author, the",
        "reviewer, and the approver were all me, and I have already",
        "forgiven myself.",
    ]
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
