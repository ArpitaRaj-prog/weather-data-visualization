import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key
API_KEY = '4f2839774cdec3c75eb89db8b0f06a56'
CITY = 'Patna'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
# Fetch data
response = requests.get(URL)
data = response.json()

# Extract temperature and time
temperatures = []
timestamps = []

for entry in data['list']:
    temp = entry['main']['temp']
    time = entry['dt_txt']
    temperatures.append(temp)
    timestamps.append(time)

# Plotting
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(timestamps[:8], temperatures[:8], marker='o', linestyle='-', color='teal')
plt.xticks(rotation=45)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title(f'Temperature Forecast for {CITY} (Next 24 Hours)')
plt.tight_layout()
plt.show()