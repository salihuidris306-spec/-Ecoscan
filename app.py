import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="EcoScan - Healthcare Innovation",
    page_icon="🩺",
    layout="centered"
)

# Manage navigation and application states using Streamlit Session State
if 'page' not in st.session_state:
    st.session_state.page = "Home"

if 'history' not in st.session_state:
    st.session_state.history = []

if 'patient_name' not in st.session_state:
    st.session_state.patient_name = ""

if 'patient_address' not in st.session_state:
    st.session_state.patient_address = ""

if 'symptoms' not in st.session_state:
    st.session_state.symptoms = ""

# Function to reset state and return to Home
def go_home():
    st.session_state.page = "Home"
    st.session_state.patient_name = ""
    st.session_state.patient_address = ""
    st.session_state.symptoms = ""

# ----------------- PAGE 1: HOME PAGE (WELCOME & DEVELOPER PROFILE) -----------------
if st.session_state.page == "Home":
    st.title("🌟 Welcome to EcoScan")
    st.subheader("Next-Generation Smart Health Assistant")
    
    st.markdown("---")
    
    # Lead Developer Profile Section
    col1, col2 = st.columns([1, 2])
    with col1:
        # Placeholder professional avatar image
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150, caption="Lead Developer")
    with col2:
        st.markdown("""
        ### Developed by: **Salihu Idris**
        *Participant, Young Innovation Challenge*
        
        **EcoScan** is an innovative medical utility application designed to bridge the gap 
        between patients and quick diagnostic assistance. It features intelligent symptom analysis 
        and digital scanning simulation to provide immediate healthcare advice.
        """)
        
    st.markdown("---")
    if st.button("🚀 Start Diagnosis", use_container_width=True):
        st.session_state.page = "Registration"
        st.rerun()

# ----------------- PAGE 2: PATIENT REGISTRATION -----------------
elif st.session_state.page == "Registration":
    st.title("📝 Patient Registration")
    st.write("Please enter the patient's personal details below.")
    
    name = st.text_input("Full Name of Patient:", value=st.session_state.patient_name)
    address = st.text_area("Home Address:", value=st.session_state.patient_address)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Home"):
            go_home()
            st.rerun()
    with col2:
        if st.button("Next: Symptoms ➡️"):
            if name and address:
                st.session_state.patient_name = name
                st.session_state.patient_address = address
                st.session_state.page = "Symptoms"
                st.rerun()
            else:
                st.error("⚠️ Please fill in all fields before proceeding!")

# ----------------- PAGE 3: SYMPTOM EVALUATION -----------------
elif st.session_state.page == "Symptoms":
    st.title("🤒 Symptom Evaluation")
    st.write(f"Patient: **{st.session_state.patient_name}**")
    
    symptoms = st.text_area(
        "Describe what you are feeling in your body (Symptoms):",
        value=st.session_state.symptoms,
        placeholder="Example: Headache, fever, chills, and body pain for 2 days..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.page = "Registration"
            st.rerun()
    with col2:
        if st.button("Next: Biometric Scan ➡️"):
            if symptoms:
                st.session_state.symptoms = symptoms
                st.session_state.page = "Scanning"
                st.rerun()
            else:
                st.error("⚠️ Please describe the symptoms!")

# ----------------- PAGE 4: BIOMETRIC SCANNER (SIMULATION) -----------------
elif st.session_state.page == "Scanning":
    st.title("🧬 EcoScan Biometric Simulation")
    st.write("Place your finger on the virtual scanner below to capture vital signs.")
    
    scan_placeholder = st.empty()
    
    # Simulated biometric interaction
    finger_placed = st.checkbox("👉 PLACE YOUR FINGER HERE TO START SCANNING")
    
    if finger_placed:
        with scan_placeholder.container():
            st.info("🔄 Connection established. Analyzing pulse and body temperature...")
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.03)  # Smooth scanning animation
                progress_bar.progress(percent_complete + 1)
            st.success("✅ Scan Completed Successfully!")
            
        if st.button("View Diagnostic Results & Advice ➡️", use_container_width=True):
            st.session_state.page = "Results"
            st.rerun()
    else:
        st.warning("Waiting for finger placement...")
        if st.button("⬅️ Back"):
            st.session_state.page = "Symptoms"
            st.rerun()

# ----------------- PAGE 5: DIAGNOSTIC RESULTS & MEDICAL ADVICE -----------------
elif st.session_state.page == "Results":
    st.title("🏥 Diagnostic Insights & Expert Medical Advice")
    st.markdown(f"**Patient Name:** {st.session_state.patient_name}")
    st.markdown(f"**Reported Symptoms:** {st.session_state.symptoms}")
    st.markdown("---")
    
    # Automated text analysis logic to deliver targeted feedback
    text_lower = st.session_state.symptoms.lower()
    
    st.subheader("🔍 Preliminary Analysis:")
    if "fever" in text_lower or "headache" in text_lower or "zazzabi" in text_lower or "ciwon kai" in text_lower:
        st.warning("⚠️ High probability of Malaria or Bacterial Infection.")
        
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Get Tested:** Visit the nearest medical laboratory for a rapid diagnostic test (RDT) or microscopy for Malaria.
        2. **Stay Hydrated:** Drink plenty of clean water to manage the body temperature.
        3. **Medication:** Take antipyretics like Paracetamol only as prescribed for temporary relief, and complete a full course of anti-malarial medication if tested positive.
        4. **Prevention:** Sleep under a treated mosquito net and eliminate stagnant water around your home.
        """)
    else:
        st.info("ℹ️ General symptoms detected. Requires baseline monitoring.")
        
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Rest:** Get at least 8 hours of sleep to boost your immune system.
        2. **Observation:** Monitor your body parameters closely over the next 24 hours.
        3. **Consultation:** If symptoms worsen or persist, please report directly to a certified clinical staff.
        """)
        
    st.markdown("---")
    
    # Save Feature to Session Log
    if st.button("💾 Save Patient Record to History", use_container_width=True):
        record = {
            "Name": st.session_state.patient_name,
            "Address": st.session_state.patient_address,
            "Symptoms": st.session_state.symptoms,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.history.append(record)
        st.success("💾 Record saved successfully into the diagnostic dashboard history!")
        
    # Historical Records Display Expansion Area
    if st.session_state.history:
        with st.expander("📊 View Saved History Logs"):
            st.table(st.session_state.history)

    if st.button("🏠 Return to Home Page", use_container_width=True):
        go_home()
        st.rerun()
