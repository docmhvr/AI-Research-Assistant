import streamlit as st
import os
from models import clean_query, get_relevant_research, summarize_papers, make_paper_recommendation
from huggingface_hub import login
from dotenv import load_dotenv

# Set the title and description of the app
st.title("📄 AI Powered Research Expert")
st.write(
    "Enter your research goal, topic, or abstract below, and this app will provide research recommendations and relevant papers!"
)

# Ask the user for a question
query = st.text_area(
    "Enter your Research goal, topic or abstract!",
    placeholder="Can you give me a short summary or abstract?"
)

if query and st.button("Let's go!"):
    # Load Hugging Face token from environment variables
    load_dotenv()
    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

    print("Got token")

    if not huggingface_token:
        st.error("HUGGINGFACE_TOKEN environment variable not set.")
    else:
        # Log in to Hugging Face Hub
        login(huggingface_token)

        # Clean the query
        cleaned_query = clean_query(query)

        # Get relevant research papers
        relevant_papers, urls = get_relevant_research(cleaned_query)

        # Summarize the papers
        summaries = summarize_papers(relevant_papers)

        # Save session state
        st.session_state['relevant_papers'] = relevant_papers
        st.session_state['urls'] = urls
        st.session_state['summaries'] = summaries

# Display the research results
if 'relevant_papers' in st.session_state:
    relevant_papers = st.session_state['relevant_papers']
    urls = st.session_state['urls']
    summaries = st.session_state['summaries']

    # Create summaries and save to session state
    tab1, tab2 = st.tabs(['Relevant Papers', 'Assistant Recommendation'])

    with tab1:
        for paper, summary, url in zip(relevant_papers, summaries, urls):
            st.markdown(f'##### [{paper.title}]({url})')
            with st.expander(f'Summary of {paper.title}'):
                st.markdown(f'*{summary["output_text"]}*')

    with tab2:
        recommendation = make_paper_recommendation(relevant_papers, query, huggingface_token)
        st.session_state['recommendation'] = recommendation
        recommendation = st.session_state['recommendation']
        st.markdown(f'**{recommendation}**')
