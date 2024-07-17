import asyncio
from fastapi import APIRouter, WebSocket
import random

router = APIRouter()

@router.websocket("/ws/physics")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            
            response = {
                "senderId": data["senderId"],
                "roomId": data["roomId"],
                "objects": [
                    {
                        "objectId": "string",
                        "layer": 0,
                        "kinds": "OBJECT_KIND_UNKNOWN",
                        "state": "OBJECT_STATE_UNKNOWN",
                        "position": {
                            "x": random.randint(0, 10),
                            "y": random.randint(0, 10),
                            "z": random.randint(0, 10)
                        },
                        "size": {
                            "x": random.randint(0, 10),
                            "y": random.randint(0, 10),
                            "z": random.randint(0, 10)
                        }
                    }
                ]
            }
            await websocket.send_json(response)
            
    except Exception as e:
        print(f"WebSocketエラー: {e}")
    finally:
        pass
