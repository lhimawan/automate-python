#switches lat/long
latlonglist = []
while True:
	latlong = input().split()
	if latlong:
		latlonglist.append(latlong)
	else:
		break

for i in range(len(latlonglist)):
	print (str(latlonglist[i][1]) + ', ' + str(latlonglist[i][0]))
