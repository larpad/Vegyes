import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from MartiSuli.media.model import Base, Szemely, Media, Media_Szerzo, Eloadas, Eloadas_Eloado_Szemely, Eloadas_Blob, Eloadas_Blob_Tipus, Kategoria, Media_Kategoria, Eloadas_Kategoria

DB_PATH = r"F:\DATA\MartiSuli\media.db"

class DatabaseManager:
    def __init__(self, create_if_not_exists=True):
        self.engine = create_engine(f'sqlite:///{DB_PATH}')
        if create_if_not_exists:
            Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def add_item(self, item):
        session = self.get_session()
        try:
            session.add(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

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

    def get_all(self, model, exclude_description=False):
        session = self.get_session()
        try:
            query = session.query(model)
            if exclude_description:
                query = query.with_entities(*[c for c in model.__table__.columns if c.name not in ['leiras', 'megjegyzes']])
            return query.all()
        finally:
            session.close()

    def get_by_id(self, model, id):
        session = self.get_session()
        try:
            return session.query(model).filter(model.id == id).first()
        finally:
            session.close()

    def bulk_insert(self, items):
        session = self.get_session()
        try:
            session.bulk_save_objects(items)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # Helper functions for initial data population
    def populate_szemely(self, szemelyek):
        self.bulk_insert(szemelyek)

    def populate_media(self, mediak):
        self.bulk_insert(mediak)

    def populate_eloadas(self, eloadasok):
        self.bulk_insert(eloadasok)

    def populate_kategoria(self, kategoriak):
        self.bulk_insert(kategoriak)

    def populate_eloadas_blob_tipus(self, blob_tipusok):
        self.bulk_insert(blob_tipusok)

    # Additional helper functions can be added for other tables as needed
