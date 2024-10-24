from fastapi import WebSocket, WebSocketDisconnect

connected_users = {}

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_id = await websocket.receive_text()
    connected_users[user_id] = websocket
    
    try:
        while True:
            data = await websocket.receive_text()
            # Логика обработки сообщений.
            for uid, conn in connected_users.items():
                if uid != user_id:
                    await conn.send_text(f"Message from {user_id}: {data}")
    except WebSocketDisconnect:
        del connected_users[user_id]
