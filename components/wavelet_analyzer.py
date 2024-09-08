# components/wavelet_analyzer.py

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import pywt


class EEGWaveletAnalyzer:
    """
    Class to handle wavelet-based frequency analysis of EEG data using Plotly.
    """

    def __init__(self, signal, sampling_rate=1000, min_freq=0.5, max_freq=100):
        """
        Initializes the EEGWaveletAnalyzer with the signal to be analyzed.

        :param signal: The EEG signal (1D array) to analyze.
        :param sampling_rate: The sampling rate of the signal (default: 1000 Hz).
        :param min_freq: Minimum frequency of interest (default: 0.5 Hz).
        :param max_freq: Maximum frequency of interest (default: 100 Hz).
        """
        self.signal = signal
        self.sampling_rate = sampling_rate
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.scales = np.arange(1, 128)  # Define scales based on the desired frequency range using a Morlet wavelet

    def perform_wavelet_transform(self, time_range):
        """
        Performs the Continuous Wavelet Transform (CWT) on the selected time range of the signal.

        :param time_range: Tuple (min_time, max_time) representing the time range in seconds.
        :return: Coefficients and frequencies from the wavelet transform.
        """
        start_idx = int(time_range[0] * self.sampling_rate)
        end_idx = int(time_range[1] * self.sampling_rate)

        # Slice the signal according to the selected time range
        signal_slice = self.signal[start_idx:end_idx]

        # Perform CWT using a parametrized Morlet wavelet
        coefficients, _ = pywt.cwt(signal_slice, self.scales, 'cmor1.5-1.0')

        # Convert scales to frequencies (in Hz)
        frequencies = pywt.scale2frequency('cmor1.5-1.0', self.scales) * self.sampling_rate
        frequencies = frequencies[(frequencies <= self.max_freq) & (frequencies >= self.min_freq)]

        # Return only the central portion to reduce the edge effect
        center_coefficients = coefficients[:, 200:-200]  # Trim to avoid edge effects

        return center_coefficients, frequencies

    @staticmethod
    def plot_wavelet_transform(coefficients, frequencies, time_range):
        """
        Plots the wavelet transform coefficients as a time-frequency heatmap using Plotly.

        :param coefficients: The CWT coefficients.
        :param frequencies: The corresponding frequencies for each scale.
        :param time_range: Tuple (min_time, max_time) representing the time range in seconds.
        """
        # Time axis based on the time range
        time = np.linspace(time_range[0], time_range[1], num=coefficients.shape[1])

        # Create heatmap using Plotly
        heatmap = go.Heatmap(
            z=np.abs(coefficients),
            x=time,
            y=frequencies,
            colorscale='Viridis',
            zmin=0, zmax=np.abs(coefficients).max()
        )

        # Layout configuration for the heatmap
        layout = go.Layout(
            title=f"Time-Frequency Representation (Wavelet Transform) from {time_range[0]}s to {time_range[1]}s",
            xaxis_title="Time (s)",
            yaxis_title="Frequency (Hz)",
            coloraxis_colorbar=dict(title="Amplitude")
        )

        fig = go.Figure(data=[heatmap], layout=layout)

        # Display the plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)
