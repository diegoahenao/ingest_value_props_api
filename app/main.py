from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mercado Libre Code Challenge"
app.version = "0.0.1"

# API path
@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>API Online</h1>")