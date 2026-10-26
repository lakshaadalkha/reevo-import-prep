"""Build the page from the template and the sample HubSpot export.

index.html       artifact version (Claude adds the document skeleton on publish)
docs/index.html  standalone version for GitHub Pages
"""
from pathlib import Path

root = Path(__file__).parent
template = (root / "src" / "index.template.html").read_text(encoding="utf-8")
sample = (root / "sample-data" / "hubspot_export.csv").read_text(encoding="utf-8")

if "</script" in sample.lower():
    raise SystemExit("Sample CSV contains '</script' and can't be embedded as-is.")

page = template.replace("__SAMPLE_CSV__", sample)
(root / "index.html").write_text(page, encoding="utf-8")

head, sep, body = page.partition("</style>")
standalone = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n"
    + head + sep + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(standalone, encoding="utf-8")
print("Built index.html and docs/index.html")
