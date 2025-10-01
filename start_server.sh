#!/bin/bash
# Start/Restart PHP Server for Duplicator Installer

echo "🚀 Starting PHP Development Server..."
echo ""

# Kill existing PHP server on port 8888
echo "🔍 Checking for existing server..."
PID=$(lsof -ti :8888)
if [ ! -z "$PID" ]; then
    echo "   Found existing server (PID: $PID)"
    echo "   Stopping..."
    kill -9 $PID 2>/dev/null
    sleep 1
    echo "   ✓ Stopped"
fi

# Navigate to project directory
cd /Users/Nguyen.vs/Documents/DrAnmytasUs

# Start PHP server in background
echo ""
echo "🌟 Starting new server with optimized settings..."
echo "   - Memory Limit: 2GB"
echo "   - Execution Time: 1 hour"
echo "   - Port: 8888"
echo ""

nohup php -d memory_limit=2G \
          -d max_execution_time=3600 \
          -d upload_max_filesize=2G \
          -d post_max_size=2G \
          -d error_reporting="E_ALL & ~E_DEPRECATED & ~E_STRICT" \
          -d display_errors=0 \
          -S localhost:8888 > server.log 2>&1 &

SERVER_PID=$!

# Wait and check if server started
sleep 2

if ps -p $SERVER_PID > /dev/null; then
    echo "✅ Server started successfully!"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "  🌐 Open in browser:"
    echo "     👉 http://localhost:8888/installer.php"
    echo ""
    echo "  📊 Server Info:"
    echo "     • PID: $SERVER_PID"
    echo "     • Port: 8888"
    echo "     • Logs: server.log"
    echo ""
    echo "  📝 Useful commands:"
    echo "     • View logs: tail -f server.log"
    echo "     • Stop server: kill $SERVER_PID"
    echo "     • Check status: lsof -i :8888"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Server is ready! 🎉"
    echo ""
    
    # Save PID to file
    echo $SERVER_PID > .server.pid
    
else
    echo "❌ Failed to start server"
    echo "Check server.log for errors:"
    tail -20 server.log
    exit 1
fi
