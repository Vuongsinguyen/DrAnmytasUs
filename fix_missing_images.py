#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def create_missing_responsive_images():
    """
    Tạo các file responsive images còn thiếu bằng cách copy từ ảnh gốc
    """
    uploads_dir = Path("/Users/Nguyen.vs/Documents/DrAnmytasUs/out/wp-content/uploads")
    
    # Danh sách các kích thước responsive phổ biến
    common_sizes = [
        "1536x864", "1536x1024", "1536x610", "1536x1536", 
        "2048x1152", "2048x1536", "2048x806",
        "1200x675", "1200x800", "1200x1200"
    ]
    
    created_count = 0
    
    # Tìm tất cả file ảnh gốc
    for img_file in uploads_dir.rglob("*"):
        if img_file.is_file() and img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
            # Bỏ qua file đã có kích thước (có dấu - và số)
            if '-' in img_file.stem and any(char.isdigit() for char in img_file.stem.split('-')[-1]):
                continue
                
            # Tạo các kích thước responsive từ file gốc
            for size in common_sizes:
                responsive_name = f"{img_file.stem}-{size}{img_file.suffix}"
                responsive_path = img_file.parent / responsive_name
                
                # Chỉ tạo nếu file chưa tồn tại
                if not responsive_path.exists():
                    try:
                        shutil.copy2(img_file, responsive_path)
                        print(f"Created: {responsive_path.relative_to(uploads_dir)}")
                        created_count += 1
                    except Exception as e:
                        print(f"Error creating {responsive_path}: {e}")
    
    print(f"\nTotal files created: {created_count}")

if __name__ == "__main__":
    create_missing_responsive_images()