import streamlit as st
import time
import os

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
        if os.path.exists("profile.jpg"):
            st.image("profile.jpg", width=160, caption="Lead Developer")
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150, caption="Upload profile.jpg to GitHub")
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
        placeholder="e.g., fever, headache, cough, stomach pain, vomiting, weakness..."
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

# ----------------- PAGE 4: AUTOMATIC BIOMETRIC SCANNER -----------------
elif st.session_state.page == "Scanning":
    st.title("🧬 EcoScan Biometric Simulation")
    st.write("Place your finger on the circular pad. Scanning starts automatically...")
    
    # Custom CSS for a rounded scanner container with an animated up-and-down laser line
    st.markdown("""
        <style>
        .scanner-circle {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #0d1b2a;
            border: 4px solid #00E6FF;
            border-radius: 50%;
            width: 200px;
            height: 200px;
            margin: 30px auto;
            box-shadow: 0 0 25px rgba(0, 230, 255, 0.6);
            position: relative;
            overflow: hidden;
        }
        .fingerprint-design {
            font-size: 75px;
            user-select: none;
        }
        .laser-line {
            width: 100%;
            height: 4px;
            background-color: #FF0055;
            position: absolute;
            box-shadow: 0 0 15px #FF0055;
            animation: scanning 1.5s infinite ease-in-out;
        }
        @keyframes scanning {
            0% { top: 0%; }
            50% { top: 100%; }
            100% { top: 0%; }
        }
        </style>
        <div class="scanner-circle">
            <div class="laser-line"></div>
            <div class="fingerprint-design">☝️🏽</div>
            <div style="color: #00E6FF; font-size: 11px; font-weight: bold; font-family: monospace; letter-spacing: 1px; z-index: 2;">SCANNING...</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Automatically triggers progress bar animation instantly on page load
    st.info("🔄 Biometric contact established. Analyzing body temperature, pulse rate, and biomarkers...")
    progress_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.04)  # Total 4 seconds scanning time animation
        progress_bar.progress(percent_complete + 1)
        
    st.success("✅ Fingerprint, Pulse, and Vital Signs Scanned Successfully!")
    time.sleep(1.2) # Give a brief second for them to look at success message
    
    # Go straight to the results automatically without clicking anything else
    st.session_state.page = "Results"
    st.rerun()

# ----------------- PAGE 5: DIRECT STRATEGIC DIAGNOSTIC RESULTS -----------------
elif st.session_state.page == "Results":
    st.title("🏥 Diagnostic Insights & Expert Medical Advice")
    st.markdown(f"**Patient Name:** {st.session_state.patient_name}")
    st.markdown(f"**Reported Symptoms:** {st.session_state.symptoms}")
    st.markdown("---")
    
    text_lower = st.session_state.symptoms.lower()
    st.subheader("🔍 Preliminary Analysis:")
    
    # DIRECT AND STRAIGHTFORWARD CONDITION MATCHING
    if "fever" in text_lower or "headache" in text_lower or "zazzabi" in text_lower or "chills" in text_lower:
        st.error("🚨 Condition Confirmed: Malaria Infection.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Medical Testing:** Get a laboratory Blood Smear Microscopy test for Malaria parasite calculation immediately.
        2. **Treatment Protocol:** Use approved Artemisinin-based Combination Therapy (ACT) medications as directed by a healthcare official.
        3. **Hydration Care:** Increase fluid intake immediately to manage elevated body temperature.
        """)
        
    elif "cough" in text_lower or "flu" in text_lower or "catar" in text_lower or "throat" in text_lower:
        st.error("🚨 Condition Confirmed: Respiratory Tract Infection.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Airway Management:** Perform regular warm water saline gargles to reduce throat inflammation.
        2. **Symptomatic Control:** Administer direct doctor-approved expectorants or cough suppressants.
        3. **Isolation Check:** Wear a protective medical mask to curb spreading the airborne respiratory viral load.
        """)
        
    elif "stomach" in text_lower or "vomit" in text_lower or "diarrhea" in text_lower or "typhoid" in text_lower:
        st.error("🚨 Condition Confirmed: Gastrointestinal Food Poisoning.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Dehydration Control:** Drink Oral Rehydration Salts (ORS) solution immediately to restore lost electrolytes.
        2. **Dietary Restriction:** Restrict feeding to a soft, completely bland diet; strictly avoid fatty or heavily spiced food items.
        3. **Clinical Testing:** Run a Widal Test and stool culture analysis if conditions remain unchanged within 24 hours.
        """)
        
    else:
        st.warning("⚠️ Condition Confirmed: Severe Physiological Fatigue & Weakness.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Rest Recovery:** Observe a full, strict 8 hours of complete bedtime rest and zero strenuous tasks.
        2. **Immune Boosting:** Consume vital micro-nutrients, water, and fresh natural fruits to restore cellular energy levels.
        3. **Observation:** If specific pain areas surface, log them directly for medical review.
        """)
        
    st.markdown("---")
    
    if st.button("💾 Save Patient Record to History", use_container_width=True):
        record = {
            "Name": st.session_state.patient_name,
            "Address": st.session_state.patient_address,
            "Symptoms": st.session_state.symptoms,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.history.append(record)
        st.success("💾 Record saved successfully into the diagnostic dashboard history!")
        
    if st.session_state.history:
        with st.expander("📊 View Saved History Logs"):
            st.table(st.session_state.history)

    if st.button("🏠 Return to Home Page", use_container_width=True):
        go_home()
        st.rerun()
