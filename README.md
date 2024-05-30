# [✨ ARAT AI-GPT ✨](https://arat-ai-gpt.streamlit.app/)
 

✨ Welcome to ARAT AI-GPT ✨, a Streamlit-based application that provides various AI functionalities such as YouTube video summarization, image-based Q&A, and text-to-image generation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](Contributing)

## Features

- **YouTube Video Summarization:** Summarize key points from a YouTube video.
- **Upload an Image and Ask About It:** Upload an image and get responses based on the image content.
- **Image Generation:** Generate images from text prompts.
- 
- ![Screenshot (157)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/bb18584a-a6bd-4038-8404-801c496ee5e2)
- ![Screenshot (158)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/5b530584-79bf-4522-bdc4-69cd9e74c1be)
- ![Screenshot (159)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/37b28e9e-f837-47e7-a093-c1370c228a92)
- ![Screenshot (160)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/e5a01fec-2a10-4f69-86b4-70ffed453603)
- ![Screenshot (161)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/4a0a75f4-6294-436f-aa87-3ce46111d847)
- ![Screenshot (162)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/0dbb8ec9-aa5e-4062-96bb-8109350dcf71)
- ![Screenshot (163)](https://github.com/KesavaAI/ARAT-AI-GPT/assets/144814421/f2a456ba-d7c1-40b2-a818-b3116e2913fb)

## Installation

To install and run this application locally, follow these steps:

### 1. Clone The Repository

First, clone the repository to your local machine using the following command:
  
    git clone https://github.com/your-username/your-repository.git
    cd your-repository


### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:
  
    python -m venv venv
    

### 3. Activate the Virtual Environment
Activate the virtual environment using the appropriate command for your operating system:
  ##### • On Windows:
     .\venv\Scripts\activate
        
  ##### • On Unix or MacOS:     
     source venv/bin/activate
        
### 4. Install Dependencies 
Install the required dependencies from the requirements.txt file:

    pip install -r requirements.txt

## Usage

After installing the dependencies, you can run the application using Streamlit: 
    
    streamlit run app.py

This will start the application and open it in your default web browser.

## Application Interface
Upon launching, you will see the following options:

#### 1. YouTube Video Summarization:

    •	Click on "YouTube Video Summarization".
    •	Enter the URL of the YouTube video you want to summarize.
    •	Click "Submit" to get the summarized key points.
   
#### 2. Upload an Image and Ask About It:

    •	Click on "Upload an Image and Ask About It".
    •	Upload an image file.
    •	Enter your question related to the image.
    •	Click "Submit" to get the response.
   
#### 3. Image Generation - Create Image of TEXT:

    •	Click on "Image Generation - Create Image of TEXT".
    •	Enter a text prompt for the image you want to generate.
    •	Click "Submit" to generate the image.
   
## Troubleshooting
If you encounter any issues during installation or running the application, refer to the following troubleshooting steps:

### Virtual Environment Creation Issue

#### 1. Ensure Python is Installed:

Verify that Python is installed and added to your system PATH:

    python --version

#### 2. Check Python Path:

Confirm the Python executable path is correct:

    where python

#### 3. Create Virtual Environment Manually:

Create the virtual environment manually if necessary:

    python -m venv path_to_your_project/venv

#### 4. Activate the Virtual Environment:

Activate the virtual environment using the appropriate command for your operating system:

##### •	On Windows:

    path_to_your_project\venv\Scripts\activate

##### •	On Unix or MacOS:

    source path_to_your_project/venv/bin/activate

#### Install Dependencies:

Install the required dependencies:

    pip install -r requirements.txt

#### Run the Application:

Start the Streamlit application:

    streamlit run UI_st.py

## Image Generation Issues

If you encounter issues with image generation, such as the ' _DecompressionBombError_ ', ensure that your image dimensions are within safe limits. Modify the image size or resolution as needed.

## Contributing

We welcome contributions from everyone, and we are grateful for every contribution made to this project, whether it's big or small.

If you're interested in helping out, here's how you can contribute:

1. **Fork the repository**: Click on the 'Fork' button at the top right corner of this page to create your own copy of this project.

2. **Clone the repository**: Once you have forked the repo, you can clone it to your local machine and make changes.

        git clone https://github.com/your-username/your-repo-name.git

3. **Create a new branch**: It's important to branch the repository so that you can manage the workflow, isolate your code, and control what features get added to the main project.

    ```bash
    git checkout -b your-new-branch-name
    ```

4. **Make your changes**: Make the necessary changes to the project and commit them. We encourage you to write clear and descriptive commit messages.

    ```bash
    git commit -m "Add a brief description of your changes"
    ```

5. **Push your changes**: After you have committed your changes, you need to push the changes back to your fork on GitHub.

    ```bash
    git push origin your-new-branch-name
    ```

6. **Submit a pull request**: Go to the 'Pull requests' tab in the original repository and click on 'New pull request'. Select your fork and branch, then submit your request with a clear title and description.

7. **Code review**: Once your pull request is submitted, it will be reviewed by the maintainers. They may suggest some changes or improvements before merging your code.

Please ensure that you read through the [CONTRIBUTING.md](https://contributing.md/example/) file for more detailed information on how to contribute.

Thank you for your contributions, and we look forward to seeing your innovative ideas and improvements to the project!


