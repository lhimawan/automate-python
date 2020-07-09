import webbrowser

def search():
#Takes long lat input & stores them into variables TODO: multiline input workaround
    latlong = input('Please enter the lat & long:').split()
    zoom = '17' #set map zoom here TODO: zoom setting?

#Open GMaps, OSM, HERE, and Mapy.cz with specified coordinates
    webbrowser.open('https://www.google.com/maps/@%s,%s,%sz' % (latlong[0], latlong[1], zoom))
    webbrowser.open('https://www.openstreetmap.org/#map=%s/%s/%s' % (zoom, latlong[0], latlong[1]))
    #swapped coordinates for the source below:
    webbrowser.open('https://en.mapy.cz/zakladni?x=%s&y=%s&z=%s' % (latlong[1], latlong[0], zoom))
    #webbrowser.open('https://wego.here.com/?map=%s,%s,%s,normal' % (latlong[0], latlong[1], zoom)) #source rarely used, commented out for now
    
#Flow control: loop back to start of program unless "no" or "0" is entered  
run = True
while run == True:
    try:
        search()
    except IndexError:
        print('')
