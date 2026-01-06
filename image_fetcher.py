import os
import requests

def fetch_background_image(query="world news background"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "assets")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "background.jpg")
    
    # 1. PEXELS API KEY (Replace with yours)
    PEXELS_API_KEY = "Lf34AiKQzTX4CEEE47EFscSeJjLfJvitutWut1faksTvJXrLkxPug3Xh"
    
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"

    print(f"🔍 Searching Pexels for: {query}...")
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if data.get("photos"):
            image_url = data["photos"][0]["src"]["landscape"]
            img_data = requests.get(image_url).content
            with open(output_file, "wb") as f:
                f.write(img_data)
            print(f"✅ Pexels image saved!")
            return output_file
        else:
            raise Exception("No photos found in API response")

    except Exception as e:
        print(f"⚠️ API Method failed ({e}). Using fallback image...")
        fallback_url = "https://images.pexels.com/photos/395196/pexels-photo-395196.jpeg?auto=compress&cs=tinysrgb&w=1280&h=720&dpr=1"
        img_data = requests.get(fallback_url).content
        with open(output_file, "wb") as f:
            f.write(img_data)
        print(f"✅ Fallback news image saved to: {output_file}")
        return output_file

if __name__ == "__main__":
    fetch_background_image()