# Dr. Anmytas - Static Website

This is a static version of the Dr. Anmytas website exported from WordPress.

## Deployment

This site is ready to be deployed to Vercel.

### Deploy to Vercel

#### Option 1: Using Vercel CLI (Recommended)

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   cd static-site
   vercel
   ```

3. Follow the prompts to link your Vercel account

#### Option 2: Using Vercel Dashboard

1. Push this `static-site` folder to a GitHub repository
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Set the root directory to `static-site`
6. Click "Deploy"

### Custom Domain

After deployment, you can add your custom domain in Vercel:
1. Go to Project Settings → Domains
2. Add your domain
3. Configure DNS records as instructed

## Features

- ✅ Static HTML files (fast loading)
- ✅ All images and assets included
- ✅ Clean URLs enabled
- ✅ Security headers configured
- ✅ Cache optimization for static assets
- ✅ Free hosting on Vercel
- ✅ SSL/HTTPS included
- ✅ Custom domain support

## Languages

This build includes only the English version of the website.

## Tech Stack

- WordPress (source)
- wget (static site generator)
- Vercel (hosting)
