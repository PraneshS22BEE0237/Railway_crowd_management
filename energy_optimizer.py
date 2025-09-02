def calculate_energy_savings(schedule, base_interval=180):
    # Assume base_interval is the default (fixed) schedule
    # Energy saved = (interval - base_interval) / base_interval
    savings = {}
    for station, interval in schedule.items():
        if interval > base_interval:
            savings[station] = (interval - base_interval) / base_interval
        else:
            savings[station] = 0
    return savings

if __name__ == "__main__":
    # Example usage
    schedule = {'Ghatkopar':90,'Andheri':180,'Dadar':300}
    print(calculate_energy_savings(schedule))
