from flask import jsonify

def handle_status_check(body):
    params = body.get("sessionInfo", {}).get("parameters", {})
    service = params.get("service_type", "trash pickup")
    status = "running as scheduled"

    return jsonify({
        "fulfillment_response": {
            "messages": [{
                "text": {"text": [f"The {service} service is currently 
{status}."]}
            }]
        }
    })

