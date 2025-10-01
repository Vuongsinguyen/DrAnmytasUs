#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to translate Vietnamese website content to English
Author: GitHub Copilot
Date: October 2025
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

# Translation dictionary - Common Vietnamese to English terms
TRANSLATION_DICT = {
    # Menu items
    'TRANG CHỦ': 'HOME',
    'Trang Chủ': 'Home',
    'Trang chủ': 'Home',
    'GIỚI THIỆU': 'ABOUT US',
    'Giới Thiệu': 'About Us',
    'Giới thiệu': 'About us',
    'SẢN PHẨM': 'PRODUCTS',
    'Sản Phẩm': 'Products',
    'Sản phẩm': 'Products',
    'DỊCH VỤ': 'SERVICES',
    'Dịch Vụ': 'Services',
    'Dịch vụ': 'Services',
    'TIN TỨC': 'NEWS',
    'Tin Tức': 'News',
    'Tin tức': 'News',
    'LIÊN HỆ': 'CONTACT',
    'Liên Hệ': 'Contact',
    'Liên hệ': 'Contact',
    'ĐÀO TẠO': 'TRAINING',
    'Đào Tạo': 'Training',
    'Đào tạo': 'Training',
    
    # Common terms
    'Chăm Sóc Da': 'Skin Care',
    'Chăm sóc da': 'Skin care',
    'CHĂM SÓC DA': 'SKIN CARE',
    'Làm Đẹp': 'Beauty',
    'Làm đẹp': 'Beauty',
    'Mỹ Phẩm': 'Cosmetics',
    'Mỹ phẩm': 'Cosmetics',
    'Dưỡng Da': 'Skin Treatment',
    'Dưỡng da': 'Skin treatment',
    'Trị Liệu': 'Treatment',
    'Trị liệu': 'Treatment',
    'Làn Da': 'Skin',
    'Làn da': 'Skin',
    'Da Mặt': 'Facial Skin',
    'Da mặt': 'Facial skin',
    'Rửa Mặt': 'Face Wash',
    'Rửa mặt': 'Face wash',
    'Kem Dưỡng': 'Moisturizer',
    'Kem dưỡng': 'Moisturizer',
    'Serum': 'Serum',
    'Toner': 'Toner',
    'Sữa Rửa Mặt': 'Facial Cleanser',
    'Sữa rửa mặt': 'Facial cleanser',
    
    # Service related
    'Bí Quyết': 'Secrets',
    'Bí quyết': 'Secrets',
    'Hướng Dẫn': 'Guide',
    'Hướng dẫn': 'Guide',
    'Cảnh Báo': 'Warning',
    'Cảnh báo': 'Warning',
    'Chính Sách': 'Policy',
    'Chính sách': 'Policy',
    'Bảo Mật': 'Privacy',
    'Bảo mật': 'Privacy',
    'Điều Khoản': 'Terms',
    'Điều khoản': 'Terms',
    
    # Common phrases
    'Xem thêm': 'Read more',
    'Xem Thêm': 'Read More',
    'Chi tiết': 'Details',
    'Chi Tiết': 'Details',
    'Gửi': 'Send',
    'Tìm kiếm': 'Search',
    'Tìm Kiếm': 'Search',
    'Đăng ký': 'Register',
    'Đăng Ký': 'Register',
    'Đăng nhập': 'Login',
    'Đăng Nhập': 'Login',
    
    # Company/Site specific
    'Dr Anmytas': 'Dr Anmytas',
    'Dr. Anmytas': 'Dr. Anmytas',
    'DR ANMYTAS': 'DR ANMYTAS',
    'DR.ANMYTAS': 'DR.ANMYTAS',
    'Hệ thống dịch vụ rửa mặt': 'Facial Cleansing Service System',
    'Facial Cleansing Service System': 'Facial Cleansing Service System',
    
    # Skin types and conditions
    'Da Khô': 'Dry Skin',
    'Da khô': 'Dry skin',
    'Da Dầu': 'Oily Skin',
    'Da dầu': 'Oily skin',
    'Da Nhạy Cảm': 'Sensitive Skin',
    'Da nhạy cảm': 'Sensitive skin',
    'Da Mụn': 'Acne Skin',
    'Da mụn': 'Acne skin',
    'Lão Hóa': 'Aging',
    'Lão hóa': 'Aging',
    'Nám Da': 'Melasma',
    'Nám da': 'Melasma',
    'Tàn Nhang': 'Freckles',
    'Tàn nhang': 'Freckles',
    'Thâm Nám': 'Dark Spots',
    'Thâm nám': 'Dark spots',
    'Sẹo': 'Scars',
    'Sẹo rỗ': 'Acne scars',
    
    # Actions
    'Mua Hàng': 'Shop',
    'Mua hàng': 'Shop',
    'Đặt Hàng': 'Order',
    'Đặt hàng': 'Order',
    'Đặt Lịch': 'Book Appointment',
    'Đặt lịch': 'Book appointment',
    'Tư Vấn': 'Consultation',
    'Tư vấn': 'Consultation',
    'Hotline': 'Hotline',
    'Email': 'Email',
    'Địa Chỉ': 'Address',
    'Địa chỉ': 'Address',
}

