# Importing necessary modules
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from MartiSuli.media.db import DatabaseManager
from MartiSuli.media.model import Szemely, Media, Eloadas, Kategoria, Eloadas_Blob_Tipus
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

# Creating FastAPI application
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Creating DatabaseManager instance
db_manager = DatabaseManager()

# Dependency to get database session
def get_db():
    db = db_manager.get_session()
    try:
        yield db
    finally:
        db.close()

# Authentication setup
SECRET_KEY = "your-secret-key"  # Change this!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authentication functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

# Pydantic models for request and response
class SzemelyBase(BaseModel):
    nev: str
    datum_szuletes: str = None
    datum_meghalt: str = None
    leiras: str = None
    megjegyzes: str = None

class SzemelyCreate(SzemelyBase):
    pass

class SzemelyResponse(SzemelyBase):
    id: int

    class Config:
        orm_mode = True

# CRUD operations for Szemely
@app.post("/szemely/", response_model=SzemelyResponse)
async def create_szemely(szemely: SzemelyCreate, db: Session = Depends(get_db)):
    db_szemely = Szemely(**szemely.dict())
    try:
        db_manager.add_item(db_szemely)
    except Exception as e:
        logger.error(f"Error creating szemely: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_szemely

@app.get("/szemely/{szemely_id}", response_model=SzemelyResponse)
async def read_szemely(szemely_id: int, db: Session = Depends(get_db)):
    szemely = db_manager.get_by_id(Szemely, szemely_id)
    if szemely is None:
        raise HTTPException(status_code=404, detail="Szemely not found")
    return szemely

@app.get("/szemely/", response_model=List[SzemelyResponse])
async def read_szemelyek(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    szemelyek = db_manager.get_all(Szemely)[skip : skip + limit]
    return szemelyek

@app.put("/szemely/{szemely_id}", response_model=SzemelyResponse)
async def update_szemely(szemely_id: int, szemely: SzemelyCreate, db: Session = Depends(get_db)):
    db_szemely = db_manager.get_by_id(Szemely, szemely_id)
    if db_szemely is None:
        raise HTTPException(status_code=404, detail="Szemely not found")
    for key, value in szemely.dict().items():
        setattr(db_szemely, key, value)
    try:
        db_manager.update_item(db_szemely)
    except Exception as e:
        logger.error(f"Error updating szemely: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_szemely

@app.delete("/szemely/{szemely_id}", response_model=SzemelyResponse)
async def delete_szemely(szemely_id: int, db: Session = Depends(get_db)):
    db_szemely = db_manager.get_by_id(Szemely, szemely_id)
    if db_szemely is None:
        raise HTTPException(status_code=404, detail="Szemely not found")
    try:
        db_manager.delete_item(db_szemely)
    except Exception as e:
        logger.error(f"Error deleting szemely: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_szemely

# Pydantic models for Media
class MediaBase(BaseModel):
    cim: str
    dalszoveg: str = None
    datum_keletkezes: int = None
    leiras: str = None
    megjegyzes: str = None
    id_zeneszerzo: int = None

class MediaCreate(MediaBase):
    pass

class MediaResponse(MediaBase):
    id: int

    class Config:
        orm_mode = True

# CRUD operations for Media
@app.post("/media/", response_model=MediaResponse)
async def create_media(media: MediaCreate, db: Session = Depends(get_db)):
    db_media = Media(**media.dict())
    try:
        db_manager.add_item(db_media)
    except Exception as e:
        logger.error(f"Error creating media: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_media

@app.get("/media/{media_id}", response_model=MediaResponse)
async def read_media(media_id: int, db: Session = Depends(get_db)):
    media = db_manager.get_by_id(Media, media_id)
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media

@app.get("/media/", response_model=List[MediaResponse])
async def read_mediak(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mediak = db_manager.get_all(Media)[skip : skip + limit]
    return mediak

@app.put("/media/{media_id}", response_model=MediaResponse)
async def update_media(media_id: int, media: MediaCreate, db: Session = Depends(get_db)):
    db_media = db_manager.get_by_id(Media, media_id)
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    for key, value in media.dict().items():
        setattr(db_media, key, value)
    try:
        db_manager.update_item(db_media)
    except Exception as e:
        logger.error(f"Error updating media: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_media

@app.delete("/media/{media_id}", response_model=MediaResponse)
async def delete_media(media_id: int, db: Session = Depends(get_db)):
    db_media = db_manager.get_by_id(Media, media_id)
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    try:
        db_manager.delete_item(db_media)
    except Exception as e:
        logger.error(f"Error deleting media: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_media

# Pydantic models for Eloadas
class EloadasBase(BaseModel):
    id_media: int
    leiras: str = None
    megjegyzes: str = None

class EloadasCreate(EloadasBase):
    pass

class EloadasResponse(EloadasBase):
    id: int

    class Config:
        orm_mode = True

# CRUD operations for Eloadas
@app.post("/eloadas/", response_model=EloadasResponse)
async def create_eloadas(eloadas: EloadasCreate, db: Session = Depends(get_db)):
    db_eloadas = Eloadas(**eloadas.dict())
    try:
        db_manager.add_item(db_eloadas)
    except Exception as e:
        logger.error(f"Error creating eloadas: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_eloadas

@app.get("/eloadas/{eloadas_id}", response_model=EloadasResponse)
async def read_eloadas(eloadas_id: int, db: Session = Depends(get_db)):
    eloadas = db_manager.get_by_id(Eloadas, eloadas_id)
    if eloadas is None:
        raise HTTPException(status_code=404, detail="Eloadas not found")
    return eloadas

@app.get("/eloadas/", response_model=List[EloadasResponse])
async def read_eloadasok(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    eloadasok = db_manager.get_all(Eloadas)[skip : skip + limit]
    return eloadasok

@app.put("/eloadas/{eloadas_id}", response_model=EloadasResponse)
async def update_eloadas(eloadas_id: int, eloadas: EloadasCreate, db: Session = Depends(get_db)):
    db_eloadas = db_manager.get_by_id(Eloadas, eloadas_id)
    if db_eloadas is None:
        raise HTTPException(status_code=404, detail="Eloadas not found")
    for key, value in eloadas.dict().items():
        setattr(db_eloadas, key, value)
    try:
        db_manager.update_item(db_eloadas)
    except Exception as e:
        logger.error(f"Error updating eloadas: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_eloadas

@app.delete("/eloadas/{eloadas_id}", response_model=EloadasResponse)
async def delete_eloadas(eloadas_id: int, db: Session = Depends(get_db)):
    db_eloadas = db_manager.get_by_id(Eloadas, eloadas_id)
    if db_eloadas is None:
        raise HTTPException(status_code=404, detail="Eloadas not found")
    try:
        db_manager.delete_item(db_eloadas)
    except Exception as e:
        logger.error(f"Error deleting eloadas: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_eloadas

# Pydantic models for Kategoria
class KategoriaBase(BaseModel):
    megnevezes: str
    leiras: str = None
    megjegyzes: str = None

class KategoriaCreate(KategoriaBase):
    pass

class KategoriaResponse(KategoriaBase):
    id: int

    class Config:
        orm_mode = True

# CRUD operations for Kategoria
@app.post("/kategoria/", response_model=KategoriaResponse)
async def create_kategoria(kategoria: KategoriaCreate, db: Session = Depends(get_db)):
    db_kategoria = Kategoria(**kategoria.dict())
    try:
        db_manager.add_item(db_kategoria)
    except Exception as e:
        logger.error(f"Error creating kategoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_kategoria

@app.get("/kategoria/{kategoria_id}", response_model=KategoriaResponse)
async def read_kategoria(kategoria_id: int, db: Session = Depends(get_db)):
    kategoria = db_manager.get_by_id(Kategoria, kategoria_id)
    if kategoria is None:
        raise HTTPException(status_code=404, detail="Kategoria not found")
    return kategoria

@app.get("/kategoria/", response_model=List[KategoriaResponse])
async def read_kategoriak(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    kategoriak = db_manager.get_all(Kategoria)[skip : skip + limit]
    return kategoriak

@app.put("/kategoria/{kategoria_id}", response_model=KategoriaResponse)
async def update_kategoria(kategoria_id: int, kategoria: KategoriaCreate, db: Session = Depends(get_db)):
    db_kategoria = db_manager.get_by_id(Kategoria, kategoria_id)
    if db_kategoria is None:
        raise HTTPException(status_code=404, detail="Kategoria not found")
    for key, value in kategoria.dict().items():
        setattr(db_kategoria, key, value)
    try:
        db_manager.update_item(db_kategoria)
    except Exception as e:
        logger.error(f"Error updating kategoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_kategoria

@app.delete("/kategoria/{kategoria_id}", response_model=KategoriaResponse)
async def delete_kategoria(kategoria_id: int, db: Session = Depends(get_db)):
    db_kategoria = db_manager.get_by_id(Kategoria, kategoria_id)
    if db_kategoria is None:
        raise HTTPException(status_code=404, detail="Kategoria not found")
    try:
        db_manager.delete_item(db_kategoria)
    except Exception as e:
        logger.error(f"Error deleting kategoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_kategoria

# Pydantic models for Eloadas_Blob_Tipus
class EloadasBlobTipusBase(BaseModel):
    megnevezes: str
    kiterjesztes: str
    megjegyzes: str = None

class EloadasBlobTipusCreate(EloadasBlobTipusBase):
    pass

class EloadasBlobTipusResponse(EloadasBlobTipusBase):
    id: int

    class Config:
        orm_mode = True

# CRUD operations for Eloadas_Blob_Tipus
@app.post("/eloadas_blob_tipus/", response_model=EloadasBlobTipusResponse)
async def create_eloadas_blob_tipus(eloadas_blob_tipus: EloadasBlobTipusCreate, db: Session = Depends(get_db)):
    db_eloadas_blob_tipus = Eloadas_Blob_Tipus(**eloadas_blob_tipus.dict())
    try:
        db_manager.add_item(db_eloadas_blob_tipus)
    except Exception as e:
        logger.error(f"Error creating eloadas_blob_tipus: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_eloadas_blob_tipus

@app.get("/eloadas_blob_tipus/{eloadas_blob_tipus_id}", response_model=EloadasBlobTipusResponse)
async def read_eloadas_blob_tipus(eloadas_blob_tipus_id: int, db: Session = Depends(get_db)):
# Note: I chose FastAPI over Flask for the following reasons:
# 1. Built-in support for asynchronous programming, which can improve performance for I/O-bound operations.
# 2. Automatic API documentation with Swagger UI and ReDoc, which is extremely helpful for both desktop and web applications.
# 3. Type checking and data validation using Pydantic models, ensuring data integrity.
# 4. Better performance compared to Flask in most benchmarks, which is crucial for handling multiple requests from desktop or web clients.
# 5. Built-in support for dependency injection, which is useful for managing database sessions and other shared resources.
# 6. Easy integration with modern frontend frameworks and desktop applications through its RESTful API design.
# 7. Built-in support for WebSocket, which can be useful for real-time communication in both desktop and web applications.
# 8. More intuitive route definitions with type hints, making the code more readable and maintainable.

# These features make FastAPI an excellent choice for creating a robust backend that can serve both desktop and web applications efficiently.

# What's missing:
# 1. CRUD operations for Eloadas_Blob_Tipus
# 2. Implementation of update and delete operations for all models
# 3. Error handling for database operations
# 4. Authentication and authorization mechanisms
# 5. Logging and monitoring
# 6. Rate limiting to prevent abuse
# 7. CORS (Cross-Origin Resource Sharing) configuration for web applications
# 8. Deployment configuration (e.g., Gunicorn, Docker)
# 9. Testing suite for API endpoints
# 10. Documentation for API usage
