from fastapi import FastAPI

app = FastAPI(
    title="API Module Chauffeur",
    description="Gestion des chauffeurs de la flotte",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"status": "online", "message": "Bienvenue sur le module Chauffeur !"}

@app.get("/api/chauffeurs/test")
def test_chauffeur():
    return {
        "id_chauffeur": 1,
        "nom": "El Mansouri",
        "prenom": "Karim",
        "statut": "DISPONIBLE"
    }