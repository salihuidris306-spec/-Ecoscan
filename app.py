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
if "patient_photo" not in st.session_state:
    st.session_state.patient_photo = None

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
    
    /* Global labels formatting to fix visibility and leveling */
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
    st.session_state.patient_photo = None
    st.session_state.page = 1
    st.rerun()

# Fix for photo reset on mobile
def capture_photo_callback():
    if st.session_state.camera_widget is not None:
        st.session_state.patient_photo = st.session_state.camera_widget

patient_id = f"ES-{st.session_state.patient_name[:2].upper() if len(st.session_state.patient_name) > 2 else '88'}21"

# ==========================================
# PAGE 1: OPENING PAGE (DEVELOPER & WELCOME ONLY)
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
        placeholder="Example: Headache, Fever, Cough..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Go Back"): go_to_page(2)
    with col2:
        if st.button("Next ➡️"):
            if st.session_state.symptoms.strip(): go_to_page(4)
            else: st.error("Please write what you are feeling in your body.")

# ==========================================
# PAGE 4: SCANNING INTERFACE (BIOMETRIC)
# ==========================================
elif st.session_state.page == 4:
    st.markdown("<h2 style='color:#1E5E3A;'>🧬 Page 4: Biometric Fingerprint Scanner</h2>", unsafe_allow_html=True)
    st.write("Look at the camera then touch the circle below to start scanning.")
    
    # Using key and on_change callback locks the snapshot safely into memory on phones
    st.camera_input("Patient Identity Capture", key="camera_widget", on_change=capture_photo_callback)
    
    if st.session_state.patient_photo is not None:
        st.success("📸 Photo locked in successfully!")

    st.write("---")
    st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; margin: 15px 0;'>
            <div style='width: 130px; height: 130px; background: radial-gradient(circle, #2CE062 0%, #1E5E3A 100%); 
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
            if st.session_state.patient_photo is None:
                st.warning("⚠️ Please stand in front of the camera to take a photo before completing the fingerprint scan.")
            else:
                progress_bar = st.progress(0)
                status_text = st.empty()
                for percent in range(0, 101, 25):
                    time.sleep(0.4)
                    progress_bar.progress(percent)
                    status_text.text(f"Scanning fingerprint and verifying photo... {percent}%")
                
                st.success("✅ Analysis completed!")
                time.sleep(0.5)
                go_to_page(5)

# ==========================================
# PAGE 5: DIAGNOSTIC DASHBOARD & RESULTS
# ==========================================
elif st.session_state.page == 5:
    st.markdown(
        f"""
        <div style="background-color: #1E5E3A; padding: 22px; border-radius: 12px; color: white; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 26px; font-weight: bold;">🌿 EcoScan</h1>
            <p style="margin: 6px 0 0 0; font-size: 16px; opacity: 0.9;">DIAGNOSTIC REPORT: Patient ID {patient_id}</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    col_left, col_right = st.columns([2.8, 1.2])
    
    with col_right:
        if st.session_state.patient_photo is not None:
            st.image(st.session_state.patient_photo, use_container_width=True)
            
    with col_left:
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)
        
        with row1_col1:
            st.markdown('<div class="metric-box"><div class="metric-title">Biometric:</div><div class="metric-value-green">VERIFIED</div></div>', unsafe_allow_html=True)
        with row1_col2:
            st.markdown('<div class="metric-box"><div class="metric-title">Heart Rate:</div><div class="metric-value-green">72 bpm</div></div>', unsafe_allow_html=True)
        with row2_col1:
            st.markdown('<div class="metric-box"><div class="metric-title">Vitals:</div><div class="metric-value-green">Stable</div></div>', unsafe_allow_html=True)
        with row2_col2:
            st.markdown('<div class="metric-box"><div class="metric-title">Assessment:</div><div class="metric-value-accent">Healthy</div></div>', unsafe_allow_html=True)

    st.markdown("<h3 style='color:#1E5E3A;'>Scan Analysis Notes</h3>", unsafe_allow_html=True)
    st.area_chart(pd.DataFrame([20, 38, 29, 48, 56, 42, 68, 32], columns=['Vitals Level']), color="#1E5E3A")
    
    st.markdown(
        f"""
        <div style="background-color: white; padding: 20px; border-radius: 12px; border-left: 6px solid #1E5E3A; box-shadow: 0px 4px 12px rgba(0,0,0,0.04);">
            <h4 style="color:#1E5E3A; margin-top:0;">📝 Analysis Results:</h4>
            <p><b>Name:</b> {st.session_state.patient_name} | <b>Address:</b> {st.session_state.patient_address}</p>
            <p><b>Complaint:</b> {st.session_state.symptoms}</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.write("")
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("💾 Save To Permanent Records"):
            save_patient_record(patient_id, st.session_state.patient_name, st.session_state.patient_address, st.session_state.symptoms)
            st.success("✅ This patient's data has been saved to the Database!")
            
    with col_btn2:
        if st.button("🏠 Start New Scan / Home"):
            reset_app()

# ==========================================
# SIDEBAR: HISTORY DATABASE
# ==========================================
st.sidebar.markdown(
    """
    <div style="background-color: #1E5E3A; padding: 12px; border-radius: 6px; color: white; text-align: center; font-weight: bold; margin-bottom:15px;">
        🗂️ Database History Records
    </div>
    """, unsafe_allow_html=True
)

records_df = load_patient_records()

if not records_df.empty:
    for idx, row in records_df.iterrows():
        st.sidebar.markdown(
            f"""
            <div style="background-color: white; padding: 10px; border-radius: 6px; margin-top: 8px; border-left: 4px solid #28A745; box-shadow: 0px 2px 5px rgba(0,0,0,0.05);">
                <b>{idx+1}. {row['Name']}</b> ({row['ID']})<br>
                <small style="color:#4A5568;">📍 {row['Residential Address']}</small><br>
                <small style="color:#4A5568;">🩺 {str(row['Symptoms / Complaints'])[:20]}...</small><br>
                <small style="color:#A0AEC0; font-size:10px;">⏱️ {row['Time']}</small>
            </div>
            """, unsafe_allow_html=True
        )
        
    if st.sidebar.button("🗑️ Delete All History"):
        if os.path.exists(DATABASE_FILE):
            os.remove(DATABASE_FILE)
            st.sidebar.success("All history has been deleted!")
            st.rerun()
else:
    st.sidebar.info("No old patient records in the Database yet.")
