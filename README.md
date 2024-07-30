# 📄 AI Powered Research Expert

A simple Streamlit app that provides research recommendations and relevant papers based on an entered research goal, topic, or abstract. The app uses open-source models from Hugging Face for language model inference.

The specified models from Hugging Face are used for the different tasks:
- **Chat Model**: `google/flan-t5-small`
- **Summarization**: `Falconsai/text_summarization`
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```

## Usage

1. Enter your research topic, goal, or abstract.
2. Click the "Let's go!" button to get research recommendations and relevant research papers.