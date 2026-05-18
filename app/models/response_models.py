from pydantic import BaseModel

class SummaryResponse(BaseModel):
    video_url: str
    status: str
    summary: str