#!/usr/bin/env python3
"""
Remove Vietnamese language links (/vi/) from all HTML files in out/ directory.
Removes:
1. <link hreflang="vi" ... /> tags
2. Menu items with href="/vi/..." or href="vi/..."
3. Language switcher elements
"""
import re
from pathlib import Path
import sys

def clean_html(content):
    """Remove Vietnamese links from HTML content"""
    
    # Remove hreflang="vi" link tags
    content = re.sub(
        r'<link[^>]*hreflang="vi"[^>]*/?>\s*',
        '',
        content,
        flags=re.IGNORECASE
    )
    
    # Remove menu items with /vi/ links
    # Pattern: <li...><a href="/vi/...">...</a></li>
    content = re.sub(
        r'<li[^>]*>\s*<a[^>]*href=["\']/?vi/[^"\']*["\'][^>]*>.*?</a>\s*</li>\s*',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Remove standalone links to /vi/
    content = re.sub(
        r'<a[^>]*href=["\']/?vi/[^"\']*["\'][^>]*>.*?</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    return content

def process_file(filepath):
    """Process a single HTML file"""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        original_len = len(content)
        
        cleaned = clean_html(content)
        
        if len(cleaned) != original_len:
            filepath.write_text(cleaned, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
        return False

def main():
    root = Path('out')
    if not root.exists():
        print("Error: 'out' directory not found")
        return 1
    
    total = 0
    modified = 0
    
    for html_file in root.rglob('*.html'):
        # Skip backup files
        if html_file.name.endswith('.backup'):
            continue
            
        total += 1
        if process_file(html_file):
            modified += 1
            print(f"✓ Cleaned: {html_file}")
    
    print(f"\nSummary: {modified}/{total} files modified")
    return 0

if __name__ == '__main__':
    sys.exit(main())
