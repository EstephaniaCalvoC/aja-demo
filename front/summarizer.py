from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def call_summarizer(opinion_url: str) -> str:
    loader = PyPDFLoader(opinion_url)
    loaded_pages = loader.lazy_load()
    text = ""
    for page in loaded_pages:
        text += page.page_content

    if text:
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        result = llm.invoke(
            "\
                            Summarize the following legal case document, \
                            highlighting the key facts, legal issues, \
                            and relevant precedents. Use Markdown to format the summary. \n"
            + text
        )
        return result.content


if __name__ == "__main__":
    print(call_summarizer("https://www.supremecourt.gov/opinions/23pdf/22-1078_4gci.pdf"))
