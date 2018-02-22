import datetime

print(datetime.date.today().strftime('%d/%m/%Y'))

miBirDay=datetime.date(1941,1,5)
miBirDay==miBirDay + datetime.timedelta(days=1)

print(miBirDay.strftime('%d/%m/%Y'))

miBirDay=miBirDay.replace(year=miBirDay.year+1)

print(miBirDay.strftime('%d/%m/%Y'))
