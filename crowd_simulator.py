import numpy as np
import pandas as pd

STATIONS = ['Ghatkopar', 'Andheri', 'Dadar', 'Churchgate', 'CST', 'Bandra', 'Kurla']

# Simulate crowd data for each station
def simulate_crowd_data(time_minute):
    # Rush hour: 8-10am, 6-8pm
    rush = (480 <= time_minute <= 600) or (1080 <= time_minute <= 1200)
    data = {}
    for station in STATIONS:
        base = np.random.randint(20, 80)
        if rush and station in ['Ghatkopar', 'Andheri', 'Dadar']:
            base += np.random.randint(100, 200)
        elif rush:
            base += np.random.randint(50, 100)
        # Event spike
        if station == 'Bandra' and 1140 <= time_minute <= 1200:
            base += np.random.randint(150, 300)
        data[station] = base
    return pd.DataFrame([data])

if __name__ == "__main__":
    # Example usage
    for t in range(480, 600, 10):
        print(simulate_crowd_data(t))
