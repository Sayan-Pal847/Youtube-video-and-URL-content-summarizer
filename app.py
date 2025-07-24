import streamlit as st
import validators

from langchain_community.document_loaders.url import UnstructuredURLLoader
from custom_youtube_loader import YoutubeLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain


def main():
    #  App Title and Description
    st.title("📽️ YouTube & 🌐 Website Summarizer")
    st.subheader("⚡ Get structured summaries from any YouTube video or web article!")

    # Sidebar Configuration
    with st.sidebar:
        st.header("🔧 Configuration")
        groq_api_key = st.text_input(" Enter your Groq API Key", type="password")
        model = st.selectbox(
            " Choose a model",
            ["gemma2-9b-it", "llama-3.1-8b-instant"]
        )

    #  URL Input
    url = st.text_input(" Enter the URL of a YouTube video or Website")

    #  Summarize Button
    if st.button(" Summarize the content"):
        #  Input Validation
        if not groq_api_key or not model:
            st.error(" Please provide a valid Groq API key and select a model.")
            return

        if not url or not validators.url(url):
            st.error(" Please enter a valid URL.")
            return

        #  Load Content and Process
        try:
            with st.spinner(" Loading and analyzing content..."):
                if "youtube.com" in url or "youtu.be" in url:
                    loader = YoutubeLoader.from_youtube_url(
                        url, add_video_info=False, language=["en"]
                    )
                    docs = loader.load()
                    if not docs:
                        st.warning("No transcript found. Transcripts might be disabled for this video.")
                        return
                else:
                    loader = UnstructuredURLLoader(urls=[url])
                    docs = loader.load()

                llm = ChatGroq(groq_api_key=groq_api_key, model_name=model)

            st.success(" Content loaded successfully!")

            #  Define Prompt
            prompt_template = """
            Summarize the content of the following document in a structured way:
            Content: {context}
            """
            prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

            #  Create Chain
            chain = create_stuff_documents_chain(llm, prompt)
            result = chain.invoke({"context": docs})

            #  Show Summary
            st.markdown(" Summary:")
            st.write(result)

        except Exception as e:
            st.error(f" An error occurred: {e}")


#  Run the App
if __name__ == "__main__":
    main()
