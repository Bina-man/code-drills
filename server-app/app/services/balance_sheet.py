import requests

def fetch_balance_sheet():
    url = 'http://localhost:3000/api.xro/2.0/Reports/BalanceSheet'
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
