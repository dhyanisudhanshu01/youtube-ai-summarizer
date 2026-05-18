import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')



genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')

def chunk_text(text: str, chunk_size: int = 5000):
    """Split transcript into chunks."""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks


def summarize_chunk(chunk: str) -> str:
    """
    Summarize a single chunk.
    """

    prompt = f"""
    Summarize the following transcript chunk.

    Provide:
    - concise summary
    - important points
    - useful insights

    Transcript:
    {chunk}
    """

    response = model.generate_content(prompt)

    return response.text


def summarize_video(transcript: str) -> str:
    """
    Summarize full transcript using chunking.
    """

    chunks = chunk_text(transcript)

    chunk_summaries = []

    for index, chunk in enumerate(chunks):

        print(f"Processing chunk {index + 1}/{len(chunks)}")

        summary = summarize_chunk(chunk)

        chunk_summaries.append(summary)

    combined_summary = "\n".join(chunk_summaries)

    final_prompt = f"""
    Below are summaries of multiple parts of a YouTube video.

    Create a FINAL COMPREHENSIVE SUMMARY.

    Include:
    1. Overall summary
    2. Main key points
    3. Important insights
    4. Final conclusion

    Chunk Summaries:
    {combined_summary}
    """

    final_response = model.generate_content(final_prompt)

    return final_response.text