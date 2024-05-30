import google.generativeai as genai
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import time
import requests

# Configure Google Generative AI
genai.configure(api_key="AIzaSyCywxL3BTdCMWt22qmZIxpOJVECFNbr02s")
model = genai.GenerativeModel('gemini-1.5-pro-latest')
model_video = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def yt_summarize(url):
    try:
        video_id = url.split("=")[1]
        yt = YouTube(url)
        transcript = yt.captions.get_by_language_code('en')
        if transcript:
            transcript_text = transcript.generate_srt_captions()
            return get_gemini_response(transcript_text)
        else:
            return "Sorry, the transcript for this video is not available. We are trying to improve."
    except Exception as e:
        return f"Error: {str(e)}"

def get_gemini_response_image(input, image):
    response = model.generate_content([input, image])
    return response.text

def get_gemini_response(input):
    response = model.generate_content([input])
    return response.text

def video_analysis(video_file_name):
    print(f"Uploading file...")
    video_file = genai.upload_file(path=video_file_name)
    print(f"Completed upload: {video_file.uri}")
    
    while video_file.state.name == "PROCESSING":
        print('.', end='')
        time.sleep(10)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError(video_file.state.name)
    
    prompt = "Describe this video."
    print("Making LLM inference request...")
    response = model_video.generate_content([prompt, video_file],
                                            request_options={"timeout": 600})
    return response.text

def imagegen(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}
    
    payload = {
        "inputs": prompt,
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
