from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import os
import uuid
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.pipeline import generate_coloring_page


app = FastAPI(title="Coloring Page Generator API")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return JSONResponse(
            status_code=400,
            content={"error": "Only image files are allowed"}
        )

    safe_input_name = f"input_{uuid.uuid4()}.jpg"
    input_path = os.path.join(TEMP_DIR, safe_input_name)

    output_path = os.path.join(TEMP_DIR, f"coloring_{uuid.uuid4()}.png")

    with open(input_path, "wb") as f:
        f.write(await file.read())

    try:
        print("INPUT:", input_path)
        print("OUTPUT:", output_path)

        generate_coloring_page(input_path, output_path)

        if not os.path.exists(output_path):
            raise RuntimeError("Output image not created")

    except Exception as e:
        print("❌ ERROR:", e)
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

    return FileResponse(
        output_path,
        media_type="image/png",
        filename="coloring_page.png"
    )

