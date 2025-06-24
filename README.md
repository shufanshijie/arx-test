# ARX Service & Python Client SDK

This project consists of two parts:
- **ARX Service**: A Spring Boot-based data anonymization service (no need to install Java separately, JRE is bundled).
- **Python Client SDK**: A Python client for interacting with the ARX Service.

---

## Directory Structure

```
Project Root/
├── deliver/                    # ARX Service package
│   ├── jre/                    # Bundled Java Runtime Environment (JRE 17)
│   ├── arx-service-1.0.0.jar   # Spring Boot executable JAR
│   ├── start.bat               # Windows startup script
│   └── README.txt              # Service-side instructions
├── arx_sdk.py                  # Main Python SDK file
├── example.py                  # SDK usage example
├── requirements.txt            # Python dependencies
└── README.md                   # This instruction file
```

---

# ARX Service Instructions (Windows)

This package allows you to run the ARX Service on Windows without installing Java separately.

### How to Start

1. Extract the `deliver` folder to any location.
2. Double-click `start.bat` to start the service.
   - Alternatively, open a command prompt in this directory and run:
     ```
     start.bat
     ```
3. The service will start using the bundled JRE. **No need to install Java.**
4. By default, the service will be available at: [http://localhost:8080](http://localhost:8080)

### Change Port

- To change the port, edit the `application.yml` inside the JAR, or add `--server.port=xxxx` at the end of `start.bat`.

### Notes

- The JRE in the `jre/` folder is only used by this service and does not affect other applications.
- If you encounter any issues, please contact the delivery team.

---

# Python Client SDK Instructions

This directory contains a Python client SDK for calling the ARX Service REST APIs.

## Features

- Simple REST API client
- Example script demonstrating usage
- Easy dependency installation

## How to Use

### 1. Prerequisites

- Start the ARX Service first (see above), default address: `http://localhost:8080`
- Python 3.6 or above

### 2. Install Dependencies

It is recommended to use a virtual environment:

```bash
cd project root
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Example

Make sure the ARX Service is running, then execute:

```bash
python example.py
```

You should see output similar to:

```
--- Initializing ARX Service Client ---

1. Checking service health...
✅ Service is UP and running.

2. Calling the 'hello' endpoint...
Response from /api/hello:
  Message: Hello from ARX Service!
  Status: success
  Timestamp: 2023-10-27T10:30:00.123456

3. Calling the 'health' endpoint for details...
Response from /api/health:
  Service Name: arx-service
  Status: UP
  Timestamp: 2023-10-27T10:30:01.234567
```

---

For more help, please refer to the README in each directory or contact the delivery team. 