# Additional translation mappings for metadata
META_TRANSLATIONS = {
    'vi-VN': 'en-US',
    'vi': 'en',
    'Việt Nam': 'Vietnam',
}

def translate_text(text, context='general'):
    """
    Translate Vietnamese text to English using dictionary
    
    Args:
        text: Text to translate
        context: Context for translation (general, title, meta)
    
    Returns:
        Translated text
    """
    if not text or not isinstance(text, str):
        return text
    
    translated = text
    
    # Apply translations from dictionary
    for vn, en in TRANSLATION_DICT.items():
        # Use word boundaries to avoid partial matches
        pattern = re.compile(r'\b' + re.escape(vn) + r'\b', re.IGNORECASE)
        translated = pattern.sub(en, translated)
    
    return translated

def translate_html_file(file_path, output_path=None, dry_run=False):
    """
    Translate a single HTML file from Vietnamese to English
    
    Args:
        file_path: Path to input HTML file
        output_path: Path to output HTML file (if None, overwrites input)
        dry_run: If True, only print what would be changed
    
    Returns:
        True if successful, False otherwise
    """
    try:
        print(f"Processing: {file_path}")
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        changes_made = 0
        
        # 1. Translate title tags
        titles = soup.find_all('title')
        for title in titles:
            if title.string:
                original = title.string
                translated = translate_text(title.string, context='title')
                if original != translated:
                    title.string = translated
                    changes_made += 1
                    if dry_run:
                        print(f"  Title: '{original}' -> '{translated}'")
        
        # 2. Translate meta tags
        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            # Translate content attribute
            if meta.get('content'):
                original = meta['content']
                translated = translate_text(meta['content'], context='meta')
                if original != translated:
                    meta['content'] = translated
                    changes_made += 1
                    if dry_run:
                        print(f"  Meta: '{original[:50]}...' -> '{translated[:50]}...'")
            
            # Update locale
            if meta.get('property') == 'og:locale' and meta.get('content') == 'vi_VN':
                meta['content'] = 'en_US'
                changes_made += 1
        
        # 3. Translate navigation/menu items
        nav_items = soup.find_all(['a', 'span', 'button'], class_=re.compile(r'nav|menu|link'))
        for item in nav_items:
            if item.string:
                original = item.string.strip()
                translated = translate_text(original)
                if original != translated:
                    item.string.replace_with(translated)
                    changes_made += 1
                    if dry_run:
                        print(f"  Nav: '{original}' -> '{translated}'")
        
        # 4. Translate headings
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(tag)
            for heading in headings:
                if heading.string:
                    original = heading.string.strip()
                    translated = translate_text(original)
                    if original != translated:
                        heading.string.replace_with(translated)
                        changes_made += 1
                        if dry_run:
                            print(f"  {tag.upper()}: '{original}' -> '{translated}'")
        
        # 5. Update language attributes
        html_tag = soup.find('html')
        if html_tag and html_tag.get('lang') in ['vi', 'vi-VN']:
            html_tag['lang'] = 'en-US'
            changes_made += 1
        
        # 6. Translate common text nodes (paragraphs, divs, spans)
        text_tags = soup.find_all(['p', 'div', 'span', 'li', 'td', 'th'])
        for tag in text_tags:
            # Only translate direct text content, not nested tags
            if tag.string and len(tag.string.strip()) > 0:
                original = tag.string.strip()
                translated = translate_text(original)
                if original != translated and len(original) < 200:  # Avoid long paragraphs
                    tag.string.replace_with(translated)
                    changes_made += 1
                    if dry_run and changes_made <= 50:  # Limit output
                        print(f"  Text: '{original[:50]}...' -> '{translated[:50]}...'")
        
        if dry_run:
            print(f"  Total changes: {changes_made}\n")
            return True
        
        # Save the translated content
        output_file = output_path if output_path else file_path
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"  ✓ Translated successfully ({changes_made} changes)")
        print(f"  Saved to: {output_file}\n")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {str(e)}\n")
        return False

