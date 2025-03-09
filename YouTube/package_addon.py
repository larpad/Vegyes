import os
import zipfile
import hashlib
import json
from datetime import datetime

def create_xpi():
    # Kiegészítő adatai
    addon_name = "marti-youtube-downloader"
    version = "1.0.0"
    
    # XPI fájlnév létrehozása
    xpi_filename = f"{addon_name}-{version}.xpi"
    
    # Becsomagolandó könyvtár
    source_dir = r"F:\GitHub\LÁ\Vegyes\YouTube\youtube-downloader-addon"
    
    # Kihagyandó fájlok és könyvtárak
    exclude = [
        'native-app',
        '.git',
        '__pycache__',
        '*.pyc',
        '.DS_Store'
    ]
    
    def should_exclude(file_path):
        for pattern in exclude:
            if pattern in file_path:
                return True
        return False
    
    # XPI fájl létrehozása
    with zipfile.ZipFile(xpi_filename, 'w', zipfile.ZIP_DEFLATED) as xpi:
        for root, dirs, files in os.walk(source_dir):
            # Kihagyandó könyvtárak kiszűrése
            dirs[:] = [d for d in dirs if not should_exclude(d)]
            
            for file in files:
                if not should_exclude(file):
                    file_path = os.path.join(root, file)
                    arc_path = os.path.relpath(file_path, source_dir)
                    print(f"Hozzáadva: {arc_path}")
                    xpi.write(file_path, arc_path)
    
    print(f"\nA kiegészítő sikeresen becsomagolva: {xpi_filename}")

if __name__ == "__main__":
    create_xpi() 