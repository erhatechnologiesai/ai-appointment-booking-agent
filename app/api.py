from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import SlotCheckRequest, BookingRequest, BookingConfirmation
from app.services.calendar_engine import get_slots, book_appointment

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def root():
    return {"service": settings.PROJECT_NAME, "status": "active"}

@app.get("/slots")
def check_slots(date: str):
    return {"date": date, "slots": get_slots(date)}

@app.post("/book", response_model=BookingConfirmation)
def make_booking(req: BookingRequest):
    b_id, msg = book_appointment(req)
    if not b_id:
        raise HTTPException(status_code=400, detail=msg)
    return BookingConfirmation(
        booking_id=b_id,
        client_name=req.client_name,
        date=req.date,
        time=req.time,
        service_type=req.service_type,
        status="CONFIRMED"
    )
