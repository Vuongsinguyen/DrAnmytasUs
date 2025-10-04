# 🖼️ HƯỚNG DẪN NÉN HÌNH SAU KHI XÓA BIẾN THỂ

## 🎯 MỤC TIÊU:
Nén mỗi hình xuống **300-500KB** với **85-90% quality**

---

## 🛠️ CÔNG CỤ NÉN (Chọn 1)

### **Option 1: ImageOptim (macOS - Miễn phí, Tốt nhất)**
✅ **KHUYẾN NGHỊ**

1. Download: https://imageoptim.com/mac
2. Kéo thả folder `out/wp-content/uploads` vào ImageOptim
3. Tự động nén lossless (~20-30% nhỏ hơn)

**Ưu điểm:**
- Miễn phí, dễ dùng
- Giữ quality gần như nguyên bản
- Hàng loạt được

---

### **Option 2: Squoosh (Web-based - Miễn phí)**
https://squoosh.app

1. Upload từng hình
2. Chọn format: **MozJPEG** hoặc **AVIF**
3. Quality: **85%**
4. Download

**Ưu điểm:**
- Không cần cài đặt
- Preview trước/sau
- Hỗ trợ AVIF (nhẹ hơn JPG 50%)

**Nhược điểm:**
- Phải làm thủ công từng hình

---

### **Option 3: jpegoptim (Command Line - Miễn phí)**

```bash
# Cài đặt
brew install jpegoptim

# Nén tất cả JPG xuống 85% quality
find out/wp-content/uploads -name "*.jpg" -type f -exec jpegoptim --max=85 {} \;

# Hoặc nén đến khi file < 500KB
find out/wp-content/uploads -name "*.jpg" -type f -exec jpegoptim --size=500k {} \;
```

**Ưu điểm:**
- Tự động, nhanh
- Xử lý hàng loạt

---

### **Option 4: TinyPNG (Web/API - 500 files/tháng miễn phí)**
https://tinypng.com

1. Upload tối đa 20 hình (5MB/hình)
2. Download hình đã nén
3. Thay thế file gốc

**Ưu điểm:**
- Nén smart (giảm 50-70%)
- Giữ quality rất tốt

**Nhược điểm:**
- Giới hạn 500 files/tháng
- Phải upload từng batch

---

## 📊 KẾT QUẢ KỲ VỌNG:

### **Trước khi nén:**
```
mo-nam-sang-da.jpg       4.9MB
HN_06014.jpg             3.6MB  
AQ07763.jpg              3.3MB
Untitled-4.jpg           4.5MB
```

### **Sau khi nén (85% quality):**
```
mo-nam-sang-da.jpg       450KB  (giảm 91%)
HN_06014.jpg             380KB  (giảm 89%)
AQ07763.jpg              350KB  (giảm 89%)
Untitled-4.jpg           420KB  (giảm 91%)
```

### **Tổng tiết kiệm:**
- 747MB → ~200MB
- **Giảm 73% dung lượng**
- Repository: 2.3GB → **700MB**

---

## ⚡ SCRIPT TỰ ĐỘNG (NHANH NHẤT)

```bash
# Nén tất cả JPG về 85% quality
find out/wp-content/uploads -name "*.jpg" -type f -exec jpegoptim --max=85 --strip-all {} \;

# Nén PNG (nếu có)
brew install optipng
find out/wp-content/uploads -name "*.png" -type f -exec optipng -o5 {} \;
```

---

## 🎯 LỰA CHỌN TỐT NHẤT:

### **Cho người không tech:**
→ **ImageOptim** (kéo thả, tự động)

### **Cho người muốn kiểm soát:**
→ **Squoosh** (preview, chọn quality)

### **Cho người muốn tự động:**
→ **jpegoptim** (command line, nhanh)

---

## ✅ CHECKLIST SAU KHI NÉN:

- [ ] Test website: `npm run dev`
- [ ] Kiểm tra hình vẫn hiển thị OK
- [ ] Kiểm tra quality chấp nhận được
- [ ] So sánh dung lượng trước/sau
- [ ] Commit lên Git

---

## 🆘 NẾU HÌNH BỊ MỜ/XẤU:

1. Khôi phục từ backup
2. Tăng quality lên 90% thay vì 85%
3. Hoặc giảm resolution xuống (resize về 1920px width)

---

## 💡 TIP:

**Thứ tự ưu tiên nén:**
1. File > 2MB (nặng nhất)
2. File trong folder 2025/04, 2025/05, 2023/12
3. Các file còn lại

**Công thức:**
- File > 2MB: nén xuống 400-500KB
- File 1-2MB: nén xuống 300-400KB  
- File < 1MB: giữ nguyên hoặc nén nhẹ
