import os
import zipfile
import json
import shutil
from pathlib import Path

def validate_manifest(manifest_path):
    """Manifest.json ellenőrzése"""
    try:
        with open(manifest_path, 'r', encoding='utf-8-sig') as f:
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

def read_file_content(file_path):
    """Fájl tartalmának beolvasása különböző kódolások próbálgatásával"""
    encodings = ['utf-8', 'utf-8-sig', 'latin1', 'cp1250', 'iso-8859-2']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    
    # Ha egyik kódolás sem működött, próbáljuk bináris módban
    with open(file_path, 'rb') as f:
        return f.read()

def create_xpi():
    # Kiírjuk a jelenlegi könyvtárat
    print(f"Jelenlegi munkakönyvtár: {os.getcwd()}")
    
    # Kiírjuk a szkript helyét
    print(f"Szkript helye: {os.path.dirname(os.path.abspath(__file__))}")
    
    # Konstansok
    ADDON_NAME = "marti-youtube-downloader"
    VERSION = "1.0.0"
    SOURCE_DIR = "youtube-downloader-addon"
    BUILD_DIR = "build"
    
    # Teljes elérési utak
    current_dir = os.getcwd()
    source_path = os.path.join(current_dir, SOURCE_DIR)
    build_path = os.path.join(current_dir, BUILD_DIR)
    
    print(f"\nKeresett mappák:")
    print(f"Forrásmappa: {source_path}")
    print(f"Build mappa: {build_path}")
    
    # Ellenőrizzük a forrásmappa létezését
    if not os.path.exists(source_path):
        print(f"\nHIBA: A forrásmappa nem található: {source_path}")
        return False
    
    # Build könyvtár létrehozása
    os.makedirs(build_path, exist_ok=True)
    print(f"\nBuild mappa létrehozva: {build_path}")
    
    # XPI fájl neve és teljes elérési útja
    xpi_filename = f"{ADDON_NAME}-{VERSION}.xpi"
    xpi_path = os.path.join(build_path, xpi_filename)
    
    try:
        # XPI létrehozása
        with zipfile.ZipFile(xpi_path, 'w', zipfile.ZIP_DEFLATED) as xpi:
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, source_path)
                    print(f"Hozzáadva: {arc_name}")
                    xpi.write(file_path, arc_name)
        
        print(f"\nA kiegészítő sikeresen becsomagolva!")
        print(f"Fájl neve: {xpi_filename}")
        print(f"Teljes elérési út: {os.path.abspath(xpi_path)}")
        print(f"Méret: {os.path.getsize(xpi_path):,} byte")
        return True
        
    except Exception as e:
        print(f"HIBA történt a becsomagolás során: {str(e)}")
        return False

if __name__ == "__main__":
    create_xpi()