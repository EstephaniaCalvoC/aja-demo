import streamlit as st
from cases import search_cases
from summarizer import call_summarizer


def sumarize_opinion():

    summary = ""
    with st.spinner("We are on it..."):
        try:
            summary = call_summarizer(str(st.session_state.opnion_url))
        except Exception as e:
            st.error("It's not possible get the summary at the moment. Please, try again later.")

    if summary:
        st.write("## Case's Summary")
        st.write(f"[**Opinion document**]({st.session_state.opnion_url})")
        st.write(summary)


def show_cases():
    if not st.session_state.cases:
        return
    for _, case in st.session_state.cases.items():
        with st.expander(case.name):
            st.write(f"**Court:** {case.court}")
            st.write(f"**Docket number:** {case.docket_number}")

            opnion_url = case.download_url

            if opnion_url:
                st.markdown(f"[Opinion]({opnion_url})")
                st.session_state.opnion_url = opnion_url

                st.button("Summarize", key=str(case.case_id), on_click=sumarize_opinion)


st.set_page_config(page_title="AJA Demo", page_icon=":robot:")
st.title("AI Judge Assistant Demo")

description = """
*AI-powered tool to summarize legal cases, \
helping judges quickly understand the key points of a case.*\
"""
st.markdown(description)

if "cases" not in st.session_state:
    st.session_state.cases = list()

if "opinion_url" not in st.session_state:
    st.session_state.opinion_url = None

"""## Case searcher"""
search_query = st.text_input("searcher", help="e.g. Party 1 vs. Party 2 2024 Court", label_visibility="hidden")

search_button = st.button("Search")

if search_button:
    try:
        # st.session_state.cases.clear()
        cases = search_cases(search_query)
    except Exception as e:
        st.error("Our searcher is present problems. Please try again later")

    if not cases:
        st.info("No cases found")
    else:
        st.session_state.cases = cases.get_all_cases()
        show_cases()
