from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Szemely(Base):
    __tablename__ = 'SZEMELY'

    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False, unique=False)
    datum_szuletes = Column(Date, info={'label': 'Születési dátum'})
    datum_meghalt = Column(Date)
    leiras = Column(Text)
    megjegyzes = Column(Text)
    
    szerzett_mediak = relationship('Media', secondary='MEDIA_SZERZO', back_populates='szerzok')
    eloadasok = relationship('Eloadas', secondary='ELOADAS_ELOADO_SZEMELY', back_populates='eloadok')
    def to_dict(self):
        return {
            'id': self.id,
            'nev': self.nev,
            'datum_szuletes': self.datum_szuletes.isoformat() if self.datum_szuletes else None,
            'datum_meghalt': self.datum_meghalt.isoformat() if self.datum_meghalt else None,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }
    def to_dict_list(self):
        return {
            'id': self.id,
            'nev': self.nev,
        }
    def to_dict_details(self):
        return {
            'id': self.id,
            'nev': self.nev,
            'datum_szuletes': self.datum_szuletes.isoformat() if self.datum_szuletes else None,
            'datum_meghalt': self.datum_meghalt.isoformat() if self.datum_meghalt else None,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'szerzett_mediak': [media.to_dict_list() for media in self.szerzett_mediak],
            'eloadasok': [eloadas.to_dict_list() for eloadas in self.eloadasok]
        }

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

    def to_dict(self):
        return {
            'id': self.id,
            'cim': self.cim,
            'dalszoveg': self.dalszoveg,
            'datum_keletkezes': self.datum_keletkezes,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'id_zeneszerzo': self.id_zeneszerzo
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'cim': self.cim,
        }

    def to_dict_details(self):
        return {
            'id': self.id,
            'cim': self.cim,
            'dalszoveg': self.dalszoveg,
            'datum_keletkezes': self.datum_keletkezes,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'id_zeneszerzo': self.id_zeneszerzo,
            'szerzok': [szerzo.to_dict_list() for szerzo in self.szerzok],
            'eloadasok': [eloadas.to_dict_list() for eloadas in self.eloadasok],
            'kategoriak': [kategoria.to_dict_list() for kategoria in self.kategoriak]
        }

class Media_Szerzo(Base):
    __tablename__ = 'MEDIA_SZERZO'
    id_media = Column(Integer, ForeignKey('MEDIA.id'), primary_key=True)
    id_szerzo = Column(Integer, ForeignKey('SZEMELY.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    def to_dict(self):
        return {
            'id_media': self.id_media,
            'id_szerzo': self.id_szerzo,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id_media': self.id_media,
            'id_szerzo': self.id_szerzo,
        }

    def to_dict_details(self):
        return {
            'id_media': self.id_media,
            'id_szerzo': self.id_szerzo,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

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

    def to_dict(self):
        return {
            'id': self.id,
            'id_media': self.id_media,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'id_media': self.id_media,
        }

    def to_dict_details(self):
        return {
            'id': self.id,
            'id_media': self.id_media,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'media': self.media.to_dict_list() if self.media else None,
            'eloadok': [eloado.to_dict_list() for eloado in self.eloadok],
            'blobok': [blob.to_dict_list() for blob in self.blobok],
            'kategoriak': [kategoria.to_dict_list() for kategoria in self.kategoriak]
        }

class Eloadas_Eloado_Szemely(Base):
    __tablename__ = 'ELOADAS_ELOADO_SZEMELY'
    id_eloadas = Column(Integer, ForeignKey('ELOADAS.id'), primary_key=True)
    id_szemely = Column(Integer, ForeignKey('SZEMELY.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    def to_dict(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_szemely': self.id_szemely,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_szemely': self.id_szemely,
        }

    def to_dict_details(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_szemely': self.id_szemely,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

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

    def to_dict(self):
        return {
            'id': self.id,
            'id_eloadas': self.id_eloadas,
            'id_eloadas_blob_tipus': self.id_eloadas_blob_tipus,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'id_eloadas': self.id_eloadas,
        }

    def to_dict_details(self):
        return {
            'id': self.id,
            'id_eloadas': self.id_eloadas,
            'id_eloadas_blob_tipus': self.id_eloadas_blob_tipus,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'eloadas': self.eloadas.to_dict_list() if self.eloadas else None,
            'blob_tipus': self.blob_tipus.to_dict_list() if self.blob_tipus else None
        }

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
    eloadas_id = Column(Integer, ForeignKey('ELOADAS.id'), primary_key=True)
    hangszer_id = Column(Integer, ForeignKey('HANGSZER.id'), primary_key=True)
    # szemely_id = Column(Integer, ForeignKey('szemely.id'))
    megjegyzes = Column(Text)

class Stilus(Base):
    __tablename__ = 'STILUS'
    id = Column(Integer, primary_key=True)
    nev = Column(String(100), nullable=False)
    leiras = Column(Text)

class MediaStilus(Base):
    __tablename__ = 'MEDIA_STILUS'
    media_id = Column(Integer, ForeignKey('MEDIA.id'), primary_key=True)
    stilus_id = Column(Integer, ForeignKey('STILUS.id'), primary_key=True)
    megjegyzes = Column(Text)

    def to_dict(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
            'kiterjesztes': self.kiterjesztes,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
        }

    def to_dict_details(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
            'kiterjesztes': self.kiterjesztes,
            'megjegyzes': self.megjegyzes
        }

class Kategoria(Base):
    __tablename__ = 'KATEGORIA'
    id = Column(Integer, primary_key=True)
    megnevezes = Column(String(100), nullable=False)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    mediak = relationship('Media', secondary='MEDIA_KATEGORIA', back_populates='kategoriak')
    eloadasok = relationship('Eloadas', secondary='ELOADAS_KATEGORIA', back_populates='kategoriak')

    def to_dict(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
        }

    def to_dict_details(self):
        return {
            'id': self.id,
            'megnevezes': self.megnevezes,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes,
            'mediak': [media.to_dict_list() for media in self.mediak],
            'eloadasok': [eloadas.to_dict_list() for eloadas in self.eloadasok]
        }

class Media_Kategoria(Base):
    __tablename__ = 'MEDIA_KATEGORIA'
    id_media = Column(Integer, ForeignKey('MEDIA.id'), primary_key=True)
    id_kategoria = Column(Integer, ForeignKey('KATEGORIA.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    def to_dict(self):
        return {
            'id_media': self.id_media,
            'id_kategoria': self.id_kategoria,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id_media': self.id_media,
            'id_kategoria': self.id_kategoria,
        }

    def to_dict_details(self):
        return {
            'id_media': self.id_media,
            'id_kategoria': self.id_kategoria,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

class Eloadas_Kategoria(Base):
    __tablename__ = 'ELOADAS_KATEGORIA'
    id_eloadas = Column(Integer, ForeignKey('ELOADAS.id'), primary_key=True)
    id_kategoria = Column(Integer, ForeignKey('KATEGORIA.id'), primary_key=True)
    leiras = Column(Text)
    megjegyzes = Column(Text)

    def to_dict(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_kategoria': self.id_kategoria,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }

    def to_dict_list(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_kategoria': self.id_kategoria,
        }

    def to_dict_details(self):
        return {
            'id_eloadas': self.id_eloadas,
            'id_kategoria': self.id_kategoria,
            'leiras': self.leiras,
            'megjegyzes': self.megjegyzes
        }