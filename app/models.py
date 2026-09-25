from pydantic import BaseModel
from typing import List, Optional

class SlotCheckRequest(BaseModel):
    date: str  # YYYY-MM-DD

class SlotAvailability(BaseModel):
    time: str
    available: bool

class BookingRequest(BaseModel):
    client_name: str
    client_email: str
    date: str  # YYYY-MM-DD
    time: str  # HH:MM
    service_type: str = "AI Architecture Consultation"

class BookingConfirmation(BaseModel):
    booking_id: str
    client_name: str
    date: str
    time: str
    service_type: str
    status: str
