# Hướng Dẫn Giải Nén WordPress Site với Duplicator

## ✅ Server đã khởi động thành công!

PHP Development Server đang chạy tại: **http://localhost:8888**

---

## 📋 Các Bước Thực Hiện

### Bước 1: Truy cập Installer
Mở trình duyệt và truy cập:
```
http://localhost:8888/installer.php
```

### Bước 2: Qua màn hình Setup/Validation
- Installer sẽ kiểm tra môi trường PHP
- Xác nhận các requirements
- Click **Next** để tiếp tục

### Bước 3: Extract Archive
Đây là bước quan trọng nhất:
- Chọn **Archive** tab
- Click nút **Extract Archive** 
- Đợi quá trình extract hoàn tất (có thể mất 5-15 phút với 1.69GB)
- Bạn sẽ thấy progress bar hiển thị tiến độ

### Bước 4: Database Setup
Có 2 lựa chọn:

#### Option A: Skip database (chỉ extract files)
Nếu bạn chỉ cần code để custom:
- Chọn "Create New Database" 
- Nhập thông tin database tạm (có thể skip bước này)
- Hoặc chọn "Manual Archive Extraction"

#### Option B: Full restore (bao gồm database)
Nếu bạn muốn website hoàn chỉnh:
- Tạo database mới (MySQL/MariaDB)
- Nhập thông tin:
  - Database Name: `dranmytas_local`
  - Database Host: `localhost`
  - Database User: `root`
  - Database Password: (your MySQL password)
  - Table Prefix: `wpp0_`

### Bước 5: Final Steps
- Cấu hình URL (localhost hoặc domain mới)
- Click **Run Deployment**
- Chờ quá trình hoàn tất

---

## 📂 Kết Quả Sau Khi Extract

Sau khi hoàn tất, bạn sẽ có cấu trúc WordPress đầy đủ:

```
DrAnmytasUs/
├── wp-admin/           # WordPress admin files
├── wp-content/         # Themes, plugins, uploads
│   ├── themes/         # WordPress themes
│   ├── plugins/        # Installed plugins  
│   └── uploads/        # Media files
├── wp-includes/        # WordPress core
├── index.php           # WordPress entry point
├── wp-config.php       # Database configuration
└── ...other WP files
```

---

## 🔧 Thông Tin Website

**Site Name:** Dr Anmytas  
**Original Domain:** dranmytas.com  
**WordPress Version:** 6.8.2  
**PHP Version:** 7.4.33  
**Total Files:** 23,596 files  
**Total Size:** ~1.69GB

**Admin Users:**
- admin
- manager  
- quanly

---

## 💡 Tips

### Nếu chỉ cần code để custom:
1. Extract xong, copy folder `wp-content/themes/` ra ngoài
2. Copy folder `wp-content/plugins/` nếu cần
3. Bỏ qua database setup
4. Làm việc trực tiếp với theme/plugin code

### Nếu muốn chạy full website locally:
1. Cài đặt MySQL/MariaDB
2. Tạo database mới
3. Hoàn tất tất cả các bước installer
4. Truy cập http://localhost:8888 để xem website

### Nếu gặp lỗi timeout:
- Tăng PHP memory limit trong php.ini
- Hoặc dùng manual extraction mode
- Restart PHP server

---

## 🚀 Next Steps Sau Khi Extract

1. **Kiểm tra cấu trúc:** `ls -la` trong thư mục gốc
2. **Xem themes:** `ls -la wp-content/themes/`
3. **Xem plugins:** `ls -la wp-content/plugins/`
4. **Update .gitignore:** Để track code, không track uploads
5. **Start developing:** Bắt đầu custom theme/plugin

---

## ⚠️ Lưu Ý

- **Backup:** Duplicator sẽ tự động backup các file gốc
- **Permissions:** Đảm bảo thư mục có quyền write (755)
- **Memory:** Process có thể dùng nhiều RAM
- **Time:** Quá trình extract có thể mất vài phút

---

## 📞 Troubleshooting

### Lỗi "Archive not found"
- Đảm bảo file .daf ở cùng thư mục với installer.php

### Lỗi "Permission denied"
```bash
chmod 755 /Users/Nguyen.vs/Documents/DrAnmytasUs
```

### Lỗi "Memory limit"
Sửa file php.ini hoặc restart với:
```bash
php -d memory_limit=2G -S localhost:8888
```

### Muốn dừng server
Nhấn `Ctrl + C` trong terminal

---

**Happy Coding! 🎉**

Sau khi extract xong, bạn sẽ có toàn bộ WordPress site để custom và build thêm tính năng mới!
