
from datetime import datetime
from time import gmtime, strftime


now = datetime.now().timestamp()

#now = datetime.now().strftime('%Y-%d-%B')
#datetime.timezone(hh[:mm[:ss]]).timestamp()

now_time = int(now)*1000

print(now_time)
#1333234800.0'