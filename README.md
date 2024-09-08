# Welcome to the EEG Analysis Platform! 🧠⚡

This repository contains interactive **EEG analysis web application**, an easy-to-use tool to visualize and analyze EEG signals using **complexity** and **entropy**.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=plastic&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=plastic&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=plastic&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=plastic&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=plastic&logo=scipy&logoColor=white)
![PyWavelets](https://img.shields.io/badge/PyWt-FF6347?style=plastic)
![NeuroKit2](https://img.shields.io/badge/NeuroKit2-FF4500?style=plastic)

The main functionalities of the platform at the moment are:
- Visualization of EEG signals
- Frequency analysis using wavelets
- Entropy analysis.
---

## Features ✨

### ⚡ EEG Visualization
Load and visualize EEG signals from the **Fp1** and **Fp2** channels, allowing you to analyze the signals over specific time intervals.

### 📡 Frequency Analysis
Perform **wavelet-based frequency analysis** on EEG signals. This feature allows you to explore the **frequency spectrum** over time and analyze dynamic changes in brainwave frequencies.

### 📊 Entropy Analysis
Evaluate the **complexity** of EEG signals by computing entropy measures, such as **Shannon Entropy**, **Approximate Entropy**, and **Sample Entropy**.

## EEG Signal Acquisition ⚙️

The EEG data used in this project was acquired with the **BITalino NeuroBIT Kit**. Electrodes were placed following the **international 10-20 system**, specifically at **Fp1** or **Fp2** for brain activity measurement. The reference electrode was placed behind the ear.

<p align="center"> <img src="https://support.pluxbiosignals.com/wp-content/uploads/2023/02/image-4.png" alt="Electrode Positioning" /> </p> <p align="center"><i>Electrode positioning for EEG at Fp1: Measuring pins IN+/- (left) and reference (right).</i></p>

## How to Use 🔧

1. Clone the repository:
   ```bash
   git clone https://github.com/Seba3995/EEG_web_app.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run Home.py
   ```

## Project Structure

```
EEG_Analysis_Platform/
│
├── components/                    # Directory for component classes
│   ├── data_loader.py             # Class for loading EEG data
│   ├── entropy_analyzer.py        # Class for performing entropy analysis
│   ├── ui_elements.py             # Class for displaying UI elements (e.g., logos)
│   ├── visualizer.py              # Class for visualizing EEG signals and analysis results
│   ├── wavelet_analyzer.py        # Class for performing wavelet-based frequency analysis
│
├── data/                          # Directory for storing CSV EEG data files
│   └── eeg_data.csv               # Example EEG data file (replace with your own data)
│
├── pages/                         # Directory for different app functionalities
│   ├── 1_⚡_Visualización_EEG.py   # Page for EEG signal visualization
│   ├── 2_📡_Análisis_Frecuencial.py# Page for frequency analysis using wavelets
│   ├── 3_📊_Analisis_Entropía.py   # Page for entropy analysis
│
├── Home.py                        # Main landing page with tabbed navigation
├── requirements.txt               # List of dependencies to install
└── README.md                      # Project documentation (this file)
```

### Architecture Overview

This platform follows a **component-based architecture** where each functionality is encapsulated in its own class, ensuring modularity, scalability, and maintainability.

### Main Components
- **EEGDataLoader**: Handles loading EEG data from CSV files.
- **EEGVisualizer**: Provides functions to visualize EEG data and results.
- **EntropyAnalyzer**: Calculates various entropy metrics for EEG signals.
- **EEGWaveletAnalyzer**: Performs continuous wavelet transformation to analyze the frequency content of EEG signals.
- **UIElements**: Displays reusable UI elements like logos and headings.

> ### **Feel free to contribute, and let me know if you encounter any issues!** 😄
