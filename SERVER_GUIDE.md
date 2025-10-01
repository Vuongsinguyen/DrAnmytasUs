# 🚀 WordPress Extraction - Server Management

## ✅ FIXED: Server đã sẵn sàng!

Server PHP đang chạy tại: **http://localhost:8888**

---

## 🌐 Truy cập Installer

Mở trình duyệt và vào:

```
http://localhost:8888/installer.php
```

**Hoặc** sử dụng một trong các cách sau:

### Chrome/Safari/Firefox:
- Gõ trực tiếp: `localhost:8888/installer.php`

### VS Code Simple Browser:
- Đã mở sẵn trong editor

---

## 🔧 Server Management Scripts

### Khởi động server:
```bash
./start_server.sh
```

### Dừng server:
```bash
./stop_server.sh
```

### Kiểm tra server:
```bash
lsof -i :8888
```

### Xem logs:
```bash
tail -f server.log
```

---

## ⚠️ Troubleshooting

### Vấn đề: "Cannot connect to localhost:8888"

**Giải pháp 1:** Restart server
```bash
./stop_server.sh
./start_server.sh
```

**Giải pháp 2:** Manual restart
```bash
# Kill existing
lsof -ti :8888 | xargs kill -9

# Start new
cd /Users/Nguyen.vs/Documents/DrAnmytasUs
php -d memory_limit=2G -S localhost:8888 &
```

### Vấn đề: "Port already in use"

```bash
# Tìm process đang dùng port 8888
lsof -i :8888

# Kill process đó
kill -9 [PID]

# Hoặc dùng script
./stop_server.sh
./start_server.sh
```

### Vấn đề: "Memory limit exceeded"

Server đã được config với:
- Memory: 2GB
- Execution time: 1 hour
- Upload size: 2GB

Nếu vẫn không đủ, edit `start_server.sh` và tăng memory_limit.

---

## 📊 Server Info

**Current Status:**
- ✅ Running
- Port: 8888
- Memory: 2GB
- Timeout: 3600s

**Logs:**
- Real-time: `tail -f server.log`
- Full log: `cat server.log`

---

## 🎯 Next Steps

1. ✅ Server đang chạy
2. 👉 Mở browser: http://localhost:8888/installer.php
3. 📋 Làm theo wizard:
   - Click "Next"
   - Click "Extract Archive"
   - Đợi 5-15 phút
   - Setup database (hoặc skip)
   - Run deployment

4. 🎉 Hoàn tất!

---

## 💡 Quick Commands

```bash
# Start server
./start_server.sh

# Check status
curl -I http://localhost:8888/installer.php

# View logs
tail -f server.log

# Stop server
./stop_server.sh

# Monitor extraction
./monitor_extraction.sh
```

---

## 🔗 Useful Links

- Installer: http://localhost:8888/installer.php
- After extract: http://localhost:8888/
- Admin (after setup): http://localhost:8888/wp-admin/

---

**Server sẵn sàng! Bắt đầu extract ngay! 🚀**
