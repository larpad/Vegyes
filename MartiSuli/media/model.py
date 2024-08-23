from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Blob
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Szemely(Base):
    __tablename__ = 'SZEMELY'

    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False)
    datum_szuletes = Column(Date)
    datum_meghalt = Column(Date)
    leiras = Column(Text)
    mejegyzes = Column(Text)
    

class Media(Base):
    __tablename__ = 'MEDIA'
    id = Column(Integer, primary_key=True)
    cim = Column(String(200), nullable=False)
    dalszoveg = Column(Text)
    datum_keletkezes = Column(Integer)
    leiras = Column(Text)
    megjegyzes = Column(Text)
    zeneszerzo_id = Column(Integer, ForeignKey('szemely.id'))

class Media_Szerzo(Base):
    __tablename__ = 'MEDIA_SZERZO'
    media_id = Column(Integer, ForeignKey('media.id'))
    szerzo_id = Column(Integer, ForeignKey('szemely.id'))
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas(Base):
    __tablename__ = 'ELOADAS'
    id_media = Column(Integer, ForeignKey('media.id'))
    id_szemely = Column(Integer, ForeignKey('szemely.id'))
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas_Eloado_Szemely(Base):
    __tablename__ = 'ELOADAS_ELODO_SZEMELY'
    id_eloadas = Column(Integer, ForeignKey('eloadas.id'))
    id_szemely = Column(Integer, ForeignKey('szemely.id'))
    leiras = Column(Text)
    megjegyzes = Column(Text)


class Eloadas_Blob(Base):
    __tablename__ = 'ELOADAS_BLOB'
    id = Column(Integer, primary_key=True)
    id_media = Column(Integer, ForeignKey('media.id'))
    id_blob_tipus = Column(Integer, ForeignKey('eloadas_blob_tipus.id'))
    blob = Column(Blob)
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas_Blob_Tipus(Base):
    __tablename__ = 'ELOADAS_BLOB_TIPUS'
    id = Column(Integer, primary_key=True)
    megnevezes = Column(String(100), nullable=False)
    kiterjesztes = Column(String(10), nullable=False)
    megjegyzes = Column(Text)


class Hangszer(Base):
    __tablename__ = 'HANGSZER'
    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False)
    leiras = Column(Text)
    megjegyzes = Column(Text)

class EloadasHangszer(Base):
    __tablename__ = 'ELOADAS_HANGSZER'
    eloadas_id = Column(Integer, ForeignKey('eloadas.id'), primary_key=True)
    hangszer_id = Column(Integer, ForeignKey('hangszer.id'), primary_key=True)
    szemely_id = Column(Integer, ForeignKey('szemely.id'))
    megjegyzes = Column(Text)

class Stilus(Base):
    __tablename__ = 'STILUS'
    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False)
    leiras = Column(Text)

class MediaStilus(Base):
    __tablename__ = 'MEDIA_STILUS'
    media_id = Column(Integer, ForeignKey('media.id'), primary_key=True)
    stilus_id = Column(Integer, ForeignKey('stilus.id'), primary_key=True)
    megjegyzes = Column(Text)
