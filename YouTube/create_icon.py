from PIL import Image, ImageDraw

def create_youtube_downloader_icon():
    # Konstansok
    SIZE = 48  # Firefox követelmény
    BACKGROUND_COLOR = (204, 0, 0)  # YouTube piros (#cc0000)
    ARROW_COLOR = (255, 255, 255)  # Fehér
    
    # Új kép létrehozása átlátszó háttérrel
    icon = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    
    # Rajzoló objektum létrehozása
    draw = ImageDraw.Draw(icon)
    
    # Kör alakú háttér rajzolása
    padding = 2
    draw.ellipse([padding, padding, SIZE-padding, SIZE-padding], 
                 fill=BACKGROUND_COLOR)
    
    # Letöltés nyíl méretei
    arrow_width = SIZE * 0.4
    arrow_height = SIZE * 0.4
    arrow_thickness = SIZE * 0.15
    
    # Nyíl pozícionálása középre
    start_x = (SIZE - arrow_width) / 2
    start_y = (SIZE - arrow_height) / 2 - 2  # Kicsit feljebb toljuk
    
    # Nyíl szár rajzolása
    shaft_x = start_x + arrow_width/2 - arrow_thickness/2
    draw.rectangle([
        shaft_x,
        start_y,
        shaft_x + arrow_thickness,
        start_y + arrow_height
    ], fill=ARROW_COLOR)
    
    # Nyílhegy pontjai
    arrow_head_points = [
        (start_x, start_y + arrow_height * 0.6),  # Bal pont
        (start_x + arrow_width, start_y + arrow_height * 0.6),  # Jobb pont
        (start_x + arrow_width/2, start_y + arrow_height)  # Alsó pont
    ]
    
    # Nyílhegy rajzolása
    draw.polygon(arrow_head_points, fill=ARROW_COLOR)
    
    # Ikon mentése
    icon_path = "youtube-downloader-addon/icons/icon.png"
    
    # Mappa létrehozása, ha nem létezik
    import os
    os.makedirs(os.path.dirname(icon_path), exist_ok=True)
    
    # Ikon mentése
    icon.save(icon_path, "PNG")
    print(f"Ikon sikeresen létrehozva: {icon_path}")
    
    # Méret ellenőrzése
    icon_size = os.path.getsize(icon_path)
    print(f"Ikon mérete: {icon_size} byte")

if __name__ == "__main__":
    create_youtube_downloader_icon() 