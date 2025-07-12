# Railway Hello World Python App

A simple Flask application ready for deployment on Railway.

## Files

- `railway_hello.py` - Main Flask application
- `railway_requirements.txt` - Python dependencies
- `Procfile` - Railway deployment configuration

## Local Development

1. Install dependencies:
```bash
pip install -r railway_requirements.txt
```

2. Run the app:
```bash
python railway_hello.py
```

3. Visit `http://localhost:5000`

## Railway Deployment

1. Push code to GitHub repository
2. Connect GitHub repo to Railway
3. Railway will automatically detect and deploy using the Procfile
4. App will be available at your Railway domain

## Environment Variables

- `PORT` - Automatically set by Railway (defaults to 5000 locally)

## Routes

- `/` - Hello World page
- `/health` - Health check endpoint