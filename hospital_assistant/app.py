import streamlit as st
from doctordatabase import find_doctor, check_slot
from llm import extract_info
from datetime import date as dt
from email_sending import send_email
from datetime import date, time, timedelta
import re

#frontend in streamlit
st.set_page_config(page_title="Healthcare Appointment Scheduler", page_icon="🩺")
st.title("🩺 Healthcare Appointment Scheduler")

name = st.text_input(" Your Full Name")
age = st.number_input(" Your Age", min_value=1, max_value=120, step=1)
symptoms = st.text_input("Describe your symptoms")
appointment_date = st.date_input(" Preferred Appointment Date", min_value=dt.today())
default_time = time(9, 0)
preferred_time = st.time_input("Preferred Time", value=default_time, step=timedelta(minutes=15))

email = st.text_input("Your Email (for confirmation)")

if st.button("Book Appointment"):
    if not all([name, age, symptoms, preferred_time, email]):
        st.warning("Please fill in all fields.")

    else:
        st.info("Detecting required department using AI...")
        user_input = f"My name is {name}. I am {age} years old. I have symptoms like {symptoms}. I prefer {preferred_time}."

        try:
            info = extract_info(user_input)
            department_raw = info.get("department", "")
            department = re.sub(r"[^a-zA-Z\s]", "", department_raw.split("(")[0]).strip().lower()
            # st.write(f" AI Detected Symptoms: {info.get('symptom', '')}")
            # st.write(f" Possible Issue: {info.get('likely_issue', '')}")
            # st.write(f" Message from AI: {info.get('message', '')}")
            # Helper function to clean text
            def clean(text):
                return str(text).replace("\\n", " ").replace("\n", " ").replace("'", "").replace('"', "").strip()

            st.write(f"Possible Issue: {clean(info.get('likely_issue', ''))}")
            st.write(f"Message from AI: {clean(info.get('message', ''))}")


            if not department:
                st.write(f" AI Extracted Department: '{department}'")
                st.warning(" Could not detect department. Please try rephrasing symptoms.")

            else:
                doctor = find_doctor(department)

                if doctor:
                    full_datetime = f"{appointment_date} {preferred_time}"

                    if check_slot(doctor, preferred_time):
                        send_email(email, doctor["name"], full_datetime, name)
                        st.success(f" Appointment with {doctor['name']} at {full_datetime} confirmed!")
                        st.write(f"AI Extracted Department: '{department}'")

                    else:
                        st.write(f" AI Extracted Department: '{department}'")
                        st.warning(" Requested slot not available. Try another time.")

                elif department == "unknown" or not department:
                    st.warning("Please describe your symptom clearly so we can find the right doctor.")

                else:
                    st.warning(f"No doctor found for department: {department}")

        except Exception as e:
            st.error(f" Failed: {str(e)}")






# import streamlit as st
# from doctordatabase import find_doctor, check_slot
# from llm import extract_info
# from email_sending import send_email
# from datetime import date, time, timedelta
# import re

# # Page setup
# st.set_page_config(page_title="Healthcare Appointment Scheduler", page_icon="🩺")
# st.title("🩺 Healthcare Appointment Scheduler")

# # User Inputs
# name = st.text_input("Your Full Name")
# age = st.number_input("Your Age", min_value=1, max_value=120)
# symptoms = st.text_area("Describe your symptoms")
# appointment_date = st.date_input("Preferred Appointment Date", min_value=date.today())
# preferred_time = st.time_input("Preferred Time", value=time(10, 0), step=timedelta(minutes=15))
# email = st.text_input("Email (for confirmation)")

# # Submit
# if st.button("Book Appointment"):
#     if not all([name.strip(), age, symptoms.strip(), email.strip()]):
#         st.warning(" Please fill in all fields.")
#     else:
#         st.info("Detecting required department using AI...")
#         try:
#             info = extract_info(symptoms)
            
#             if isinstance(info, dict):
#                 likely_issue = info.get("likely_issue", "").strip()
#                 department_raw = info.get("department", "")
#                 department = re.sub(r"[^a-zA-Z\s]", "", department_raw.split("(")[0]).strip().lower()

#                 st.markdown(f"** Likely Issue:** {likely_issue or 'Not identified'}")
#                 st.markdown(f"** Department:** {department or 'Not identified'}")

#                 if not department:
#                     st.warning(" Could not detect department. Please rephrase your symptoms.")
#                 else:
#                     doctor = find_doctor(department)
#                     if doctor:
#                         full_time = f"{appointment_date} {preferred_time}"
#                         if check_slot(doctor, preferred_time):
#                             send_email(email, doctor["name"], full_time, name)
#                             st.success(f" Appointment with **{doctor['name']}** at **{full_time}** confirmed!")
#                         else:
#                             st.warning(" Requested slot not available. Try another time.")
#                     else:
#                         st.warning(f"No doctor found for department: {department}")
#             else:
#                 st.markdown(f"** Likely Issue:** {info}")
#                 st.markdown("** Department:** general")
#                 st.warning(" Could not extract structured info. AI fallback to general department.")

#         except Exception as e:
#             st.error(f" An error occurred: {str(e)}")
