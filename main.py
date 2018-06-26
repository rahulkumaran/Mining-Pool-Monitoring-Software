from src.monitor import MonitorPool
import time


if(__name__=="__main__"):
	while(True):

		mp = MonitorPool()
		mp.get_stats_data()
		time.sleep(900)

