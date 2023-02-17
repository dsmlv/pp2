import datetime 
td = datetime.date.today()
yd = td - datetime.timedelta(days = 1)
tmrw = td + datetime.timedelta(days = 1) 
print('Yesterday : ',yd)
print('Today : ',td)
print('Tomorrow : ',tmrw)