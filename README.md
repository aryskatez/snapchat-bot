# Snapchat Bot 🤖

A Python-based Snapchat bot that responds to messages using AI (OpenAI ChatGPT or Google Gemini).

## Features
- ✅ Receives messages from Snapchat users
- ✅ AI-powered responses (ChatGPT or Gemini)
- ✅ Easy to deploy
- ✅ Customizable prompts
- ✅ Webhook support for Snapchat API

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/aryskatez/snapchat-bot.git
cd snapchat-bot
```

### 2. Create virtual environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
```

Edit `.env` and add:
- **SNAPCHAT_API_TOKEN**: Get from Snapchat Business Dashboard
- **AI_SERVICE**: Choose `openai` or `gemini`
- **OPENAI_API_KEY** or **GEMINI_API_KEY**: Get from respective providers

### 5. Run the bot
```bash
python main.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Test Endpoint (Local Testing)
```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi bot!"}'
```

### Webhook Endpoint (For Snapchat)
```
POST /webhook

Body:
{
  "sender_id": "user123",
  "message": "Hello!"
}
```

### Health Check
```bash
curl http://localhost:5000/health
```

## Getting API Keys

### OpenAI (ChatGPT)
1. Go to [openai.com](https://openai.com)
2. Sign up/Login
3. Go to API Keys section
4. Create new secret key
5. Add to `.env` as `OPENAI_API_KEY`

### Google Gemini
1. Go to [makersuite.google.com](https://makersuite.google.com)
2. Click "Get API Key"
3. Create new API key
4. Add to `.env` as `GEMINI_API_KEY`

### Snapchat
1. Create a Snapchat Business Account
2. Go to Snapchat Business Suite
3. Create a Snapchat App
4. Get your API token
5. Add to `.env` as `SNAPCHAT_API_TOKEN`

## Deployment

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku config:set SNAPCHAT_API_TOKEN=your_token
heroku config:set OPENAI_API_KEY=your_key
```

### Railway / Replit
Upload the repo and set environment variables in the dashboard.

## Project Structure
```
snapchat-bot/
├── main.py           # Flask app & endpoints
├── bot.py            # Bot logic
├── ai.py             # AI service integration
├── config.py         # Configuration
├── requirements.txt  # Dependencies
├── .env.example      # Example env variables
└── README.md         # This file
```

## Customization

### Change AI Prompt
Edit the `system` message in `ai.py` line 44:
```python
'You are a helpful and friendly Snapchat bot...'
```

### Add More Commands
Edit `bot.py` to add custom logic for specific commands.

## Troubleshooting

**Bot not responding?**
- Check API keys in `.env`
- Ensure all dependencies are installed
- Check console for error messages

**Snapchat webhook not working?**
- Verify webhook URL is publicly accessible
- Check that SNAPCHAT_API_TOKEN is correct
- Review Snapchat API documentation

**Out of API credits?**
- Monitor your OpenAI/Gemini usage
- Add spending limits in your API dashboard

## License
MIT

## Support
For issues, create a GitHub issue or check Snapchat/AI provider documentation.
