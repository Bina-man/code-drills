import requests
from app.config.env import get_base_url

def fetch_balance_sheet():
    base_url = get_base_url()
    url = f'{base_url}/api.xro/2.0/Reports/BalanceSheet'
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()
        data = response_data.get('Reports')
        if data is None:
            return {"error": "No Reports data found"}
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
