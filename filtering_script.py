import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load the data
with open('data/moving_lfp.pickle', 'rb') as f:
    data = pickle.load(f)

# Take a few seconds of the data
sample_rate = data['sample_rate']
duration = 5  # Duration of data to use in seconds
data_subset = data['data'][:duration * sample_rate]
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y
# Define frequency bands of interest
frequency_bands = [(1, 4), (4, 8), (8, 12), (12, 30), (30, 50)]

# Plot the original signal
plt.figure(figsize=(10, 6))
plt.plot(data_subset, label='Original Signal')

# Filter and plot signals for each frequency band
for band in frequency_bands:
    lowcut, highcut = band
    filtered_signal = butter_bandpass_filter(data_subset, lowcut, highcut, sample_rate)
    plt.plot(filtered_signal, label=f'{lowcut}-{highcut} Hz')

plt.title('Filtered Signal in Different Frequency Bands')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

