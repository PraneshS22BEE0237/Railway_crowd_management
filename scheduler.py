import numpy as np

# Dynamic scheduling logic
def get_train_schedule(crowd_df):
    schedule = {}
    for station in crowd_df.columns:
        crowd = crowd_df[station].values[0]
        # More crowd, higher frequency (min interval 90s, max 5min)
        if crowd > 200:
            interval = 90
        elif crowd > 100:
            interval = 180
        else:
            interval = 300
        schedule[station] = interval
    return schedule

if __name__ == "__main__":
    # Example usage
    import pandas as pd
    df = pd.DataFrame({'Ghatkopar':[220],'Andheri':[180],'Dadar':[90]})
    print(get_train_schedule(df))
