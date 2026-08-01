from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount the static directory to serve HTML, CSS, and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.post("/order")
def handle_order(data: dict):
    # Here you can process order data coming from the Telegram Mini App
    print("Received order:", data)
    return {"status": "success", "message": "Order received successfully"}
