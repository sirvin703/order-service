from fastapi import FastAPI

app = FastAPI(title="order-service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/orders")
def list_orders():
    return [
        {"id": 1001, "product_id": 1, "qty": 2, "total": 19.98},
        {"id": 1002, "product_id": 2, "qty": 1, "total": 14.99},
    ]
