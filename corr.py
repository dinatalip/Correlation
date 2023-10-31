import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your data into pandas DataFrames
data = {
    "2001_BahirDar": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2001_BahirDar.csv"),
    "2011_BahirDar": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2011_BahirDar.csv"),
    "2021_BahirDar": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2021_BahirDar.csv"),
    "2001_Hawassa": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2001_Hawassa.csv"),
    "2011_Hawassa": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2011_Hawassa.csv"),
    "2021_Hawassa": pd.read_csv("https://raw.githubusercontent.com/Manniy/Corr/main/2021_Hawassa.csv")
}

# Streamlit app
st.title("Correlation Analysis")
st.sidebar.header("User Preferences")

# User selects the year with hover-over tooltip
selected_year = st.sidebar.selectbox("Select Year", [2001, 2011, 2021], help="Select the year for analysis")

# User selects the city with hover-over tooltip
selected_city = st.sidebar.selectbox("Select City", ["BahirDar", "Hawassa"], help="Select the city for analysis")

# Change cursor style for user preference elements
st.markdown(
    f"""
    <style>
        div[data-baseweb="select"] .Select-control {{
            cursor: pointer !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Button to trigger data analysis
if st.sidebar.button("Analyze"):
    # Retrieve the selected data based on user preferences
    selected_data = data[f"{selected_year}_{selected_city}"]

    # Calculate correlations
    lst_ndbi_corr = selected_data["LST"].corr(selected_data["NDBI"])
    lst_ndvi_corr = selected_data["LST"].corr(selected_data["NDVI"])

    # Create and display scatter plots with customizations
    fig, ax = plt.subplots()
    scatter = ax.scatter(selected_data["NDBI"], selected_data["LST"], c=selected_data["NDVI"], cmap='viridis', s=50, alpha=0.7)
    plt.title("Scatter Plot of NDBI vs. LST")
    plt.xlabel("NDBI", color="#1c2d3c")
    plt.ylabel("LST (°C)", color="#1c2d3c")
    ax.set_facecolor("#1c2d3c")
    ax.xaxis.label.set_color("#1c2d3c")
    ax.yaxis.label.set_color("#1c2d3c")
    ax.tick_params(axis="x", colors="#1c2d3c")
    ax.tick_params(axis="y", colors="#1c2d3c")



    # Add a colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label("  ", color="#1c2d3c")
    cbar.ax.yaxis.label.set_color("#1c2d3c")

    st.pyplot(fig)

    # Create and display scatter plot for NDVI vs. LST
    fig2, ax2 = plt.subplots()
    scatter2 = ax2.scatter(selected_data["NDVI"], selected_data["LST"], c=selected_data["NDBI"], cmap='viridis', s=50, alpha=0.7)
    plt.title("Scatter Plot of NDVI vs. LST")
    plt.xlabel("NDVI", color="#1c2d3c")
    plt.ylabel("LST (°C)", color="#1c2d3c")
    ax2.set_facecolor("#1c2d3c")
    ax2.xaxis.label.set_color("#1c2d3c")
    ax2.yaxis.label.set_color("#1c2d3c")
    ax2.tick_params(axis="x", colors="#1c2d3c")
    ax2.tick_params(axis="y", colors="#1c2d3c")



    # Add a colorbar
    cbar2 = plt.colorbar(scatter2)
    cbar2.set_label("  ", color="#1c2d3c")
    cbar2.ax.yaxis.label.set_color("#1c2d3c")

    st.pyplot(fig2)

    # Display the correlation values
    st.write(f"Correlation between LST and NDBI: {lst_ndbi_corr}")
    st.write(f"Correlation between LST and NDVI: {lst_ndvi_corr}")
