from weather import weather
weather = weather

def weathers(halifax):
    location = weather.lookup_by_location('halifax')
    condition = location.condition()
    p = condition['text']
    print(p)
    t = []
    d = []
    h = []
    l = []
    c = []
    j = []
    y = []
    
    for forecasts in location.forecast():
        t.append(forecasts['text']
        d.append(forecasts['date']
        h.append(forecasts['high']
        l.append(forecasts['low']

    for item in l:
        temp = int(item)
        c.append(temp)
    print max("Max temp in 5 days is:" c)
    
    for item in h:
        temp = int(item)
        j.append(temp)
    print max("Max temp in 5 days is :" j)
    
    for item in t:
        if item = "rainy"

weathers(halifax)







