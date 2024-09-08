# components/visualizer.py

import plotly.graph_objects as go
import streamlit as st


class EEGVisualizer:
    """
    Class to handle the visualization of EEG data using Plotly.
    """

    def __init__(self, data, sampling_rate=1000):
        """
        Initializes the EEGVisualizer with the loaded EEG data.

        :param data: pandas DataFrame containing the EEG data.
        :param sampling_rate: Sampling rate of the EEG data (default: 1000 Hz).
        """
        self.data = data
        self.sampling_rate = sampling_rate
        self.time = [i / sampling_rate for i in range(len(data))]  # Calculate time axis based on sampling rate

    def plot_channels(self, channel_fp1=None, channel_fp2=None, time_range=(0, 5)):
        """
        Plots EEG channels (Fp1 and/or Fp2) in a single graph using Plotly, limited to the given time range.

        :param channel_fp1: Column name for the Fp1 channel (can be None).
        :param channel_fp2: Column name for the Fp2 channel (can be None).
        :param time_range: Tuple (min_time, max_time) representing the time range to display in seconds.
        """
        start_idx = int(time_range[0] * self.sampling_rate)
        end_idx = int(time_range[1] * self.sampling_rate)

        fig = go.Figure()

        # Plot Fp1 if available
        if channel_fp1 and channel_fp1 in self.data.columns:
            fig.add_trace(go.Scatter(x=self.time[start_idx:end_idx], y=self.data[channel_fp1][start_idx:end_idx],
                                     mode='lines', name='Fp1'))

        # Plot Fp2 if available
        if channel_fp2 and channel_fp2 in self.data.columns:
            fig.add_trace(go.Scatter(x=self.time[start_idx:end_idx], y=self.data[channel_fp2][start_idx:end_idx],
                                     mode='lines', name='Fp2'))

        # Update layout if data is available
        if fig.data:
            fig.update_layout(
                title="EEG Channels",
                xaxis_title="Time (s)",
                yaxis_title="Amplitude (µV)",
                legend_title="Electrode"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Fp1 or Fp2 channels are not available in the loaded data.")

    @staticmethod
    def plot_entropy_over_time(entropies_fp1, entropies_fp2, window_size_sec):
        """
        Plots entropy over time for Fp1 and Fp2 for all entropy metrics (Shannon, Approximate, Sample)
        using a scatter plot with lines.

        :param entropies_fp1: List of entropy values for Fp1.
        :param entropies_fp2: List of entropy values for Fp2.
        :param window_size_sec: Size of each window in seconds.
        """
        times = [i * window_size_sec for i in range(len(entropies_fp1))]

        fig = go.Figure()

        # Define colors for each entropy type
        colors = {"Shannon": "red", "Approximate": "green", "Sample": "blue"}

        # Plot entropy for Fp1 with circle markers
        for metric, color in colors.items():
            values_fp1 = [window[metric] for window in entropies_fp1]
            fig.add_trace(go.Scatter(x=times, y=values_fp1, mode='lines+markers',
                                     marker=dict(symbol="circle", size=10, color=color),
                                     line=dict(width=0.5),
                                     name=f"Fp1 - {metric}"))

        # Plot entropy for Fp2 with triangle-up markers
        for metric, color in colors.items():
            values_fp2 = [window[metric] for window in entropies_fp2]
            fig.add_trace(go.Scatter(x=times, y=values_fp2, mode='lines+markers',
                                     marker=dict(symbol="triangle-up", size=10, color=color),
                                     line=dict(width=0.5),
                                     name=f"Fp2 - {metric}"))

        fig.update_layout(
            title="Entropy Over Time - Fp1 vs Fp2",
            xaxis_title="Time (s)",
            yaxis_title="Entropy Value"
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def plot_entropy_bars(entropy_fp1, entropy_fp2, labels):
        """
        Plots a bar chart comparing the average entropy values for Fp1 and Fp2.

        :param entropy_fp1: List of average entropy values for Fp1.
        :param entropy_fp2: List of average entropy values for Fp2.
        :param labels: Labels for the entropy measures.
        """
        fig = go.Figure()

        # Add bars for Fp1
        fig.add_trace(go.Bar(x=labels, y=entropy_fp1, name="Fp1", marker_color='orange'))

        # Add bars for Fp2
        fig.add_trace(go.Bar(x=labels, y=entropy_fp2, name="Fp2", marker_color='purple'))

        fig.update_layout(
            title="Average Entropy Comparison - Fp1 vs Fp2",
            xaxis_title="Entropy Type",
            yaxis_title="Average Entropy Value",
            barmode="group"
        )

        st.plotly_chart(fig)