def translate_directory(input_dir, output_dir=None, dry_run=False, file_pattern='**/*.html'):
    """
    Translate all HTML files in a directory
    
    Args:
        input_dir: Input directory path
        output_dir: Output directory path (if None, overwrites input files)
        dry_run: If True, only show what would be changed
        file_pattern: Glob pattern for files to process
    
    Returns:
        Dictionary with statistics
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: Directory {input_dir} does not exist")
        return None
    
    # Find all HTML files
    html_files = list(input_path.glob(file_pattern))
    
    if not html_files:
        print(f"No HTML files found in {input_dir}")
        return None
    
    print(f"Found {len(html_files)} HTML files to process")
    print(f"{'DRY RUN MODE - No files will be modified' if dry_run else 'TRANSLATION MODE - Files will be modified'}")
    print("=" * 60)
    print()
    
    stats = {
        'total': len(html_files),
        'success': 0,
        'failed': 0,
        'skipped': 0
    }
    
    for html_file in html_files:
        # Determine output path
        if output_dir:
            output_path = Path(output_dir) / html_file.relative_to(input_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            output_path = None
        
        # Translate file
        if translate_html_file(html_file, output_path, dry_run):
            stats['success'] += 1
        else:
            stats['failed'] += 1
    
    print("=" * 60)
    print(f"Translation complete!")
    print(f"Total files: {stats['total']}")
    print(f"Success: {stats['success']}")
    print(f"Failed: {stats['failed']}")
    
    return stats

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Translate Vietnamese website to English',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run - see what would be changed
  python translate_to_english.py --dry-run
  
  # Translate all files in static-site (overwrites originals)
  python translate_to_english.py
  
  # Translate to a new directory
  python translate_to_english.py --output static-site-en
  
  # Translate a single file
  python translate_to_english.py --file static-site/index.html
        """
    )
    
    parser.add_argument(
        '--input',
        default='static-site',
        help='Input directory (default: static-site)'
    )
    
    parser.add_argument(
        '--output',
        help='Output directory (if not specified, overwrites input files)'
    )
    
    parser.add_argument(
        '--file',
        help='Translate a single file instead of directory'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    
    parser.add_argument(
        '--pattern',
        default='**/*.html',
        help='File pattern to match (default: **/*.html)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Vietnamese to English Website Translator")
    print("=" * 60)
    print()
    
    if args.file:
        # Translate single file
        output_file = None
        if args.output:
            output_file = Path(args.output) / Path(args.file).name
            output_file.parent.mkdir(parents=True, exist_ok=True)
        
        translate_html_file(args.file, output_file, args.dry_run)
    else:
        # Translate directory
        translate_directory(args.input, args.output, args.dry_run, args.pattern)

if __name__ == '__main__':
    main()
