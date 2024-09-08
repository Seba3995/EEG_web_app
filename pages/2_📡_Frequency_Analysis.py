# pages/2_📡_Frequency_Analysis.py

from components.data_loader import EEGDataLoader
from components.wavelet_analyzer import EEGWaveletAnalyzer
from components.ui_elements import UIElements
from components.visualizer import EEGVisualizer
import streamlit as st
import os



def main():
    st.set_page_config(page_title="Frequency Analysis (Wavelet)", page_icon="📡")

    UIElements.display_usach_logo()

    st.title("EEG Frequency Analysis using Wavelet")

    # List available CSV files in the data directory
    available_files = [f for f in os.listdir("data") if f.endswith(".csv")]
    selected_file = st.selectbox("Select an EEG file to load", available_files)

    # Load EEG data using the EEGDataLoader class
    eeg_loader = EEGDataLoader(selected_file)
    data = eeg_loader.load_data()

    if data is not None:
        # Get available channels using the EEGDataLoader class
        channels = eeg_loader.get_channels()
        channel = st.selectbox("Select a channel for frequency analysis", channels)

        if channel:
            # Extract the signal from the selected channel
            signal = data[channel]
            sampling_rate = 1000

            # Instantiate the EEGVisualizer with the data
            visualizer = EEGVisualizer(data, sampling_rate)

            # Instantiate the EEGWaveletAnalyzer with the full signal
            wavelet_analyzer = EEGWaveletAnalyzer(signal, sampling_rate)

            # Add a slider for selecting the time range
            total_duration = int(len(signal) / sampling_rate)
            max_window_size = 30
            time_range = st.slider(
                "Select the time range to analyze (maximum 30 seconds)",
                0, total_duration, (0, 5), 1
            )
            #  Limit to 30 seconds
            if time_range[1] - time_range[0] > max_window_size:
                st.error(f"The selected window cannot exceed {max_window_size} seconds.")
                time_range = (time_range[0], time_range[0] + max_window_size)
                st.info(f"The range will be automatically adjusted between {time_range[0]} and {time_range[1]}")

            # Plot the selected channel
            visualizer.plot_channels(f"{channel}", None, time_range)

            # Perform wavelet analysis
            coefficients, frequencies = wavelet_analyzer.perform_wavelet_transform(time_range)

            # Plot the wavelet transform
            wavelet_analyzer.plot_wavelet_transform(coefficients, frequencies, time_range)


if __name__ == "__main__":
    main()
