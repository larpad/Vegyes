# index.html WEB Felhasználói felület terv

## 1. Általános elrendezés

Az alkalmazás egy egyablakos (Single Page Application) webalkalmazás lesz, amely a következő fő elemekből áll:

1. Fejléc (Header)
2. Navigációs sáv (Navigation bar)
3. Fő tartalom terület (Main content area)
4. Lábléc (Footer)

### 1.1 Wireframe - Általános elrendezés

[Ide kerül egy általános wireframe kép az alkalmazás fő elrendezéséről]

## 2. Részletes felületi elemek

### 2.1 Fejléc (Header)
- Alkalmazás logó és név
- Keresőmező (globális keresés az összes entitásban)
- Bejelentkezés/Kijelentkezés gomb (jövőbeli fejlesztéshez)

### 2.2 Navigációs sáv (Navigation bar)
- Főoldal
- Entitások menüpontjai (Személy, Média, Előadás, Kategória, Előadás Blob, Előadás Blob Típus)
- Riportok és statisztikák menüpont
- Adatimport/export menüpont

### 2.3 Fő tartalom terület (Main content area)
- Dinamikusan változó tartalom az aktuális nézetnek megfelelően
- Entitás listák megjelenítése
- Űrlapok új entitások létrehozásához és szerkesztéséhez
- Részletes nézetek az egyes entitásokhoz
- Riportok és statisztikák megjelenítése
- Asszociációk kezelése

### 2.4 Lábléc (Footer)
- Copyright információ
- Kapcsolat link
- Verzió információ

## 3. Funkcionális követelmények

### 3.1 HTML
- Szemantikus HTML5 elemek használata
- Reszponzív design (Bootstrap vagy hasonló keretrendszer használata)
- Akadálymentesítés (ARIA attribútumok használata)
- Moduláris felépítés, újrahasználható komponensek
- Megfelelő meta tagek használata a SEO optimalizáláshoz

### 3.2 JavaScript
- Modern JavaScript (ES6+) használata
- AJAX hívások az API-hoz
- Dinamikus tartalom betöltés és frissítés
- Űrlap validáció
- Interaktív elemek kezelése (pl. modális ablakok, legördülő menük)
- Táblázatok rendezése és szűrése
- Grafikonok és vizualizációk generálása (pl. Chart.js vagy D3.js használatával)
- Aszinkron műveletek kezelése (Promises, async/await)
- Moduláris kódszervezés (pl. ES6 modulok használata)
- Eseménykezelés és delegálás
- Lokális tárolás használata (localStorage, sessionStorage)
- Hibakezelés és naplózás

### 3.3 CSS
- Reszponzív design
- Konzisztens színséma és tipográfia
- Animációk és átmenetek a jobb felhasználói élmény érdekében
- Nyomtatási stílusok definiálása
- CSS Grid és Flexbox használata a layout kialakításához
- CSS változók használata a könnyebb testreszabhatóság érdekében
- Mobile-first megközelítés
- Böngésző-kompatibilitás biztosítása (vendor prefixek használata)
- Teljesítmény optimalizálás (pl. CSS minifikálás)

## 4. Speciális funkciók és felületi elemek

### 4.1 Entitás listák
- Táblázatos megjelenítés lapozással
- Oszlopok szerinti rendezés
- Szűrési lehetőségek (dátum, név, kategória stb.)
- Gyors műveletek (szerkesztés, törlés, részletek megtekintése)
- Többszörös kijelölés lehetősége
- Exportálás különböző formátumokba (CSV, JSON)
- Oszlopok elrejtése/megjelenítése
- Egyéni nézetek mentése

### 4.2 Entitás részletek és szerkesztés
- Részletes információk megjelenítése
- Kapcsolódó entitások listázása
- Inline szerkesztési lehetőség
- Asszociációk hozzáadása/törlése
- Változások előnézete
- Verziókövetés és változások visszaállítása
- Fájlfeltöltés drag-and-drop funkcióval
- Automatikus mentés

### 4.3 Riportok és statisztikák
- Interaktív grafikonok és diagramok
- Szűrési és testreszabási lehetőségek
- Exportálási lehetőség (PDF, CSV)
- Valós idejű frissítés
- Összehasonlító nézetek
- Prediktív elemzések
- Hőtérképek és egyéb vizualizációk

