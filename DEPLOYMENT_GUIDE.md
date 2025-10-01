# Dr. Anmytas - Multi-language Static Site

## 📁 Cấu trúc thư mục

```
DrAnmytasUs/
├── static-site/          # Phiên bản tiếng Việt (Vietnamese)
├── static-site-en/       # Phiên bản tiếng Anh (English)
├── out/                  # Build output (được tạo tự động)
├── wp-content/           # WordPress content
├── wp-includes/          # WordPress includes
└── translate_to_english.py  # Script tự động dịch
```

## 🚀 Build Commands

### Build phiên bản tiếng Anh (mặc định cho production)
```bash
npm run build
# hoặc
npm run build:en
```

### Build phiên bản tiếng Việt
```bash
npm run build:vi
```

### Development

```bash
# Run dev server với phiên bản tiếng Anh
npm run dev:en

# Run dev server với phiên bản tiếng Việt
npm run dev:vi
```

Truy cập: http://localhost:8888

## 🌍 Deploy lên Vercel

### Deploy phiên bản tiếng Anh (English - Mặc định)

1. **Commit và push code:**
```bash
git add .
git commit -m "Update: English version ready for deployment"
git push origin main
```

2. **Vercel sẽ tự động deploy** với cấu hình hiện tại (English version)

### Chuyển sang deploy phiên bản tiếng Việt

Nếu muốn deploy phiên bản tiếng Việt thay vì tiếng Anh:

1. Sửa file `package.json`, dòng `"build"`:
```json
"build": "echo 'Building Vietnamese static site...' && mkdir -p out && cp -r static-site/* out/ && cp -r wp-content out/ && cp -r wp-includes out/"
```

2. Commit và push:
```bash
git add package.json
git commit -m "Switch to Vietnamese version"
git push origin main
```

## 🔄 Dịch lại website

Nếu bạn cập nhật nội dung trong `static-site/` (tiếng Việt) và muốn dịch lại sang tiếng Anh:

```bash
# Dịch toàn bộ và cập nhật static-site-en/
python3 translate_to_english.py --output static-site-en

# Xem trước thay đổi trước khi dịch
python3 translate_to_english.py --dry-run

# Dịch một file cụ thể
python3 translate_to_english.py --file static-site/index.html --output static-site-en/index.html
```

## 📝 Quy trình làm việc thông thường

### Cập nhật nội dung website:

1. **Chỉnh sửa file tiếng Việt** trong `static-site/`
2. **Dịch sang tiếng Anh:**
   ```bash
   python3 translate_to_english.py --output static-site-en
   ```
3. **Test local:**
   ```bash
   npm run build:en
   npm run dev
   ```
4. **Commit và deploy:**
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```

## 🛠️ Tùy chỉnh từ điển dịch

Để thêm hoặc sửa từ dịch, chỉnh sửa file `translate_to_english.py`:

```python
TRANSLATION_DICT = {
    'Từ tiếng Việt': 'English Word',
    'Chăm Sóc Da': 'Skin Care',
    # Thêm từ mới ở đây...
}
```

## 📊 Thống kê

- **Tổng số file đã dịch:** 292 files
- **Ngôn ngữ hiện tại trên production:** English (en-US)
- **Ngôn ngữ source:** Vietnamese (vi-VN)

## ⚙️ Cấu hình Vercel

File `vercel.json` hiện tại:
```json
{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": "out"
}
```

Build command mặc định: `npm run build` → Deploy phiên bản tiếng Anh

## 📞 Liên hệ

- Website: https://dranmytas.vercel.app
- GitHub: https://github.com/Vuongsinguyen/DrAnmytasUs

---

**Lưu ý:** 
- Folder `out/` được tạo tự động, không cần commit vào Git
- Luôn chỉnh sửa trong `static-site/` (Vietnamese) hoặc `static-site-en/` (English)
- Không chỉnh sửa trực tiếp trong folder `out/` vì sẽ bị ghi đè khi build
