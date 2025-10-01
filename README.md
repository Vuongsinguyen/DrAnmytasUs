# Dr Anmytas WordPress Site

WordPress site extracted from Duplicator Pro backup, ready for local development.

## 📊 Project Info

- **Site Name:** Dr Anmytas
- **WordPress Version:** 6.8.2
- **Total Files:** 23,617 files
- **Total Folders:** 2,635 directories
- **Original Domain:** dranmytas.com
- **Local URL:** http://localhost:8888

## 🎨 Themes

1. **Flatsome** (Primary theme)
2. **Ruamat**

Location: `wp-content/themes/`

## 🔌 Plugins Installed (17 plugins)

### Essential
- Advanced Custom Fields Pro
- Classic Editor
- Classic Widgets
- Contact Form 7

### E-commerce & Location
- Devvn Local Stores Pro
- WooCommerce (via Flatsome theme)

### SEO & Performance
- Rank Math SEO
- Rank Math SEO Pro
- LiteSpeed Cache

### Media & Files
- FileBird Pro
- HTML5 Video Player

### Backup & Utilities
- Duplicator Pro
- ... and more!

Location: `wp-content/plugins/`

## 🚀 Quick Start

### Start Development Server

```bash
./start_server.sh
```

Server will run at: http://localhost:8888

### Stop Server

```bash
./stop_server.sh
```

### Check MySQL Status

```bash
./check_mysql.sh
```

## 🗄️ Database Configuration

- **Host:** localhost
- **Database:** dranmytas_local
- **User:** root
- **Password:** (empty)
- **Charset:** utf8mb4
- **Collation:** utf8mb4_unicode_ci

### Access Database

```bash
mysql -u root dranmytas_local
```

## 💻 Development

### Directory Structure

```
DrAnmytasUs/
├── wp-admin/           # WordPress admin panel (102 files)
├── wp-content/         # Your themes, plugins, uploads
│   ├── themes/         # Flatsome, Ruamat
│   ├── plugins/        # 17 plugins
│   ├── uploads/        # Media files (gitignored)
│   └── cache/          # Cache files (gitignored)
├── wp-includes/        # WordPress core libraries (274 files)
├── index.php           # WordPress entry point
├── wp-config.php       # Database config (gitignored)
└── [helper scripts]
```

### Working with Code

**View Themes:**
```bash
cd wp-content/themes
ls -la
```

**View Plugins:**
```bash
cd wp-content/plugins
ls -la
```

**Edit Theme:**
```bash
code wp-content/themes/flatsome/
```

## 🌐 URLs

- **Frontend:** http://localhost:8888
- **Admin Panel:** http://localhost:8888/wp-admin
- **Login Page:** http://localhost:8888/wp-login.php

## 🧹 Cleanup

To remove installer files and temporary scripts:

```bash
./cleanup_installer.sh
```

This will remove:
- `dup-installer/` directory
- `installer.php`
- Temporary extraction scripts
- Boot log files

## 📝 Helper Scripts

| Script | Purpose |
|--------|---------|
| `start_server.sh` | Start PHP development server |
| `stop_server.sh` | Stop PHP server |
| `check_mysql.sh` | Check MySQL status and database |
| `cleanup_installer.sh` | Remove installer files |
| `monitor_extraction.sh` | Monitor extraction progress |

## 🔧 Server Configuration

**PHP Settings:**
- Memory Limit: 2GB
- Execution Timeout: 3600s (1 hour)
- Error Reporting: Deprecation warnings suppressed
- Upload Max: 2GB
- Post Max: 2GB

**MySQL:**
- Version: 9.4.0
- Character Set: utf8mb4
- Collation: utf8mb4_unicode_ci

## 📚 Documentation Files

- `EXTRACTION_SUMMARY.txt` - Complete extraction summary
- `DATABASE_SETUP_GUIDE.txt` - Database configuration guide
- `ERROR_FIXED.txt` - PHP deprecation warnings fix
- `HUONG_DAN_EXTRACT.md` - Vietnamese extraction guide
- `QUICK_START.txt` - Quick reference
- `SERVER_GUIDE.md` - Server management
- `MYSQL_INFO.txt` - MySQL connection details

## 🛠️ Troubleshooting

### Server won't start
```bash
# Check if port 8888 is in use
lsof -i :8888

# Force stop and restart
./stop_server.sh
./start_server.sh
```

### Database connection failed
```bash
# Check MySQL is running
./check_mysql.sh

# Restart MySQL
brew services restart mysql
```

### Can't access site
1. Make sure server is running: `ps aux | grep "php.*8888"`
2. Check server logs: `tail -f server.log`
3. Verify database: `mysql -u root dranmytas_local`

## 📦 Git Workflow

### What's tracked:
- ✅ WordPress core files
- ✅ Themes code
- ✅ Plugins code
- ✅ Helper scripts
- ✅ Documentation

### What's ignored:
- ❌ `wp-config.php` (sensitive credentials)
- ❌ `wp-content/uploads/*` (media files)
- ❌ `wp-content/cache/*` (cache)
- ❌ `*.log` files
- ❌ Backup files (*.daf, *.zip)
- ❌ Installer files

## 🎯 Next Steps

1. ✅ Extraction completed
2. 🌐 Visit http://localhost:8888 to view your site
3. 🔐 Login to wp-admin to verify everything works
4. 💻 Start customizing themes/plugins
5. 🧹 Run cleanup script when ready
6. 📝 Commit your changes to git

## 🔐 Security Notes

- This is a **local development** environment
- MySQL has no password (fine for local)
- Don't expose port 8888 to public network
- Keep `wp-config.php` out of version control

## 📞 Support

If you encounter any issues:
1. Check the documentation files
2. Review server logs: `tail -f server.log`
3. Check MySQL status: `./check_mysql.sh`
4. Review WordPress debug.log: `tail -f wp-content/debug.log`

---

**Generated:** October 1, 2025  
**Project:** DrAnmytasUs  
**Repository:** https://github.com/Vuongsinguyen/DrAnmytasUs

Happy coding! 🚀
