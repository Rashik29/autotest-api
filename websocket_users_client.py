import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        await websocket.send(message)  # Отправляем сообщение
        print(f"Отправлено сообщение серверу: {message}")

        for i in range(5):
            response = await websocket.recv()
            print(f"Получено сообщение от сервера: {response}")


if __name__ == "__main__":
    asyncio.run(client())