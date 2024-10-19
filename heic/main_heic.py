import os
import sys
import site
from loguru import logger

def add_site_packages_to_path():
    if getattr(sys, 'frozen', False):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    site_packages = os.path.join(base_path, 'pillow_heif')
    site.addsitedir(site_packages)

add_site_packages_to_path()

try:
    import pillow_heif
except ImportError as e:
    logger.error(f"Failed to import pillow_heif: {e}")
    sys.exit(1)

from PIL import Image

def convert_heic_to_jpg(directory):
    logger.info(f"Starting HEIC to JPG conversion in directory: {directory}")
    try:
        # Ensure pillow_heif is registered
        pillow_heif.register_heif_opener()
        logger.debug("pillow_heif registered successfully")

        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            if filename.lower().endswith('.heic'):
                heic_path = os.path.join(directory, filename)
                jpg_path = os.path.join(directory, os.path.splitext(filename)[0] + '.jpg')

                logger.info(f"Processing file: {filename}")
                try:
                    # Open the HEIC image
                    with Image.open(heic_path) as img:
                        # Convert and save as JPG
                        img.convert('RGB').save(jpg_path, 'JPEG')
                    logger.success(f"Converted {filename} to JPG successfully")
                except Exception as e:
                    logger.error(f"Error converting {filename}: {str(e)}")
    except Exception as e:
        logger.error(f"Error in convert_heic_to_jpg function: {str(e)}")

if __name__ == "__main__":
    try:
        import argparse

        logger.info("Starting HEIC to JPG conversion script")

        parser = argparse.ArgumentParser(description="Convert HEIC images to JPG")
        parser.add_argument("--directory", default=os.environ.get('DIRECTORY_HIC', 'C:\\Users\\Apu\\OneDrive\\2024.09.23 Picurok születésnapja'), help="Directory containing HEIC images")
        args = parser.parse_args()

        directory_path = args.directory
        logger.info(f"Directory path: {directory_path}")

        if not os.path.isdir(directory_path):
            logger.error(f"Error: {directory_path} is not a valid directory")
            sys.exit(1)

        # Ensure the correct Python environment is used
        python_executable = sys.executable
        logger.info(f"Using Python executable: {python_executable}")

        convert_heic_to_jpg(directory_path)
        logger.success("HEIC to JPG conversion completed")
    except Exception as e:
        logger.error(f"Unhandled exception in main script: {str(e)}")
        sys.exit(1)
