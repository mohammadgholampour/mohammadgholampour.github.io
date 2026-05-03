#!/usr/bin/env python3
"""Render static résumé HTML to PDF via WeasyPrint (Lunaya image has dependencies).

Uses the repo root as base URL so ``fonts/*.ttf`` and relative links resolve inside HTML/CSS.

docker compose -f docker-compose.dev.yml run --rm --no-deps \\
  -v /path/to/mohammadgholampour.github.io:/resume \\
  lunaya-api python /resume/scripts/render_resume_pdf.py \\
    --html /resume/resume-fa.html \\
    --output /resume/Mohammad_Gholampour_Resume_FA.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from weasyprint import HTML


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument(
        "--base",
        type=Path,
        default=None,
        help="Filesystem root for resolving relative URLs (default: resume repo root inferred from ./fonts next to HTML's parent)",
    )
    args = ap.parse_args()

    html_path = args.html.expanduser().resolve()
    if not html_path.is_file():
        raise SystemExit(f"HTML not found: {html_path}")

    if args.base is not None:
        base = args.base.expanduser().resolve()
    else:
        base = html_path.parent
        if not (base / "fonts").is_dir():
            base = html_path.parent.parent

    missing = []
    for name in (
        "NotoSansArabic-Regular.ttf",
        "NotoSansArabic-Bold.ttf",
        "NotoSans-Regular.ttf",
        "NotoSans-Bold.ttf",
    ):
        if not (base / "fonts" / name).is_file():
            missing.append(f"fonts/{name}")
    if missing:
        raise SystemExit(f"Bundled fonts missing under {base}: {', '.join(missing)}")

    base_uri = base.as_uri().rstrip("/") + "/"

    args.output.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(html_path), base_url=base_uri).write_pdf(target=str(args.output.resolve()))


if __name__ == "__main__":
    main()
