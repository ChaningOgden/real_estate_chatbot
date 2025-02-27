import requests

def search_properties(location, max_price, min_acres):
    api_url = f"https://realestate-api.com/search?location={location}&max_price={max_price}&min_acres={min_acres}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()["properties"]
        else:
            return []
    except:
        return []