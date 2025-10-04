#!/bin/bash

# Script to add menu-loader.js to all HTML files in out/ directory
# This will insert the script tag before the closing </head> tag

MENU_SCRIPT='<script src="/shared/menu-loader.js"><\/script>'
FILES_UPDATED=0
FILES_SKIPPED=0

echo "🔍 Scanning HTML files in out/ directory..."

for file in out/*.html; do
    if [ -f "$file" ]; then
        # Check if menu-loader.js is already included
        if grep -q "menu-loader.js" "$file"; then
            echo "⏭️  Skipping $file (already has menu-loader.js)"
            ((FILES_SKIPPED++))
        else
            # Check if file has </head> tag
            if grep -q "</head>" "$file"; then
                # Insert script before </head>
                sed -i '' "s|</head>|${MENU_SCRIPT}\n</head>|" "$file"
                echo "✅ Updated: $file"
                ((FILES_UPDATED++))
            else
                echo "⚠️  Warning: $file doesn't have </head> tag"
                ((FILES_SKIPPED++))
            fi
        fi
    fi
done

echo ""
echo "📊 Summary:"
echo "   ✅ Files updated: $FILES_UPDATED"
echo "   ⏭️  Files skipped: $FILES_SKIPPED"
echo ""
echo "🎉 Done! Menu loader has been added to all pages."
