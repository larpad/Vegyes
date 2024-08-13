from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Szemely(Base):
    __tablename__ = 'SZEMELY'

    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False)
    datum_szuletes = Column(Date)
    datum_meghalt = Column(Date)
    leiras = Column(Text)
    megjegyzes = Column(Text)
    
    szerzett_mediak = relationship('Media', secondary='MEDIA_SZERZO', back_populates='szerzok')
    eloadasok = relationship('Eloadas', secondary='ELOADAS_ELOADO_SZEMELY', back_populates='eloadok')

class Media(Base):
    __tablename__ = 'MEDIA'
    id = Column(Integer, primary_key=True)
    cim = Column(String(200), nullable=False)
    dalszoveg = Column(Text)
    datum_keletkezes = Column(Integer)
    leiras = Column(Text)
    megjegyzes = Column(Text)
    id_zeneszerzo = Column(Integer, ForeignKey('SZEMELY.id'))

    szerzok = relationship('Szemely', secondary='MEDIA_SZERZO', back_populates='szerzett_mediak')
    eloadasok = relationship('Eloadas', back_populates='media')
    kategoriak = relationship('Kategoria', secondary='MEDIA_KATEGORIA', back_populates='mediak')

class Media_Szerzo(Base):
    __tablename__ = 'MEDIA_SZERZO'
    id_media = Column(Integer, ForeignKey('MEDIA.id'), primary_key=True)
    id_szerzo = Column(Integer, ForeignKey('SZEMELY.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas(Base):
    __tablename__ = 'ELOADAS'
    id = Column(Integer, primary_key=True)
    id_media = Column(Integer, ForeignKey('MEDIA.id'))
    leiras = Column(Text)
    megjegyzes = Column(Text)

    media = relationship('Media', back_populates='eloadasok')
    eloadok = relationship('Szemely', secondary='ELOADAS_ELOADO_SZEMELY', back_populates='eloadasok')
    blobok = relationship('Eloadas_Blob', back_populates='eloadas')
    kategoriak = relationship('Kategoria', secondary='ELOADAS_KATEGORIA', back_populates='eloadasok')

class Eloadas_Eloado_Szemely(Base):
    __tablename__ = 'ELOADAS_ELOADO_SZEMELY'
    id_eloadas = Column(Integer, ForeignKey('ELOADAS.id'), primary_key=True)
    id_szemely = Column(Integer, ForeignKey('SZEMELY.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas_Blob(Base):
    __tablename__ = 'ELOADAS_BLOB'
    id = Column(Integer, primary_key=True)
    id_eloadas = Column(Integer, ForeignKey('ELOADAS.id'))
    id_eloadas_blob_tipus = Column(Integer, ForeignKey('ELOADAS_BLOB_TIPUS.id'))
    blob = Column(LargeBinary)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    eloadas = relationship('Eloadas', back_populates='blobok')
    blob_tipus = relationship('Eloadas_Blob_Tipus')

class Eloadas_Blob_Tipus(Base):
    __tablename__ = 'ELOADAS_BLOB_TIPUS'
    id = Column(Integer, primary_key=True)
    megnevezes = Column(String(100), nullable=False)
    kiterjesztes = Column(String(10), nullable=False)
    megjegyzes = Column(Text)

class Kategoria(Base):
    __tablename__ = 'KATEGORIA'
    id = Column(Integer, primary_key=True)
    megnevezes = Column(String(100), nullable=False)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    mediak = relationship('Media', secondary='MEDIA_KATEGORIA', back_populates='kategoriak')
    eloadasok = relationship('Eloadas', secondary='ELOADAS_KATEGORIA', back_populates='kategoriak')

class Media_Kategoria(Base):
    __tablename__ = 'MEDIA_KATEGORIA'
    id_media = Column(Integer, ForeignKey('MEDIA.id'), primary_key=True)
    id_kategoria = Column(Integer, ForeignKey('KATEGORIA.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

class Eloadas_Kategoria(Base):
    __tablename__ = 'ELOADAS_KATEGORIA'
    id_eloadas = Column(Integer, ForeignKey('ELOADAS.id'), primary_key=True)
    id_kategoria = Column(Integer, ForeignKey('KATEGORIA.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)