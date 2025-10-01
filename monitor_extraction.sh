#!/bin/bash
# Monitor extraction progress

echo "🔍 Monitoring WordPress Extraction..."
echo ""

while true; do
    clear
    echo "=================================="
    echo "   Extraction Progress Monitor"
    echo "=================================="
    echo ""
    date
    echo ""
    
    # Check if wordpress files exist
    if [ -d "wp-admin" ]; then
        echo "✓ wp-admin/       EXTRACTED"
    else
        echo "⏳ wp-admin/       Waiting..."
    fi
    
    if [ -d "wp-content" ]; then
        echo "✓ wp-content/     EXTRACTED"
        
        # Count themes
        if [ -d "wp-content/themes" ]; then
            theme_count=$(ls -1 wp-content/themes 2>/dev/null | wc -l)
            echo "  └─ Themes: $theme_count"
        fi
        
        # Count plugins  
        if [ -d "wp-content/plugins" ]; then
            plugin_count=$(ls -1 wp-content/plugins 2>/dev/null | wc -l)
            echo "  └─ Plugins: $plugin_count"
        fi
        
        # Check uploads
        if [ -d "wp-content/uploads" ]; then
            echo "  └─ Uploads: OK"
        fi
    else
        echo "⏳ wp-content/     Waiting..."
    fi
    
    if [ -d "wp-includes" ]; then
        echo "✓ wp-includes/    EXTRACTED"
    else
        echo "⏳ wp-includes/    Waiting..."
    fi
    
    if [ -f "wp-config.php" ]; then
        echo "✓ wp-config.php   CREATED"
    else
        echo "⏳ wp-config.php   Waiting..."
    fi
    
    if [ -f "index.php" ]; then
        echo "✓ index.php       READY"
    else
        echo "⏳ index.php       Waiting..."
    fi
    
    echo ""
    
    # Count total files
    total_files=$(find . -maxdepth 1 -type f 2>/dev/null | wc -l)
    total_dirs=$(find . -maxdepth 1 -type d 2>/dev/null | wc -l)
    
    echo "📊 Current Status:"
    echo "   Files: $total_files"
    echo "   Folders: $total_dirs"
    
    echo ""
    echo "Press Ctrl+C to stop monitoring"
    echo ""
    
    # Check if extraction is complete
    if [ -f "index.php" ] && [ -d "wp-admin" ] && [ -d "wp-content" ] && [ -d "wp-includes" ]; then
        echo ""
        echo "=================================="
        echo "   ✅ EXTRACTION COMPLETE!"
        echo "=================================="
        echo ""
        echo "WordPress site đã được giải nén thành công!"
        echo ""
        echo "Bước tiếp theo:"
        echo "1. Check themes: ls -la wp-content/themes/"
        echo "2. Check plugins: ls -la wp-content/plugins/"
        echo "3. Update .gitignore"
        echo "4. Start coding!"
        echo ""
        break
    fi
    
    sleep 5
done
