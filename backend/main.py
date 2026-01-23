from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uuid, os

from backend.processing import generate_coloring_page

app = FastAPI()

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.get("/")
def serve_ui():
    return FileResponse("backend/static/index.html")

TEMP_DIR = "backend/temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    input_path = f"{TEMP_DIR}/{uuid.uuid4()}_{file.filename}"
    output_path = f"{TEMP_DIR}/output_{uuid.uuid4()}.png"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    generate_coloring_page(input_path, output_path)

    return FileResponse(
        output_path,
        media_type="image/png",
        filename="coloring_page.png"
    )