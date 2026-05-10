from ai import AIResponder
import os

class SnapchatBot:
    def __init__(self):
        self.ai = AIResponder()
        self.snapchat_token = os.getenv('SNAPCHAT_API_TOKEN')
        self.snapchat_api_url = os.getenv('SNAPCHAT_API_URL', 'https://api.snapchat.com/v1')
    
    def respond(self, message):
        """Get AI response to user message"""
        try:
            response = self.ai.generate_response(message)
            return response
        except Exception as e:
            print(f'Error generating response: {e}')
            return "Sorry, I couldn't process that. Try again!"
    
    def send_message(self, sender_id, message):
        """Send message back to Snapchat user"""
        try:
            # TODO: Implement actual Snapchat API call
            # For now, just log it
            print(f'Sending to {sender_id}: {message}')
            return True
        except Exception as e:
            print(f'Error sending message: {e}')
            return False
    
    def process_conversation(self, sender_id, message):
        """Main conversation handler"""
        response = self.respond(message)
        self.send_message(sender_id, response)
        return response
