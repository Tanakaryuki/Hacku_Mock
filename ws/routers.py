import asyncio
from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await asyncio.sleep(0.1)
            await websocket.send_text(f"ping")    
            
    except Exception as e:
        print(f"WebSocketエラー: {e}")
    finally:
        pass
