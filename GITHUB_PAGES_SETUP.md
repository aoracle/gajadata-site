# GitHub Pages Setup for gajadata.com

## Current Status
- ✅ CNAME file created with `gajadata.com`
- ✅ File pushed to GitHub repository
- ⏳ DNS configuration needed
- ⏳ GitHub Pages activation needed

## Step 1: Update DNS Records at Domain Registrar (Squarespace)

**Delete the current forwarding rule** and replace with these DNS records:

### A Records (for apex domain gajadata.com)
```
Type: A
Name: @
Value: 185.199.108.153

Type: A  
Name: @
Value: 185.199.109.153

Type: A
Name: @  
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153
```

### CNAME Record (for www subdomain)
```
Type: CNAME
Name: www
Value: aoracle.github.io
```

## Step 2: Enable GitHub Pages

1. Go to: https://github.com/aoracle/gajadata-site/settings/pages
2. Under "Source": Select "Deploy from a branch"
3. Branch: Select `master`
4. Folder: Select `/ (root)`
5. Under "Custom domain": Enter `gajadata.com`
6. Check "Enforce HTTPS" (after domain verification)
7. Click "Save"

## Step 3: Verification

After DNS propagation (5-60 minutes):
- Site will be live at: https://gajadata.com
- GitHub will automatically provision SSL certificate
- Site will redirect www.gajadata.com → gajadata.com

## Benefits of GitHub Pages vs EC2

### GitHub Pages (Recommended)
- ✅ **FREE** hosting
- ✅ **HTTPS** included automatically  
- ✅ **No server maintenance**
- ✅ **Auto-deploys** on git push
- ✅ **99.9% uptime** on GitHub infrastructure
- ✅ **Global CDN** for fast loading

### EC2 (Current - Not needed)
- ❌ **$10-20/month** costs
- ❌ **Security updates** required
- ❌ **Apache configuration** maintenance
- ❌ **SSL certificate** manual setup
- ❌ **Server monitoring** needed

## Migration Steps (When Ready)

1. Complete DNS setup above
2. Verify GitHub Pages is working
3. Stop EC2 instance
4. Release Elastic IP (54.156.122.252)
5. Terminate EC2 instance

## Notes
- DNS changes can take up to 24 hours to fully propagate
- GitHub Pages deployment typically takes 1-3 minutes after push
- SSL certificate provisioning takes 15-30 minutes after domain verification