from flask import jsonify

def handle_greeting(body):
    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {"text": ["Hi there! How can I help you with city 
services today?"]}
            }]
        }
    })

