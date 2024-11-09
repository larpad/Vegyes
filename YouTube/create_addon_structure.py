import os
import json

# Alap könyvtárszerkezet
base_dir = "youtube-downloader-addon"
directories = [
    "",
    "icons",
    "popup",
    "content_scripts",
    "native-app"
]

# Létrehozandó fájlok és tartalmuk
files = {
    "manifest.json": {
        "manifest_version": 2,
        "name": "Márti YouTube Letöltő",
        "version": "1.0",
        "description": "YouTube videók letöltése egyszerűen",
        "icons": {
            "48": "icons/icon.png"
        },
        "permissions": [
            "activeTab",
            "downloads",
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
        }
    },
    "popup/popup.html": """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            width: 300px;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h2>Márti YouTube Letöltő</h2>
    <p>Kattints a "Márti letölt" gombra bármely YouTube videó alatt a letöltéshez!</p>
</body>
</html>""",
    "content_scripts/youtube-downloader.js": "",
    "native-app/youtube_downloader.py": "",
    "native-app/youtube_downloader.json": {
        "name": "youtube_downloader",
        "description": "YouTube Downloader Native App",
        "path": "/teljes/elérési/út/youtube_downloader.py",
        "type": "stdio",
        "allowed_extensions": ["youtube_downloader@example.com"]
    }
}

def create_directory_structure():
    # Könyvtárak létrehozása
    for dir_path in directories:
        full_path = os.path.join(base_dir, dir_path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    # Fájlok létrehozása
    for file_name, file_content in files.items():
        full_path = os.path.join(base_dir, file_name)
        with open(full_path, 'w') as f:
            if isinstance(file_content, dict):
                json.dump(file_content, f)
            else:
                f.write(file_content)

create_directory_structure() 