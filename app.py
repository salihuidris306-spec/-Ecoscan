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
        # Tries to load your custom photo from GitHub repo; falls back to avatar icon if not uploaded yet
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

# ----------------- PAGE 4: BIOMETRIC SCANNER (ROUNDED DESIGN) -----------------
elif st.session_state.page == "Scanning":
    st.title("🧬 EcoScan Biometric Simulation")
    st.write("Place your finger on the circular scanner pad below to capture vital signs.")
    
    # Custom CSS for a PERFECTLY ROUNDED/CIRCULAR glowing fingerprint container
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
            cursor: pointer;
            user-select: none;
            animation: pulse-effect 1.5s infinite alternate;
        }
        @keyframes pulse-effect {
            from { transform: scale(0.95); opacity: 0.7; }
            to { transform: scale(1.05); opacity: 1; }
        }
        </style>
        <div class="scanner-circle">
            <div class="fingerprint-design">☝️🏽</div>
            <div style="color: #00E6FF; font-size: 11px; font-weight: bold; font-family: monospace; letter-spacing: 1px;">SCAN PAD</div>
        </div>
    """, unsafe_allow_html=True)
    
    scan_placeholder = st.empty()
    finger_placed = st.checkbox("👉 SIMULATE FINGER PLACEMENT (TOUCH PAD)")
    
    if finger_placed:
        with scan_placeholder.container():
            st.info("🔄 Biometric contact detected! Synchronizing vitals and data...")
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.03)  
                progress_bar.progress(percent_complete + 1)
            st.success("✅ Vital signs captured successfully!")
            
        if st.button("View Diagnostic Results & Advice ➡️", use_container_width=True):
            st.session_state.page = "Results"
            st.rerun()
    else:
        st.warning("Awaiting biometric input... Please check the box above.")
        if st.button("⬅️ Back"):
            st.session_state.page = "Symptoms"
            st.rerun()

# ----------------- PAGE 5: SMART DIAGNOSTIC RESULTS & MEDICAL ADVICE -----------------
elif st.session_state.page == "Results":
    st.title("🏥 Diagnostic Insights & Expert Medical Advice")
    st.markdown(f"**Patient Name:** {st.session_state.patient_name}")
    st.markdown(f"**Reported Symptoms:** {st.session_state.symptoms}")
    st.markdown("---")
    
    text_lower = st.session_state.symptoms.lower()
    st.subheader("🔍 Preliminary Analysis:")
    
    # ADVANCED MULTI-DISEASE DETECTION ENGINE
    if "fever" in text_lower or "headache" in text_lower or "zazzabi" in text_lower or "chills" in text_lower:
        st.warning("⚠️ High Clinical Correlation: Suspicion of Malaria or Acute Bacterial Infection.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Laboratory Confirmation:** Undergo a blood smear microscopy or Rapid Diagnostic Test (RDT) for Malaria.
        2. **Hydration Management:** Consume increased volumes of fluids to counteract thermal perspiration.
        3. **Therapeutic Action:** Administer Antipyretics (e.g., Paracetamol) for symptomatic pyrexia management, and consult a physician for appropriate ACT prescription if positive.
        """)
        
    elif "cough" in text_lower or "flu" in text_lower or "catar" in text_lower or "throat" in text_lower:
        st.warning("⚠️ High Clinical Correlation: Respiratory Tract Irritation / Viral Upper Respiratory Infection.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Respiratory Support:** Practice warm saline gargles and stay in well-ventilated spaces.
        2. **Symptomatic Relief:** Use over-the-counter expectorants or mucolytics if congestion worsens.
        3. **Red Flags:** Seek immediate critical attention if breathing difficulty or chest retraction develops.
        """)
        
    elif "stomach" in text_lower or "vomit" in text_lower or "diarrhea" in text_lower or "typhoid" in text_lower:
        st.warning("⚠️ High Clinical Correlation: Gastrointestinal Infection / Potential Food Poisoning or Gastroenteritis.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Electrolyte Replacement:** Administer Oral Rehydration Salts (ORS) instantly to avoid systemic dehydration.
        2. **Dietary Changes:** Maintain a bland diet (BRAT protocol) and strictly avoid oily, spiced food elements.
        3. **Clinical Testing:** A stool analysis or Widal test is recommended if condition persists beyond 48 hours.
        """)
        
    else:
        st.info("ℹ️ Baseline Assessment: General physiological fatigue or unspecified low-grade viral prodrome.")
        st.subheader("💡 Recommended Medical Advice:")
        st.write("""
        1. **Rest Optimization:** Ensure complete physical rest and a minimum of 8 hours of quality sleep.
        2. **Nutritional Reinforcement:** Boost immune health by consuming fresh fruits and micronutrient-dense items.
        3. **Monitoring Protocol:** Record core metrics regularly. If local localized symptoms arise, schedule a clinical checkup.
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
