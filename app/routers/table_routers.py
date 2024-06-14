from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.table_schemas import TapsCreate, PrintsCreate, PaysCreate
from app.database.database import SessionLocal
from app.services.crud import Tables
from app.auth.security import get_current_user

tables_router = APIRouter()

@tables_router.post('/taps', tags=['tables'], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)])
def create_taps_api(taps: List[TapsCreate]) -> dict:
    try:
        db = SessionLocal()
        Tables(db).create_taps(taps)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "taps registered"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@tables_router.get('/taps', tags=['tables'], response_model=List[TapsCreate], status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_user)])
def read_taps_api() -> List[TapsCreate]:
    try:
        db = SessionLocal()
        result = Tables(db).get_taps()
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@tables_router.post('/prints', tags=['tables'], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)])
def create_prints_api(prints: List[PrintsCreate]) -> dict:
    try:
        db = SessionLocal()
        Tables(db).create_prints(prints)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Prints registrados"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@tables_router.get('/prints', tags=['tables'], response_model=List[PrintsCreate], status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_user)])
def read_prtints_api() -> List[PrintsCreate]:
    try:
        db = SessionLocal()
        result = Tables(db).get_prints()
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@tables_router.post('/pays', tags=['tables'], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)])
def create_pays_api(pays: List[PaysCreate]) -> dict:
    try:
        db = SessionLocal()
        Tables(db).create_pays(pays)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Pays registrados"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@tables_router.get('/pays', tags=['tables'], response_model=List[PaysCreate], status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_user)])
def read_pays_api() -> List[PaysCreate]:
    try:
        db = SessionLocal()
        result = Tables(db).get_pays()
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))