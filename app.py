import streamlit as st
import time

# Set up app title and configuration
st.set_page_config(page_title="EcoScan Health Assistant", page_icon="🏥")
st.title("🏥 EcoScan Rural Health Assistant")
st.write("---")

# Initialize session state to manage step-by-step navigation
if 'step' not in st.session_state:
    st.session_state.step = 1

# ----------------- STEP 1: PATIENT REGISTRATION -----------------
if st.session_state.step == 1:
    st.subheader("Step 1: Patient Registration")
    st.write("Please enter your personal details below.")
    
    name = st.text_input("Full Name")
    address = st.text_input("Home Address")
    
    if st.button("Proceed to Medical Assessment ➡️"):
        if name and address:
            st.session_state.name = name
            st.session_state.address = address
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("Please enter your name and address before proceeding.")

# ----------------- STEP 2: SYMPTOMS ASSESSMENT -----------------
elif st.session_state.step == 2:
    st.subheader(f"Step 2: Symptoms Assessment (Patient: {st.session_state.name})")
    st.write("Please describe what you are feeling in detail.")
    
    symptoms = st.text_area("What symptoms are you experiencing? (e.g., Fever, Headache, Cough...)")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Go Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Proceed to Vital Scan ➡️"):
            if symptoms:
                st.session_state.symptoms = symptoms
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("Please write down your symptoms before proceeding.")

# ----------------- STEP 3: SCANNER & DIAGNOSIS -----------------
elif st.session_state.step == 3:
    st.subheader("Step 3: Biometric Vital Scan")
    
    st.warning("⚠️ **Instruction:** Please place your finger on your screen or device sensor to scan your vitals, body temperature, and pulse.")
    
    # Visual representation of the scanner
    st.markdown("""
    <div style="background-color:#1e293b; border: 3px solid #00ffcc; border-radius: 50%; width: 150px; height: 150px; margin: 20px auto; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 15px #00ffcc;">
        <span style="color:#00ffcc; font-size: 40px; font-weight: bold; animation: pulse 1.5s infinite;">🔴</span>
    </div>
    <p style="text-align: center; color: #00ffcc; font-weight: bold;">[ PLACE YOUR FINGER HERE ]</p>
    """, unsafe_allow_html=True)
    
    if st.button("Start Scanning 🧬"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            time.sleep(0.03)
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"Scanning body vitals: {percent_complete + 1}%")
        
        status_text.success("Scan completed successfully! ✅")
        st.write("---")
        
        # AI Diagnosis Logic
        st.subheader("📋 Medical Diagnosis Results")
        
        symptoms_lower = st.session_state.symptoms.lower()
        
        # Checking symptoms to match with a diagnosis
        if "fever" in symptoms_lower or "zazzabi" in symptoms_lower or "hot" in symptoms_lower:
            illness = "Malaria Fever"
            advice = """
            1. **Medication:** Consult a healthcare professional or community health worker for recommended antimalarial treatment (like ACT).
            2. **Rest & Hydration:** Get plenty of bed rest and drink clean, safe water regularly.
            3. **Prevention:** Sleep under a treated mosquito net and ensure your surroundings are free from stagnant water.
            """
        elif "headache" in symptoms_lower or "ciwon kai" in symptoms_lower:
            illness = "Stress or Elevated Blood Pressure"
            advice = """
            1. **Rest:** Lie down in a quiet, cool, and dark room to reduce tension.
            2. **Hydration:** Drink 2 to 3 glasses of water immediately.
            3. **Monitoring:** If the headache persists, please get your Blood Pressure (BP) checked at the nearest health center.
            """
        elif "diarrhea" in symptoms_lower or "gudawa" in symptoms_lower or "zawo" in symptoms_lower:
            illness = "Gastroenteritis / Watery Stool"
            advice = """
            1. **Rehydration:** Drink Oral Rehydration Salts (ORS) or a salt-sugar solution immediately to replace lost fluids.
            2. **Diet:** Avoid oily, spicy, or heavy foods. Stick to light meals like porridge or bananas.
            3. **Hygiene:** Ensure strict handwashing with soap and clean water before meals.
            """
        else:
            illness = "General Body Fatigue or Mild Viral Infection"
            advice = """
            1. **Rest:** Your body needs adequate sleep (at least 8 hours).
            2. **Nutrition:** Eat balanced, nutritious meals and include fresh fruits or vegetables.
            3. **Follow-up:** If symptoms do not improve within 48 hours, visit the nearest medical clinic.
            """
            
        st.error(f"**Diagnosis Suggests:** The patient might be suffering from: **{illness}**")
        st.info(f"**Recommendations & Guidelines:** \n{advice}")
        
    if st.button("⬅️ Restart New Assessment"):
        st.session_state.step = 1
        st.rerun()
