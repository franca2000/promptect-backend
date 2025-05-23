from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import dashboard_data, recent_events, auth
import os
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()

# Inicializa la app FastAPI
app = FastAPI()

# Lista de orígenes permitidos para CORS
origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5173").split(",")

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas principales
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(dashboard_data.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(recent_events.router, prefix="/events", tags=["events"])
