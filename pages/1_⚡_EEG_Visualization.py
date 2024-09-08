# pages/1_⚡_EEG_Visualization.py

from components.data_loader import EEGDataLoader
from components.visualizer import EEGVisualizer
from components.ui_elements import UIElements
import streamlit as st
import os


def main():
    st.set_page_config(page_title="EEG Visualization", page_icon="⚡")

    UIElements.display_usach_logo()

    st.title("EEG Visualization")
    st.subheader("Fp1 and Fp2 Channels")

    # List available CSV files in the data directory
    available_files = [f for f in os.listdir("data") if f.endswith(".csv")]
    selected_file = st.selectbox("Select an EEG file to load", available_files)

    eeg_loader = EEGDataLoader(selected_file)
    data = eeg_loader.load_data()

    if data is not None:
        # Display signal information
        st.markdown(f"**Sampling rate:** {1000} Hz")
        st.markdown("**Electrodes:** Fp1 and Fp2 according to the international 10-20 system")
        st.markdown("**Reference electrode:** Behind the ear")

        # Instantiate the EEGVisualizer
        visualizer = EEGVisualizer(data)

        # Add a slider for selecting the time range
        total_duration = len(data) / visualizer.sampling_rate
        time_range = st.slider("Select the time range to visualize", 0.0, total_duration, (0.0, total_duration), 0.1)

        # Plot both channels in a single graph, limited to the selected time range
        visualizer.plot_channels("A1", "A2", time_range)


if __name__ == "__main__":
    main()
