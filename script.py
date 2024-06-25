from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import marvin
import typer

load_dotenv()


def get_youtube_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])
    return full_text


def create_social_media_post(transcript: str, n: int) -> list[str]:
    instructions = (
        f"Create a social media post from this YouTube transcript: {transcript}"
    )
    post_content = marvin.generate(
        n=n,
        instructions=instructions,
    )
    return post_content


def main(video_id: str, num_posts: int = 1):
    transcript = get_youtube_transcript(video_id)
    # print("Retrieved transcript:", transcript)
    # print(f"Generating {num_posts} social media post(s) from transcript...")
    post_content = create_social_media_post(transcript, num_posts)

    print("Generated Social Media Post Content:")
    for i, content in enumerate(post_content, 1):
        print(f"Version {i}: {content}\n")


if __name__ == "__main__":
    typer.run(main)
