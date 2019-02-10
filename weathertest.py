from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup(2517274)
condition = location.conditio
print(condition.text)
