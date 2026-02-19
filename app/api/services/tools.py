from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

# Web search tool
search = DuckDuckGoSearchRun()

web_search = Tool(
    name="Web_Search",
    func=search.run,
    description="A web browsing tool to search the internet for information.",
)

# Wikipedia search tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=221)  # type: ignore
wp_search = WikipediaQueryRun(api_wrapper=api_wrapper)


wiki_search = Tool(
    name="Wikipedia_Search",
    func=wp_search.run,
    description="Searches Wikipedia for factual information.",
)
