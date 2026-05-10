from ai import AIResponder
from joke_generator import JokeGenerator
import os

class SnapchatBot:
    def __init__(self):
        self.ai = AIResponder()
        self.joke_gen = JokeGenerator()
        self.snapchat_token = os.getenv('SNAPCHAT_API_TOKEN')
        self.snapchat_api_url = os.getenv('SNAPCHAT_API_URL', 'https://api.snapchat.com/v1')
    
    def respond(self, message):
        """Get response to user message - checks for commands first"""
        try:
            message_lower = message.lower().strip()
            
            # Check for joke command
            if any(word in message_lower for word in ['joke', 'funny', 'make me laugh', 'lol', 'haha']):
                return self.joke_gen.get_joke()
            
            # Check for motivation command
            if any(word in message_lower for word in ['motivate', 'inspire', 'motivation', 'push me', 'hype', 'pump me up']):
                return self.get_motivation()
            
            # Default: Use AI response
            response = self.ai.generate_response(message)
            return response
        except Exception as e:
            print(f'Error generating response: {e}')
            return "Sorry, I couldn't process that. Try again!"
    
    def get_motivation(self):
        """Return an interesting and motivating message"""
        motivations = [
            "yo, listen... you're capable of SO much more than you think 💪✨ go out there and show the world what you're made of!",
            "bestie, every single day is a chance to level up 📈 you got this, i believe in you 🔥",
            "ngl, you're literally crushing it. keep that energy and watch what happens 🚀💯",
            "remember: your vibe attracts your tribe. stay authentic, stay focused 🎯✨",
            "the fact that you're even trying means you're already winning 🏆 keep going, you're so close!",
            "you know what? the best version of you is coming soon... and it's gonna be INSANE 😤🔥",
            "lowkey, your potential is absolutely unmatched. don't let anyone dim your light ✨💫",
            "fr fr, progress > perfection. every step forward counts, celebrate that 🎉",
            "you're not just surviving, you're about to THRIVE. i can feel it 🌟💪",
            "real talk: you're exactly where you need to be. trust the process and keep grinding 💯🚀",
            "okay but like... imagine how good you'll feel when you accomplish your goals 🎯✨ that's YOUR future",
            "bestie, you're a vibe and your energy is CONTAGIOUS. spread that good stuff 🌈💋",
            "no cap, you deserve all the good things coming your way. stay ready 🙏✨",
            "the universe is literally conspiring in your favor rn 🌌 you just gotta believe it 💫",
            "you're not just passing through life, you're building your empire 👑 keep stacking wins 💯",
            "wake up: you're literally the main character of your story 📖✨ act like it!",
            "facts: you're stronger than your excuses. what you're about to do will be LEGENDARY 🔥",
            "not to be dramatic but... you're about to change the game 🎮 believe the hype!",
        ]
        import random
        return random.choice(motivations)
    
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