### 4.4 Keresés és szűrés
- Globális keresőmező autocomplete funkcióval
- Részletes szűrési lehetőségek minden entitáshoz
- Keresési előzmények és mentett szűrők
- Összetett keresési feltételek építése
- Fuzzy keresés támogatása
- Keresési eredmények kiemelése
- Releváns javaslatok megjelenítése

### 4.5 Adatimport és -export
- Fájl feltöltési felület
- Formátum választási lehetőség
- Folyamat állapotjelző
- Hibajelentések és összefoglalók
- Adatvalidáció importálás előtt
- Inkrementális import lehetősége
- Automatikus adattisztítás
- Ütemezett import/export feladatok

## 5. Követelmények a weblappal kapcsolatban

- Gyors betöltési idő és optimalizált teljesítmény
- Konzisztens megjelenés különböző böngészőkben és eszközökön
- Intuitív és felhasználóbarát felület
- Megfelelő hibakezelés és felhasználói visszajelzések
- Biztonságos adatkezelés és CSRF védelem
- Skálázhatóság és bővíthetőség
- Offline működés támogatása (Progressive Web App)
- Többnyelvűség támogatása
- Akadálymentesség (WCAG 2.1 irányelvek követése)
- Teljesítmény optimalizálás (lazy loading, code splitting)
- SEO-barát kialakítás
- Analitika és felhasználói viselkedés követése
- Biztonságos hitelesítés és jogosultságkezelés
- Rendszeres biztonsági auditok és frissítések
- Adatvédelmi szabályoknak való megfelelés (GDPR)

## 6. Wireframe-ek

### 6.1 Főoldal wireframe
[Ide kerül a főoldal wireframe képe]

### 6.2 Entitás lista wireframe
[Ide kerül az entitás lista wireframe képe]

### 6.3 Entitás részletek wireframe
[Ide kerül az entitás részletek wireframe képe]

### 6.4 Új entitás létrehozása wireframe
[Ide kerül az új entitás létrehozása wireframe képe]

### 6.5 Riportok és statisztikák wireframe
[Ide kerül a riportok és statisztikák wireframe képe]

## 7. Létrehozandó funkciók és felületi elemek specifikációja

### 7.1 Főoldal
- Üdvözlő üzenet és az alkalmazás céljának rövid ismertetése
- Gyorselérési gombok a fő entitásokhoz (Személy, Média, Előadás, Kategória)
- Összesített statisztikák megjelenítése (pl. összes rekord száma entitásonként)
- Legutóbbi tevékenységek listája
- Hírek és frissítések szekció

### 7.2 Entitás kezelő oldalak (Személy, Média, Előadás, Kategória, Előadás Blob, Előadás Blob Típus)
- Lista nézet táblázatos formában
- Részletes nézet az entitás adataival és kapcsolódó rekordokkal
- Új rekord létrehozása űrlap
- Meglévő rekord szerkesztése űrlap
- Törlés megerősítő ablak
- Kapcsolódó entitások hozzáadása/eltávolítása
- Szűrési és keresési lehetőségek
- Rendezési opciók
- Lapozás nagy adathalmazok esetén

### 7.3 Keresés és szűrés funkciók
- Globális kereső minden entitásra
- Részletes szűrők entitásonként (pl. dátum tartomány, kategória, stb.)
- Mentett keresések és szűrők
- Keresési előzmények

### 7.4 Asszociációk kezelése
- Kapcsolatok létrehozása és törlése entitások között
- Kapcsolódó rekordok listázása és kezelése
- Többszörös kapcsolatok kezelése (pl. több szerző egy médiához)

### 7.5 Adatimport és -export funkciók
- CSV és JSON formátumok támogatása
- Fájl feltöltési felület drag-and-drop támogatással
- Importálási folyamat előnézete és validálása
- Exportálási opciók (teljes adatbázis vagy szűrt eredmények)

### 7.6 Riportok és statisztikák
- Előre definiált riportok (pl. legnépszerűbb média, legaktívabb személy)
- Egyéni riportok létrehozása
- Interaktív grafikonok és diagramok
- Adatok exportálása különböző formátumokban

