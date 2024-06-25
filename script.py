import os
import sys

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import marvin

load_dotenv()

marvin.settings.openai.api_key = os.environ["OPENAI_API_KEY"]


def get_youtube_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])
    return full_text


def create_social_media_post(
    transcript: str, versions: int = 1, max_length: int = 280
) -> list[str]:
    post_content = marvin.generate(
        n=versions,
        instructions=f"Create a social media post from this YouTube transcript: {transcript}",
    )
    return post_content


def main(video_id):
    transcript = get_youtube_transcript(video_id)
    posts = create_social_media_post(transcript)
    for post in posts:
        print(post)
        print("---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <youtube_video_id>")
        sys.exit(1)

    video_id = sys.argv[1]
    main(video_id)
