from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import gc

from prompt_router import route_prompt
from image_utils import load_image, send_image

# OpenCV features
from ai_modules.face_blur import blur_face
from ai_modules.vintage import vintage_filter
from ai_modules.lighting import dramatic_lighting, cinematic_lighting
from ai_modules.clarity import studio_clarity
from ai_modules.portrait import soft_portrait
from ai_modules.cyberpunk_cv import cyberpunk_cv
from ai_modules.minimal import minimal_aesthetic
from ai_modules.bw import black_white


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_image(
    image: UploadFile = File(...),
    prompt: str = Form(...)
):
    print("🔥 /process HIT")

    image_bytes = await image.read()
    img = load_image(image_bytes)

    task = route_prompt(prompt)

    if task == "face_blur":
        output = blur_face(img)

    elif task == "vintage":
        output = vintage_filter(img)

    elif task == "dramatic":
        output = dramatic_lighting(img)

    elif task == "cinematic":
        output = cinematic_lighting(img)

    elif task == "studio":
        output = studio_clarity(img)

    elif task == "portrait":
        output = soft_portrait(img)

    elif task == "cyberpunk":
        output = cyberpunk_cv(img)

    elif task == "minimal":
        output = minimal_aesthetic(img)

    elif task == "bw":
        output = black_white(img)
        
    else:
        output = img  # fallback

    response = send_image(output)

    # ZeroReuse cleanup
    del img, output, image_bytes
    gc.collect()

    return response
