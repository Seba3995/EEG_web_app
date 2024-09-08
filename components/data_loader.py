# components/data_loader.py

import os
import pandas as pd
import streamlit as st


class EEGDataLoader:
    """
    Class to handle loading EEG data from CSV files.
    """

    def __init__(self, file_name):
        """
        Initializes the EEGDataLoader with a specific CSV file.

        :param file_name: The name of the file (in the 'data' directory) to load.
        """
        self.file_path = os.path.join("data", file_name)
        self.data = None

    def load_data(self):
        """
        Loads the EEG data from the CSV file and stores it in the data attribute.

        :return: pandas DataFrame containing EEG data, or None if an error occurs.
        """
        try:
            self.data = pd.read_csv(self.file_path, delimiter=",")
            return self.data
        except FileNotFoundError:
            st.error(f"The file '{self.file_path}' was not found.")
            return None
        except pd.errors.EmptyDataError:
            st.error(f"The file '{self.file_path}' is empty.")
            return None
        except pd.errors.ParserError:
            st.error(f"There was an error parsing the file '{self.file_path}'.")
            return None

    def get_channels(self):
        """
        Returns the available EEG channels (columns) from the loaded data.

        :return: List of column names representing EEG channels, or an empty list if no data is loaded.
        """
        if self.data is not None:
            return self.data.columns.tolist()
        else:
            st.error("EEG data has not been loaded.")
            return []
