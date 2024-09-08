# components/ui_elements.py

import streamlit as st

class UIElements:
    """
    Class to handle UI elements like logos and other visual components.
    """

    @staticmethod
    def display_usach_logo():
        """
        Displays the USACH logo.
        """
        png_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Usach_P1.png/240px-Usach_P1.png"
        st.logo(png_icon)
        st.markdown("""
        <style>
            [alt=Logo] {
                height: 5rem;
            }
        </style>
        """, unsafe_allow_html=True)
