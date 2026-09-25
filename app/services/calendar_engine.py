import sqlite3
import uuid
from app.config import settings

def init_calendar_db():
    conn = sqlite3.connect(settings.DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
        booking_id TEXT PRIMARY KEY,
        client_name TEXT,
        client_email TEXT,
        date TEXT,
        time TEXT,
        service_type TEXT,
        status TEXT DEFAULT 'CONFIRMED'
    )''')
    conn.commit()
    conn.close()

ALL_SLOTS = ["09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00"]

def get_slots(date: str):
    init_calendar_db()
    conn = sqlite3.connect(settings.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT time FROM appointments WHERE date = ? AND status = 'CONFIRMED'", (date,))
    booked = {r[0] for r in c.fetchall()}
    conn.close()
    return [{"time": s, "available": s not in booked} for s in ALL_SLOTS]

def book_appointment(req):
    init_calendar_db()
    slots = {s["time"]: s["available"] for s in get_slots(req.date)}
    if not slots.get(req.time, False):
        return None, "Selected slot is already reserved or unavailable."
        
    booking_id = f"BK-{uuid.uuid4().hex[:6].upper()}"
    conn = sqlite3.connect(settings.DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO appointments (booking_id, client_name, client_email, date, time, service_type) VALUES (?, ?, ?, ?, ?, ?)",
              (booking_id, req.client_name, req.client_email, req.date, req.time, req.service_type))
    conn.commit()
    conn.close()
    return booking_id, "Booking confirmed."
