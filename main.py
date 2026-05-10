from flask import Flask, request, jsonify
from bot import SnapchatBot
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bot = SnapchatBot()

@app.route('/webhook', methods=['POST'])
def webhook():
    """Receive messages from Snapchat"""
    try:
        data = request.json
        sender_id = data.get('sender_id')
        message = data.get('message')
        
        if not sender_id or not message:
            return jsonify({'error': 'Missing sender_id or message'}), 400
        
        # Get AI response
        response = bot.respond(message)
        
        # Send back to Snapchat
        bot.send_message(sender_id, response)
        
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500

@app.route('/test', methods=['POST'])
def test():
    """Test endpoint for local testing"""
    try:
        data = request.json
        message = data.get('message', 'Hello')
        response = bot.respond(message)
        return jsonify({'message': message, 'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
