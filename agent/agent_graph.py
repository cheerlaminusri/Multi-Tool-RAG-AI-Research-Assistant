from langgraph.graph import StateGraph
from typing import TypedDict
from agent.tools import web_search

# Define state structure
class AgentState(TypedDict):
   query: str
   results: list

# Agent node
def agent_node(state: AgentState):
   query = state["query"]
   return {"query": query}

# Search node
def search_node(state: AgentState):
   query = state["query"]
   results = web_search(query)
   return {"results": results}

# Build graph
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("search", search_node)
graph.set_entry_point("agent")
graph.add_edge("agent", "search")
agent = graph.compile()