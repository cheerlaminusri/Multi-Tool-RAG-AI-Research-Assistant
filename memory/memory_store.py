memory = []

def save_interaction(q, a):
    # Store question and answer
    memory.append({"q": q, "a": a})

def get_memory():
    # Return last 5 interactions
    return memory[-5:]