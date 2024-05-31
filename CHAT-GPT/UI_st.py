import streamlit as st
from models import get_gemini_response, get_gemini_response_image, yt_summarize, imagegen
from PIL import Image
import io
import warnings

# Suppress DecompressionBombWarning
warnings.simplefilter('ignore', Image.DecompressionBombWarning)
Image.MAX_IMAGE_PIXELS = None

# Set page configuration
st.set_page_config(page_title="ARAT GPT", page_icon="✨", layout="wide")

# Custom CSS for enhanced styling with colors
st.markdown("""
    <style>
    body {
        background-color: #f5f6f8; /* background color */
    }
    .stApp {
        color: #31394d; /* Hugging Face text color */
        background-color: #f5f6f8; /* background color */
    }
    .stTitle {
        color: #BB377D; /* Neon green color for the title */
        text-align: center;
        margin-top: 20px;
        font-size: 36px;
    }
    .stAttribution {
        color: #858999; /* attribution color */
        text-align: center;
        margin-bottom: 20px;
        font-size: 14px;
    }
    .stButton > button {
        background-color: #00FFA3;
        color: #000080; /* Pink color for the text */
        border: none;
        border-radius: 25px;
        padding: 15px 25px;
        font-size: 16px;
        cursor: pointer;
        transition: transform 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #5C258D;
        color: #FFC837;
    }
    .stTextArea > div > textarea {
        background-color: #ffffff; /* Textarea background color */
        border: 1px solid #ced4da; /* Textarea border */
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        color: #495057; /* Textarea text color */
    }
    .stFileUploader > div > button {
        background-color: #09b1ba; /* Hugging Face upload button background color */
        color: #ffffff; /* Hugging Face upload button text color */
        border: none;
        border-radius: 25px;
        padding: 15px 25px;
        font-size: 16px;
        cursor: pointer;
        transition: transform 0.2s ease-in-out;
    }
    .stFileUploader > div > button:hover {
        background-color: #00777f; /* upload button hover background color */
    }
    .stImage {
        border-radius: 10px; /* Image border radius */
        border: 5px solid #ccc; /* Image border */
        margin: 50px auto; /* Center the image */
        max-width: 100%;
        height: auto;
    }
    .stMarkdown h2 {
        color: #31394d; /* Markdown h2 color */
    }
    .stMarkdown p {
        color: #31394d; /* Markdown p color */
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the application
st.markdown("<h1 class='stTitle'>✨ Welcome to ARAT AI-GPT ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='stAttribution'>made by @Chenna Kesava Reddy</p>", unsafe_allow_html=True)

# Define columns for buttons
col1, col2, col3 = st.columns(3)
with col1:
    yt_button = st.button("YouTube Video Summarization")
with col2:
    img_button = st.button("Upload an Image and Ask About It")
with col3:
    gen_button = st.button("Image Generation - Create Image of TEXT")

# Input area
input_prompt = st.text_area("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error opening the image: {e}")
        image = None
else:
    image = None

# Submit button
submit = st.button("Submit")

response = ''
yt = "https://www.youtube.com/watch?v=example"
keywords = ["create", "generate"]
contains_keyword = any(keyword in input_prompt.lower() for keyword in keywords)

if submit:
    if contains_keyword:
        st.write("Generating images...")
        columns = st.columns(4)
        variations = ["variation 1", "variation 2", "variation 3", "variation 4"]
        with st.container():
            for i in range(4):  # Generate 4 different types of images
                modified_prompt = f"{input_prompt} {variations[i]}"
                try:
                    response = imagegen(modified_prompt)
                    image = Image.open(io.BytesIO(response))
                    image = image.resize((15360, 8640))  # 12k Resize image quality
                    columns[i].image(image, caption=f"Generated Image {i+1}", use_column_width=True)
                except Exception as e:
                    st.error(f"Error generating image {i+1}: {e}")
        st.write("Generating articles on the images...")
        # Generate articles based on the generated images
        for i in range(4):
            modified_prompt = f"Write an article about the generated image {i+1}: {input_prompt}"
            try:
                article_response = get_gemini_response(modified_prompt)
                st.markdown(f"## Article for Generated Image {i+1}:")
                st.write(article_response)
            except Exception as e:
                st.error(f"Error generating article for image {i+1}: {e}")
    elif yt in input_prompt:
        try:
            response = yt_summarize(input_prompt)
            st.markdown("### Key Points from the Video:")
            st.write(response)
        except Exception as e:
            st.error(f"Error summarizing YouTube video: {e}")
    else:
        try:
            if image:
                st.write("Generating text...")
                response = get_gemini_response_image(input_prompt, image)
            else:
                st.write("Generating text...")
                response = get_gemini_response(input_prompt)
            st.write(response)
        except Exception as e:
            st.error(f"Error generating text: {e}")

# Add refresh button
if st.button("Refresh"):
    st.experimental_rerun()
