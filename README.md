# AI News Video Generation Tool

This project is a prototype that automatically generates short news videos
by fetching trending news, creating a script, generating voiceover audio,
and assembling a video using images.

## Features
- Fetches trending news (Google News RSS)
- Generates short news scripts (AI-based with fallback)
- Converts script to voiceover (gTTS)
- Builds 30–60 second videos using MoviePy

## Setup Instructions

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Create a `.env` file using `.env.example`
5. Run the pipeline scripts from `src/`

## Notes
- Generated output files are not committed to GitHub
- API keys are managed securely using environment variables
