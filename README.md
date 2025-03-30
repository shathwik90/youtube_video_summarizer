# YouTube Video Summarizer

## Description

This project is a **YouTube Video Summarizer** that extracts transcripts from YouTube videos and generates a structured summary using the **Gemini API**. The application is built using Flask for the backend and a simple HTML/JavaScript frontend to interact with the API.

## Features

- Extracts video transcripts from YouTube URLs.
- Generates a detailed Markdown-formatted summary using **Google Gemini API**.
- User-friendly web interface.

## Technologies Used

- **Backend:** Flask, Python
- **Frontend:** HTML, JavaScript (with Marked.js for Markdown rendering)
- **APIs:** YouTube Transcript API, Google Gemini API
- **Environment Variables:** dotenv

## Installation

### Prerequisites

Ensure you have **Python 3.7+** and **pip** installed on your system.

### Steps to Set Up

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-repo/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the root directory and add the following:
     ```sh
     GEMINI_API_KEY=your_google_gemini_api_key
     PORT=5000  # Optional: Change if needed
     ```

5. **Run the Flask application:**

   ```sh
   python app.py
   ```

6. **Access the application:**
   Open your browser and go to `http://localhost:5000/`.

## Usage

1. Enter a **YouTube video URL** in the input field.
2. Click the **"Generate Summary"** button.
3. The application will extract the transcript and generate a structured summary.
4. The summary will be displayed in **Markdown format**.

## File Structure

```
📂 youtube-video-summarizer
├── 📂 templates
│   ├── index.html  # Frontend UI
├── app.py  # Main Flask backend
├── requirements.txt  # Dependencies
├── .env.example  # Environment variables template
```

## Dependencies

The required dependencies are listed in `requirements.txt`:

```
Flask==2.3.2
python-dotenv==1.0.0
youtube-transcript-api==0.6.0
google-genai==0.3.0
```

## API Endpoints

### 1. Home Page

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Serves the web application frontend.

### 2. Summarize Video

- **Endpoint:** `/summarize`
- **Method:** `POST`
- **Request Body:**
  ```json
  { "youtube_url": "<YouTube Video URL>" }
  ```
- **Response:**
  ```json
  {
    "summary": "<Generated Summary>",
    "format": "markdown"
  }
  ```

## Future Enhancements

- Add support for **multiple languages**.
- Implement **authentication for API access**.
- Improve **summary customization options**.

## License

This project is licensed under the **MIT License**.

## Author

Developed by **Shathwik Reddy Duvvuru**
