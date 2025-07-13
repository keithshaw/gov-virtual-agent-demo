# 🏛️ Government Virtual Agent Demo (Python)

This project simulates a Dialogflow CX-style virtual agent using Python 
and Flask. It demonstrates how to handle conversational logic via 
webhooks, modular intent routing, mock API responses, and simulated human 
agent escalation (e.g., for Genesys Cloud).

---

## 🔧 Tech Stack

- **Python 3.8+**
- **Flask** (minimal web server)
- Modular Python intent handlers
- CX-style payload structure (no external dependencies)

---

## 📦 Features

- Dialogflow CX-style fulfillment via intent `tags`
- Modular routing for each intent
- Simulated service status checks
- Escalation handoff logic (mocked as payload)
- JSON mock of flow structure for visual reference

---

## 🚀 Getting Started

```bash
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask

# Run the webhook server
python webhook/app.py
Send POST requests to:
http://localhost:3000/webhook

Example Payload:

{
  "fulfillmentInfo": {"tag": "check_service_status"},
  "sessionInfo": {
    "parameters": {
      "service_type": "recycling"
    }
  }
}

🎯 Available Tags
Tag	Description
greeting	Welcomes the user
check_service_status	Returns mocked status for city services
escalate_to_agent	Simulates handoff to a human (e.g., Genesys)

⚠️ Disclaimer
This project is for demonstration purposes only. It doesn’t connect to 
actual Dialogflow CX or Genesys Cloud systems — but the logic, structure, 
and payloads are designed to mirror real-world usage.

🧪 License
MIT — use it, remix it, show it off. Just don’t sell it back to the city.

