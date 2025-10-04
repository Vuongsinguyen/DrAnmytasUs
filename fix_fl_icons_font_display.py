#!/usr/bin/env python3
"""
Script to change font-display: block to font-display: swap
For fl-icons font to improve FCP
"""

import os
import re
from pathlib import Path

def optimize_fl_icons_font_display(html_content):
    """
    Change fl-icons font-display from block to swap
    """
    # Pattern: font-display: block in fl-icons @font-face
    pattern = r'(@font-face\s*\{\s*font-family:\s*"fl-icons";\s*font-display:\s*)block(;)'
    replacement = r'\1swap\2'
    
    return re.sub(pattern, replacement, html_content, flags=re.DOTALL)

def process_html_file(file_path):
    """
    Process a single HTML file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply optimization
        content = optimize_fl_icons_font_display(content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        return False

def main():
    """
    Main function
    """
    out_dir = Path('out')
    
    if not out_dir.exists():
        print("❌ Directory 'out' not found!")
        return
    
    print("🚀 Starting fl-icons font-display optimization...")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(out_dir.rglob('*.html'))
    
    updated_count = 0
    
    for html_file in html_files:
        file_path = str(html_file)
        
        # Skip certain directories
        if any(skip in file_path for skip in ['wp-admin', 'wp-includes', 'feed']):
            continue
        
        if process_html_file(file_path):
            print(f"  ✅ Updated: {file_path}")
            updated_count += 1
    
    print("=" * 60)
    print(f"✅ Optimization completed!")
    print(f"📊 Updated: {updated_count} files")
    print("")
    print("🎯 Changed: font-display: block → font-display: swap")
    print("📈 Estimated FCP improvement: ~330ms")

if __name__ == '__main__':
    main()
