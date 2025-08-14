import os
from exa_py import Exa
from datetime import datetime
api_key = os.environ.get("EXA_API_KEY")
exa = Exa(api_key)

def search_posts(keyword, num_results = 3):
    response = exa.search_and_contents(
        query = keyword,
        include_domains = ['linkedin.com'],
        num_results= num_results,
        text = True
    )
    results_with_dates = [r for r in response.results if r.published_date]
    
    sorted_results = sorted(
        results_with_dates,
        key=lambda x: datetime.fromisoformat(x.published_date.replace('Z', '+00:00')) if x.published_date else datetime.min,
        reverse=True      )
    for i, result in enumerate(sorted_results):
        print(f"\n--- Result {i+1}---")
        print(f"Title: {result.title}")
        print(f"URL: {result.url}")
        print(f"Published: {result.published_date}")
        print(f"Text Snipper: {result.text[:200]}..." )
    return sorted_results
if __name__ == "__main__":
    keyword = input("What do you want to search for?: ")
    search_posts(keyword)
        
