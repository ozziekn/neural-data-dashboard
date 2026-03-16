import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Neural Data Dashboard")

# Simulated spike data
np.random.seed(42)
spike_times = np.cumsum(np.random.exponential(scale=0.1, size=200))

# Compute statistics
firing_rate = len(spike_times) / spike_times[-1]
isi = np.diff(spike_times)

st.write("### Firing Rate")
st.write(f"{firing_rate:.2f} Hz")

# Raster plot
fig, ax = plt.subplots()
ax.eventplot(spike_times)
ax.set_title("Spike Raster Plot")
ax.set_xlabel("Time (s)")
ax.set_yticks([])

st.pyplot(fig)

# ISI histogram
fig2, ax2 = plt.subplots()
ax2.hist(isi, bins=30)
ax2.set_title("Interspike Interval Distribution")
ax2.set_xlabel("Interval (s)")

st.pyplot(fig2)
