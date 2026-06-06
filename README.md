# Yoga Day — Simple Site

A minimal static site for Yoga Day. This repo is intended to be hosted on GitHub Pages or previewed locally.

## Local preview

Run a simple static server from the `yodaday` folder:

```bash
cd yodaday
python -m http.server 8000
# then open http://localhost:8000 in your browser
```

## Image reference

The site includes a hero image from `assets/whatsapp.jpg` which is already copied to the project. When deploying to GitHub Pages, ensure the `assets` folder is committed.

### To update the image

Simply replace `assets/whatsapp.jpg` with your new image (same name and path).

## Git setup

To initialize the repo and commit:

```bash
cd yodaday
git init
git add .
git commit -m "Initial commit: Yoga Day site"
git remote add origin https://github.com/YOUR_USERNAME/yodaday.git
git branch -M main
git push -u origin main
```

Then enable GitHub Pages in your repo settings (Pages > Deploy from a branch > main).
