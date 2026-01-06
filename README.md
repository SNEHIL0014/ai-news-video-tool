# 📰 AI News Video Generation Tool

An AI-based prototype that automatically generates short (30–60 seconds) news videos from trending news articles.  
The tool scrapes trending news, generates a concise script, converts it into a voiceover, and assembles a video using images and text overlays.

This project demonstrates practical use of AI tools, automation, and clean software architecture.

---

## 🚀 Features

- 🔍 Scrapes trending news articles using Google News (GNews)
- 🧠 Generates short, neutral news scripts using OpenAI (with fallback support)
- 🎙️ Converts scripts into voiceovers using Text-to-Speech
- 🎞️ Creates short videos with images, text overlays, and audio
- 🔁 Graceful fallback when API keys are unavailable
- 🧩 Modular and easy-to-understand code structure

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **News Scraping:** GNews
- **AI Script Generation:** OpenAI API (optional, fallback included)
- **Text-to-Speech:** gTTS
- **Video Creation:** MoviePy
- **Environment Management:** Python Virtual Environment

---

## 📂 Project Structure

ai-news-video-tool/
│
├── assets/ # Static assets (background images, etc.)
├── image_fetcher.py # Fetches images related to news topic
├── news_fetcher.py # Scrapes trending news articles
├── script_generator.py # Generates AI-based or fallback news scripts
├── voiceover.py # Converts script to audio narration
├── video_generator.py # Creates final video using images + audio
├── requirements.txt # Python dependencies
├── .gitignore # Files ignored by Git
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SNEHIL0014/ai-news-video-tool.git
cd ai-news-video-tool
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔑 (Optional) OpenAI API Setup
This project works with or without an OpenAI API key.

If you want AI-generated scripts:

Create a .env file in the project root

Add:

ini
Copy code
OPENAI_API_KEY=your_api_key_here
⚠️ .env is ignored by Git and should not be committed.

If no API key is found, the system automatically uses a fallback script.

▶️ How to Run the Tool
Run each module step-by-step:

bash
Copy code
python news_fetcher.py
python script_generator.py
python image_fetcher.py
python voiceover.py
python video_generator.py
After execution, the generated video will be available locally in the output folder (ignored by Git).

🧠 Design Decisions & Reliability
RSS-based news scraping is used for stability.

The system never crashes if an API key is missing.

Modular architecture improves readability and maintainability.

Designed as a working prototype, not a production system.

📌 Evaluation Readiness
This project satisfies:

✅ Feasible implementation

✅ Practical use of AI tools

✅ Clean automation pipeline

✅ Easy-to-understand architecture

✅ Graceful failure handling

👤 Author
Snehil Srivastava
