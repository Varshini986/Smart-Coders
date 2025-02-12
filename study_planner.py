import streamlit as st
import datetime
import pandas as pd
from study_planner_backend import create_study_schedule, recommend_study_plan

# Streamlit App UI
st.title("AI Study Planner")

# Step 1: Collect User Inputs
st.subheader("1. Enter Your Study Details")

subjects_input = st.text_input("Enter subjects (comma-separated)", "Math, Science, History")
study_hours_input = st.text_input("Enter study hours for each subject (comma-separated)", "2, 1, 1")

# Parse the input into lists
subjects = [subject.strip() for subject in subjects_input.split(",")]
study_hours = [int(hour.strip()) for hour in study_hours_input.split(",")]

# Step 2: Allow the User to Select Study Duration and Start Date
start_date = st.date_input("Select your start date", datetime.date.today())
study_duration = st.number_input("Enter the number of days for your study plan", min_value=1, value=7)

# Step 3: AI Recommendation for Study Hours
available_time = st.number_input("Enter available study time (in hours)", min_value=1, value=8)
if st.checkbox("Get AI-Recommended Study Hours"):
    recommended_hours = recommend_study_plan(subjects, available_time)
    st.write(f"AI Recommended study hours: {dict(zip(subjects, recommended_hours))}")

# Step 4: Generate Study Schedule
if st.button("Generate Study Schedule"):
    # Generate the study schedule
    schedule_df = create_study_schedule(subjects, study_hours, start_date, study_duration)
    
    # Show the study schedule
    st.write("Your personalized study schedule:")
    st.dataframe(schedule_df)

    # Option to download the study schedule as a CSV file
    st.download_button("Download Schedule as CSV", schedule_df.to_csv(), "study_schedule.csv", "text/csv")
