#!/usr/bin/env python3
"""
Inject footer logo snippet into all static HTML files under out/ that do not already contain it.

Strategy:
- Scan out/ recursively for *.html
- Skip backup variants containing '@p=' with '.backup' suffix
- For each file, detect if marker <!-- footer-logo --> already present; if yes, skip
- Insert snippet just before closing </body>. If </body> not present, append at end.
- Provide --dry-run option to only report planned changes
- Provide --limit option for testing
"""
import argparse
import os
import sys
from pathlib import Path

LOGO_RELATIVE_PATH = "/wp-content/uploads/2023/08/logo-dr-anmytas-white.svg"
MARKER = "<!-- footer-logo -->"
SNIPPET = f"""
    {MARKER}\n    <div class=\"footer-logo\" style=\"margin:40px 0;text-align:center;\">\n        <a href=\"/\" aria-label=\"Logo\">\n            <img src=\"{LOGO_RELATIVE_PATH}\" alt=\"Dr Anmytas Logo\" style=\"max-width:220px;height:auto;\" loading=\"lazy\" />\n        </a>\n    </div>\n""".strip()+"\n"


def find_html_files(root: Path):
    for p in root.rglob('*.html'):
        # Skip backup versions
        if p.name.endswith('.backup'):
            continue
        yield p

def process_file(path: Path, dry_run: bool) -> bool:
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"[ERROR] Cannot read {path}: {e}", file=sys.stderr)
        return False
    if MARKER in content:
        return False  # already injected

    # Decide insertion point
    lower = content.lower()
    insert_index = lower.rfind('</body>')
    if insert_index == -1:
        # append
        new_content = content + '\n' + SNIPPET
    else:
        new_content = content[:insert_index] + SNIPPET + content[insert_index:]

    if dry_run:
        print(f"[DRY] Would inject logo into: {path}")
        return True
    try:
        path.write_text(new_content, encoding='utf-8')
        print(f"[OK] Injected logo into: {path}")
        return True
    except Exception as e:
        print(f"[ERROR] Cannot write {path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Inject footer logo into static HTML files")
    parser.add_argument('--root', default='out', help='Root directory containing exported static HTML')
    parser.add_argument('--dry-run', action='store_true', help='Only show what would change')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of files modified (0 = no limit)')
    args = parser.parse_args()

    root_path = Path(args.root)
    if not root_path.exists():
        print(f"[FATAL] Root path not found: {root_path}")
        return 2

    total = 0
    changed = 0
    for html_file in find_html_files(root_path):
        total += 1
        if args.limit and changed >= args.limit:
            break
        modified = process_file(html_file, args.dry_run)
        if modified:
            changed += 1

    print(f"Summary: scanned={total} changed={changed} dry_run={args.dry_run}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
