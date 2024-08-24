import sys
import os
import sqlite3
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model import Base, Szemely, Media, Media_Szerzo, Eloadas, Eloadas_Eloado_Szemely, Eloadas_Blob, Eloadas_Blob_Tipus, Kategoria, Media_Kategoria, Eloadas_Kategoria
from datetime import date, datetime
import random

class DatabaseManager:
    def __init__(self, create_if_not_exists=True):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'database.db')
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
        if create_if_not_exists:
            # self.initialize_test_data()
            pass

    def get_session(self):
        return self.Session()
# ------------------------------------------------------------------------------------------

    def select(self, model, id=None, search_term=None):
        session = self.get_session()
        try:
            query = session.query(model)
            if id:
                return query.filter(model.id == id).first()
            
            elif search_term:
                results = []
                for model_name in ['szemely', 'media', 'eloadas', 'kategoria']:
                    model = globals().get(model_name.capitalize())
                    query = session.query(model)
                
                    if hasattr(model, 'nev'):
                        query = query.filter(model.nev.ilike(f'%{search_term}%'))
                    elif hasattr(model, 'cim'):
                        query = query.filter(model.cim.ilike(f'%{search_term}%'))
                    elif hasattr(model, 'megnevezes'):
                        query = query.filter(model.megnevezes.ilike(f'%{search_term}%'))
                    else:
                        continue  # Skip this model if it doesn't have any of these attributes

                    model_results = query.all()
                    results.extend([    {    "ID": item.id
                                            ,"Név":     getattr(item, 'nev', None)
                                                    or  getattr(item, 'cim', None)
                                                    or  getattr(item, 'megnevezes', None)
                                            ,"type": model_name}
                                        for item in model_results
                                   ])
                return results



            # elif search_term:
            #     if hasattr(model, 'nev'):
            #         query = query.filter(model.nev.ilike(f'%{search_term}%'))
            #     elif hasattr(model, 'cim'):
            #         query = query.filter(model.cim.ilike(f'%{search_term}%'))
            #     elif hasattr(model, 'megnevezes'):
            #         query = query.filter(model.megnevezes.ilike(f'%{search_term}%'))

            #     else: # If the model doesn't have any of these attributes, return an empty list
            #         return []
            #     return query.all()
            
            else:
                return query.all()
            
        except SQLAlchemyError as e:
            print(f"An error occurred: {str(e)}")
            return []
        finally:
            session.close()

