import streamlit as st
from langchain.prompts.prompt import PromptTemplate  # type: ignore
from langchain_ollama import ChatOllama  # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore


st.set_page_config(
    page_title="Text Genarator",
    page_icon="favicon.ico",  # Replace with your favicon path
    layout="centered"  # or "wide" depending on your preference
)


st.title("Text Generation App 🤖✍️")

user_prompt = st.text_area("Enter your prompt:",height=300)
if st.button("Generate Text"):
    if user_prompt:
        
        text_template = """
        Based on the following prompt: {prompt}, generate a coherent and engaging piece of text.
        """

        text_template_prompt = PromptTemplate(input_variable = ['prompt'],template=text_template)

        llm = ChatOllama(temprature = 1,model = "llama3.1")

        chain = text_template_prompt | llm | StrOutputParser()

        result = chain.invoke(input={"prompt":user_prompt})

        # Display the result
        st.subheader("Generated Text:")
        st.write(result)
        st.balloons()
    else:
        st.warning("Please enter a prompt to generate text.")

st.markdown(
    """
    <footer style="text-align: center; margin-top: 20px; font-size: 14px;">
        <a href="https://whoiskrishi.vercel.app/" target="_blank" style="text-decoration: none; color: white;">
            <br>
            © 2024 @whoisKrishi — KRISHI DEVANI
        </a>
        
    </footer>
    """,
    unsafe_allow_html=True
)
