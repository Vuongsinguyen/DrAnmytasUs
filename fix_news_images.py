#!/usr/bin/env python3
"""
Fix image paths in ALL HTML files - add ../ prefix to wp-content paths where needed
"""

import re
from pathlib import Path
import glob

def fix_image_paths():
    """Fix image paths in all HTML files"""
    
    # Find all HTML files in subdirectories (not root index.html)
    files_to_fix = []
    for pattern in ['out/**/index.html', 'static-site-en/**/index.html', 'static-site/**/index.html']:
        files_to_fix.extend(glob.glob(pattern, recursive=True))
    
    # Exclude root index.html files
    files_to_fix = [f for f in files_to_fix if not f.endswith(('out/index.html', 'static-site-en/index.html', 'static-site/index.html'))]
    
    print(f"Found {len(files_to_fix)} HTML files to process\n")
    
    fixed_count = 0
    for file_path_str in files_to_fix:
        file_path = Path(file_path_str)
        
        if not file_path.exists():
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix patterns where wp-content/uploads is missing ../
        # Pattern 1: data-src="wp-content/uploads -> data-src="../wp-content/uploads
        content = re.sub(
            r'data-src="wp-content/uploads',
            r'data-src="../wp-content/uploads',
            content
        )
        
        # Pattern 2: data-srcset="wp-content/uploads -> data-srcset="../wp-content/uploads
        content = re.sub(
            r'data-srcset="wp-content/uploads',
            r'data-srcset="../wp-content/uploads',
            content
        )
        
        # Pattern 3: Inside srcset attributes, fix paths like "wp-content/uploads" -> "../wp-content/uploads"
        content = re.sub(
            r'([,\s])wp-content/uploads',
            r'\1../wp-content/uploads',
            content
        )
        
        # Check if any changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            print(f"✅ Fixed: {file_path}")
    
    print(f"\n🎉 Fixed {fixed_count} files!")

if __name__ == '__main__':
    fix_image_paths()
