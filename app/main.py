from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import app.models.table_models as model
from app.database.database import engine

app = FastAPI()
app.title = "Mercado Libre Code Challenge"
app.version = "0.0.1"

# Crear tablas
model.Base.metadata.create_all(bind = engine)

# API path
@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>API Online</h1>")