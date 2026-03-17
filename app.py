import streamlit as st
from agent.agent_graph import agent

st.title("AI Research Assistant")

# User input
query = st.text_input("Ask a Question")

if query:
    # Run the agent with the query
    response = agent.invoke({"query": query})

    # Display response
    st.write(response)