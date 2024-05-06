import requests
import time
import logging
from config import API_KEY

logging.basicConfig(level=logging.INFO)

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

try:
	response = requests.get(url, headers=headers, params=querystring)
except requests.exceptions.RequestException as e:
	logging.error(e)
	exit()
response = response.json()
logging.info(f"Raw response: {response}")

response_time = response['data']['timestamp']
response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response_time))
response['data']['timestamp'] = response_time
logging.info(response)
