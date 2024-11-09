import os
import json

def create_addon_structure():
    # Alap könyvtárszerkezet
    base_dir = "youtube-downloader-addon"
    directories = [
        "icons",
        "content_scripts",
        "popup"
    ]
    
    # Könyvtárak létrehozása
    for dir_path in directories:
        full_path = os.path.join(base_dir, dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Könyvtár létrehozva: {full_path}")

    # Javított manifest.json tartalom
    manifest = {
        "manifest_version": 2,
        "name": "Marti YouTube Downloader",
        "version": "1.0.0",
        "description": "Simple YouTube video downloader",
        "icons": {
            "48": "icons/icon.png"
        },
        "permissions": [
            "activeTab",
            "nativeMessaging",
            "*://*.youtube.com/*"
        ],
        "content_scripts": [
            {
                "matches": ["*://*.youtube.com/*"],
                "js": ["content_scripts/youtube-downloader.js"]
            }
        ],
        "browser_action": {
            "default_icon": "icons/icon.png",
            "default_popup": "popup/popup.html"
        },
        "applications": {
            "gecko": {
                "id": "youtube-downloader@example.com",
                "strict_min_version": "57.0"
            }
        },
        "author": "Marti",
        "homepage_url": "https://github.com/yourusername/youtube-downloader"
    }

    # Egyszerűsített popup.html
    popup_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { width: 300px; padding: 10px; }
    </style>
</head>
<body>
    <h2>YouTube Downloader</h2>
    <p>Click the download button below any YouTube video.</p>
</body>
</html>"""

    # Egyszerű content script
    content_script = """
function addDownloadButton() {
    if (!window.location.pathname.includes('/watch')) return;
    
    const menuContainer = document.querySelector('#top-level-buttons-computed');
    if (!menuContainer || document.querySelector('.marti-download-btn')) return;
    
    const downloadBtn = document.createElement('button');
    downloadBtn.className = 'marti-download-btn';
    downloadBtn.innerHTML = 'Download';
    downloadBtn.style.cssText = `
        background: #cc0000;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 18px;
        cursor: pointer;
        margin-left: 8px;
    `;
    
    downloadBtn.addEventListener('click', () => {
        const videoId = new URLSearchParams(window.location.search).get('v');
        if (videoId) {
            alert('Download started for video: ' + videoId);
        }
    });
    
    menuContainer.appendChild(downloadBtn);
}

// Initial run
addDownloadButton();

// Watch for page changes
new MutationObserver(() => {
    addDownloadButton();
}).observe(document.body, { childList: true, subtree: true });
"""

    # Fájlok létrehozása
    files = {
        os.path.join(base_dir, "manifest.json"): json.dumps(manifest, indent=4, ensure_ascii=False),
        os.path.join(base_dir, "popup", "popup.html"): popup_html,
        os.path.join(base_dir, "content_scripts", "youtube-downloader.js"): content_script,
    }

    for file_path, content in files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fájl létrehozva: {file_path}")

if __name__ == "__main__":
    create_addon_structure() 