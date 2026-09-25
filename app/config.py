import os
class Settings:
    PROJECT_NAME: str = "AI Appointment Booking Agent"
    VERSION: str = "1.0.0"
    DEFAULT_SLOT_MINUTES: int = 30
    DB_PATH: str = "bookings.db"
settings = Settings()
