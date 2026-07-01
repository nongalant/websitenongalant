from pathlib import Path
import re

folder = Path("svg")

for file in folder.glob("*.svg"):

    text = file.read_text(encoding="utf-8")

    # replace fixed stroke colors/widths with CSS variables
    text = re.sub(
        r"stroke:\s*#[0-9a-fA-F]{6}",
        "stroke:var(--outline-color)",
        text
    )

    text = re.sub(
        r"stroke-width:\s*[\d.]+",
        "stroke-width:var(--outline-width)",
        text
    )

    file.write_text(
        text,
        encoding="utf-8"
    )

    print("Fixed:", file.name)

print("Done")