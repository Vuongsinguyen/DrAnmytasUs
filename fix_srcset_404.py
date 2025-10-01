#!/usr/bin/env python3
"""Remove non-existent 2048px image references from srcsets"""

import re
from pathlib import Path

def fix_srcsets():
    # Files to process
    files = [
        'static-site-en/canh-bao-mua-hang/index.html',
        'static-site-en/vi/canh-bao-mua-hang/index.html'
    ]
    
    total_fixed = 0
    
    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
            
        print(f"\n📁 Processing: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove 2048x references from srcset attributes
        # Pattern: ../wp-content/uploads/2025/08/filename-2048x1431.jpg 2048w, 
        patterns = [
            # Remove 2048x references with sizes
            (r'([^\s"]+)-2048x\d+\.jpg\s+2048w,\s*', ''),
            (r'([^\s"]+)-2048x\d+\.png\s+2048w,\s*', ''),
            # Remove 1536x references if they also don't exist (to be safe)
            (r'([^\s"]+)-1536x\d+\.jpg\s+1536w,\s*', ''),
            (r'([^\s"]+)-1536x\d+\.png\s+1536w,\s*', ''),
        ]
        
        count = 0
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                matches = len(re.findall(pattern, content))
                count += matches
                content = new_content
        
        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"   ✅ Removed {count} non-existent image references")
            total_fixed += count
        else:
            print(f"   ℹ️  No changes needed")
    
    print(f"\n✅ Complete! Fixed {total_fixed} image references across all files")

if __name__ == '__main__':
    fix_srcsets()
