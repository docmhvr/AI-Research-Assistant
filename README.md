# 📄 AI Powered Research Expert

A Streamlit app that provides research recommendations and relevant papers with summaries based on an entered research goal, topic, or abstract. The app uses open-source models run locally using Ollama for text generation and hugging face inference for text summarization tasks.

The specified models from Hugging Face are used for the different tasks:
- **Chat Model**: `meta/llama3`
- **Summarization**: `Falconsai/text_summarization`

### How to run it on your own machine

1. Clone the repository

   ```
   $ git clone 
   ```

2. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

3. Create env file and add your hugging face api

   ```
   $ HUGGINGFACE_TOKEN = "your_api_key"
   ```

4. Run the app

   ```
   $ streamlit run app.py
   ```

## Usage

1. Enter your research topic, goal, or abstract.
2. Click the "Let's go!" button to get research recommendations and relevant research papers and their summaries.

## Demo
![Demo](Demo/Screenshot%20(229).png)
Make sure you have Ollama installed on your device, with loaded Llama3 model or change as per your need
