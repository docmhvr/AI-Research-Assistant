from transformers import pipeline
import arxiv
from tqdm import tqdm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

def clean_query(query):
    return query.strip()

def get_relevant_research(cleaned_query):
    search = arxiv.Search(
        query=cleaned_query,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = [result for result in search.results()]
    return results, [result.pdf_url for result in results]

def summarize_papers(papers):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    summaries = []
    for paper in tqdm(papers):
        summary = summarizer(paper.summary, max_length=200, min_length=100, do_sample=False)[0]['summary_text']
        summaries.append({"output_text": summary})
    print(summaries)
    return summaries

def make_paper_recommendation(relevant_papers, query, huggingface_token):
    # Create a detailed prompt to generate a thorough recommendation
    prompt_template = """
    Based on the following research papers and their relevance to your query:
    {relevant_papers}
    Provide a detailed recommendation based on the query: '{query}' including explanations and potential next steps for research.
    """

    relevant_papers_list = "\n".join([f"{i+1}. {paper.title}" for i, paper in enumerate(relevant_papers)])
    
    # Initialize the HuggingFaceHub model

    llm = Ollama(model = "llama3")

    # Create the ChatPromptTemplate
    template = ChatPromptTemplate.from_template(prompt_template)

    # Initialize the LLMChain with the prompt and model
    chain = template | llm | StrOutputParser()

    # Run the chain with the formatted summaries and query
    response = chain.invoke({"relevant_papers":relevant_papers_list, "query":query})
    print(response)
    return response
    # recommedation = response
    # recommendation = response["text"]
    # print(recommendation)

    # return recommendation