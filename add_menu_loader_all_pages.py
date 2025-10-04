#!/usr/bin/env python3
"""
Add menu-loader.js script to all HTML files in out/ directory
This ensures consistent menu across all pages
"""

import os
import re
from pathlib import Path

def add_menu_loader_to_html(file_path):
    """Add menu-loader.js script tag before </body> if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if menu-loader.js is already included
        if 'menu-loader.js' in content:
            print(f"✓ Already has menu-loader.js: {file_path}")
            return False
        
        # Find </body> tag
        if '</body>' not in content:
            print(f"⚠ No </body> tag found: {file_path}")
            return False
        
        # Add script tag before </body>
        menu_loader_script = '<script src="/shared/menu-loader.js"></script>\n</body>'
        content = content.replace('</body>', menu_loader_script)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added menu-loader.js to: {file_path}")
        return True
    
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Process all HTML files in out/ directory"""
    out_dir = Path('out')
    
    if not out_dir.exists():
        print("❌ Error: 'out' directory not found!")
        return
    
    # Find all HTML files
    html_files = list(out_dir.rglob('*.html'))
    
    print(f"📊 Found {len(html_files)} HTML files")
    print("=" * 60)
    
    added_count = 0
    skipped_count = 0
    error_count = 0
    
    for html_file in html_files:
        result = add_menu_loader_to_html(html_file)
        if result is True:
            added_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1
    
    print("=" * 60)
    print(f"📊 SUMMARY:")
    print(f"   ✅ Added: {added_count} files")
    print(f"   ✓ Skipped (already has): {skipped_count} files")
    print(f"   ❌ Errors: {error_count} files")
    print(f"   📁 Total processed: {len(html_files)} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
