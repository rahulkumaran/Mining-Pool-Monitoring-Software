import json
import requests as r
import time
import logging
import pandas as pd


class MonitorPool:
	def __init__(self, choice=1):
		self.url = "http://107.173.118.210:8080/api/"
		self.choice = choice

	def send_request(self, url):
		return r.get(url)

	def get_json(self, req_data):
		return req_data.json()

	def get_stats_json(self):
		url = ""
		if(self.choice == 1):
			url += self.url + "stats"
		
		else:
			print("Wrong option entered!")
			return

		req_data = self.send_request(url)
		json_obj = self.get_json(req_data)

		return json_obj


	def get_stats_data(self):
		stats_json= self.get_stats_json()
		#print(json.dumps(stats_json, indent=2))
		if(self.choice==1):
			
			print(time.ctime(stats_json["time"]))
			print("Total Paid:",stats_json["pools"]["zen"]["poolStats"]["totalPaid"])
			print("Valid Blocks:",stats_json["pools"]["zen"]["poolStats"]["validBlocks"])
			print("Orphaned:",stats_json["pools"]["zen"]["blocks"]["orphaned"])

			print("Confirmed:",stats_json["pools"]["zen"]["blocks"]["confirmed"])

			print("Pending:",stats_json["pools"]["zen"]["blocks"]["pending"])

			print("Hashrate:",stats_json["pools"]["zen"]["hashrate"])
			print("----------------------------------------------------------")

			logging.basicConfig(filename="stats.log", level=logging.DEBUG)
			logging.info(time.ctime(stats_json["time"]))
			logging.info("Total Paid: "+str(stats_json["pools"]["zen"]["poolStats"]["totalPaid"]))
			logging.info("Valid Blocks: "+str(stats_json["pools"]["zen"]["poolStats"]["validBlocks"]))
			logging.info("Orphaned: "+str(stats_json["pools"]["zen"]["blocks"]["orphaned"]))
			logging.info(" Confirmed: "+str(stats_json["pools"]["zen"]["blocks"]["confirmed"]))
			logging.info("Pending: "+str(stats_json["pools"]["zen"]["blocks"]["pending"]))
			logging.info("Hashrate: "+str(stats_json["pools"]["zen"]["hashrate"]))
			logging.info("----------------------------------------")

		return

	def store_data_csv(file_name):
		return		
