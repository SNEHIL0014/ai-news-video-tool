import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def fallback_script(title, description):
    return (
        f"{title}. {description} "
        "Officials have advised citizens to remain alert and follow official guidance. "
        "The situation is being closely monitored, and further updates will be shared."
    )

def generate_news_script(title, description):

    # ✅ CASE 1: No API key → fallback ONLY
    if not api_key:
        print("⚠️ OpenAI API key not found. Using fallback script.")
        return fallback_script(title, description)

    # ✅ CASE 2: API key exists → try OpenAI safely
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a professional news anchor.
Write a clear, neutral, factual news script for a 30–60 second video.
5–7 short sentences max.

Title: {title}
Description: {description}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"⚠️ OpenAI failed ({e}). Using fallback script.")
        return fallback_script(title, description)

if __name__ == "__main__":
    print("SCRIPT FILE IS RUNNING")

    title = "India urges citizens to avoid non-essential travel to Iran"
    description = "India has advised its citizens to avoid non-essential travel to Iran amid rising tensions."

    script = generate_news_script(title, description)

    print("\nGenerated News Script:\n")
    print(script)
