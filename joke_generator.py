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
            return self.make_flirty(joke) if joke else self.get_fallback_joke()
            
        except requests.exceptions.Timeout:
            print('Joke API timeout')
            return self.get_fallback_joke()
        except requests.exceptions.RequestException as e:
            print(f'Error fetching joke: {e}')
            return self.get_fallback_joke()
    
    def make_flirty(self, joke):
        """Add a flirty twist to the joke"""
        flirty_intros = [
            "okay but like... ",
            "so hear me out... ",
            "ngl this is kinda funny... ",
            "bestie listen... ",
            "not me but like... ",
            "lowkey... ",
            "no but fr fr... ",
        ]
        flirty_outros = [
            " 😘✨",
            " 💋😉",
            " *winks* ✨",
            " you getting this? 😏",
            " caught that, right? 😘",
            " bet you didn't see that coming 😉",
            " pretty smooth right? 😏✨",
        ]
        
        import random
        intro = random.choice(flirty_intros)
        outro = random.choice(flirty_outros)
        
        return intro + joke + outro
    
    def get_fallback_joke(self):
        """Return a pre-loaded flirty joke if API fails"""
        jokes = [
            "ngl... do you believe in love at first sight, or should i walk by again? 😘✨",
            "okay but like, are you a parking ticket? cause you've got FINE written all over you 😉💋",
            "so like... do you have a map? i just got lost in your eyes 🥺✨",
            "bestie, are you a magician? because whenever i look at you, everyone else disappears 😏💫",
            "not me but like... do you have a sunburn or are you always this hot? 🔥😘",
            "lowkey... are you french? because eiffel for you 😉✨",
            "no but fr fr, if you were a vegetable, you'd be a cute-cumber 🥒😘",
            "caught this... are we french fries? because we're a pretty perfect match 🍟💋",
        ]
        import random
        return random.choice(jokes)

# Test it out
if __name__ == '__main__':
    generator = JokeGenerator()
    print(generator.get_joke())
