import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('h601.csv', header=None, skiprows=1)

# Specify the names of the columns
df.columns = ['year', 'month', 'day', 'hour', 'sea_level']

# Remove rows with negative sea level values
df = df[df.sea_level >= 0]

# Combine the year, month, day, and hour columns into a single 'datetime' column
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']], format='%Y-%m-%d %H')

# Set datetime as index
df = df.set_index('datetime')

# Drop the individual date and time columns
df = df.drop(['year', 'month', 'day', 'hour'], axis=1)

# Plot
plt.figure(figsize=(20,10))
plt.title('Esperanza Antarctic Base Sea Level')
plt.xlabel('Date')
plt.ylabel('Sea Level (mm)')
plt.plot(df)

# Plot the three-month rolling mean
plt.plot(df.rolling(window=2160).mean())

# Save plot to png
plt.savefig('h601.png')