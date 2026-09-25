import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestAppointmentAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_slots_availability(self):
        res = self.client.get("/slots?date=2026-10-15")
        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(res.json()["slots"]), 0)

    def test_booking_workflow(self):
        payload = {
            "client_name": "Sarah Connor",
            "client_email": "sarah@cyberdyne.com",
            "date": "2026-10-15",
            "time": "10:00",
            "service_type": "AI Architecture Consultation"
        }
        res = self.client.post("/book", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "CONFIRMED")
        
        # Double booking check
        res2 = self.client.post("/book", json=payload)
        self.assertEqual(res2.status_code, 400)

if __name__ == "__main__":
    unittest.main()
