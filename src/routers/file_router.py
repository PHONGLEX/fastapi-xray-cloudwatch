import io
import uuid
from pathlib import Path
from PIL import Image

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from helper.authentication import validate_token

BASE_DIR = Path(__file__).parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

file_router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@file_router.post('/upload-file')
@validate_token
async def upload_file(Authorize: AuthJWT=Depends(), file:UploadFile=File(...)):
    UPLOAD_DIR.mkdir(exist_ok=True)
    bytes_str = io.BytesIO(await file.read())
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file format")
    fname = Path(file.filename)
    fext = fname.suffix
    dest = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    img.save(dest)
    return {"success": True}