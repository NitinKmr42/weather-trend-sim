#Weather Trend Simulator
##Overview

This project simulates daily weather temperature data over a year using synthetic time-series data.
It demonstrates how long-term trends can be hidden by short-term randomness and how rolling averages help reveal underlying patterns.

##Concepts Covered

*Time-series data

*Trend vs noise

*Rolling (moving) averages

*Effect of window size on smoothing

*Data visualization using Matplotlib


##How the Simulation Works

*A time axis is created representing daily measurements.

*A slow linear temperature trend is defined.

*Random daily noise is added to simulate weather variability.

*Rolling averages (7-day and 30-day) are applied to smooth the data.

*Results are visualized to compare raw data, smoothed data, and the true underlying trend.

##Key Insight

*Short rolling windows preserve short-term variation but remain noisy.

*Larger rolling windows produce smoother curves that make long-term trends easier to analyze.

*There is a trade-off between responsiveness and clarity.

##Technologies Used

*Python

*NumPy

*Matplotlib