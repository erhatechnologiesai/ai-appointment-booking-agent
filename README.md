# Appointment Booking Agent

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An intelligent appointment booking system utilizing natural language understanding and constraint satisfaction algorithms to schedule, reschedule, and verify calendar appointments without double-booking.

---

## Key Features

- **Real-time**: calendar slot constraint solver eliminating scheduling conflicts
- **Natural**: language time parsing (e.g., 'next Tuesday at 3 PM')
- **Automated**: booking confirmation and unique appointment reference code generator
- **Cancellation**: and rescheduling state machine
- **Multi-staff**: calendar partitioning support

---

## Architecture

```mermaid
flowchart TD
    User([Customer]) -->|Booking Request| API[FastAPI Booking Service]
    API --> Parser[Natural Language Time Parser]
    Parser --> Solver[Slot Constraint Solver]
    Solver --> Calendar[(Calendar Database)]
    Solver -->|Available| Confirm[Confirm & Generate Reference]
    Solver -->|Conflict| Suggest[Suggest Alternative Slots]
    Confirm --> User
```

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| **Runtime** | Python 3.12 | Core execution environment |
| **API Framework** | FastAPI & Uvicorn | High-performance asynchronous REST endpoints |
| **Data Validation** | Pydantic v2 | Strict schema validation and serialization |
| **Execution Engine** | Dual-Mode (Local + Cloud) | Production-ready logic with offline verification |
| **Testing** | Unittest & Pytest | Deterministic automated verification suite |

---

## Project Structure

```text
appointment-booking-agent/
├── app/
│   ├── __init__.py
│   ├── api.py           # FastAPI routes and server definitions
│   ├── config.py        # Environment variables and application settings
│   ├── models.py        # Pydantic data schemas
│   └── services/        # Core business automation logic
├── tests/
│   ├── __init__.py
│   └── test_booking.py   # Automated test suite
├── .env.example         # Template for environment configuration
├── .gitignore           # Python and runtime exclusions
├── LICENSE              # MIT License
├── README.md            # Comprehensive project documentation
└── requirements.txt     # Python package dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.10+ (Python 3.12 recommended)
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/erhatechnologiesai/appointment-booking-agent.git
   cd appointment-booking-agent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

---

## Running the Application

Start the local development server with auto-reload:

```bash
python -m uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
```

Once running, interactive documentation is accessible at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Booking system status |
| `GET` | `/slots` | Retrieve all available calendar slots for a date range |
| `POST` | `/book` | Reserve a specific slot with customer details |

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/book -H "Content-Type: application/json" -d '{"client_name": "Jane Doe", "slot_time": "2026-10-15T14:00:00Z", "service_type": "Consultation"}'
```

---

## Running Tests

Execute the automated test suite:

```bash
python -m unittest tests/test_booking.py
```

Or using pytest:

```bash
pytest tests/
```

All test cases are self-contained and run offline without requiring third-party API credentials.

---

## Security & Best Practices

- **Zero Credential Leakage**: API tokens and secrets are loaded exclusively via environment variables and excluded by `.gitignore`.
- **Strict Validation**: All incoming request payloads are strictly validated using Pydantic schemas.
- **Fail-Safe Fallbacks**: Deterministic offline engines guarantee application continuity even during external provider outages.

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
