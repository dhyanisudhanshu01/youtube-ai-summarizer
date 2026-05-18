import re
from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

def extract_video_id(url: str) -> str:
    # Regular expression to extract video ID from YouTube URL
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"

    match = re.search(pattern, url)
    
    if not match:
        raise ValueError("Invalid YouTube URL")
    else:
        return match.group(1)
    
def get_transcript(video_url: str) -> str:
    """Fetches the transcript of a YouTube video given its URL."""
    video_id = extract_video_id(video_url)
    
    try:
        # Try English first
        transcript_data = api.fetch(video_id, languages=['en'])
        transcript_text = " ".join([item.text for item in transcript_data])

    except:
        # Fallback to Hindi
        transcript_data = api.fetch(video_id, languages=['hi'])
        transcript_text = " ".join([item.text for item in transcript_data])

    cleaned_transcript = transcript_text.replace('\n', ' ')
    
    return cleaned_transcript