import requests
import time
import logging
import os
from config import API_KEY, PRICE_GTE, PRICE_LTE, ALERT_TIMES

logging.basicConfig(level=logging.INFO)

def get_btc_price_call():
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

	if response.status_code != 200:
		logging.error(f"API returned status code {response.status_code}")
		logging.info(f"Raw response: {response.json()}")
		exit()
	return response.json()


def get_btc_price():
	response = get_btc_price_call()
	response_time = response['data']['timestamp']
	response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response_time))
	response['data']['timestamp'] = response_time
	logging.info(response['data'])
	return response['data']['price']

def trigger_alert_notification(times=ALERT_TIMES):
	for i in range(times):
		os.system("say bit coin price alert!")
		time.sleep(3)

loop = True
while loop:
	btc_price = float(get_btc_price())
	if btc_price >= PRICE_GTE:
		logging.info(f"BTC price is {btc_price}, which is greater than or equal to {PRICE_GTE}")
		trigger_alert_notification()
	if btc_price <= PRICE_LTE:
		logging.info(f"BTC price is {btc_price}, which is less than or equal to {PRICE_LTE}")
		trigger_alert_notification()
	else:
		time.sleep(600)

