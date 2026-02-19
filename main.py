from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, WebSocket
from app.api.services import llm_service

app = FastAPI()


app.mount("/frontend", StaticFiles(directory="app/frontend"), name="frontend")


@app.get("/")
async def get_index():
    return FileResponse("app/frontend/index.html")


@app.websocket("/chat")
async def chatbot(ws: WebSocket):
    await ws.accept()
    await ws.send_text("""
    Welcome! I'm Rio, your marketing assistant. 
    I can help you craft marketing content and conduct market research to boost your facilities services business. 
    How can I help you today?""")

    while True:
        data = await ws.receive_text()
        reply = await llm_service.reply_to_chat(data)
        await ws.send_text(reply)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
