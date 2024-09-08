# Home.py

import streamlit as st
from components.ui_elements import UIElements


def main():
    st.set_page_config(page_title="EEG Analysis", page_icon="🧠", layout="wide")

    UIElements.display_usach_logo()

    st.title("Welcome to the EEG Analysis Platform")

    # Description
    st.markdown("""
    This application allows you to upload and analyze EEG signals. Use the tabs below to learn more about the functionalities 
    and redirect yourself to the corresponding page to work with the data.
    """)

    tabs = st.tabs(["⚡ EEG Visualization", "📡 Frequency Analysis", "📊 Entropy Analysis"])
    with tabs[0]:
        st.header("⚡ EEG Visualization")
        st.markdown("""
        On this page, you can visualize EEG signals from the Fp1 and Fp2 channels. 
        This feature allows you to see the EEG data in the time domain and select specific time intervals for analysis.

        ### Instructions:
        - 1️⃣ Upload a CSV file containing the EEG data.
        - 2️⃣ Select the time range you wish to visualize.
        - 3️⃣ View the signal in an interactive graph.
        """)

    with tabs[1]:
        st.header("📡 EEG Frequency Analysis")
        st.markdown("""
        This page allows you to perform frequency analysis using the Continuous Wavelet Transform (CWT) on EEG signals. 
        You will be able to observe the frequency spectrum over time and analyze the frequency characteristics of the signal.

        ### Instructions:
        - 1️⃣ Upload a CSV file containing the EEG data.
        - 2️⃣ Select the EEG channel and the time range you wish to analyze.
        - 3️⃣ View the frequency analysis results in a spectrum graph.
        """)

    with tabs[2]:
        st.header("📊 EEG Entropy Analysis")
        st.markdown("""
        On this page, you can perform entropy analysis on EEG signals to assess the complexity of the signals in the time domain. 
        Metrics such as Shannon Entropy, Approximate Entropy, and Sample Entropy will be calculated.

        ### Instructions:
        - 1️⃣ Upload a CSV file containing the EEG data.
        - 2️⃣ Select the time range and window size for the analysis.
        - 3️⃣ View the entropy analysis results in graphs.
        """)


if __name__ == "__main__":
    main()
