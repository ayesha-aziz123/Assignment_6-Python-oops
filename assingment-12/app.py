class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f)  # Output: 77.0
