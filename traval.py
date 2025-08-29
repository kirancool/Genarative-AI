# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 22:31:01 2025

@author: kiran
"""

import os
import streamlit as st
from groq import Groq


client = Groq(api_key="")

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("AI Travel Planner (Groq LLM)")

# --- Sidebar Inputs ---
st.sidebar.header("Trip Details")
destination = st.sidebar.text_input("Enter Destination")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")
budget = st.sidebar.selectbox("Budget Level", ["Low", "Medium", "High"])
interests = st.sidebar.multiselect(
    "Interests", 
    ["History", "Food", "Shopping", "Nature", "Nightlife", "Adventure", "Culture"],
    #default=["Food", "Culture"]
)

# --- Main Area ---
if st.sidebar.button("Generate Itinerary"):
    with st.spinner("Planning your trip..."):
        prompt = f"""
        You are a travel planner.
        Plan a detailed daily itinerary for a trip to {destination}.
        Dates: {start_date} to {end_date}.
        Budget: {budget}.
        Interests: {', '.join(interests)}.
        
        Include:
        - Morning, Afternoon, Evening activities
        - Local food recommendations
        - Transportation tips
        - Approximate costs
        - Must-visit attractions
        """

        response = client.chat.completions.create(
            model="gemma2-9b-it",  # Fast Groq LLM
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
        )

        itinerary = response.choices[0].message.content

    st.success("Your Itinerary is Ready!")
    st.write(itinerary)

    # Optional: Save as text file
    st.download_button(
        "Download Itinerary",
        itinerary,
        file_name="travel_itinerary.txt",
        mime="text/plain",
    )

else:
    st.info("Fill in trip details on the left and click **Generate Itinerary**")