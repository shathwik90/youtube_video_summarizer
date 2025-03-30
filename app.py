from flask import Flask, request, jsonify, render_template
import re
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__, template_folder="templates")


class YouTubeTranscriptAgent:
    """Handles YouTube transcript extraction."""

    def __init__(self):
        self.transcript_api = YouTubeTranscriptApi()

    def get_video_id(self, url):
        """
        Extracts the YouTube video ID from a given URL.
        Returns None if the URL is invalid.
        """
        match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
        return match.group(1) if match else None

    def fetch_transcript(self, url):
        """
        Fetches the transcript for a given YouTube video URL.
        Returns the transcript text or an error message.
        """
        video_id = self.get_video_id(url)
        if not video_id:
            return None, "Invalid YouTube URL"

        try:
            transcript = self.transcript_api.get_transcript(video_id)
            text = " ".join([entry["text"] for entry in transcript])
            return text, None
        except Exception as e:
            return None, f"Error fetching transcript: {str(e)}"


class SummaryGenerator:
    """Handles summary generation using the Gemini API."""

    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set.")
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash"

    def generate_summary(self, script):
        """
        Generates a summary for the given script using the Gemini API.
        Returns the summary as a string in Markdown format.
        """
        prompt_text = (
            "Provide a detailed summary of the following video in Markdown format. "
            "Include every key point, elaborate on important ideas, and explain the context thoroughly. "
            "Ensure the summary is structured and easy to read:\n"
            + script
            + "\n\nHere's a detailed summary of the video, formatted in Markdown:"
        )

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt_text),
                ],
            )
        ]

        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
        )

        summary = "\n"
        try:
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=contents,
                config=generate_content_config,
            ):
                summary += chunk.text
            return summary
        except Exception as e:
            return f"Error generating summary: {str(e)}"


# Serve the frontend
@app.route("/")
def home():
    """Serve the index.html file."""
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    """API endpoint to summarize a YouTube video."""
    data = request.json
    youtube_url = data.get("youtube_url")

    if not youtube_url:
        return jsonify({"error": "YouTube URL is required"}), 400

    agent = YouTubeTranscriptAgent()
    transcript, error = agent.fetch_transcript(youtube_url)

    if error:
        return jsonify({"error": error}), 400

    generator = SummaryGenerator()
    summary = generator.generate_summary(transcript)

    # Return the summary in Markdown format
    return jsonify({"summary": summary, "format": "markdown"})


if __name__ == "__main__":
    app.run(debug=True)
