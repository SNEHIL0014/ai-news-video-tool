import os
from moviepy import ImageClip, TextClip, AudioFileClip, CompositeVideoClip, ColorClip

os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"

def create_final_video(script_text, audio_path):
    print("🎬 Starting Video Assembly...")
    
    if not os.path.exists(audio_path):
        print(f"❌ Audio file NOT found at: {audio_path}")
        return None

    try:
        audio = AudioFileClip(audio_path)
        duration = audio.duration

        image_path = os.path.join(os.getcwd(), "assets", "background.jpg")
        
        if os.path.exists(image_path):
            background = ImageClip(image_path).with_duration(duration).resized((1280, 720))
        else:
            # Using light gray background so black text is visible if image fails
            background = ColorClip(size=(1280, 720), color=(240, 240, 240)).with_duration(duration)

        headline = TextClip(
            text=script_text,
            font_size=50,
            color='black',           # Set to Black
            method='caption',
            size=(1000, 600)
        ).with_duration(duration).with_position('center')

        video = CompositeVideoClip([background, headline])
        video = video.with_audio(audio)

        output_path = os.path.join(os.getcwd(), "news_final_video.mp4")
        
        video.write_videofile(
            output_path, 
            fps=24, 
            codec="libx264", 
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            write_logfile=False
        )
        
        return output_path

    except Exception as e:
        print(f"❌ Error during assembly: {e}")
        return None

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_file = os.path.join(current_dir, "assets", "voiceover.mp3")
    news_text = "India urges citizens to avoid non-essential travel to Iran due to rising tensions."
    
    create_final_video(news_text, audio_file)