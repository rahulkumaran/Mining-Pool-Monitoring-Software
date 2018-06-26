import json
import requests as r
import time
import logging

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
		'''elif(self.choice == 2):
			url += self.url + "pool_stats"
		elif(self.choice == 3):
			url += self.url + "live_stats"
		elif(self.choice == 4):
			url += self.url + "getblocksstats"'''
		else:
			print("Wrong option entered!")
			return

		req_data = self.send_request(url)
		json_obj = self.get_json(req_data)

		return json_obj


	def get_stats_data(self):
		stats_json= self.get_stats_json()
		#print(time.ctime(stats_json["time"]))
		print(json.dumps(stats_json, indent=2))
		if(self.choice==1):
			
			
			print("Total Paid:",stats_json["pools"]["litecoin"]["poolStats"]["totalPaid"])
			print("Valid Blocks:",stats_json["pools"]["litecoin"]["poolStats"]["validBlocks"])
			print("Orphaned:",stats_json["pools"]["litecoin"]["blocks"]["orphaned"])

			print("Confirmed:",stats_json["pools"]["litecoin"]["blocks"]["confirmed"])

			print("Pending:",stats_json["pools"]["litecoin"]["blocks"]["pending"])

			print("Hashrate:",stats_json["pools"]["litecoin"]["hashrate"])
			print("----------------------------------------------------------")

			logging.basicConfig(filename="stats.log", level=logging.DEBUG)
			logging.info(time.ctime(stats_json["time"]))
			logging.info("Total Paid: "+str(stats_json["pools"]["litecoin"]["poolStats"]["totalPaid"]))
			logging.info("Valid Blocks: "+str(stats_json["pools"]["litecoin"]["poolStats"]["validBlocks"]))
			logging.info("Orphaned: "+str(stats_json["pools"]["litecoin"]["blocks"]["orphaned"]))
			logging.info(" Confirmed: "+str(stats_json["pools"]["litecoin"]["blocks"]["confirmed"]))
			logging.info("Pending: "+str(stats_json["pools"]["litecoin"]["blocks"]["pending"]))
			logging.info("Hashrate: "+str(stats_json["pools"]["litecoin"]["hashrate"]))
			logging.info("----------------------------------------")


		

if(__name__=="__main__"):
	while(True):

		mp = MonitorPool(2)
		d = mp.get_stats_data()
		time.sleep(900)

		
