#!/usr/bin/env python3
"""Fix image paths in Purchase Warning page"""

import re
from pathlib import Path

def fix_purchase_warning_images():
    # Files to process
    files = [
        'static-site-en/canh-bao-mua-hang/index.html',
        'static-site-en/vi/canh-bao-mua-hang/index.html'
    ]
    
    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
            
        # Calculate depth
        depth = len(path.parent.parts)
        prefix = '../' * depth
        
        print(f"📁 Processing: {file_path}")
        print(f"   Depth: {depth}, Prefix: {prefix}")
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix patterns:
        # 1. data-src="../wp-content -> data-src="{prefix}wp-content
        # 2. data-srcset="../wp-content -> data-srcset="{prefix}wp-content
        # 3. src="../wp-content -> src="{prefix}wp-content
        # 4. srcset="../wp-content -> srcset="{prefix}wp-content
        # 5. href="../wp-content -> href="{prefix}wp-content
        # 6. url("../wp-content -> url("{prefix}wp-content
        
        patterns = [
            (r'data-src="(\.\./)*wp-content/', f'data-src="{prefix}wp-content/'),
            (r'data-srcset="(\.\./)*wp-content/', f'data-srcset="{prefix}wp-content/'),
            (r'src="(\.\./)*wp-content/', f'src="{prefix}wp-content/'),
            (r'srcset="(\.\./)*wp-content/', f'srcset="{prefix}wp-content/'),
            (r'href="(\.\./)*wp-content/', f'href="{prefix}wp-content/'),
            (r'url\("(\.\./)*wp-content/', f'url("{prefix}wp-content/'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ Fixed image paths")
        else:
            print(f"   ℹ️  No changes needed")
    
    print("\n✅ Purchase Warning image fix complete!")

if __name__ == '__main__':
    fix_purchase_warning_images()
