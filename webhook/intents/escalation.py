from flask import jsonify

def handle_escalation(body):
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {"text": {"text": ["I’m connecting you to a live agent. 
One moment please…"]}},
                {"payload": {"handoff": True}}  # Simulated Genesys 
integration payload
            ]
        }
    })

