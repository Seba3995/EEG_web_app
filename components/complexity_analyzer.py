# components/complexity_analyzer.py

import neurokit2 as nk


class ComplexityAnalyzer:
    """
    Class to handle the calculation of complexity for EEG signals using nk.complexity().
    """

    def __init__(self, signal):
        """
        Initialize with the EEG signal.

        :param signal: The EEG signal data (array-like).
        """
        self.signal = signal

    def calculate_complexity(self):
        """
        Calculate complexity metrics for the signal using the 'makowski2022' subset.
        Returns a dataframe with the complexity results and additional information.
        """
        # Compute the complexity using the "makowski2022" subset of metrics
        complexity_df, complexity_info = nk.complexity(self.signal, which="makowski2022")
        return complexity_df, complexity_info
