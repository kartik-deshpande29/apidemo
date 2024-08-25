from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to extract numbers, alphabets, and find the highest lowercase alphabet
def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase = [max([char for char in alphabets if char.islower()], default="")]
    
    return numbers, alphabets, highest_lowercase

# Unified GET and POST endpoint
@app.route('/bfhl', methods=['GET', 'POST'])
def process_request():
    if request.method == 'POST':
        data = request.json.get("data", [])
        
        numbers, alphabets, highest_lowercase = process_data(data)
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        
        return jsonify(response)
    
    elif request.method == 'GET':
        operation_code = "OP123456"
        return jsonify({"operation_code": operation_code})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
