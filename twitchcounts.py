import requests

# Twitch TV 'streams' end point.
BASE_URL = 'https://api.twitch.tv/kraken/streams'

def crawl(url, params):
	r = requests.get(url, params=params, timeout=30)

	if r.status_code == 200:
		js = r.json()
	if '_total' in js:
		print("There are {0} streamers doing it live.".format(js['_total']))


def main():
	query_params = {
		'limit': 1,
		'stream_type': 'live'
	}
	crawl(BASE_URL, query_params)


if __name__ == '__main__':
	main()
