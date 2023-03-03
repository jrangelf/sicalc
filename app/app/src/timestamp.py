from datetime import datetime

def time_stamp():
	
	timestamp = str(datetime.now()).replace(' ','_').split('.')[0].replace(':','')
	
	return timestamp