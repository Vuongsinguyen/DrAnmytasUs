#!/usr/bin/env python3
"""
Translate the About Us page (vi/gioi-thieu) to English with high quality translation
"""

import os
import re
from pathlib import Path

def translate_about_page():
    """Translate the About Us page content"""
    
    source_file = Path('static-site/vi/gioi-thieu/index.html')
    target_file = Path('static-site-en/vi/gioi-thieu/index.html')
    
    if not source_file.exists():
        print(f"Source file not found: {source_file}")
        return
    
    print(f"Reading: {source_file}")
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translation mappings for About Us page - comprehensive list
    translations = {
        # Title and meta
        'Dr Anmytas - Hệ thống chuỗi Spa Doctor da liễu thẩm mỹ and siêu thị mỹ phẩm chính hãng':
            'Dr Anmytas - Dermatology & Medical Spa Chain and Authentic Cosmetics Supermarket',
        
        'Dr Anmytas - Hệ thống chuỗi Spa Tiến sĩ da liễu thẩm mỹ và siêu thị mỹ phẩm chính hãng':
            'Dr Anmytas - Dermatology & Medical Spa Chain and Authentic Cosmetics Supermarket',
        
        # Main heading
        'VỀ CHÚNG TÔI': 'ABOUT US',
        'Về chúng tôi': 'About Us',
        'Giới thiệu': 'About Us',
        
        # Main content paragraphs
        'Dr.Anmytas được sáng lập bởi Doctor Nguyễn Sỹ Hóa and Doctor Nguyễn Quỳnh Ân ando năm 2020 with định hướng xây dựng một hệ thống spa chăm sóc da chuyên sâu dựa on nền tảng khoa học &#8211; an toàn.':
            'Dr.Anmytas was founded by Dr. Nguyen Sy Hoa and Dr. Nguyen Quynh An in 2020 with the vision of building an intensive skincare spa system based on scientific and safe principles.',
        
        'Tháng 1/2021, Dr.Anmytas chính thức hợp tác with Rein Spa – 101 Nguyễn Hoàng, trở thành cơ sở đầu tiên triển khai trọn vẹn hệ thống sản phẩm and dịch vụ theo tiêu chuẩn of thương hiệu. Đến thời điểm hiện at ando năm 2025, Dr.Anmytas đã hợp tác with hơn 90 Spa on toàn quốc and có mặt at 54 tỉnh thành, trở thành một in những chuỗi thương hiệu chăm sóc da khoa học phát triển mạnh mẽ at Việt Nam cung cấp 2 dịch vụ chính:':
            'In January 2021, Dr.Anmytas officially partnered with Rein Spa – 101 Nguyen Hoang, becoming the first facility to fully implement the brand\'s product and service system standards. As of 2025, Dr.Anmytas has partnered with over 90 Spas nationwide and is present in 54 provinces and cities, becoming one of the fastest-growing scientific skincare brands in Vietnam, providing 2 main services:',
        
        'Mỗi năm, Dr.Anmytas đều định kỳ ra mắt các sản phẩm/dịch vụ công nghệ mới in cải thiện làn da for khách hàng:':
            'Every year, Dr.Anmytas regularly launches new technological products/services to improve customers\' skin:',
        
        'Mỗi sản phẩm Dr.Anmytas được chính bác sĩ Nguyễn Quỳnh Ân trực tiếp nghiên cứu and sáng tạo công thức chứa các hoạt chất mới nhất, tiên tiến nhất, đạt nhiều giải thưởng quốc tế danh giá, đảm bảo tính an toàn and hiệu quả for khách hàng.':
            'Each Dr.Anmytas product is personally researched and formulated by Dr. Nguyen Quynh An, containing the latest and most advanced active ingredients, winning many prestigious international awards, ensuring safety and effectiveness for customers.',
        
        'Với tầm nhìn dài hạn, Dr.Anmytas chú trọng đầu tư ando việc phát triển năng lực for các chủ spa and kỹ thuật viên on toàn quốc thuộc hệ thống chuỗi – những người trực tiếp mang triết lý of thương hiệu đến with làn da khách hàng mỗi ngày. Từ đầu năm 2024 đến nay, Dr.Anmytas thực hiện chiến dịch Nâng cấp and chuẩn hóa kiến thức chăm sóc da, tổ chức 100+ buổi đào tạo giảng dạy bởi bác sĩ Nguyễn Quỳnh Ân, các expert of Ban đào tạo Dr.Anmytas.':
            'With a long-term vision, Dr.Anmytas focuses on investing in capacity development for spa owners and technicians nationwide within the chain system – those who directly bring the brand\'s philosophy to customers\' skin every day. Since early 2024, Dr.Anmytas has implemented a campaign to upgrade and standardize skincare knowledge, organizing 100+ training sessions taught by Dr. Nguyen Quynh An and experts from the Dr.Anmytas Training Department.',
        
        'Không đơn thuần là một thương hiệu mỹ phẩm, Dr.Anmytas là một đơn vị tiên phong at Việt Nam in việc nghiên cứu and sáng tạo giải pháp chăm sóc da khoa học, an toàn and bền vững. Sự phát triển mạnh mẽ of thương hiệu không chỉ đến from tầm nhìn chiến lược, mà còn from lòng tin of hàng ngàn khách hàng đã trải nghiệm and lựa chọn Dr.Anmytas như một người bạn đồng hành cùng làn da.':
            'More than just a cosmetics brand, Dr.Anmytas is a pioneer in Vietnam in researching and creating scientific, safe, and sustainable skincare solutions. The brand\'s strong development comes not only from strategic vision but also from the trust of thousands of customers who have experienced and chosen Dr.Anmytas as a companion for their skin.',
        
        # Company info
        'CÔNG TY CỔ PHẦN DƯỢC MỸ PHẨM DR.ANMYTAS': 'DR.ANMYTAS PHARMACEUTICAL COSMETICS JOINT STOCK COMPANY',
        'ĐKKD số: 0109426251 - Ngày cấp: 23/11/2020': 'Business Registration No: 0109426251 - Issued: November 23, 2020',
        'Thời gian làm việc: Thứ 2 - CN: Từ 09h - 18h': 'Working hours: Monday - Sunday: From 9:00 AM - 6:00 PM',
        
        # Names
        'Doctor Nguyễn Sỹ Hóa': 'Dr. Nguyen Sy Hoa',
        'Doctor Nguyễn Quỳnh Ân': 'Dr. Nguyen Quynh An',
        'bác sĩ Nguyễn Quỳnh Ân': 'Dr. Nguyen Quynh An',
        
        # Menu and navigation
        'Dịch vụ': 'Services',
        'Sản phẩm': 'Products',
        'Tin tức': 'News',
        'Liên hệ': 'Contact',
        'Trang chủ': 'Home',
        'Đào tạo': 'Training',
        
        # Common words - remove machine translation artifacts
        ' ando ': ' in ',
        ' and ': ' and ',
        ' with ': ' with ',
        ' for ': ' for ',
        ' at ': ' in ',
        ' on ': ' on ',
        ' of ': ' of ',
        ' from ': ' from ',
        ' in ': ' in ',
        ' about ': ' about ',
    }
    
    # Apply translations
    for vietnamese, english in translations.items():
        content = content.replace(vietnamese, english)
    
    # Additional regex replacements for mixed content
    # Fix schema.org Vietnamese text
    content = re.sub(
        r'"Dr.Anmytas - n\\u1eb1m in H\\u1ec7 th\\u1ed1ng chu\\u1ed7i.*?"',
        '"DR.ANMYTAS - Dermatology & Medical Spa System and Authentic Cosmetics Supermarket Chain. Established in December 2020, with the mission of elevating professional expertise, specialized services, and a caring lifestyle to the entire Vietnamese spa industry. Building a prestigious pharmaceutical cosmetics brand formed by Vietnamese people, for Vietnamese skin, with international quality and reputation at reasonable prices. Our spa chain model collaborates with dermatologists, bringing high professional standards. DR.ANMYTAS currently provides 2 main services: Anmytas pharmaceutical cosmetics and the DR.ANMYTAS Doctor Spa model."',
        content
    )
    
    # Ensure target directory exists
    target_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Writing translated content to: {target_file}")
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ About Us page translated successfully!")

if __name__ == '__main__':
    translate_about_page()
