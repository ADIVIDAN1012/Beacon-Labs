# 🚀 Redeploy Beacon Website to GitHub Pages

## ✅ Changes Pushed to GitHub

Your website files are now updated and pushed to: https://github.com/ADIVIDAN1012/Beacon-Labs

**Updated:**
- Download links now point to v1.0.0 GitHub release assets
- BPL.exe link: `https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/BPL.exe`
- VS Code extension link: `https://github.com/ADIVIDAN1012/Beacon-Labs/releases/download/v1.0.0/beacon-0.0.3.vsix`

---

## 📋 Next Steps: Configure GitHub Pages

### Option 1: Deploy from `beacon-website` folder (Recommended)

1. Go to: https://github.com/ADIVIDAN1012/Beacon-Labs/settings/pages

2. Under **Source**:
   - Branch: Select **main**
   - Folder: Select **/beacon-website**
   - Click **Save**

3. Wait 1-2 minutes for deployment

4. Your site will be live at:
   ```
   https://adividan1012.github.io/Beacon-Labs/
   ```

### Option 2: Deploy from root with custom workflow

If you want the site at the root URL without the `/beacon-website` path, you'll need to either:
- Move the website files to the root directory, OR
- Create a custom GitHub Actions workflow

---

## ⚡ Quick Deploy (Recommended)

**Just follow these 3 steps:**

1. **Open Settings**: https://github.com/ADIVIDAN1012/Beacon-Labs/settings/pages

2. **Configure**:
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/beacon-website**

3. **Save** and wait 1-2 minutes

---

## 🔍 Verify Deployment

Once deployed, check:
- ✅ Site loads: https://adividan1012.github.io/Beacon-Labs/
- ✅ Download buttons work
- ✅ Styling looks correct
- ✅ Images load properly

---

## 🔄 Future Updates

To update the website in the future:

```bash
cd c:\Users\aadit\OneDrive\Desktop\project_2_Beacon

# Make changes to beacon-website/index.html or style.css

git add beacon-website/
git commit -m "Update website"
git push origin main
```

GitHub will automatically redeploy within 1-2 minutes!

---

**Your website is ready to go live! 🎉**
