# YouTube AI Summarizer API

An AI-powered backend service that summarizes YouTube video transcripts using Google's Gemini AI and FastAPI.

This project demonstrates:
- AI backend engineering
- FastAPI REST APIs
- Gemini AI integration
- transcript processing
- chunk-based summarization
- production deployment
- cloud-hosted AI services

---

# Features

- Summarize YouTube video transcripts using AI
- FastAPI-based REST API
- Gemini AI integration
- Chunk-based transcript processing
- Swagger API documentation
- Environment variable support
- Production-ready backend structure
- Deployable on free cloud platforms like Render

---

# Tech Stack

- Python
- FastAPI
- Google Gemini AI
- Pydantic
- Uvicorn
- python-dotenv

---

# Project Structure

```text
youtube-ai-summarizer/
│
├── app/
│   ├── main.py
│   │
│   ├── services/
│   │   ├── transcript_service.py
│   │   └── summary_service.py
│   │
│   └── models/
│       ├── request_models.py
│       └── response_models.py
│
├── requirements.txt
├── runtime.txt
├── .env
├── .gitignore
└── README.md
```

---

# API Flow

```text
Client Request
      ↓
FastAPI Backend
      ↓
Transcript Processing
      ↓
Gemini AI Summarization
      ↓
JSON Response
```

---

# Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_URL
```

```bash
cd youtube-ai-summarizer
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

## `.env`

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

---

# Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation.

---

# API Endpoints

## Health Check

### GET `/`

Response:

```json
{
  "message": "API is running successfully"
}
```

---

## Summarize Video

### POST `/summarize`

Request Body:

```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

Response:

```json
{
  "status": "success",
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "summary": "Generated AI summary..."
}
```

---

# Deployment on Render

This project can be deployed for free using Render.

## Build Command

```text
pip install -r requirements.txt
```

## Start Command

```text
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

# runtime.txt

```text
python-3.11.9
```

---

# Add Environment Variable on Render

```text
GEMINI_API_KEY=your_api_key
```

---

# Current Limitations

- YouTube transcript extraction may fail on cloud platforms due to YouTube IP restrictions
- Some videos may not contain subtitles
- Free hosting services may have cold start delays

---

# Future Improvements

- Timestamped summaries
- Chapter generation
- Multilingual summarization
- RAG-based video chat
- Vector database integration
- Whisper AI transcription
- Authentication and rate limiting
- Async background jobs
- Docker support
- CI/CD pipeline

---

# Learning Outcomes

This project covers:

- Backend API development
- FastAPI fundamentals
- AI service integration
- Environment variable management
- Cloud deployment
- Production API architecture
- AI summarization pipelines
- Error handling and logging

---

# Author

Developed by SUDHANSHU DHYANI

---

# License

This project is open-source and available under the MIT License.
