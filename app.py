import streamlit as st
import pandas as pd
import time
import os

# --- 1. SET PAGE CONFIG & FILES ---
st.set_page_config(page_title="EcoScan - Smart Health Assistant", page_icon="🌿", layout="centered")

DATABASE_FILE = "ecoscan_records.csv"

def load_patient_records():
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    return pd.DataFrame(columns=["ID", "Name", "Residential Address", "Symptoms / Complaints", "Time"])

def save_patient_record(p_id, name, address, symptoms):
    df_existing = load_patient_records()
    new_data = pd.DataFrame([{
        "ID": p_id,
        "Name": name,
        "Residential Address": address,
        "Symptoms / Complaints": symptoms,
        "Time": time.strftime("%Y-%m-%d %H:%M:%S")
    }])
    df_combined = pd.concat([df_existing, new_data], ignore_index=True)
    df_combined.to_csv(DATABASE_FILE, index=False)

# INITIALIZE PAGE SYSTEM (1 to 5)
if "page" not in st.session_state:
    st.session_state.page = 1
if "patient_name" not in st.session_state:
    st.session_state.patient_name = ""
if "patient_address" not in st.session_state:
    st.session_state.patient_address = ""
if "symptoms" not in st.session_state:
    st.session_state.symptoms = ""

# --- 2. PREMIUM GREEN DESIGN STYLING (CSS) ---
st.markdown(
    """
    <style>
    .stApp { background-color: #F4F7F5 !important; }
    .metric-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
    .metric-title { color: #6C757D; font-size: 13px; font-weight: 600; text-transform: uppercase; }
    .metric-value-green { color: #1E5E3A; font-size: 24px; font-weight: bold; }
    .metric-value-accent { color: #28A745; font-size: 24px; font-weight: bold; }
    .metric-value-warning { color: #D9381E; font-size: 24px; font-weight: bold; }
    
    .stButton>button {
        background-color: #1E5E3A !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        width: 100%;
        border: none !important;
    }
    .stButton>button:hover { background-color: #144026 !important; }
    
    label {
        color: #1E5E3A !important;
        font-weight: bold !important;
        font-size: 16px !important;
        margin-bottom: 5px !important;
        display: block !important;
    }
    div.stTextInput, div.stTextArea {
        margin-bottom: 20px !important;
    }
    
    /* Custom Styling for the History List View */
    .history-list-item {
        background-color: #ffffff;
        padding: 12px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 14px;
        color: #2D3748;
    }
    .history-list-item:last-child {
        border-bottom: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def go_to_page(page_num):
    st.session_state.page = page_num
    st.rerun()

def reset_app():
    st.session_state.patient_name = ""
    st.session_state.patient_address = ""
    st.session_state.symptoms = ""
    st.session_state.page = 1
    st.rerun()

# --- 3. MEDICAL DIAGNOSTIC ENGINE ---
def analyze_symptoms(symptoms_text):
    text = symptoms_text.lower()
    
    if "malaria" in text or ("fever" in text and "chills" in text) or ("fever" in text and "headache" in text):
        return {
            "disease": "Suspected Malaria Infection",
            "status": "Needs Attention",
            "heart_rate": "88 bpm (Elevated)",
            "assessment": "Feverish",
            "color_class": "metric-value-warning",
            "chart_data": [40, 55, 62, 70, 85, 78, 90, 88],
            "advice": """
                - **Immediate Action:** Get a rapid diagnostic blood test (RDT) at the nearest clinic to confirm.
                - **Medication:** If confirmed, use prescribed Artemisinin-based Combination Therapy (ACTs) like Lumartem or Coartem under medical guidance. Take Paracetamol for fever management.
                - **Recovery Support:** Sleep under a treated mosquito net, drink plenty of fluids to fight dehydration, and get absolute bed rest.
            """
        }
    elif "typhoid" in text or ("fever" in text and "stomach" in text) or ("fever" in text and "vomit" in text):
        return {
            "disease": "Suspected Typhoid Fever",
            "status": "Needs Attention",
            "heart_rate": "82 bpm",
            "assessment": "Infection Risk",
            "color_class": "metric-value-warning",
            "chart_data": [35, 42, 50, 65, 75, 80, 83, 82],
            "advice": """
                - **Immediate Action:** Medical evaluation via blood culture or Widal test is recommended. Requires target antibiotic therapies.
                - **Care Guidelines:** Drink only boiled or properly treated pure drinking water. Consume easily digestible light, warm meals.
                - **Hygiene Plan:** Wash hands rigorously with soap after using restrooms and before any handling of food.
            """
        }
    elif "cough" in text or "catarrh" in text or "flu" in text or "chest" in text:
        return {
            "disease": "Acute Respiratory Tract Inflammation / Flu",
            "status": "Stable",
            "heart_rate": "76 bpm",
            "assessment": "Mild Illness",
            "color_class": "metric-value-warning",
            "chart_data": [25, 30, 45, 55, 60, 58, 62, 76],
            "advice": """
                - **Immediate Action:** Take warm steam inhalations twice daily to loosen congestion. Use a cough expectorant or lozenges.
                - **Dietary Boost:** Increase Vitamin C intake through citrus fruits (oranges, lemons) or supplements, and drink warm ginger tea with honey.
                - **Prevention:** Avoid cold environments and wear a mask in dusty or public areas to limit transmission or airway irritation.
            """
        }
    else:
        return {
            "disease": "Condition Is Normal / Healthy Profile",
            "status": "Stable",
            "heart_rate": "72 bpm",
            "assessment": "Healthy",
            "color_class": "metric-value-accent",
            "chart_data": [20, 38, 29, 48, 56, 42, 68, 32],
            "advice": """
                - **Assessment:** Your current biometric parameters and reported inputs align within acceptable healthy baseline metrics. 
                - **Maintenance Advice:** Continue eating balanced meals, drink at least 3 liters of water daily, and aim for 7-8 hours of sound sleep.
                - **Notice:** If you develop any sudden symptoms later, log them here immediately or consult your medical officer.
            """
        }

patient_id = f"ES-{st.session_state.patient_name[:2].upper() if len(st.session_state.patient_name) > 2 else '88'}21"

# ==========================================
# PAGE 1: OPENING PAGE
# ==========================================
if st.session_state.page == 1:
    st.markdown(
        """
        <div style="background-color: #1E5E3A; padding: 35px; border-radius: 12px; color: white; text-align: center; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 34px; font-weight: bold;">🌟 Welcome to EcoScan</h1>
            <p style="margin: 8px 0 0 0; font-size: 18px; opacity: 0.9; font-weight: 500;">Next-Generation Smart Health Assistant</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-bottom: 25px;">
            <div style="width: 130px; height: 130px; background-color: #E2E8F0; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 3px solid #1E5E3A;">
                <span style="color: #4A5568; font-size: 14px; font-weight: bold; text-align: center;">EcoScan<br>Core</span>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.03); margin-bottom: 30px; border-left: 5px solid #28A745; text-align: center;">
            <h3 style="color: #1E5E3A; margin-top: 0; font-size: 22px;">Developed by: Salihu Idris</h3>
            <p style="color: #4A5568; font-style: italic; font-size: 14px; margin-bottom: 15px;">Participant, Young Innovation Challenge</p>
            <hr style="border: 0; border-top: 1px solid #E2E8F0;">
            <p style="margin: 10px 0 0 0; color: #718096; line-height: 1.6; font-size: 14.5px;">
                EcoScan is an innovative medical utility application designed to bridge the gap between patients and quick diagnostic assistance. 
                It features intelligent symptom analysis and digital scanning simulation to provide immediate healthcare advice.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    
    if st.button("Get Started / Enter App 🚀"):
        go_to_page(2)

