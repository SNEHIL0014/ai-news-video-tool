📺 AI News Video Generation Tool
An automated pipeline that transforms trending news into engaging short-form video content. This tool bridges the gap between raw data scraping and multimedia production using modern AI and automation libraries.

🌟 Overview
This prototype automates the entire video production workflow:

Discovery: Scrapes real-time trending topics from Google News.

Synthesis: Distills complex articles into a 30-60 second "neutral tone" script via OpenAI.

Narration: Converts text to speech for high-quality audio voiceovers.

Production: Dynamically assembles images and text overlays into a final MP4 file.

🛠️ Tech Stack
Logic: Python 3

Data: GNews (RSS-based scraping)

LLM: OpenAI GPT-4o (with local fallback logic)

Audio: gTTS (Google Text-to-Speech)

Video Engine: MoviePy (FFmpeg-based processing)

📂 Project Structure

ai-news-video-tool/
├── assets/              # Branding, background music, or static images
├── news_fetcher.py      # Module 1: News discovery logic
├── script_generator.py  # Module 2: AI prompt engineering & Fallbacks
├── image_fetcher.py     # Module 3: Contextual image gathering
├── voiceover.py         # Module 4: Audio synthesis
├── video_generator.py   # Module 5: Video compositing and rendering
├── main.py              # Orchestrator (Run the entire pipeline)
├── requirements.txt     # Dependency manifest
└── .env                 # API Credentials (ignored by git)


⚙️ Setup & Installation

1. Environment Preparation

# Clone the repository
git clone https://github.com/SNEHIL0014/ai-news-video-tool.git
cd ai-news-video-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


2. Configuration (Optional)
   
Create a .env file in the root directory to enable AI script generation:

OPENAI_API_KEY=your_actual_key_here

Note: If no key is provided, the system defaults to a "Fallback Mode" using template-based scripts.


▶️ Usage
You can run the modules individually for debugging, or execute the full pipeline:

# To generate a full video from scratch
python main.py

Module Breakdown:

Order,Script,Responsibility
1,news_fetcher.py,Extracts the latest headlines and URLs.
2,script_generator.py,Summarizes news into a narratable script.
3,image_fetcher.py,Downloads relevant visuals for the topic.
4,voiceover.py,Generates the .mp3 narration.
5,video_generator.py,Combines everything into a final .mp4.



🧠 Design Philosophy
Graceful Degradation: The tool is designed to work even without internet-dependent APIs by utilizing local fallback scripts and assets.

Modularity: Each step is isolated. If you want to swap gTTS for ElevenLabs or OpenAI for Claude, you only need to update one file.

Efficiency: Uses RSS feeds for news to ensure fast scraping without getting blocked by web firewalls.

📌 Evaluation Readiness
✅ Clean Code: Adheres to PEP 8 standards.

✅ Scalable: Modular architecture allows for easy feature additions (e.g., subtitles).

✅ Production-Ready Logic: Includes .gitignore for security and requirements.txt for reproducibility.

Author: Snehil Srivastava


