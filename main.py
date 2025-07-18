from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import subprocess
from fastapi.responses import StreamingResponse
from fastapi import Request


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoURL(BaseModel):
    url: str
    
@app.post("/miniatura")
def obtener_miniatura(data: VideoURL):
    print("miniatura")
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(data.url, download=False)
            return {"miniatura": info.get("thumbnail")}
    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/descargarvideo")
def descargar(request: Request, url: str):
    try:
        print("Descargando:", url)

        comando = [
            "yt-dlp",
            "-f", "best",
            "-o", "-",  # salida a stdout
            url
        ]

        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE)

        headers = {
            "Content-Disposition": 'attachment; filename="video.mp4"'
        }
        return StreamingResponse(proceso.stdout, media_type="video/mp4", headers=headers)

    except Exception as e:
        return {"error": f"Error al descargar: {str(e)}"}
    
@app.get("/descargaraudio")
def descargar(request: Request, url: str):
    try:
        print("Descargando:", url)

        comando = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", "-",
            url
        ]

        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE)
        
        headers = {
            "Content-Disposition": 'attachment; filename="audio.mp3"'
        }

        return StreamingResponse(proceso.stdout, media_type="audio/mp3", headers=headers)

    except Exception as e:
        return {"error": f"Error al descargar: {str(e)}"}
    
        
"""@app.post("/descargar")
def descargar(data: VideoURL):
    try:
        print("Descargando:", data.url)  # DEBUG
        with yt_dlp.YoutubeDL({'format': 'best'}) as descarga:
            descarga.download([data.url])
        return {"mensaje": "Video descargado correctamente"}
    except Exception as e:
        return {"error": f"Error al descargar: {str(e)}"}"""