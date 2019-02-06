from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('indianapolis')
condition = location.condition
print(condition.text)
