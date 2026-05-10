import os
from dotenv import load_dotenv

load_dotenv()

class AIResponder:
    def __init__(self):
        self.ai_service = os.getenv('AI_SERVICE', 'openai')  # 'openai' or 'gemini'
        self.api_key = os.getenv('OPENAI_API_KEY') or os.getenv('GEMINI_API_KEY')
        
        if self.ai_service == 'openai':
            try:
                import openai
                openai.api_key = self.api_key
                self.client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                print('OpenAI not installed. Install with: pip install openai')
        elif self.ai_service == 'gemini':
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-pro')
            except ImportError:
                print('Google AI not installed. Install with: pip install google-generativeai')
    
    def generate_response(self, message):
        """Generate AI response using configured service"""
        if self.ai_service == 'openai':
            return self._openai_response(message)
        elif self.ai_service == 'gemini':
            return self._gemini_response(message)
        else:
            return self._fallback_response(message)
    
    def _openai_response(self, message):
        """Get response from OpenAI ChatGPT"""
        try:
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': 'You are a helpful and friendly Snapchat bot. Keep responses short and casual (under 150 characters).'},
                    {'role': 'user', 'content': message}
                ],
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'OpenAI Error: {e}')
            return 'Oops! Something went wrong. Try again!'
    
    def _gemini_response(self, message):
        """Get response from Google Gemini"""
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            print(f'Gemini Error: {e}')
            return 'Oops! Something went wrong. Try again!'
    
    def _fallback_response(self, message):
        """Fallback response when no AI service is configured"""
        return f'You said: {message}. (Configure an AI service to enable smart responses!)'
