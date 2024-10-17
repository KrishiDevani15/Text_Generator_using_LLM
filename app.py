import streamlit as st
from langchain.prompts.prompt import PromptTemplate  # type: ignore
from langchain_ollama import ChatOllama  # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore

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
