#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Translate all menu items across all static pages
"""

import os
import re
from pathlib import Path

# Comprehensive menu translation dictionary
MENU_TRANSLATIONS = {
    # Main Navigation Menu
    "Trang chủ": "Homepage",
    "Giới thiệu": "About Us",
    "Sản Phẩm": "Products",
    "Sản phẩm": "Products",
    "Đào Tạo": "Training",
    "Đào tạo": "Training",
    "Tin tức": "News",
    "Tin Tức": "News",
    "Cảnh Báo Mua Hàng": "Purchase Warning",
    "Cảnh báo mua hàng": "Purchase Warning",
    "Liên hệ": "Contact",
    "Liên Hệ": "Contact",
    "Bí quyết làm đẹp": "Beauty Tips",
    
    # Product Categories
    "Chăm sóc da mụn": "Acne Skincare",
    "Chăm Sóc Da Mụn": "Acne Skincare",
    "Chăm sóc da nam": "Men's Skincare",
    "Chăm Sóc Da Nam": "Men's Skincare",
    "Hỗ trợ phục hồi": "Recovery Support",
    "Hỗ Trợ Phục Hồi": "Recovery Support",
    "Sản phẩm khác": "Other Products",
    "Sản Phẩm Khác": "Other Products",
    
    # Service Menu
    "Dịch vụ": "Services",
    "Dịch Vụ": "Services",
    "Chăm sóc da chuyên sâu": "Advanced Skincare",
    "Chăm Sóc Da Chuyên Sâu": "Advanced Skincare",
    "Trị liệu bệnh lý về da": "Dermatological Treatment",
    "Trị Liệu Bệnh Lý Về Da": "Dermatological Treatment",
    "Trị liệu mụn": "Acne Treatment",
    "Trị Liệu Mụn": "Acne Treatment",
    "Trị liệu nám": "Melasma Treatment",
    "Trị Liệu Nám": "Melasma Treatment",
    "Trị liệu sẹo": "Scar Treatment",
    "Trị Liệu Sẹo": "Scar Treatment",
    "Tái sinh làn da": "Skin Regeneration",
    "Tái Sinh Làn Da": "Skin Regeneration",
    "Phun thêu thẩm mỹ": "Aesthetic Tattooing",
    "Phun Thêu Thẩm Mỹ": "Aesthetic Tattooing",
    
    # Training Menu
    "Sơ cấp nghề": "Basic Professional Training",
    "Sơ Cấp Nghề": "Basic Professional Training",
    "Đào tạo nâng cao": "Advanced Training",
    "Đào Tạo Nâng Cao": "Advanced Training",
    
    # Footer Menu
    "Chính sách bảo mật": "Privacy Policy",
    "Chính Sách Bảo Mật": "Privacy Policy",
    "Điều khoản sử dụng": "Terms of Use",
    "Điều Khoản Sử Dụng": "Terms of Use",
    
    # Common Menu Items
    "Tất cả": "All",
    "Xem thêm": "View More",
    "Xem Thêm": "View More",
    "Thu gọn": "Show Less",
    "Thu Gọn": "Show Less",
    "Mới nhất": "Latest",
    "Mới Nhất": "Latest",
    "Phổ biến": "Popular",
    "Phổ Biến": "Popular",
    
    # Shop/Cart Menu
    "Giỏ hàng": "Cart",
    "Giỏ Hàng": "Cart",
    "Thanh toán": "Checkout",
    "Thanh Toán": "Checkout",
    "Đơn hàng": "Orders",
    "Đơn Hàng": "Orders",
    "Tài khoản": "Account",
    "Tài Khoản": "Account",
    
    # Blog/News Categories
    "Bài viết": "Articles",
    "Bài Viết": "Articles",
    "Danh mục": "Categories",
    "Danh Mục": "Categories",
    "Tìm kiếm": "Search",
    "Tìm Kiếm": "Search",
    
    # Additional common menu terms
    "Trang": "Page",
    "Về chúng tôi": "About Us",
    "Về Chúng Tôi": "About Us",
    "Dịch vụ của chúng tôi": "Our Services",
    "Dịch Vụ Của Chúng Tôi": "Our Services",
    "Sản phẩm của chúng tôi": "Our Products",
    "Sản Phẩm Của Chúng Tôi": "Our Products",
}

def translate_menu_in_file(filepath):
    """Translate menu items in a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        translation_count = 0
        
        # Apply translations
        for vietnamese, english in MENU_TRANSLATIONS.items():
            # Pattern to match menu text in various HTML contexts
            # Match in menu links, list items, navigation elements
            patterns = [
                # <a>Menu Text</a>
                (rf'(<a[^>]*>)\s*{re.escape(vietnamese)}\s*(</a>)', rf'\1{english}\2'),
                # <li>Menu Text</li>
                (rf'(<li[^>]*>)\s*{re.escape(vietnamese)}\s*(</li>)', rf'\1{english}\2'),
                # <span>Menu Text</span>
                (rf'(<span[^>]*>)\s*{re.escape(vietnamese)}\s*(</span>)', rf'\1{english}\2'),
                # <div>Menu Text</div>
                (rf'(<div[^>]*class="[^"]*menu[^"]*"[^>]*>)\s*{re.escape(vietnamese)}\s*(</div>)', rf'\1{english}\2'),
                # title="Menu Text"
                (rf'(title="){re.escape(vietnamese)}(")', rf'\1{english}\2'),
                # aria-label="Menu Text"
                (rf'(aria-label="){re.escape(vietnamese)}(")', rf'\1{english}\2'),
                # In navigation lists
                (rf'(<nav[^>]*>.*?)({re.escape(vietnamese)})(.*?</nav>)', rf'\1{english}\3'),
            ]
            
            for pattern, replacement in patterns:
                new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                if new_content != content:
                    translation_count += 1
                    content = new_content
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return translation_count
        return 0
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return 0

def translate_all_menus(base_dir='static-site'):
    """Translate menus in all HTML files"""
    base_path = Path(base_dir)
    html_files = list(base_path.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process...")
    print("=" * 60)
    
    total_translations = 0
    files_modified = 0
    
    for filepath in html_files:
        count = translate_menu_in_file(filepath)
        if count > 0:
            files_modified += 1
            total_translations += count
            print(f"✓ Translated {count} menu items in: {filepath.relative_to(base_path)}")
    
    print("=" * 60)
    print(f"\nTranslation Summary:")
    print(f"- Total files processed: {len(html_files)}")
    print(f"- Files modified: {files_modified}")
    print(f"- Total menu translations: {total_translations}")
    print("=" * 60)

if __name__ == '__main__':
    # Translate in both static-site and out directories
    print("Translating menus in 'static-site' directory...")
    translate_all_menus('static-site')
    
    print("\n\nTranslating menus in 'out' directory...")
    translate_all_menus('out')
    
    print("\n✅ Menu translation complete!")
