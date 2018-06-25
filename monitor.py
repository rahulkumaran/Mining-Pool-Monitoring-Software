import json
import requests as r
import time
class MonitorPool:
	def __init__(self):
		self.url = "http://107.173.118.210/api/"

	def send_request(self, url):
		return r.get(url)

	def get_json(self, req_data):
		return req_data.json()

	def get_stats(self, choice):
		url = ""
		if(choice == 1):
			url += self.url + "stats"
		elif(choice == 2):
			url += self.url + "pool_stats"
		elif(choice == 3):
			url += self.url + "live_stats"
		elif(choice == 4):
			url += self.url + "getblocksstats"
		else:
			print("Wrong option entered!")
			return

		req_data = self.send_request(url)
		json_obj = self.get_json(req_data)

		return json_obj



if(__name__=="__main__"):
	while(True):
		mp = MonitorPool()
		d = mp.get_stats(1)

		print(json.dumps(d, indent = 2))

		time.sleep(60)
