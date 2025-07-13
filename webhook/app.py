from flask import Flask, request, jsonify
from intents.greeting import handle_greeting
from intents.service_status import handle_status_check
from intents.escalation import handle_escalation

app = Flask(__name__)

handlers = {
    "greeting": handle_greeting,
    "check_service_status": handle_status_check,
    "escalate_to_agent": handle_escalation,
}

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    tag = body.get("fulfillmentInfo", {}).get("tag")

    if tag in handlers:
        return handlers[tag](body)
    else:
        return jsonify({
            "fulfillment_response": {
                "messages": [{
                    "text": {"text": ["Sorry, I didn't understand that."]}
                }]
            }
        })

if __name__ == "__main__":
    app.run(port=3000)