# ==========================================
# PAGE 2: PATIENT REGISTRATION FORM
# ==========================================
elif st.session_state.page == 2:
    st.markdown("<h2 style='color:#1E5E3A;'>📝 Page 2: Patient Registration Form</h2>", unsafe_allow_html=True)
    st.write("Enter patient details to launch the health assessment.")
    
    st.session_state.patient_name = st.text_input("Full Name of the Patient:", value=st.session_state.patient_name)
    st.session_state.patient_address = st.text_area("Patient Address:", value=st.session_state.patient_address)
    
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back To Home"): go_to_page(1)
    with col2:
        if st.button("Next ➡️"):
            if st.session_state.patient_name.strip() and st.session_state.patient_address.strip():
                go_to_page(3)
            else:
                st.error("⚠️ Please enter Name and Address before you proceed.")

# ==========================================
# PAGE 3: PATIENT ILLNESS DETAILS (SYMPTOMS)
# ==========================================
elif st.session_state.page == 3:
    st.markdown("<h2 style='color:#1E5E3A;'>🏥 Page 3: Body Condition Details</h2>", unsafe_allow_html=True)
    st.info(f"📋 Patient: {st.session_state.patient_name}")
    
    st.session_state.symptoms = st.text_area(
        "What are you feeling in your body regarding this illness?",
        value=st.session_state.symptoms,
        placeholder="Example: Headache, Fever, Cough, Malaria symptoms..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Go Back"): go_to_page(2)
    with col2:
        if st.button("Next ➡️"):
            if st.session_state.symptoms.strip(): go_to_page(4)
            else: st.error("Please write what you are feeling in your body.")

# ==========================================
# PAGE 4: SCANNING INTERFACE (BIOMETRIC ONLY)
# ==========================================
elif st.session_state.page == 4:
    st.markdown("<h2 style='color:#1E5E3A;'>🧬 Page 4: Biometric Fingerprint Scanner</h2>", unsafe_allow_html=True)
    st.write("Touch the circle below to start scanning the fingerprint.")
    
    st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; margin: 30px 0;'>
            <div style='width: 140px; height: 140px; background: radial-gradient(circle, #2CE062 0%, #1E5E3A 100%); 
            border-radius: 50%; display: flex; justify-content: center; align-items: center; 
            box-shadow: 0px 0px 25px rgba(44, 224, 98, 0.6); color: white; font-weight: bold; font-size: 14px; text-align:center;'>
                ☝️ PLACE<br>FINGER
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Go Back"): go_to_page(3)
    with col2:
        if st.button("START SCANNING NOW"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            for percent in range(0, 101, 25):
                time.sleep(0.4)
                progress_bar.progress(percent)
                status_text.text(f"Scanning fingerprint and analyzing vital signs... {percent}%")
            
            st.success("✅ Analysis completed successfully!")
            time.sleep(0.5)
            go_to_page(5)

# ==========================================
# PAGE 5: DIAGNOSTIC DASHBOARD & RESULTS
# ==========================================
elif st.session_state.page == 5:
    diagnosis = analyze_symptoms(st.session_state.symptoms)

    st.markdown(
        f"""
        <div style="background-color: #1E5E3A; padding: 22px; border-radius: 12px; color: white; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 26px; font-weight: bold;">🌿 EcoScan</h1>
            <p style="margin: 6px 0 0 0; font-size: 16px; opacity: 0.9;">DIAGNOSTIC REPORT: Patient ID {patient_id}</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    row1_col1
