from fastapi import FastAPI, HTTPException
from app.services.transcript_service import get_transcript
from app.services.summary_service import summarize_video
from app.models.request_models import VideoRequest
from app.models.response_models import SummaryResponse
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="YouTube AI Summarizer API",
    description="An API to summarize YouTube videos using AI",
    version="1.0.0" 
)


@app.get("/")
async def home():
    return {
        "message": "YouTube AI Summarizer API is running"
    }


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(request: VideoRequest):

    try:
        logging.info(f"Received request to summarize video: {request.video_url}")
        transcript = get_transcript(
            str(request.video_url)
        )

        summary = summarize_video(transcript)

        return SummaryResponse(
            status="success",
            video_url=str(request.video_url),
            summary=summary
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")

        raise HTTPException(status_code=400, detail=str(e))
        