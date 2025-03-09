# Build Script for Multiple Applications

import os
import glob
import subprocess
from pathlib import Path

def find_main_files():
    """Megkeresi az összes main.py fájlt a src könyvtárban."""
    return glob.glob("src/**/main.py", recursive=True)

def get_app_name(main_file):
    """Generál egy alkalmazás nevet a main fájl útvonaláből."""
    parts = Path(main_file).parts
    # Az src utáni első könyvtárnév lesz az app neve
    app_index = parts.index('src') + 1
    if app_index < len(parts):
        return parts[app_index]
    return 'default'

def build_executable(main_file):
    """Létrehoz egy executable-t a megadott main fájlból."""
    app_name = get_app_name(main_file)
    output_extension = os.getenv('OUTPUT_EXTENSION', '')
    
    # PyInstaller konfiguráció
    command = [
        'pyinstaller',
        '--onefile',                          # Egy fájlba csomagolás
        '--clean',                            # Tiszta build
        f'--name={app_name}{output_extension}',  # Kimeneti fájlnév
        '--add-data=src/resources:resources', # Erőforrás fájlok hozzáadása (ha vannak)
        main_file
    ]
    
    # Extra ikonok vagy erőforrások hozzáadása Windows esetén
    if output_extension == '.exe':
        if os.path.exists(f'icons/{app_name}.ico'):
            command.append(f'--icon=icons/{app_name}.ico')
    
    # Build folyamat futtatása
    subprocess.run(command, check=True)

def main():
    """Fő build folyamat."""
    # Build könyvtár létrehozása
    os.makedirs('dist', exist_ok=True)
    
    # Minden main fájl megkeresése és build-elése
    main_files = find_main_files()
    for main_file in main_files:
        print(f"Building executable for {main_file}...")
        try:
            build_executable(main_file)
            print(f"Successfully built executable for {main_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error building executable for {main_file}: {e}")
            continue

if __name__ == "__main__":
    main()