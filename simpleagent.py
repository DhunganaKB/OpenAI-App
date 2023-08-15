import streamlit as st
from streamlit_chat import message

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool  
from langchain.llms import OpenAI

st.title('Simple math chatbot')

#query = st.text_input("Query: ", key="input")

#query = st.text_input("write your question")

query = st.text_input("Write a simple math question: ", key="input")


llm = OpenAI(temperature=0)
agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True
)
# agent_executor.run('Calculate the square root of the factorial of 20 \
# and display it with 4 decimal points')
print(query)
if not query:
    print('yes None')

if query:
    output=agent_executor.run(query)
    st.write(output)
    st.write('*************')
    st.write("Thank you for using it")

