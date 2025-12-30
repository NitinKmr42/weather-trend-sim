import numpy as np
import matplotlib.pyplot as plt
NoOfDays=int(input("Enter the number of days="))
days=np.arange(1,NoOfDays+1)
slope=0.01
trend=slope*days
std_dev=2
noise=np.random.normal(0,std_dev,NoOfDays)

baseTemp=25
temperature=baseTemp+trend+noise
window_7=7
window_30=30
rolling_avg_7= np.convolve(
    temperature,
    np.ones(window_7) / window_7,
    mode="valid"
)
rolling_days_7=days[window_7-1:]
rolling_avg_30= np.convolve(
    temperature,
    np.ones(window_30) / window_30,
    mode="valid"
)
rolling_days_30=days[window_30-1:]


plt.plot(days, temperature, alpha=0.4, label="Daily Temperature")
plt.plot(
    rolling_days_7,
    rolling_avg_7,
    linewidth=2,
    label="7-Day Rolling Avg"
)
plt.plot(
    rolling_days_30,
    rolling_avg_30,
    linewidth=3,
    label="30-Day Rolling Avg"
)
plt.plot(
    days,
    baseTemp + trend,
    linestyle="--",
    label="Underlying Trend"
)

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Effect of Rolling Window Size on Trend Visibility")
plt.legend()
plt.show()


