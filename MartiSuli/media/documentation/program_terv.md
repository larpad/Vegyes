# Program terv: MartiSuli Adatbázis Kezelő Alkalmazás

## 1. Általános leírás
Ez a program terv egy Flask-alapú, egyablakos (SDI) webalkalmazást ír le, amely a MartiSuli adatbázis kezelésére szolgál. Az alkalmazás a korábban definiált adatbázis modellt használja, amely tartalmazza a Szemely, Media, Eloadas, Kategoria, Eloadas_Blob és Eloadas_Blob_Tipus entitásokat, valamint a közöttük lévő kapcsolatokat.

## 2. Technológiai stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Adatbázis: SQLAlchemy ORM, SQLite adatbázis

## 3. Alkalmazás struktúra

### 3.1 Backend (Flask)
- `app.py`: A fő Flask alkalmazás
- `models.py`: Az adatbázis modellek definíciói
- `views.py`: Az API végpontok és nézetek
- `utils.py`: Segédfüggvények
- `db.py`: DatabaseManager osztály az adatbázis műveletek kezelésére

### 3.2 Frontend
- `index.html`: Az egyetlen HTML oldal, amely az alkalmazás vázát tartalmazza
- `static/css/styles.css`: Az alkalmazás stíluslapja
- `static/js/app.js`: A kliens oldali JavaScript kód

## 4. Fő funkciók

### 4.1 Navigáció
- Főoldal
- Entitások böngészése (Szemely, Media, Eloadas, Kategoria, Eloadas_Blob, Eloadas_Blob_Tipus)

### 4.2 CRUD műveletek
- Új rekord hozzáadása minden entitáshoz
- Meglévő rekordok szerkesztése
- Rekordok törlése
- Rekordok részleteinek megtekintése

### 4.3 Keresés és szűrés
- Keresés minden entitásban
- Szűrés különböző mezők alapján (pl. dátum, név, cím)
- Szűrés Szemely rekordokra születési és halálozási dátum alapján
- Szűrés Media rekordokra létrehozási dátum alapján
- Szűrés Media és Eloadas rekordokra leiras vagy megjegyzes tartalom alapján
- Szűrés Kategoria rekordokra leiras vagy megjegyzes tartalom alapján
- Szűrés Eloadas_Blob rekordokra leiras vagy megjegyzes tartalom alapján
- Szűrés Media rekordokra zeneszerzo (composer) alapján
- Szűrés Eloadas rekordokra előadó (performer) alapján
- Szűrés Eloadas_Blob rekordokra Eloadas_Blob_Tipus alapján

### 4.4 Asszociációk kezelése
- Entitások közötti kapcsolatok létrehozása és törlése
- Kapcsolódó rekordok megtekintése
- Szemely asszociálása Media-hoz szerzőként vagy zeneszerzőként
- Szemely asszociálása Eloadas-hoz előadóként
- Media és Eloadas asszociálása Kategoria-hoz
- Több Kategoria hozzáadása egy Media-hoz vagy Eloadas-hoz egyszerre

### 4.5 Adatexport és -import
- Adatok exportálása CSV vagy JSON formátumban
- Adatok importálása fájlból

### 4.6 Riportok és statisztikák
- Különböző riportok generálása (pl. legnépszerűbb média, legaktívabb személy)
- Adatbázis statisztikák megtekintése
- Leggyakrabban használt kategóriák riportja
- Személy-együttműködési hálózat generálása közös Media vagy Eloadas alapján
- Idővonalas riportok generálása (pl. Szemely Media és Eloadas története)
- Riport generálása a legtöbb Media-val vagy Eloadas-sal rendelkező Szemely-ekről
- Riport generálása a legproduktívabb zeneszerzőkről
- Riport generálása a legtöbb asszociált Kategoria-val rendelkező Media-ról és Eloadas-ról
- Riport generálása a legváltozatosabb Eloadas_Blob_Tipus-sal rendelkező Eloadas-okról
- Riport generálása a legsokoldalúbb Szemely-ekről (több szerepben is részt vesznek)
- Riport generálása a leggyakrabban használt fájlkiterjesztésekről az Eloadas_Blob-okban
- Riport generálása a Szemely-ek legváltozatosabb Kategoria asszociációiról (Media és Eloadas keresztül)

