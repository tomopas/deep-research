import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
import re

# Download necessary NLTK data
nltk.download('punkt')

# Step 1: Perform a DuckDuckGo search
def search_duckduckgo(query, num_results=5):
    print(f"\n🔍 Searching DuckDuckGo for: '{query}'...\n")
    results = []
    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=num_results):
            results.append(result)
    return results

# Step 2: Fetch content from a URL
def fetch_page_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract only the meaningful text (ignoring scripts and styles)
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()
        # Clean up whitespace and newlines
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None

# Step 3: Summarize text using NLP
def summarize_text(text, num_sentences=5):
    text = "Summarize the following text: " + text
    return useAI(text)

# Step 4: Perform the deep research pipeline
def deep_research(query, num_results=5):
    print("\n🚀 Starting Deep Research...\n")
    # Step 0: Preprocess the query and ask for more information
    # text = useAI("Do you need more information on the following query to return a suitable and detailed report about the topic? Answer No for no or Yes and the needed information for yes. Query: " + query)
    # if  text == "No":
    #     print("❌ No additional information")
    # else:
    #     print(text)
    #     query = query + input("Enter the needed information: ")

    # Step 1: Use AI to make a plan
    # plan = useAI("Create a research plan for the following query, seperate each step by |. Query: " + query + " Keep in mind to seperate each step by |")
    # plan = plan.split("|")


    # search = []
    # for step in plan:
    #     print("Step: " + step)
    #     search_results = search_duckduckgo(step, num_results)
    #     if not search_results:
    #         print("❌ No results found.")
    #     else:
    #         search.append(search_results)

    
    # Step 2: Search DuckDuckGo
    search_results = search_duckduckgo(query, num_results)
    if not search_results:
        print("❌ No results found.")
        return
    
    all_content = []
    
    for i, result in enumerate(search_results):
        print(f"{i + 1}. {result['title']}")
        print(f"   URL: {result['href']}")
        print(f"   Snippet: {result['body']}\n")

        # Step 2: Fetch and process page content
        print(f"🌐 Fetching content from {result['href']}...")
        content = fetch_page_content(result['href'])
        if content:
            print("✅ Content fetched successfully.")
            all_content.append(content)
        else:
            print("⚠️ Failed to fetch content.\n")

    # Step 3: Summarize the content
    if all_content:
        print("\n📝 Summarizing content...\n")
        combined_text = ' '.join(all_content)
        print("Text found: " + combined_text)
        summary = summarize_text(combined_text, num_sentences=10)
        print("\n📢 RESEARCH SUMMARY:\n")
        print(summary)
    
    print("\n✅ Research Completed!")

def useAI(text, model="tinyllama:latest"):
    import ollama
    # Generate a response
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': text}])
    response = str(response.message.content)
    return response

# Step 5: Run the program
if __name__ == "__main__":
    query = input("Enter your research topic: ")
    deep_research(query)
