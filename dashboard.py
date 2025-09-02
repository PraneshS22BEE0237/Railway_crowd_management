import streamlit as st
import pandas as pd
from crowd_simulator import simulate_crowd_data, STATIONS
from scheduler import get_train_schedule
from energy_optimizer import calculate_energy_savings

st.title("AI-Powered Smart Metro Scheduling Dashboard")

minute = st.slider("Select time (minutes since midnight)", 0, 1440, 480, 10)
crowd_df = simulate_crowd_data(minute)
st.subheader("Simulated Crowd Data")
st.dataframe(crowd_df)

schedule = get_train_schedule(crowd_df)
st.subheader("Dynamic Train Schedule (interval in seconds)")
st.write(schedule)

energy = calculate_energy_savings(schedule)
st.subheader("Estimated Energy Savings per Station")
st.write(energy)

if st.button("Simulate Next 2 Hours"):
    results = []
    for t in range(minute, minute+120, 10):
        crowd = simulate_crowd_data(t)
        sched = get_train_schedule(crowd)
        energy = calculate_energy_savings(sched)
        results.append({"time":t,"crowd":crowd.to_dict('records')[0],"schedule":sched,"energy":energy})
    st.write(results)
