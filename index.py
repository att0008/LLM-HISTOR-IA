app = FastAPI()

# Configura CORS (permite llamadas desde tu app Kivy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carga la API Key desde variables de entorno
API_KEY = os.getenv("DEEPSEEK_API_KEY")

@app.get("/hechos")
async def obtener_hechos(year: int):
    # Ejemplo de respuesta (reemplaza con tu lógica real)
    return {
        "hechos": [
            f"Evento 1 del año {year} (ejemplo)",
            f"Evento 2 del año {year} (ejemplo)"
        ]
    }