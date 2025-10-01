#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to decouple static site from WordPress
- Remove WordPress admin references
- Replace localhost URLs with relative paths
- Remove unnecessary WordPress scripts
"""

import re
import os
import glob

def clean_wordpress_references(html_content):
    """Remove WordPress-specific references from HTML content"""
    
    # Remove localhost:8888 URLs
    html_content = re.sub(r'http://localhost:8888/', '', html_content)
    
    # Remove wp-admin URLs
    html_content = re.sub(r'\/wp-admin\/admin-ajax\.php[^"\']*', '', html_content)
    
    # Remove WordPress meta tags
    html_content = re.sub(r'<meta name="generator" content="WordPress[^>]*>', '', html_content)
    
    # Remove WordPress shortlinks
    html_content = re.sub(r'<link rel=["\']shortlink["\'][^>]*>', '', html_content)
    
    # Remove REST API links
    html_content = re.sub(r'<link rel=["\']https://api\.w\.org/[^>]*>', '', html_content)
    
    # Remove RSD link
    html_content = re.sub(r'<link rel=["\']EditURI["\'][^>]*>', '', html_content)
    
    # Remove pingback
    html_content = re.sub(r'<link rel=["\']pingback["\'][^>]*>', '', html_content)
    
    # Remove admin bar scripts
    html_content = re.sub(r'<script[^>]*admin-bar[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    
    # Remove WooCommerce and WordPress JavaScript variables (handle nested objects)
    html_content = re.sub(r'var wc_add_to_cart_params = \{.*?\};', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'var woocommerce_params = \{.*?\};', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'var wc_order_attribution = \{.*?\};', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'var flatsomeVars = \{.*?\};(?=\s*</script>)', '', html_content, flags=re.DOTALL)
    
    # Remove wp-admin references in JSON/JavaScript configs
    html_content = re.sub(r'"\/wp-admin\/[^"]*"', '""', html_content)
    html_content = re.sub(r"'\/wp-admin\/[^']*'", "''", html_content)
    html_content = re.sub(r'\\\/wp-admin\\\/[^\\"]*', '', html_content)
    
    return html_content

def process_html_file(filepath):
    """Process a single HTML file"""
    print(f"Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean WordPress references
        cleaned_content = clean_wordpress_references(content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"✓ Cleaned: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all HTML files"""
    print("=" * 60)
    print("Decoupling Static Site from WordPress")
    print("=" * 60)
    
    # Process static-site directory
    static_dir = "/Users/Nguyen.vs/Documents/DrAnmytasUs/static-site"
    html_files = glob.glob(os.path.join(static_dir, "**/*.html"), recursive=True)
    
    total = len(html_files)
    success = 0
    
    print(f"\nFound {total} HTML files to process\n")
    
    for filepath in html_files:
        if process_html_file(filepath):
            success += 1
    
    print("\n" + "=" * 60)
    print(f"Processing complete: {success}/{total} files successfully cleaned")
    print("=" * 60)
    
    # Also process out directory if it exists
    out_dir = "/Users/Nguyen.vs/Documents/DrAnmytasUs/out"
    if os.path.exists(out_dir):
        print("\nProcessing 'out' directory...")
        out_files = glob.glob(os.path.join(out_dir, "**/*.html"), recursive=True)
        for filepath in out_files:
            process_html_file(filepath)

if __name__ == "__main__":
    main()
