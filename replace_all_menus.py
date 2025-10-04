#!/usr/bin/env python3
"""
Script to replace hardcoded menu with empty div in all HTML pages
Let menu-loader.js inject the shared menu component
"""

import os
import re
from pathlib import Path

def replace_menu_in_file(file_path):
    """Replace hardcoded menu with empty div in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the menu section
        # Looking for: <div class="header-bottom wide-nav ... id="wide-nav">...</div>
        # Up to the closing </header> or next major div
        
        # Find the menu start
        menu_start_pattern = r'(<div class="header-bottom[^>]*id="wide-nav"[^>]*>)'
        
        if not re.search(menu_start_pattern, content):
            return False, "No menu found with id='wide-nav'"
        
        # Pattern to match the entire menu block until the next closing div at same level
        # This matches from <div class="header-bottom... id="wide-nav"> to its closing </div>
        menu_pattern = r'<div class="header-bottom[^>]*id="wide-nav"[^>]*>.*?</div>\s*</div>\s*</div>'
        
        # Replacement: empty div with comment
        replacement = '<!-- Menu will be loaded by menu-loader.js -->\n<div class="header-bottom wide-nav flex-has-center hide-for-medium" id="wide-nav"></div>'
        
        # Try to replace
        new_content, count = re.subn(menu_pattern, replacement, content, flags=re.DOTALL)
        
        if count == 0:
            return False, "Pattern not matched"
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Replaced {count} menu(s)"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to process all HTML files"""
    out_dir = Path(__file__).parent / 'out'
    
    # Find all index.html files (excluding special ones)
    html_files = []
    for root, dirs, files in os.walk(out_dir):
        # Skip certain directories
        skip_dirs = {'wp-content', 'wp-includes', 'wp-json', 'feed', 'shared'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.html') and file != 'index.html@p=2437.html':  # Skip specific files if needed
                html_files.append(Path(root) / file)
    
    print(f"📊 Found {len(html_files)} HTML files")
    print("=" * 60)
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for html_file in html_files:
        rel_path = html_file.relative_to(out_dir)
        
        # Skip files that already have the empty menu div
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if '<!-- Menu will be loaded by menu-loader.js -->' in content:
                print(f"⏭️  SKIP: {rel_path} (already updated)")
                skip_count += 1
                continue
        
        success, message = replace_menu_in_file(html_file)
        
        if success:
            print(f"✅ SUCCESS: {rel_path}")
            success_count += 1
        else:
            if "No menu found" in message:
                print(f"⚠️  SKIP: {rel_path} (no menu)")
                skip_count += 1
            else:
                print(f"❌ ERROR: {rel_path} - {message}")
                error_count += 1
    
    print("=" * 60)
    print(f"\n📈 SUMMARY:")
    print(f"  ✅ Successfully replaced: {success_count}")
    print(f"  ⏭️  Skipped: {skip_count}")
    print(f"  ❌ Errors: {error_count}")
    print(f"  📊 Total processed: {len(html_files)}")

if __name__ == "__main__":
    main()
