from fastapi import FastAPI, WebSocket
import json

app = FastAPI()
ws_connections = []

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    ws_connections.append(ws)
    try:
        while True:
            await ws.receive_text()
    except:
        ws_connections.remove(ws)

def broadcast(data):
    for ws in ws_connections:
        ws.send_text(json.dumps(data))