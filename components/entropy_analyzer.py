# components/entropy_analyzer.py

import neurokit2 as nk


class EntropyAnalyzer:
    """
    Class to handle the calculation of different entropy measures for EEG signals in windows of time.
    """

    def __init__(self, signal, sampling_rate=1000):
        """
        Initialize the analyzer with the EEG signal and the sampling rate.

        :param signal: The EEG signal data (array-like).
        :param sampling_rate: Sampling rate of the EEG data (default: 1000 Hz).
        """
        self.signal = signal
        self.sampling_rate = sampling_rate

    def calculate_entropies_in_windows(self, window_size_sec=5):
        """
        Calculate entropy measures for each window of the signal.

        :param window_size_sec: Window size in seconds for which to calculate entropy.
        :return: List of dictionaries with entropy values for each window.
        """
        window_size = window_size_sec * self.sampling_rate  # Convert window size to number of samples
        num_windows = len(self.signal) // window_size

        entropies = []

        for i in range(num_windows):
            start_idx = i * window_size
            end_idx = start_idx + window_size
            window_signal = self.signal[start_idx:end_idx]

            # Calculate entropy measures for the window
            entropy_values = self._calculate_entropies(window_signal)
            entropies.append(entropy_values)

        return entropies

    @staticmethod
    def _calculate_entropies(window_signal):
        """
        Calculate different types of entropy for a given signal window.

        :param window_signal: The EEG signal window.
        :return: Dictionary with entropy values for Shannon, Approximate, and Sample Entropy.
        """
        return {
            "Shannon": nk.entropy_shannon(window_signal)[0],
            "Approximate": nk.entropy_approximate(window_signal)[0],
            "Sample": nk.entropy_sample(window_signal)[0]
        }
