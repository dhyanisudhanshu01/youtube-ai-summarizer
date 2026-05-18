from pydantic import BaseModel, HttpUrl

class VideoRequest(BaseModel):
    video_url: HttpUrl