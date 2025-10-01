#!/bin/bash

# Script để xóa language switcher khỏi tất cả file HTML

cd /Users/Nguyen.vs/Documents/DrAnmytasUs/static-site

# Tìm và xóa language switcher trong tất cả file HTML
find . -name "*.html" -type f -exec perl -i -0777 -pe 's/<div\s+class="trp-language-switcher[^>]*>.*?<\/div>\s*(?=<\/body>)//gs' {} \;

echo "✓ Đã xóa language switcher khỏi tất cả file HTML trong static-site"
