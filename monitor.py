import json
import requests as r
import time
from datetime import datetime


class MonitorPool:
	def __init__(self, choice=1):
		self.url = "http://107.173.118.210/api/"
		self.choice = choice

	def send_request(self, url):
		return r.get(url)

	def get_json(self, req_data):
		return req_data.json()

	def get_stats_json(self):
		url = ""
		if(self.choice == 1):
			url += self.url + "stats"
		elif(self.choice == 2):
			url += self.url + "pool_stats"
		elif(self.choice == 3):
			url += self.url + "live_stats"
		elif(self.choice == 4):
			url += self.url + "getblocksstats"
		else:
			print("Wrong option entered!")
			return

		req_data = self.send_request(url)
		json_obj = self.get_json(req_data)

		return json_obj


	def get_stats_data(self):
		stats_json= self.get_stats_json()
		if(self.choice==1):
			print("Total Paid:",stats_json["pools"]["litecoin"]["poolStats"]["totalPaid"])
			print("Valid Blocks:",stats_json["pools"]["litecoin"]["poolStats"]["validBlocks"])
			print("Orphaned:",stats_json["pools"]["litecoin"]["blocks"]["orphaned"])

			print("Confirmed:",stats_json["pools"]["litecoin"]["blocks"]["confirmed"])

			print("Pending:",stats_json["pools"]["litecoin"]["blocks"]["pending"])

			print("Hashrate:",stats_json["pools"]["litecoin"]["hashrate"])
		#print(stats_json)

if(__name__=="__main__"):
	while(True):
		mp = MonitorPool()
		d = mp.get_stats_data()

		#print(json.dumps(d, indent = 2))

		time.sleep(60)