### 4.7 Speciális funkciók
- Több Eloadas_Blob rekord hozzáadása egy Eloadas-hoz egyszerre
- Tömeges törlés több rekordra bármely típusból
- Tömeges frissítés több azonos típusú rekordra
- Törölt rekordok visszaállítása (ha soft delete van implementálva)
- Árva rekordok megtekintése (pl. Media Szemely nélkül)
- Duplikált rekordok összevonása (Szemely, Media, Kategoria)
- Szófelhő generálása az összes Media dalszövegéből
- Idővonalas nézet egy Kategoria használatáról Media és Eloadas között
- Hálózati gráf generálása a Kategoria kapcsolatokról közös Media vagy Eloadas alapján
- Media rekordok megtekintése dalszöveggel (dalszoveg)
- Media rekordok keresése dalszöveg tartalom alapján
- Eloadas rekordok rendezése a hozzájuk kapcsolódó Eloadas_Blob rekordok száma alapján
- Media rekordok megtekintése egy adott Eloadas_Blob_Tipus-hoz kapcsolódóan
- Szemely rekordok megtekintése, akik mind szerzők, mind előadók
- Media rekordok rendezése a hozzájuk kapcsolódó Eloadas-ok száma alapján
- Eloadas_Blob_Tipus rekordok rendezése használati gyakoriság alapján
- Media létrehozás legaktívabb időszakainak riportja
- Szemely rekordok megtekintése, akiknek van kapcsolódó Media-juk, de nincs Eloadas-uk
- Media rekordok megtekintése, amelyeknek van kapcsolódó Eloadas-uk, de nincs Eloadas_Blob-juk
- Media rekordok megtekintése adott létrehozási évvel
- Szemely rekordok szűrése azokra, akik szereztek Media-t
- Szemely rekordok szűrése azokra, akik előadtak Eloadas-t
- Kategoria rekordok rendezése a hozzájuk kapcsolódó Media és Eloadas száma alapján
- Eloadas rekordok megtekintése adott számú kapcsolódó Eloadas_Blob rekorddal
- Media rekordok megtekintése adott datum_keletkezes értékkel
- Riport generálása a leggyakoribb szavakról a Media leiras mezőjében
- Eloadas_Blob rekordok megtekintése egy adott Eloadas-hoz
- Media rekordok megtekintése Kategoria nélkül
- Szemely rekordok rendezése név, születési dátum vagy halálozási dátum alapján
- Media rekordok rendezése cím vagy létrehozási dátum alapján
- Eloadas rekordok rendezése a kapcsolódó Media címe alapján
- Kategoria rekordok rendezése név alapján
- Összes olyan Media rekord megtekintése, ahol egy Szemely egyszerre szerző és zeneszerző
- Eloadas_Blob rekordok szűrése fájlméret alapján
- Összes olyan Szemely megtekintése, akik mind Media-t szereztek, mind Eloadas-ban szerepeltek
- Összes olyan Media megtekintése, amelynek nincs zeneszerzője (zeneszerzo)

## 5. Felhasználói felület terv

### 5.1 Főoldal
- Üdvözlő üzenet
- Gyors linkek a fő funkciókhoz
- Összesített statisztikák

### 5.2 Entitás listák
- Táblázatos megjelenítés
- Lapozás
- Rendezési lehetőségek
- Keresés és szűrés mezők

### 5.3 Rekord részletek
- Minden mező megjelenítése
- Kapcsolódó entitások listája
- Szerkesztés és törlés gombok

### 5.4 Űrlapok
- Új rekord hozzáadása
- Meglévő rekord szerkesztése
- Validáció

### 5.5 Modális ablakok
- Megerősítő üzenetek (pl. törlés előtt)
- Gyors műveletek (pl. asszociációk hozzáadása/törlése)

## 6. API végpontok

Az alkalmazás RESTful API-t biztosít a következő műveletekhez:
- GET /api/{entity}: Entitások listázása
- POST /api/{entity}: Új entitás létrehozása
- GET /api/{entity}/{id}: Entitás részleteinek lekérése
- PUT /api/{entity}/{id}: Entitás frissítése
- DELETE /api/{entity}/{id}: Entitás törlése
- GET /api/{entity}/search: Entitások keresése
- POST /api/import: Adatok importálása
- GET /api/export: Adatok exportálása
- GET /api/reports/{report_type}: Riportok generálása
- POST /api/{entity}/{id}/associate: Entitások asszociálása

## 7. Adatbázis műveletek

Az alkalmazás az SQLAlchemy ORM-et használja az adatbázis műveletekhez. A fő műveletek:
- Rekordok létrehozása, olvasása, frissítése és törlése
- Kapcsolatok kezelése (pl. Media_Szerzo, Eloadas_Eloado_Szemely)
- Összetett lekérdezések a riportokhoz és statisztikákhoz

## 8. Biztonság

- CSRF védelem a Flask-WTF segítségével
- Bemeneti adatok validálása és szanitizálása
- SQL injection elleni védelem az ORM használatával

## 9. Teljesítmény optimalizálás

- Lapozás nagy adathalmazok esetén
- Indexek használata a gyakran keresett mezőkön
- Kapcsolódó entitások lazy loading-ja

## 10. Jövőbeli fejlesztési lehetőségek

- Felhasználói autentikáció és jogosultságkezelés
- Többnyelvű támogatás
- Részletesebb riportok és grafikonok
- Teljes szöveges keresés implementálása
- Verziókövetés és változások naplózása
- Tömeges műveletek végrehajtása (pl. több rekord egyidejű törlése vagy frissítése)
- Duplikált rekordok összevonása (Szemely, Media, Kategoria)
- Árva rekordok kezelése és megjelenítése
- Eloadas_Blob fájlméret alapú szűrése és kezelése
- Audit napló implementálása a rekordokon végzett változtatások követésére
- Szemely-ek idővonalas nézetének implementálása a hozzájuk kapcsolódó Media és Eloadas eseményekkel
- Kategoria használati idővonalas nézet implementálása az összes Media és Eloadas között
- Eloadas_Blob hozzáadások idővonalas nézetének implementálása egy adott Eloadas-hoz
- Szemely diverzitási riport implementálása (különböző szerepekben való részvétel alapján)
- Eloadas_Blob_Tipus eloszlási riport implementálása az összes Eloadas között

Ez a program terv egy átfogó keretet biztosít a MartiSuli adatbázis kezelő alkalmazás fejlesztéséhez. A terv rugalmas és bővíthető, lehetővé téve további funkciók és fejlesztések beépítését a jövőben, valamint figyelembe veszi a komplex adatmodellt és a különböző entitások közötti kapcsolatokat.