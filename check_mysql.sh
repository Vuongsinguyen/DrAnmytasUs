#!/bin/bash
# Quick MySQL Health Check

echo "🔍 MySQL Health Check"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if MySQL is running
if brew services list | grep mysql | grep started > /dev/null; then
    echo "✅ MySQL Service: RUNNING"
else
    echo "❌ MySQL Service: NOT RUNNING"
    echo "   Fix: brew services start mysql"
    exit 1
fi

# Check MySQL connection
if mysql -u root -e "SELECT 1;" > /dev/null 2>&1; then
    echo "✅ MySQL Connection: OK"
else
    echo "❌ MySQL Connection: FAILED"
    echo "   Fix: brew services restart mysql"
    exit 1
fi

# Check MySQL version
VERSION=$(mysql -u root -e "SELECT VERSION();" -s -N 2>/dev/null)
echo "✅ MySQL Version: $VERSION"

# Check if database exists
if mysql -u root -e "USE dranmytas_local;" > /dev/null 2>&1; then
    echo "✅ Database 'dranmytas_local': EXISTS"
    
    # Count tables
    TABLE_COUNT=$(mysql -u root -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'dranmytas_local';" -s -N 2>/dev/null)
    echo "   Tables: $TABLE_COUNT"
else
    echo "⚠️  Database 'dranmytas_local': NOT FOUND"
    echo "   Creating..."
    mysql -u root -e "CREATE DATABASE dranmytas_local CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    echo "   ✅ Created!"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 Connection Info for Duplicator:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   Host:     localhost"
echo "   Database: dranmytas_local"
echo "   User:     root"
echo "   Password: [empty - no password]"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ All systems ready!"
echo ""
