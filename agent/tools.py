from duckduckgo_search import DDGS

def web_search(query):

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=5)

        for r in search_results:
            print(r)  # DEBUG

            # Safe extraction
            if "body" in r:
                results.append(r["body"])
            elif "snippet" in r:
                results.append(r["snippet"])
            else:
                results.append(str(r))

    return results