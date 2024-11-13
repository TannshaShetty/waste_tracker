import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'food_wastage_data.csv'
data = pd.read_csv(file_path)

# App title and description with emojis, centered
st.markdown("<h1 style='text-align: center;'>Waste Reduction & Sustainability Tracker 🌎🍽️🥗</h1>", unsafe_allow_html=True)

# Center align and increase font size for the description
st.markdown("<h2 style='text-align: center; font-size: 24px;'>Analyze daily food waste and sustainability metrics to minimize environmental impact.</h2>", unsafe_allow_html=True)

# Change the background color of the app to orange
st.markdown(
    """
    <style>
    body {
        background-color: #FFA500;  /* Orange background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add an image related to food waste
image_path = '/Users/tannshashetty/Desktop/waste.png'  # Replace with your actual image path
st.image(image_path, caption="", use_column_width=True)

# Enhanced caption below the image, now centered
st.markdown("<h3 style='text-align: center;'>Together we can reduce food waste!</h3>", unsafe_allow_html=True)

# Create tabs for different analyses
tab1, tab2, tab3 = st.tabs(["Overview", "Wastage Analysis", "Additional Insights"])

# Tab 1: Overview
with tab1:
    st.subheader("Data Overview")
    st.write(data.head())

# Tab 2: Wastage Analysis
with tab2:
    st.subheader("Wastage Analysis")

    # Pie chart for Wastage Amount by Type of Food
    st.subheader("Wastage Amount by Type of Food")
    wastage_by_food = data.groupby("Type of Food")["Wastage Food Amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(wastage_by_food, labels=wastage_by_food.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Box plot for Wastage Amount by Type of Food
    st.subheader("Wastage Amount Distribution by Type of Food")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x="Type of Food", y="Wastage Food Amount", data=data, palette="Set3", ax=ax)
    ax.set_xlabel("Type of Food")
    ax.set_ylabel("Wastage Amount")
    ax.set_title("Distribution of Wastage Amount by Type of Food")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Scatter plot for Wastage Amount vs. Number of Guests with regression line
    st.subheader("Wastage Amount vs. Number of Guests")
    fig, ax = plt.subplots()
    sns.scatterplot(x="Number of Guests", y="Wastage Food Amount", data=data, color='blue', alpha=0.6, ax=ax)
    sns.regplot(x="Number of Guests", y="Wastage Food Amount", data=data, scatter=False, color='red', ax=ax)
    ax.set_xlabel("Number of Guests")
    ax.set_ylabel("Wastage Amount")
    ax.set_title("Wastage Amount vs. Number of Guests")
    st.pyplot(fig)

# Tab 3: Additional Insights
with tab3:
    st.subheader("Average Wastage by Number of Guests")

    # Calculate average wastage by number of guests
    average_wastage_by_guests = data.groupby("Number of Guests")["Wastage Food Amount"].mean().reset_index()

    # Line chart for Average Wastage by Number of Guests
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="Number of Guests", y="Wastage Food Amount", data=average_wastage_by_guests, marker='o', color='green')

    ax.set_xlabel("Number of Guests", fontsize=12)
    ax.set_ylabel("Average Wastage Amount", fontsize=12)
    ax.set_title("Average Wastage Amount by Number of Guests", fontsize=14)

    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Interactive Filter for Event Type
    st.subheader("Filter by Event Type")
    event_type = st.selectbox("Select an Event Type:", data["Event Type"].unique())
    filtered_data = data[data["Event Type"] == event_type]

    # Display filtered data
    st.write(f"Showing data for {event_type}:")
    st.write(filtered_data)

    # Download Button for Data
    st.subheader("Download Filtered Data")
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f"{event_type}_data.csv",
        mime='text/csv',
    )

    # Footer with educational tips
    st.subheader("Tips to Reduce Food Waste:")
    st.write("- Plan your meals and make shopping lists.")
    st.write("- Store food properly to extend its shelf life.")
    st.write("- Understand expiration dates—“best before” is not the same as “use by.”")
    st.write("- Share surplus food with friends or local food banks.")

# Instructions for running the app
st.write("Run this app using the command: `streamlit run <your_script_name.py>`")
