from weather import weather
weather = weather

def weathers(halifax):
    location = weather.lookup_by_location('halifax')
    condition = location.condition()
    p = condition['text']
    print(p)


