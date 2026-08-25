import re
from pathlib import Path

path = Path(r"index.html")

text: str = path.read_text(encoding="utf-8")

def update_version(match) -> str:
    version = int(match.group(1))
    return f"?ver={version + 1}"

text = re.sub(pattern=r"\?ver=(\d+)", repl=update_version, string=text)

path.write_text(data=text, encoding="utf-8")