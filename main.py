from src.monitor import MonitorPool
import time


if(__name__=="__main__"):
	while(True):

		mp = MonitorPool()
		stats_json = mp.get_stats_data()
		mp.store_data_csv(stats_json)
		time.sleep(0.1)

