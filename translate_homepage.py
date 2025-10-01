#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import html

# Comprehensive Vietnamese to English translation dictionary
translations = {
    # Meta descriptions
    "Chào mừng bạn đến với Dr.Anmytas – điểm đến tiên phong tại Việt Nam về các dòng dược mỹ phẩm dành riêng cho người Việt Nam. Chúng tôi không chỉ là một thương": "Welcome to Dr.Anmytas – the pioneering destination in Vietnam for cosmeceutical lines specifically designed for Vietnamese people. We are not just a brand",
    
    # Site names
    "Hệ thống dịch vụ rửa mặt": "Facial Cleansing Service System",
    "Dr Anmytas": "Dr Anmytas",
    
    # Schema descriptions  
    "Hoạt Động Sự Kiện Văn Hóa Tập Thể DR.ANMYTAS": "DR.ANMYTAS Corporate Cultural Event Activities",
    "Dr.Anmytas - Tết Trọn Vị | Phim Tết 2025": "Dr.Anmytas - Complete Tet Celebration | Tet Movie 2025",
    "PHIM TẾT 2025 | DR.ANMYTAS - TẾT TRỌN VỊ": "TET MOVIE 2025 | DR.ANMYTAS - COMPLETE TET CELEBRATION",
    "Trong năm qua, bạn đã về nhà được bao nhiêu lần???Cuộc sống cứ cuốn chúng ta đi với công việc, với những cuộc": "In the past year, how many times have you been home??? Life keeps sweeping us away with work, with those",
    
    # Menu items - Must check case sensitivity
    "Trang chủ": "Home",
    "Giới thiệu": "About Us",
    "Sản Phẩm": "Products",
    "Đào Tạo": "Training",
    "Tin tức": "News",
    "Cảnh Báo Mua Hàng": "Purchase Warning",
    "Liên hệ": "Contact",
    "Bí quyết làm đẹp": "Beauty Tips",
    
    # Service menu items
    "Chăm sóc da": "Skincare",
    "Trị liệu": "Treatment",
    "Chăm Sóc Da Chuyên Sâu": "Advanced Skincare",
    "Trị Liệu Bệnh Lý Về Da": "Dermatological Treatment",
    
    # Product categories
    "Sản phẩm": "Products",
    "Chăm sóc da mụn": "Acne Skincare",
    "Chăm sóc da nám": "Melasma Skincare",
    "Hỗ trợ phục hồi": "Recovery Support",
    "Sản phẩm khác": "Other Products",
    
    # Common UI elements
    "Xem thêm": "See more",
    "Chi tiết": "Details",
    "Thêm vào giỏ hàng": "Add to cart",
    "Mua ngay": "Buy now",
    "Đọc thêm": "Read more",
    "Gửi": "Send",
    "Tìm kiếm": "Search",
    "Giỏ hàng": "Cart",
    "Thanh toán": "Checkout",
    "Xem ngay": "View now",
    "Tư vấn ngay": "Consult now",
    "Đặt lịch": "Book appointment",
    
    # Page elements
    "Trang chủ": "Homepage",
    
    # Footer and contact
    "Thông tin liên hệ": "Contact Information",
    "Địa chỉ": "Address",
    "Điện thoại": "Phone",
    "Email": "Email",
    "Theo dõi chúng tôi": "Follow us",
    "Bản quyền": "Copyright",
    "Chính sách": "Policy",
    "Chính sách bảo mật": "Privacy Policy",
    "Điều khoản": "Terms & Conditions",
    
    # Training
    "Đào Tạo Nâng Cao": "Advanced Training",
    "Sơ Cấp Nghề": "Basic Vocational Training",
}

def translate_text(text):
    """Dịch text từ tiếng Việt sang tiếng Anh"""
    for vi_text, en_text in translations.items():
        text = text.replace(vi_text, en_text)
    return text

def translate_html_file(input_file, output_file):
    """Đọc file HTML, dịch nội dung và lưu lại"""
    print(f"Reading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Translating content...")
    translated_content = translate_text(content)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print("✓ Translation completed!")

if __name__ == "__main__":
    input_file = "/Users/Nguyen.vs/Documents/DrAnmytasUs/static-site/index.html"
    output_file = "/Users/Nguyen.vs/Documents/DrAnmytasUs/static-site/index.html"
    
    translate_html_file(input_file, output_file)