# ------------------------------------------------------------------------------------------

    def add_item(self, item):
        session = self.get_session()
        try:
            # Convert string dates to Python date objects
            for attr in ['datum_szuletes', 'datum_meghalt']:
                if hasattr(item, attr):
                    value = getattr(item, attr)
                    if isinstance(value, str) and value:  # Only convert non-empty strings
                        try:
                            setattr(item, attr, datetime.strptime(value, '%Y.%m.%d').date())
                        except ValueError:
                            setattr(item, attr, None)
                    elif not value:  # Set empty strings to None
                        setattr(item, attr, None)
            
            session.add(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
# ------------------------------------------------------------------------------------------
            
    def update_item(self, item):
        session = self.get_session()
        try:
            session.merge(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
# ------------------------------------------------------------------------------------------

    def delete_item(self, item):
        session = self.get_session()
        try:
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

    # def bulk_insert(self, items):
    #     session = self.get_session()
    #     try:
    #         session.bulk_save_objects(items)
    #         session.commit()
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         raise e
    #     finally:
    #         session.close()

    def initialize_test_data(self):
        session = self.get_session()
        try:
            # Kategóriák létrehozása
            kategoriak = [
                Kategoria(megnevezes="Klasszikus"),
                Kategoria(megnevezes="Magyar népzene"),
                Kategoria(megnevezes="Barokk"),
                Kategoria(megnevezes="Romantikus"),
                Kategoria(megnevezes="Modern klasszikus")
            ]
            session.add_all(kategoriak)
            
            # Klasszikus zeneszerzők
            klasszikus_zeneszerzok = [
                Szemely(nev="Johann Sebastian Bach", datum_szuletes=date(1685, 3, 31), datum_meghalt=date(1750, 7, 28)),
                Szemely(nev="Wolfgang Amadeus Mozart", datum_szuletes=date(1756, 1, 27), datum_meghalt=date(1791, 12, 5)),
                Szemely(nev="Ludwig van Beethoven", datum_szuletes=date(1770, 12, 17), datum_meghalt=date(1827, 3, 26)),
                Szemely(nev="Frédéric Chopin", datum_szuletes=date(1810, 3, 1), datum_meghalt=date(1849, 10, 17)),
                Szemely(nev="Johannes Brahms", datum_szuletes=date(1833, 5, 7), datum_meghalt=date(1897, 4, 3)),
                Szemely(nev="Pyotr Ilyich Tchaikovsky", datum_szuletes=date(1840, 5, 7), datum_meghalt=date(1893, 11, 6)),
                Szemely(nev="Claude Debussy", datum_szuletes=date(1862, 8, 22), datum_meghalt=date(1918, 3, 25)),
                Szemely(nev="Igor Stravinsky", datum_szuletes=date(1882, 6, 17), datum_meghalt=date(1971, 4, 6)),
                Szemely(nev="Sergei Rachmaninoff", datum_szuletes=date(1873, 4, 1), datum_meghalt=date(1943, 3, 28)),
                Szemely(nev="George Gershwin", datum_szuletes=date(1898, 9, 26), datum_meghalt=date(1937, 7, 11))
            ]
            session.add_all(klasszikus_zeneszerzok)
            
            # Magyar zeneszerzők
            magyar_zeneszerzok = [
                Szemely(nev="Bartók Béla", datum_szuletes=date(1881, 3, 25), datum_meghalt=date(1945, 9, 26)),
                Szemely(nev="Kodály Zoltán", datum_szuletes=date(1882, 12, 16), datum_meghalt=date(1967, 3, 6)),
                Szemely(nev="Liszt Ferenc", datum_szuletes=date(1811, 10, 22), datum_meghalt=date(1886, 7, 31)),
                Szemely(nev="Erkel Ferenc", datum_szuletes=date(1810, 11, 7), datum_meghalt=date(1893, 6, 15)),
                Szemely(nev="Dohnányi Ernő", datum_szuletes=date(1877, 7, 27), datum_meghalt=date(1960, 2, 9)),
                Szemely(nev="Weiner Leó", datum_szuletes=date(1885, 4, 16), datum_meghalt=date(1960, 9, 13)),
                Szemely(nev="Kurtág György", datum_szuletes=date(1926, 2, 19)),
                Szemely(nev="Ligeti György", datum_szuletes=date(1923, 5, 28), datum_meghalt=date(2006, 6, 12)),
                Szemely(nev="Eötvös Péter", datum_szuletes=date(1944, 1, 2)),
                Szemely(nev="Szokolay Sándor", datum_szuletes=date(1931, 3, 30), datum_meghalt=date(2013, 12, 8))
            ]
            session.add_all(magyar_zeneszerzok)
            
            # Előadók
            eloadok = [
                Szemely(nev="Kocsis Zoltán", datum_szuletes=date(1952, 5, 30), datum_meghalt=date(2016, 11, 6)),
                Szemely(nev="Fischer Iván", datum_szuletes=date(1951, 1, 20)),
                Szemely(nev="Schiff András", datum_szuletes=date(1953, 12, 21)),
                Szemely(nev="Ránki Dezső", datum_szuletes=date(1951, 9, 8)),
                Szemely(nev="Perényi Miklós", datum_szuletes=date(1948, 1, 5))
            ]
            session.add_all(eloadok)
            
            session.commit()
            
            # Művek és előadások hozzáadása
            for zeneszerzo in klasszikus_zeneszerzok + magyar_zeneszerzok:
                for i in range(random.randint(5, 10)):  # Minden zeneszerzőhöz 5-10 mű
                    media = Media(
                        cim=f"{zeneszerzo.nev} műve {i+1}",
                        datum_keletkezes=zeneszerzo.datum_szuletes.year + 20 + i,
                        id_zeneszerzo=zeneszerzo.id
                    )
                    session.add(media)
                    session.flush()
                    
                    media_szerzo = Media_Szerzo(id_media=media.id, id_szerzo=zeneszerzo.id)
                    session.add(media_szerzo)
                    
                    # Minden műhöz véletlenszerű kategória
                    kategoria = session.query(Kategoria).order_by(func.random()).first()
                    media_kategoria = Media_Kategoria(id_media=media.id, id_kategoria=kategoria.id)
                    session.add(media_kategoria)
                    
                    # Minden műhöz előadás
                    eloadas = Eloadas(id_media=media.id)
                    session.add(eloadas)
                    session.flush()
                    
                    # Minden előadáshoz véletlenszerű előadó
                    eloado = random.choice(eloadok)
                    eloadas_eloado = Eloadas_Eloado_Szemely(id_eloadas=eloadas.id, id_szemely=eloado.id)
                    session.add(eloadas_eloado)
                    
                    # Minden előadáshoz YouTube link (szimulált)
                    eloadas_blob = Eloadas_Blob(
                        id_eloadas=eloadas.id,
                        leiras=f"YouTube link: https://www.youtube.com/watch?v={zeneszerzo.nev.replace(' ', '')}{i}"
                    )
                    session.add(eloadas_blob)
            
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Hiba történt az adatbázis inicializálása során: {str(e)}")
        finally:
            session.close()

    # def get_szemely_model(self):
    #     return Szemely

    # def get_media_model(self):
    #     return Media

    # def get_eloadas_model(self):
    #     return Eloadas

    # def get_kategoria_model(self):
    #     return Kategoria

    # def get_eloadas_blob_tipus_model(self):
    #     return Eloadas_Blob_Tipus
