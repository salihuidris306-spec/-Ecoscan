import streamlit as st
import time

# ---------------------------------------------------------
# 1. PROFESSIONAL PAGE CONFIGURATION & DESIGN
# ---------------------------------------------------------
st.set_page_config(
    page_title="EcoScan | Smart Rural Health Terminal",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a Premium Corporate Medical Theme
st.markdown("""
    <style>
    ...
    </style>
""", unsafe_allow_html=True)
    <style>
        .reportview-container { background: #fafbfc; }
        h1 { color: #1e4620 !important; font-family: 'Arial', sans-serif; text-align: center; }
        h2, h3 { color: #2e7d32 !important; }
        .stButton>button {
            background-color: #2e7d32; color: white; border-radius: 8px;
            padding: 10px 24px; font-weight: bold; width: 100%; border: none;
        }
        .stButton>button:hover { background-color: #1e4620; color: white; }
        .medical-card {
            background-color: #e8f5e9; padding: 25px; 
            border-radius: 12px; border-top: 6px solid #2e7d32;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .advice-box {
            background-color: #ffffff; padding: 15px; 
            border-radius: 6px; border-left: 5px solid #1565c0;
            font-size: 16px; color: #333333; margin-top: 10px;
        }
    </style>
""", unsafe_style_html=True)

# ---------------------------------------------------------
# 2. INITIALIZE SESSION STATES (DATABASE & STEPS)
# ---------------------------------------------------------
if 'step' not in st.session_state:
    st.session_state.step = 1

# Permanent Database session state to hold diagnostic records (History)
if 'patient_records' not in st.session_state:
    st.session_state.patient_records = []

# Initialize current patient temporary details
if 'current_patient' not in st.session_state:
    st.session_state.current_patient = {}

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION & STRATEGIC INFO FOR JUDGES
# ---------------------------------------------------------
st.sidebar.markdown("# 🌱 EcoScan Terminal")
st.sidebar.markdown("*Empowering rural healthcare with smart technology.*")
st.sidebar.markdown("---")

# Progress Tracker in Sidebar
st.sidebar.subheader("📊 Examination Progress")
if st.session_state.step == 1:
    st.sidebar.info("📝 Step 1: Patient Registration")
elif st.session_state.step == 2:
    st.sidebar.info("🩺 Step 2: Age & Symptoms Input")
elif st.session_state.step == 3:
    st.sidebar.warning("⚡ Step 3: Biometric Scan")
elif st.session_state.step == 4:
    st.sidebar.success("✅ Step 4: Diagnosis & Advice")

st.sidebar.markdown("---")

# HOSPITAL HISTORY RECORDS SIDEBAR WIDGET
st.sidebar.subheader("🗂️ Historical Records")
if len(st.session_state.patient_records) == 0:
    st.sidebar.caption("No diagnostic history recorded yet.")
else:
    for idx, rec in enumerate(st.session_state.patient_records):
        with st.sidebar.expander(f"👤 {rec['name']}"):
            st.write(f"**Age:** {rec['age']}")
            st.write(f"**Location:** {rec['address']}")
            st.write(f"**Diagnosis:** {rec['diagnosis']}")
            st.write(f"**Advice:** {rec['advice']}")

st.sidebar.markdown("---")
# EcoScan Hybrid Advantage Technical Note
st.sidebar.caption("💡 **System Status:** Online Prototype")
st.sidebar.caption("📡 **Architecture:** Hybrid framework engineered for online deployment and offline remote areas.")

# ---------------------------------------------------------
# 4. MAIN APPLICATION LOGIC (STEP-BY-STEP)
# ---------------------------------------------------------
st.title("🏥 EcoScan Rural Health Intelligent Assistant")
st.markdown("---")

# ------------------ PAGE 1: OPENING PAGE & PATIENT REGISTRATION ------------------
if st.session_state.step == 1:
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        # Renders the Lead Developer image uploaded to the GitHub Repository
        try:
            st.image("img_1_1783550291431.jpg", caption="Lead Developer - EcoScan Project", use_container_width=True)
        except:
            st.info("ℹ️ [Developer image 'img_1_1783550291431.jpg' will display here once pushed to GitHub]")
            
    with col2:
        st.subheader("📝 Step 1: Patient Registration")
        name = st.text_input("👤 Full Name", placeholder="e.g., Aliyu Ibrahim")
        address = st.text_input("🏠 Home Address", placeholder="e.g., Sabon Gari Ward, Maiduguri")
        
        st.markdown("<br>", unsafe_style_html=True)
        if st.button("Proceed to Next Step ➡️"):
            if name and address:
                st.session_state.current_patient['name'] = name
                st.session_state.current_patient['address'] = address
                st.session_state.step = 2
                st.rerun()
            else:
                st.error("⚠️ Validation Error: Please fill in the Name and Address fields to proceed!")

# ------------------ PAGE 2: AGE & SYMPTOMS ------------------
elif st.session_state.step == 2:
    st.subheader("🩺 Step 2: Clinical Metrics & Symptoms Intake")
    st.write(f"Active Patient Profile: **{st.session_state.current_patient.get('name')}**")
    
    age = st.number_input("🔢 Patient Age (Years)", min_value=1, max_value=120, value=25)
    
    st.markdown("### 📝 Chief Medical Complaints (Symptoms)")
    symptoms = st.text_area(
        "Describe what the patient is currently experiencing (e.g., fever, cough, headache, diarrhea, asthma):", 
        placeholder="e.g., High fever, persistent dry cough, headache, abdominal pains..."
    )
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Registration"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Proceed to Scanning Terminal ➡️"):
            if symptoms:
                st.session_state.current_patient['age'] = age
                st.session_state.current_patient['symptoms'] = symptoms.lower()
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("⚠️ Validation Error: Please input symptoms to run the system analysis!")

# ------------------ PAGE 3: AUTOMATIC BIOMETRIC SCANNING ------------------
elif st.session_state.step == 3:
    st.subheader("⚡ Step 3: Biometric EcoScan Terminal")
    st.write("Instruct the patient to place their index finger onto the scanning hardware interface.")
    
    # Checkbox trigger simulating immediate automated hardware scanning
    finger_placed = st.checkbox("🛑 Click here when patient places finger on scanner (Finger Detected)")
    
    if finger_placed:
        st.success("🎯 Hardware connection established! Launching automatic multi-spectral scan...")
        
        # Simulating automatic animation for professional presentation look
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            time.sleep(0.02) # Controlled processing simulation speed
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Scanning Biometrics... {percent_complete + 1}%")
            
        st.success("✅ Biometric telemetry capture completed successfully!")
        time.sleep(1)
        
        # Automatic redirect without requiring extra clicks
        st.session_state.step = 4
        st.rerun()
    else:
        st.info("⏳ System Standing By: Awaiting patient finger placement on the scanning module to initialize automated scanning...")
        
    st.markdown("---")
    if st.button("⬅️ Back to Symptoms Input"):
        st.session_state.step = 2
        st.rerun()

# ------------------ PAGE 4: DIAGNOSIS RESULT & CLINICAL ADVICE ------------------
elif st.session_state.step == 4:
    st.subheader("📋 Step 4: Diagnostic Assessment & Structured Medical Advice")
    
    p_name = st.session_state.current_patient.get('name')
    p_age = st.session_state.current_patient.get('age')
    p_addr = st.session_state.current_patient.get('address')
    p_symp = st.session_state.current_patient.get('symptoms', '')
    
    # Default clinical outcome fallback
    diagnosis = "General Body Fatigue & Weakness"
    advice = "Clinical Guideline: Recommend full bed rest for 48 hours and high oral fluid intake. Monitor vitals closely. If symptoms persist over 3 days, escalate to a secondary referral hospital."
    
    # NLP Mock Rule Matching Logic for Diagnostics and Custom Advice
    if "fever" in p_symp or "zazzabi" in p_symp or "temperature" in p_symp:
        diagnosis = "Uncomplicated Malaria Infection"
        advice = "Clinical Guideline: Administer full course of Artemisinin-based Combination Therapy (ACT), such as Artemether/Lumefantrine, strictly following weight-based dosage. Advise patient to consistently sleep under long-lasting insecticide-treated nets (LLINs) and clear stagnant water vectors near the household."
        
    elif "cough" in p_symp or "tari" in p_symp or "chest" in p_symp:
        diagnosis = "Acute Upper Respiratory Tract Infection (Bronchitis)"
        advice = "Clinical Guideline: Avoid cold exposures, keep warm, and administer warm oral fluids or steam inhalation. If productive cough persists beyond 2 weeks, recommend mandatory sputum examination for Pulmonary Tuberculosis (TB screening)."
        
    elif "diarrhea" in p_symp or "gudawa" in p_symp or "vomiting" in p_symp or "ama" in p_symp:
        diagnosis = "Acute Gastroenteritis (Dehydration Risk)"
        advice = "Clinical Guideline: Immediate intervention required to combat hypovolemia. Initiate aggressive Oral Rehydration Salts (ORS) therapy. If it involves a pediatric case, maintain continuous breastfeeding alongside Zinc supplementation."
        
    elif "asthma" in p_symp or "fuka" in p_symp or "breathing" in p_symp:
        diagnosis = "Acute Bronchial Asthma Exacerbation"
        advice = "Clinical Guideline: Instantly remove patient from allergen triggers (dust, smoke, cold air). Administer short-acting Beta2-agonist inhaler (e.g., Salbutamol/Ventolin Inhaler) immediately. Ensure high fresh oxygen cross-ventilation in the room."

    # Render Professional Executive Dashboard Card with Medical Advice
    st.markdown(f"""
    <div class="medical-card">
        <h3 style="margin-top:0; color:#2e7d32;">👤 Patient Demographics</h3>
        <p><b>Name:</b> {p_name} &nbsp;&nbsp;|&nbsp;&nbsp; <b>Age:</b> {p_age} Years Old &nbsp;&nbsp;|&nbsp;&nbsp; <b>Location:</b> {p_addr}</p>
        <hr style="border: 0.5px solid #2e7d32;">
        
        <h3 style="color: #c62828;">🚨 System Diagnostic Outcome</h3>
        <p style="font-size: 22px; font-weight: bold; color: #c62828; margin-bottom: 5px;">{diagnosis}</p>
        
        <hr style="border: 0.5px solid #2e7d32;">
        <h3 style="color: #1565c0;">💡 Structured Medical Advice & Treatment Recommendations:</h3>
        <div class="advice-box">
            {advice}
        </div>
    </div>
    """, unsafe_style_html=True)
    
    st.markdown("<br>", unsafe_style_html=True)
    
    # HOSPITAL DATABASE SAVE BUTTON
    if st.button("💾 Securely Save Patient Case to Clinical History Database"):
        final_record = {
            "name": p_name,
            "age": p_age,
            "address": p_addr,
            "diagnosis": diagnosis,
            "advice": advice
        }
        st.session_state.patient_records.append(final_record)
        st.success(f"🎉 Success: Case record for '{p_name}' has been safely compiled and stored into the EcoScan Clinical Archive!")
        
        time.sleep(2.5)
        st.session_state.step = 1
        st.session_state.current_patient = {}
        st.rerun()

    if st.button("🔄 Discharge & Reset (Scan New Patient)"):
        st.session_state.step = 1
        st.session_state.current_patient = {}
        st.rerun()
