from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from escale_ai.agent_factory import AgentFactory
import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve static files
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/")
async def read_index():
    """Serve the chat interface"""
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))

@app.post("/run_base")
async def run_base():
    """Execute the base team pipeline and return its context"""
    try:
        result = AgentFactory.run_base_pipeline()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ClientRequest(BaseModel):
    client_name: str

@app.post("/run_client")
async def run_client(req: ClientRequest):
    """Execute a client team pipeline given a client name"""
    try:
        result = AgentFactory.run_client_pipeline(req.client_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
