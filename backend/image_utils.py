from PIL import Image
import io
from fastapi.responses import StreamingResponse

def load_image(data: bytes):
    return Image.open(io.BytesIO(data)).convert("RGB")

def send_image(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
