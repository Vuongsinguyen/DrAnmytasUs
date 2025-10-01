#!/bin/bash

# Script để dọn dẹp installer files

echo "🧹 Cleaning up installer files..."

# Xóa thư mục dup-installer
if [ -d "dup-installer" ]; then
    echo "  → Removing dup-installer/"
    rm -rf dup-installer
fi

# Xóa installer.php
if [ -f "installer.php" ]; then
    echo "  → Removing installer.php"
    rm -f installer.php
fi

# Xóa bootlog files
rm -f dup-installer-bootlog*.txt 2>/dev/null

# Xóa các script extract tạm
echo "  → Removing temporary extraction scripts"
rm -f extract_archive.php 2>/dev/null
rm -f full_extract.php 2>/dev/null
rm -f extract_duparchive.py 2>/dev/null
rm -f extract_wordpress.php 2>/dev/null

# Xóa các file guide (giữ lại nếu cần)
# rm -f HUONG_DAN_EXTRACT.md
# rm -f DATABASE_SETUP_GUIDE.txt
# rm -f ERROR_FIXED.txt

echo ""
echo "✅ Cleanup completed!"
echo ""
echo "Kept files:"
echo "  - .gitignore"
echo "  - start_server.sh / stop_server.sh"
echo "  - check_mysql.sh"
echo "  - Guide files (HUONG_DAN_EXTRACT.md, etc.)"
echo ""
echo "To remove guides too, delete them manually:"
echo "  rm -f *_GUIDE.txt *.md"
