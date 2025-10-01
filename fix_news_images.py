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
        
        # Calculate directory depth to determine number of ../ needed
        # Count slashes after the base directory (out/, static-site-en/, static-site/)
        parts = file_path.parts
        if 'out' in parts:
            depth = len(parts) - parts.index('out') - 2  # -2 for 'out' and 'index.html'
        elif 'static-site-en' in parts:
            depth = len(parts) - parts.index('static-site-en') - 2
        elif 'static-site' in parts:
            depth = len(parts) - parts.index('static-site') - 2
        else:
            depth = 1
        
        # Build the correct prefix (../ or ../../ or ../../../ etc.)
        prefix = '../' * depth if depth > 0 else ''
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix patterns - replace incorrect paths with correct depth
        # Pattern 1: data-src="wp-content/uploads or data-src="../wp-content/uploads (wrong depth)
        content = re.sub(
            r'data-src="(\.\./)*(wp-content/uploads)',
            f'data-src="{prefix}\\2',
            content
        )
        
        # Pattern 2: data-srcset="wp-content/uploads or data-srcset="../wp-content/uploads (wrong depth)
        content = re.sub(
            r'data-srcset="(\.\./)*(wp-content/uploads)',
            f'data-srcset="{prefix}\\2',
            content
        )
        
        # Pattern 3: src="wp-content or src="../wp-content (wrong depth)
        content = re.sub(
            r'src="(\.\./)*(wp-content/)',
            f'src="{prefix}\\2',
            content
        )
        
        # Pattern 4: href="wp-content or href="../wp-content (wrong depth)
        content = re.sub(
            r'href="(\.\./)*(wp-content/)',
            f'href="{prefix}\\2',
            content
        )
        
        # Pattern 5: Inside srcset attributes (with commas and spaces)
        content = re.sub(
            r'([,\s])(\.\./)*(wp-content/uploads)',
            f'\\1{prefix}\\3',
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
