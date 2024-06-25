import argparse

# import os

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import marvin

load_dotenv()

DEFAULT_POST_LENGTH = 280
# marvin.settings.openai.api_key = os.environ["OPENAI_API_KEY"]


def get_youtube_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])
    return full_text


def create_social_media_post(
    transcript: str, versions: int, max_length: int
) -> list[str]:
    instructions = (
        "Create a social media post from this YouTube transcript:\n\n"
        f"{transcript}\n\n"
        f"The post should be concise and within {max_length} characters."
    )

    post_content = marvin.generate(
        n=versions,
        instructions=instructions,
    )
    return post_content


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("video_id", help="YouTube video ID")
    parser.add_argument("-n", "--num_posts", type=int, default=1, help="Number of posts to generate")
    parser.add_argument("-m", "--max_length", type=int, default=280, help="Maximum length of the post")
    args = parser.parse_args()

    breakpoint()
    transcript = get_youtube_transcript(args.video_id)

    post_content = create_social_media_post(transcript, args.num_posts, args.max_length)

    print("Generated Social Media Post Content:")
    for i, content in enumerate(post_content, 1):
        print(f"Version {i}:")
        print(f"{content}\n\n")


if __name__ == "__main__":
    main()
