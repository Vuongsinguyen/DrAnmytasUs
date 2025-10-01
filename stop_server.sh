#!/bin/bash
# Stop PHP Development Server

echo "🛑 Stopping PHP Server..."
echo ""

# Check if PID file exists
if [ -f .server.pid ]; then
    PID=$(cat .server.pid)
    if ps -p $PID > /dev/null 2>&1; then
        echo "   Found server (PID: $PID)"
        kill $PID
        sleep 1
        
        if ! ps -p $PID > /dev/null 2>&1; then
            echo "   ✓ Server stopped successfully"
            rm .server.pid
        else
            echo "   ⚠ Server still running, force killing..."
            kill -9 $PID
            rm .server.pid
            echo "   ✓ Server force stopped"
        fi
    else
        echo "   ℹ Server not running (PID: $PID)"
        rm .server.pid
    fi
else
    # Try to find by port
    PID=$(lsof -ti :8888)
    if [ ! -z "$PID" ]; then
        echo "   Found server on port 8888 (PID: $PID)"
        kill -9 $PID
        echo "   ✓ Server stopped"
    else
        echo "   ℹ No server found on port 8888"
    fi
fi

echo ""
echo "Done! ✅"
