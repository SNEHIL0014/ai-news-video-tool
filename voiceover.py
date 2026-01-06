import os
from gtts import gTTS

def generate_voiceover(script_text):
    # This gets the absolute path of the folder WHERE THIS SCRIPT LIVES
    # This is the industry standard for path resolution.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # We create a folder called 'assets' inside your project folder
    output_dir = os.path.join(base_dir, "assets")
    
    # Create the folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "voiceover.mp3")

    print(f"DEBUG: Script location: {base_dir}")
    print(f"DEBUG: Saving to: {output_file}")

    tts = gTTS(text=script_text, lang='en')
    tts.save(output_file)
    
    return output_file

if __name__ == "__main__":
    test_script = "India urges citizens to avoid non-essential travel to Iran due to rising tensions."
    path = generate_voiceover(test_script)
    print(f"\nSUCCESS! File saved at: {path}")
