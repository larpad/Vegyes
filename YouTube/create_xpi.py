import os
import zipfile
import json
import shutil
from pathlib import Path

def validate_manifest(manifest_path):
    """Manifest.json ellenőrzése"""
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        required_fields = ['manifest_version', 'name', 'version', 'description']
        for field in required_fields:
            if field not in manifest:
                print(f"HIBA: Hiányzó kötelező mező a manifest.json-ból: {field}")
                return False
                
        return True
    except json.JSONDecodeError as e:
        print(f"HIBA: Érvénytelen JSON formátum a manifest.json fájlban: {str(e)}")
        return False
    except Exception as e:
        print(f"HIBA a manifest.json ellenőrzése során: {str(e)}")
        return False

def create_xpi():
    # Konstansok
    ADDON_NAME = "marti-youtube-downloader"
    VERSION = "1.0.0"
    SOURCE_DIR = "youtube-downloader-addon"
    BUILD_DIR = "build"
    
    # Build könyvtár létrehozása/tisztítása
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)
    
    # Manifest ellenőrzése
    manifest_path = os.path.join(SOURCE_DIR, "manifest.json")
    if not validate_manifest(manifest_path):
        return False
    
    # Kötelező fájlok ellenőrzése
    required_files = [
        "manifest.json",
        "icons/icon.png",
        "content_scripts/youtube-downloader.js",
        "popup/popup.html"
    ]
    
    for file_path in required_files:
        full_path = os.path.join(SOURCE_DIR, file_path)
        if not os.path.exists(full_path):
            print(f"HIBA: Hiányzó kötelező fájl: {file_path}")
            return False
    
    # XPI fájl neve
    xpi_filename = f"{ADDON_NAME}-{VERSION}.xpi"
    xpi_path = os.path.join(BUILD_DIR, xpi_filename)
    
    try:
        # XPI létrehozása
        with zipfile.ZipFile(xpi_path, 'w', zipfile.ZIP_DEFLATED) as xpi:
            for root, dirs, files in os.walk(SOURCE_DIR):
                # Kihagyandó fájlok és mappák
                if '.git' in dirs:
                    dirs.remove('.git')
                if '__pycache__' in dirs:
                    dirs.remove('__pycache__')
                if 'native-app' in dirs:
                    dirs.remove('native-app')
                
                for file in files:
                    if file.endswith(('.pyc', '.pyo', '.DS_Store')):
                        continue
                        
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, SOURCE_DIR)
                    
                    # UTF-8 kódolás biztosítása szöveges fájloknál
                    if file.endswith(('.json', '.js', '.html', '.css')):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        xpi.writestr(arc_name, content.encode('utf-8'))
                    else:
                        xpi.write(file_path, arc_name)
                    
                    print(f"Hozzáadva: {arc_name}")
        
        print(f"\nA kiegészítő sikeresen becsomagolva: {xpi_path}")
        print(f"Méret: {os.path.getsize(xpi_path)} byte")
        return True
        
    except Exception as e:
        print(f"HIBA történt a becsomagolás során: {str(e)}")
        return False

if __name__ == "__main__":
    create_xpi() 