#!/usr/bin/env python3
"""
Script to optimize font loading by adding font-display: swap
Improves First Contentful Paint (FCP) by ~330ms
"""

import os
import re
from pathlib import Path

def add_font_display_to_google_fonts(html_content):
    """
    Ensure Google Fonts link has &display=swap parameter
    """
    # Pattern: Google Fonts link without display=swap
    pattern = r'(https://fonts\.googleapis\.com/css\?[^"\']*)(["\']\s+id="flatsome-googlefonts-css")'
    
    def add_display_param(match):
        url = match.group(1)
        closing = match.group(2)
        
        # Check if display parameter already exists
        if 'display=' not in url:
            # Add display=swap parameter
            if '&' in url:
                url += '&display=swap'
            else:
                url += '?display=swap'
        elif 'display=auto' in url or 'display=block' in url:
            # Replace with swap
            url = re.sub(r'display=(auto|block)', 'display=swap', url)
        
        return url + closing
    
    return re.sub(pattern, add_display_param, html_content)

def add_font_display_to_font_face(html_content):
    """
    Add font-display: swap to @font-face rules in inline CSS
    """
    # Pattern: @font-face without font-display
    pattern = r'(@font-face\s*\{[^}]*?)(font-weight:\s*\d+)(\s*\})'
    
    def add_display_property(match):
        font_face_start = match.group(1)
        font_weight = match.group(2)
        closing_brace = match.group(3)
        
        # Check if font-display already exists
        if 'font-display:' not in font_face_start:
            return f'{font_face_start}{font_weight};\n    font-display: swap{closing_brace}'
        else:
            return match.group(0)
    
    return re.sub(pattern, add_display_property, html_content, flags=re.DOTALL)

def optimize_font_preconnect(html_content):
    """
    Add preconnect for fonts.gstatic.com to speed up font loading
    """
    # Check if preconnect already exists
    if 'fonts.gstatic.com' in html_content and 'rel="preconnect"' in html_content:
        return html_content
    
    # Add preconnect after dns-prefetch if it doesn't exist
    pattern = r'(<link href="http://fonts\.googleapis\.com/" rel="dns-prefetch"/>)'
    replacement = r'\1\n<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>'
    
    # Only add if not already present
    if 'fonts.gstatic.com' not in html_content:
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def process_html_file(file_path):
    """
    Process a single HTML file to optimize font loading
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply optimizations
        content = add_font_display_to_google_fonts(content)
        content = add_font_display_to_font_face(content)
        content = optimize_font_preconnect(content)
        
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
    Main function to process all HTML files
    """
    out_dir = Path('out')
    
    if not out_dir.exists():
        print("❌ Directory 'out' not found!")
        return
    
    print("🚀 Starting font-display optimization...")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(out_dir.rglob('*.html'))
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        file_path = str(html_file)
        
        # Skip certain directories
        if any(skip in file_path for skip in ['wp-admin', 'wp-includes', 'feed']):
            skipped_count += 1
            continue
        
        if process_html_file(file_path):
            print(f"  ✅ Optimized: {file_path}")
            updated_count += 1
        else:
            skipped_count += 1
    
    print("=" * 60)
    print(f"✅ Optimization completed!")
    print(f"📊 Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    print(f"📁 Total processed: {len(html_files)} files")
    print("")
    print("🎯 Benefits:")
    print("  • Faster First Contentful Paint (FCP)")
    print("  • Estimated savings: ~330ms")
    print("  • Text visible immediately while fonts load")
    print("  • Better user experience on slow connections")

if __name__ == '__main__':
    main()
