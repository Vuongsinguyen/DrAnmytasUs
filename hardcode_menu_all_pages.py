#!/usr/bin/env python3
"""
Script to hardcode menu HTML into all pages (remove JavaScript injection)
Only use CSS for active state styling
"""

import os
import re
from pathlib import Path

# Menu HTML template (no nav-dark, no nav-divided classes)
MENU_HTML = '''<div class="header-bottom wide-nav flex-has-center hide-for-medium" id="wide-nav">
  <div class="flex-row container">
    <div class="flex-col hide-for-medium flex-center">
      <ul class="nav header-nav header-bottom-nav nav-center nav-size-xlarge nav-spacing-xlarge nav-uppercase">
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-2068 menu-item-design-default" id="menu-item-2068">
          <a class="nav-top-link" href="/index.html">Homepage</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2067 menu-item-design-default" id="menu-item-2067">
          <a class="nav-top-link" href="/gioi-thieu/index.html">About Us</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2065 menu-item-design-default" id="menu-item-2065">
          <a class="nav-top-link" href="/shop/index.html">Products</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2099 menu-item-design-default" id="menu-item-2099">
          <a class="nav-top-link" href="/dao-tao/index.html">Training</a>
        </li>
        <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-2070 menu-item-design-default has-dropdown" id="menu-item-2070">
          <a aria-expanded="false" aria-haspopup="menu" class="nav-top-link" href="/tin-tuc/index.html">News<i aria-hidden="true" class="icon-angle-down"></i></a>
          <ul class="sub-menu nav-dropdown nav-dropdown-simple">
            <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2069" id="menu-item-2069">
              <a href="/bi-quyet-lam-dep/index.html">Beauty Tips</a>
            </li>
          </ul>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2838 menu-item-design-default" id="menu-item-2838">
          <a class="nav-top-link" href="/canh-bao-mua-hang/index.html">Purchase Warning</a>
        </li>
        <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2066 menu-item-design-default" id="menu-item-2066">
          <a class="nav-top-link" href="/lien-he/index.html">Contact</a>
        </li>
        <li class="header-search header-search-lightbox has-icon">
          <div class="header-button"> 
            <a aria-controls="search-lightbox" aria-expanded="false" aria-haspopup="dialog" aria-label="Search" class="icon primary button round is-small" data-flatsome-role-button="" data-focus="input.search-field" data-open="#search-lightbox" href="#search-lightbox" role="button">
              <i aria-hidden="true" class="icon-search" style="font-size:16px;"></i>
            </a> 
          </div>
          <div class="mfp-hide dark text-center" id="search-lightbox">
            <div class="searchform-wrapper ux-search-box relative form-flat is-large">
              <form action="/index.html" class="searchform" method="get" role="search">
                <div class="flex-row relative">
                  <div class="flex-col flex-grow">
                    <label class="screen-reader-text" for="woocommerce-product-search-field-0">Search for:</label>
                    <input class="search-field mb-0" id="woocommerce-product-search-field-0" name="s" placeholder="Search…" type="search" value=""/>
                    <input name="post_type" type="hidden" value="product"/>
                  </div>
                  <div class="flex-col">
                    <button aria-label="Submit" class="ux-search-submit submit-button secondary button icon mb-0" type="submit" value="Search">
                      <i aria-hidden="true" class="icon-search"></i> 
                    </button>
                  </div>
                </div>
                <div class="live-search-results text-left z-top"></div>
              </form>
            </div> 
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>'''

def add_active_class_to_menu(html_content, file_path):
    """
    Add current-menu-item class to the appropriate menu item based on page
    """
    menu_html = MENU_HTML
    
    # Determine which menu item should be active
    if 'gioi-thieu' in file_path:
        # About Us page
        menu_html = menu_html.replace(
            'menu-item-2067 menu-item-design-default',
            'menu-item-2067 menu-item-design-default current-menu-item current_page_item'
        )
    elif 'shop' in file_path or 'index.html@p=' in file_path:
        # Products page or product detail pages
        menu_html = menu_html.replace(
            'menu-item-2065 menu-item-design-default',
            'menu-item-2065 menu-item-design-default current-menu-item current_page_item'
        )
    elif 'dao-tao' in file_path:
        # Training page
        menu_html = menu_html.replace(
            'menu-item-2099 menu-item-design-default',
            'menu-item-2099 menu-item-design-default current-menu-item current_page_item'
        )
    elif 'tin-tuc' in file_path or 'bi-quyet-lam-dep' in file_path:
        # News pages
        menu_html = menu_html.replace(
            'menu-item-2070 menu-item-design-default',
            'menu-item-2070 menu-item-design-default current-menu-item current_page_item'
        )
    elif 'canh-bao-mua-hang' in file_path:
        # Purchase Warning page
        menu_html = menu_html.replace(
            'menu-item-2838 menu-item-design-default',
            'menu-item-2838 menu-item-design-default current-menu-item current_page_item'
        )
    elif 'lien-he' in file_path:
        # Contact page
        menu_html = menu_html.replace(
            'menu-item-2066 menu-item-design-default',
            'menu-item-2066 menu-item-design-default current-menu-item current_page_item'
        )
    elif file_path.endswith('out/index.html'):
        # Homepage
        menu_html = menu_html.replace(
            'menu-item-2068 menu-item-design-default',
            'menu-item-2068 menu-item-design-default current-menu-item current_page_item'
        )
    
    return menu_html

def remove_script_tags(html_content):
    """
    Remove menu-loader.js and footer-loader.js script tags
    """
    # Remove menu-loader.js
    html_content = re.sub(
        r'<script\s+src=["\']shared/menu-loader\.js["\'].*?></script>\s*',
        '',
        html_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Remove footer-loader.js
    html_content = re.sub(
        r'<script\s+src=["\']shared/footer-loader\.js["\'].*?></script>\s*',
        '',
        html_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    return html_content

def replace_menu_in_file(file_path):
    """
    Replace menu in a single HTML file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Get the menu HTML with proper active class
        menu_html = add_active_class_to_menu(content, file_path)
        
        # Pattern 1: Replace empty div with id="wide-nav"
        pattern1 = r'<div class="header-bottom wide-nav flex-has-center hide-for-medium" id="wide-nav"></div>'
        if re.search(pattern1, content):
            content = re.sub(pattern1, menu_html, content)
            print(f"  ✅ Replaced empty menu div in: {file_path}")
        
        # Pattern 2: Replace full menu structure (existing menu)
        pattern2 = r'<div class="header-bottom wide-nav flex-has-center hide-for-medium" id="wide-nav">.*?</div>\s*</div>\s*</div>'
        if re.search(pattern2, content, re.DOTALL):
            content = re.sub(pattern2, menu_html, content, flags=re.DOTALL)
            print(f"  ✅ Replaced existing menu in: {file_path}")
        
        # Remove script tags
        content = remove_script_tags(content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            print(f"  ⏭️  No changes needed: {file_path}")
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
    
    print("🚀 Starting menu hardcode process...")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(out_dir.rglob('*.html'))
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        file_path = str(html_file)
        
        # Skip menu-loader.js file itself
        if 'menu-loader.js' in file_path:
            continue
            
        # Skip files in certain directories if needed
        if any(skip in file_path for skip in ['wp-admin', 'wp-includes']):
            skipped_count += 1
            continue
        
        if replace_menu_in_file(file_path):
            updated_count += 1
    
    print("=" * 60)
    print(f"✅ Process completed!")
    print(f"📊 Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    print(f"📁 Total processed: {len(html_files)} files")

if __name__ == '__main__':
    main()
