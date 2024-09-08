# pages/3_📊_Entropy_Analysis.py

import streamlit as st
import os
from components.data_loader import EEGDataLoader
from components.ui_elements import UIElements
from components.entropy_analyzer import EntropyAnalyzer
from components.visualizer import EEGVisualizer


def main():
    st.set_page_config(page_title="Entropy Analysis", page_icon="📊")

    UIElements.display_usach_logo()

    st.title("Entropy Analysis - Fp1 and Fp2 Channels")

    # List available CSV files in the data directory
    available_files = [f for f in os.listdir("data") if f.endswith(".csv")]
    selected_file = st.selectbox("Select an EEG file to load", available_files)

    # Load EEG data using the EEGDataLoader class
    eeg_loader = EEGDataLoader(selected_file)
    data = eeg_loader.load_data()

    if data is not None:
        # Display signal information
        st.markdown(f"**Sampling rate:** {1000} Hz")
        st.markdown("**Electrodes:** Fp1 and Fp2 according to the international 10-20 system")
        st.markdown("**Reference electrode:** Behind the ear")

        # Get the Fp1 and Fp2 data
        signal_fp1 = data["A1"]
        signal_fp2 = data["A2"]

        # Add a slider for selecting the time range
        total_duration = int(len(signal_fp1) / 1000)
        time_range = st.slider(
            "Select the time range to analyze (seconds)",
            0, total_duration, (0, 30), 1
        )
        start_time, end_time = time_range

        # Slice the signal for the selected time range
        signal_fp1 = signal_fp1[start_time * 1000:end_time * 1000]
        signal_fp2 = signal_fp2[start_time * 1000:end_time * 1000]

        # Select the window size
        col1, _ = st.columns([1, 1])
        with col1:
            window_size = st.number_input("Select the window size (seconds)", min_value=5, max_value=30,
                                          value=5, step=5)

        # Calculate entropy
        entropy_analyzer_fp1 = EntropyAnalyzer(signal_fp1)
        entropies_fp1 = entropy_analyzer_fp1.calculate_entropies_in_windows(window_size_sec=window_size)

        entropy_analyzer_fp2 = EntropyAnalyzer(signal_fp2)
        entropies_fp2 = entropy_analyzer_fp2.calculate_entropies_in_windows(window_size_sec=window_size)

        # Visualize entropy
        visualizer = EEGVisualizer(data)
        visualizer.plot_entropy_over_time(entropies_fp1, entropies_fp2, window_size)

        # Calculate the average entropy
        entropy_labels = ["Shannon", "Approximate", "Sample"]
        avg_entropy_fp1 = {metric: sum([window[metric] for window in entropies_fp1]) / len(entropies_fp1) for metric in
                           entropy_labels}
        avg_entropy_fp2 = {metric: sum([window[metric] for window in entropies_fp2]) / len(entropies_fp2) for metric in
                           entropy_labels}

        # Visualize bars to compare the average entropy between Fp1 and Fp2
        visualizer.plot_entropy_bars(list(avg_entropy_fp1.values()), list(avg_entropy_fp2.values()), entropy_labels)


if __name__ == "__main__":
    main()
