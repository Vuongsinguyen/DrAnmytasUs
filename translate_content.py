#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comprehensive content translation script
Translates all Vietnamese content to English across all pages
"""

import os
import re
from pathlib import Path

# Comprehensive Vietnamese-English translation dictionary
TRANSLATIONS = {
    # Schema/Meta content
    "Hệ thống dịch vụ rửa mặt": "Facial Cleansing Service System",
    "Chào mừng bạn đến với Dr.Anmytas – điểm đến tiên phong tại Việt Nam về các dòng dược mỹ phẩm dành riêng cho người Việt Nam. Chúng tôi không chỉ là một thương": "Welcome to Dr.Anmytas – the pioneering destination in Vietnam for cosmeceutical lines specifically designed for Vietnamese people. We are not just a brand",
    
    # Video titles
    "Hoạt Động Sự Kiện Văn Hóa Tập Thể DR.ANMYTAS": "DR.ANMYTAS Corporate Cultural Event Activities",
    "Dr.Anmytas - Tết Trọn Vị | Phim Tết 2025": "Dr.Anmytas - Complete Tet Celebration | Tet Movie 2025",
    "PHIM TẾT 2025 | DR.ANMYTAS - TẾT TRỌN VỊ": "TET MOVIE 2025 | DR.ANMYTAS - COMPLETE TET CELEBRATION",
    "Trong năm qua, bạn đã về nhà được bao nhiêu lần???Cuộc sống cứ cuốn chúng ta đi với công việc, với những cuộc": "In the past year, how many times have you been home??? Life keeps sweeping us away with work, with those",
    
    # Common phrases
    "Xem thêm": "View More",
    "Đọc thêm": "Read More",
    "Chi tiết": "Details",
    "Liên hệ ngay": "Contact Now",
    "Đặt hàng": "Order Now",
    "Mua ngay": "Buy Now",
    "Thêm vào giỏ hàng": "Add to Cart",
    "Tìm hiểu thêm": "Learn More",
    
    # Footer content
    "Theo dõi chúng tôi": "Follow Us",
    "Đăng ký nhận tin": "Subscribe",
    "Bản quyền thuộc về": "Copyright belongs to",
    "Tất cả các quyền được bảo lưu": "All rights reserved",
    
    # Service descriptions
    "Dịch vụ chăm sóc da chuyên nghiệp": "Professional Skincare Services",
    "Sản phẩm chất lượng cao": "High-Quality Products",
    "Đội ngũ chuyên gia giàu kinh nghiệm": "Experienced Expert Team",
    
    # Button text
    "Gửi": "Send",
    "Gửi đi": "Submit",
    "Đóng": "Close",
    "Mở": "Open",
    "Tìm kiếm": "Search",
    
    # Form labels
    "Họ và tên": "Full Name",
    "Họ tên": "Full Name",
    "Email": "Email",
    "Số điện thoại": "Phone Number",
    "Điện thoại": "Phone",
    "Tin nhắn": "Message",
    "Nội dung": "Content",
    "Địa chỉ": "Address",
    
    # Product related
    "Giá": "Price",
    "Còn hàng": "In Stock",
    "Hết hàng": "Out of Stock",
    "Mã sản phẩm": "Product Code",
    "Danh mục": "Category",
    "Thương hiệu": "Brand",
    
    # Blog/News
    "Tin mới nhất": "Latest News",
    "Bài viết liên quan": "Related Articles",
    "Chia sẻ": "Share",
    "Bình luận": "Comments",
    "Đăng bởi": "Posted by",
    "Ngày đăng": "Posted on",
    
    # Common UI elements
    "Trang chủ": "Homepage",
    "Giới thiệu": "About Us",
    "Sản phẩm": "Products",
    "Dịch vụ": "Services",
    "Tin tức": "News",
    "Liên hệ": "Contact",
    "Đào tạo": "Training",
    
    # More specific content from homepage
    "Nguyên Bí thư Đảng ủy": "Former Party Secretary",
    "Phó Viện trưởng": "Deputy Director",
    "kinh nghiệm": "years of experience",
    "chuyên gia": "expert",
    "Tiến sĩ": "Doctor",
    "Bác sĩ": "Doctor",
    "Founder": "Founder",
    
    # Additional common Vietnamese words
    "và": "and",
    "của": "of",
    "cho": "for",
    "với": "with",
    "từ": "from",
    "về": "about",
    "tại": "at",
    "trong": "in",
    "trên": "on",
}

def translate_content(html_content):
    """Translate Vietnamese content to English"""
    
    # Track translations
    translation_count = 0
    
    # Sort translations by length (longest first) to avoid partial replacements
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for vietnamese, english in sorted_translations:
        # Escape special regex characters
        vietnamese_escaped = re.escape(vietnamese)
        
        # Replace in various contexts
        patterns = [
            # In text content
            (vietnamese_escaped, english),
            # In JSON/JavaScript strings (escaped)
            (vietnamese_escaped.replace(' ', r'\\u0020'), english),
            # URL encoded
            (vietnamese_escaped.replace(' ', '%20'), english.replace(' ', '%20')),
        ]
        
        for pattern, replacement in patterns:
            new_content = html_content.replace(vietnamese, english)
            if new_content != html_content:
                translation_count += 1
                html_content = new_content
    
    return html_content, translation_count

def translate_file(filepath):
    """Translate a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        translated_content, count = translate_content(content)
        
        if translated_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            return count
        return 0
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return 0

def translate_all_files(base_dir='static-site'):
    """Translate all HTML files"""
    base_path = Path(base_dir)
    html_files = list(base_path.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to translate...")
    print("=" * 60)
    
    total_translations = 0
    files_modified = 0
    
    for filepath in html_files:
        count = translate_file(filepath)
        if count > 0:
            files_modified += 1
            total_translations += count
            relative_path = filepath.relative_to(base_path)
            if len(str(relative_path)) < 60:
                print(f"✓ {count} translations: {relative_path}")
            else:
                print(f"✓ {count} translations: ...{str(relative_path)[-50:]}")
    
    print("=" * 60)
    print(f"\nTranslation Summary:")
    print(f"- Total files processed: {len(html_files)}")
    print(f"- Files modified: {files_modified}")
    print(f"- Total translations: {total_translations}")
    print("=" * 60)

if __name__ == '__main__':
    print("\n🌐 Translating Vietnamese content to English...\n")
    
    # Translate in static-site directory
    print("Processing 'static-site' directory...")
    translate_all_files('static-site')
    
    # Translate in out directory
    print("\n\nProcessing 'out' directory...")
    translate_all_files('out')
    
    print("\n✅ Content translation complete!\n")
