import requests
import os
from dotenv import load_dotenv

load_dotenv()

class JokeGenerator:
    def __init__(self):
        # Using JokeAPI - free, no key required
        self.joke_api_url = os.getenv('JOKE_API_URL', 'https://v2.jokeapi.dev/joke/Any')
    
    def get_joke(self):
        """Fetch a random joke from external API"""
        try:
            # Add parameters for better jokes
            params = {
                'format': 'txt',  # Get plain text response
                'blacklistFlags': 'nsfw,religious,political,racist,sexist',  # Filter bad jokes
            }
            
            response = requests.get(self.joke_api_url, params=params, timeout=5)
            response.raise_for_status()
            
            # JokeAPI returns plain text in 'txt' format
            joke = response.text.strip()
            return joke if joke else self.get_fallback_joke()
            
        except requests.exceptions.Timeout:
            print('Joke API timeout')
            return self.get_fallback_joke()
        except requests.exceptions.RequestException as e:
            print(f'Error fetching joke: {e}')
            return self.get_fallback_joke()
    
    def get_fallback_joke(self):
        """Return a pre-loaded joke if API fails"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
            "What do you call a fake noodle? An impasta! 🍝",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚",
            "What did the ocean say to the beach? Nothing, it just waved! 🌊",
            "Why did the cookie go to the doctor? Because it felt crumbly! 🍪",
        ]
        import random
        return random.choice(jokes)

# Test it out
if __name__ == '__main__':
    generator = JokeGenerator()
    print(generator.get_joke())
