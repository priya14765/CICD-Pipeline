from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="CodeNova Service", version="1.0.0")


@app.get("/")
def read_root() -> FileResponse:
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api")
def read_api() -> dict[str, str]:
    return {"message": "CodeNova service is running"}


@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
