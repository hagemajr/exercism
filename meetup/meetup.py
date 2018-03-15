import datetime
from dateutil.relativedelta import *

def meetup_day(year,month,dayname,qualifier):
	start_date = datetime.date(year,month,1)
	end_date = (start_date + relativedelta(months=1)) - relativedelta(days=1)
	daymap = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
	count = 1
	daydict = {}
	
	for x in range(end_date.day):
		if datetime.date(year,month,x+1).weekday() == daymap[dayname]:
			if count == 1:
				daydict['1st'] = datetime.date(year,month,x+1)
				count += 1
			elif count == 2:
				daydict['2nd'] = datetime.date(year,month,x+1)
				count += 1
			elif count == 3:
				daydict['3rd'] = datetime.date(year,month,x+1)
				count += 1
			elif count == 4:
				daydict['4th'] = datetime.date(year,month,x+1)
				count += 1
			elif count == 5:
				daydict['5th'] = datetime.date(year,month,x+1)
			
			if x+1 > 10 and x+1 < 20:
				daydict['teenth'] = datetime.date(year,month,x+1)
				
	if '5th' in daydict.keys():
		daydict['last'] = daydict['5th']
	elif '4th' in daydict.keys():
		daydict['last'] = daydict['4th']
	else:
		daydict['last'] = daydict['3rd']
				
	if qualifier in daydict.keys():
		return daydict[qualifier]
	else:
		raise ValueError("That does not appear to be a valid date.")

#print(meetup_day(2013,9,'Friday',"teenth"))