### 7.7 Speciális funkciók
- Tömeges műveletek (pl. több rekord egyidejű törlése vagy frissítése)
- Verziókövetés és változások naplózása
- Duplikált rekordok kezelése és összevonása
- Árva rekordok azonosítása és kezelése
- Idővonalas nézetek (pl. egy személy média és előadás története)
- Hálózati grafikonok (pl. személyek közötti kapcsolatok vizualizálása)
- Szófelhő generálás (pl. média leírásokból vagy dalszövegekből)

### 7.8 Személy kezelés
- Személy rekordok böngészése, létrehozása, szerkesztése és törlése
- Szűrés születési és halálozási dátum alapján
- Kapcsolódó média és előadások megjelenítése
- Személy-együttműködési hálózat vizualizálása

### 7.9 Média kezelés
- Média rekordok böngészése, létrehozása, szerkesztése és törlése
- Szűrés létrehozási dátum, zeneszerző és dalszöveg tartalom alapján
- Kapcsolódó személyek (szerzők, zeneszerzők) és kategóriák megjelenítése
- Dalszövegek kezelése és megjelenítése

### 7.10 Előadás kezelés
- Előadás rekordok böngészése, létrehozása, szerkesztése és törlése
- Szűrés előadó és kapcsolódó média alapján
- Kapcsolódó személyek (előadók) és kategóriák megjelenítése
- Előadás blobok kezelése és megjelenítése

### 7.11 Kategória kezelés
- Kategória rekordok böngészése, létrehozása, szerkesztése és törlése
- Kapcsolódó média és előadások megjelenítése
- Kategória használati statisztikák és idővonalas nézet

### 7.12 Előadás Blob kezelés
- Előadás Blob rekordok böngészése, létrehozása, szerkesztése és törlése
- Fájl feltöltés és kezelés
- Szűrés fájlméret és típus alapján

### 7.13 Előadás Blob Típus kezelés
- Előadás Blob Típus rekordok böngészése, létrehozása, szerkesztése és törlése
- Kapcsolódó Előadás Blob-ok megjelenítése
- Használati statisztikák

### 7.14 Asszociációk kezelése
- Media_Szerzo asszociációk létrehozása, megtekintése és törlése
- Eloadas_Eloado_Szemely asszociációk létrehozása, megtekintése és törlése
- Media_Kategoria asszociációk létrehozása, megtekintése és törlése
- Eloadas_Kategoria asszociációk létrehozása, megtekintése és törlése

### 7.15 Komplex lekérdezések és riportok
- Legproduktívabb zeneszerzők riportja
- Legtöbb kategóriával rendelkező média és előadások riportja
- Legváltozatosabb Előadás Blob Típussal rendelkező előadások riportja
- Legsokoldalúbb személyek riportja (több szerepben is részt vesznek)
- Leggyakrabban használt fájlkiterjesztések az Előadás Blob-okban
- Személyek legváltozatosabb kategória asszociációinak riportja

### 7.16 Vizualizációk
- Idővonalas nézet egy személy média és előadás történetéről
- Hálózati gráf a kategória kapcsolatokról közös média vagy előadás alapján
- Szófelhő generálása az összes média dalszövegéből
- Interaktív grafikonok a különböző statisztikákról és riportokról

Ez a felhasználói felület terv egy átfogó keretet biztosít a MartiSuli adatbázis kezelő alkalmazás fejlesztéséhez. A terv részletesen leírja a szükséges funkciókat, felületi elemeket és követelményeket, amelyek alapján a fejlesztők már közvetlenül elkezdhetik a kódolást. A terv figyelembe veszi a modern webfejlesztési gyakorlatokat, a felhasználói élmény optimalizálását és a komplex adatmodell kezelésének kihívásait.

### 7.17 Főoldal
- Üdvözlő üzenet és az alkalmazás céljának rövid ismertetése
- Gyorselérési gombok a fő entitásokhoz (Személy, Média, Előadás, Kategória)
- Összesített statisztikák megjelenítése (pl. összes rekord száma entitásonként)
