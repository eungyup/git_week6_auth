
import requests
import secrets

# NEWSAPI_KEY = '3819868a3c9b4d50a2a4bcef01885bf5' 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "new hampshire",
    # "country": "us",
    "apiKey": secrets.NEWSAPI_KEY
}


response = requests.get(base_url, params)
result = response.json()
print(f"\nresult: {result}\n\n")
#(my)
result_source = result['articles']
print(f"result_source: {result_source}\n\n")

# for a_dic in result_source:
#     title = a_dic['title']
#     print(f"{title}")

for a_dict in result_source:
    print(a_dict['title'], "-", a_dict["source"]["name"])