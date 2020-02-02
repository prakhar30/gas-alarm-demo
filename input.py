import RPi.GPIO as GPIO
import asyncio
import websockets

GPIO.setmode(GPIO.BCM)

GAS_DETECTOR_GPIO = 17
GPIO.setup(GAS_DETECTOR_GPIO, GPIO.IN)


async def time(websocket, path):
    lastDataSent = "All okay!"
    dataToSend = ""
    while True:
        currentStatus = GPIO.input(GAS_DETECTOR_GPIO)
        if currentStatus:
            dataToSend = "DANGER"
        else:
            dataToSend = "All okay!"
        if dataToSend != lastDataSent:
            lastDataSent = dataToSend
            await websocket.send(dataToSend)
            if dataToSend == "DANGER":
                await asyncio.sleep(4)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()