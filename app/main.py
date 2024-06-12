from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import app.models.table_models as model
from app.database.database import engine
from app.routers.table_routers import tables_router
from app.routers.auth_routers import auth_router

app = FastAPI()
app.title = "Mercado Libre Code Challenge"
app.version = "0.0.1"

# Routers
app.include_router(tables_router)
app.include_router(auth_router)

# Crear tablas
model.Base.metadata.create_all(bind = engine)

# API path
@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>API Online</h1>")