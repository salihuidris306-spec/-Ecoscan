import streamlit as st
import time

# Set up page styling
st.set_page_config(page_title="EcoScan Health Assistant", page_icon="🏥", layout="centered")

# Initialize "session state" to remember data across pages
if "page" not in st.session_state:
    st.session_state.page = 1
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_address" not in st.session_state:
    st.session_state.user_address = ""

# --- PAGE 1: REGISTRATION FACE PAGE ---
if st.session_state.page == 1:
    st.title("🏥 EcoScan Rural Health Assistant")
    st.subheader("Step 1: Patient Registration")
    st.write("Please enter your personal details below.")
    
    # Input fields
    name = st.text_input("Full Name", value=st.session_state.user_name)
    address = st.text_input("Home Address", value=st.session_state.user_address)
    
    # Next Button
    if st.button("Proceed to Medical Assessment ➡️"):
        if name and address:
            st.session_state.user_name = name
            st.session_state.user_address = address
            st.session_state.page = 2
            st.rerun()
        else:
            st.error("Please fill in both your Name and Address before moving forward.")

# --- PAGE 2: MEDICAL ASSESSMENT & DIAGNOSIS ---
elif st.session_state.page == 2:
    st.title("🏥 Medical Assessment Screen")
    st.write(f"**Patient:** {st.session_state.user_name} | **Address:** {st.session_state.user_address}")
    st.markdown("---")
    
    # 1. Fingerprint Simulation
    st.subheader("📌 Step 2: Biometric Verification")
    if "fingerprint_done" not in st.session_state:
        st.session_state.fingerprint_done = False
        
    if not st.session_state.fingerprint_done:
        if st.button("👍 Click here to Scan Thumbprint"):
            with st.spinner("Scanning thumbprint... please hold still..."):
                time.sleep(2) # Simulates a real scan delay
            st.session_state.fingerprint_done = True
            st.rerun()
    else:
        st.success("✅ Thumbprint scanned and verified successfully!")

    st.markdown("---")
    
    # 2. Symptom Inputs
    st.subheader("🩺 Step 3: Tell Us How You Feel")
    symptoms = st.text_input("What primary symptoms are you feeling? (e.g., fever, headache, cough)")
    extra_info = st.text_area("Add more information about your sickness:")
    
    # 3. Submit and Diagnosis Logic
    if st.button("Submit for Diagnosis 🧪"):
        if not st.session_state.fingerprint_done:
            st.error("Please scan your thumbprint first!")
        elif not symptoms:
            st.error("Please specify at least one symptom.")
        else:
            st.subheader("📋 Diagnostic Results & Medical Advice")
            with st.spinner("Analyzing your symptoms..."):
                time.sleep(1.5)
            
            # Simple rules to diagnose based on what the user types
            text_to_check = (symptoms + " " + extra_info).lower()
            
            if "fever" in text_to_check and "chills" in text_to_check:
                st.warning("⚠️ **Potential Diagnosis:** Symptoms point toward Malaria.")
                st.info("""
                **💡 Health Advice for Malaria:**
                * **Immediate Action:** Please visit the nearest clinic or hospital for a proper rapid diagnostic test (RDT) or blood smear.
                * **Medication:** If confirmed, use approved anti-malarial medications (like ACTs) as prescribed by a doctor. Complete the full dose!
                * **Rest & Fluids:** Drink plenty of clean water to stay hydrated and get adequate rest.
                * **Prevention:** Sleep under a treated mosquito net and clear stagnant water around your home.
                """)
                
            elif "cough" in text_to_check or "catarrh" in text_to_check or "flu" in text_to_check:
                st.info("ℹ️ **Potential Diagnosis:** Symptoms suggest a Common Cold or Respiratory Infection.")
                st.info("""
                **💡 Health Advice for Cold/Flu:**
                * **Rest:** Allow your body to rest so your immune system can fight the virus.
                * **Hydration:** Drink warm liquids like tea or soup to soothe your throat and break up congestion.
                * **Medication:** You can take mild pain relievers (like Paracetamol) to reduce headache or mild fever if needed.
                * **Hygiene:** Cover your mouth when coughing and wash your hands often to protect others.
                """)
                
            elif "stomach" in text_to_check or "diarrhea" in text_to_check:
                st.warning("⚠️ **Potential Diagnosis:** Symptoms suggest Food Poisoning or a Stomach Infection.")
                st.info("""
                **💡 Health Advice for Stomach Infection:**
                * **Stay Hydrated:** This is critical. Drink Oral Rehydration Salts (ORS) or clean water mixed with a little salt and sugar to replace lost fluids.
                * **Diet:** Eat bland, easy-to-digest foods like bananas, rice, or porridge. Avoid oily, spicy, or heavy foods.
                * **Hygiene:** Ensure all food and water are properly cooked and boiled. Wash hands before eating.
                * **When to see a doctor:** If the diarrhea lasts more than 2 days or you see blood, go to a clinic immediately.
                """)
                
            else:
                st.success("✅ **Analysis:** Symptoms are unclear.")
                st.info("""
                **💡 General Health Advice:**
                * Because the symptoms provided are general, we cannot pin down a specific condition.
                * Please monitor how you feel over the next 24 hours.
                * If you feel worse, develop a high fever, or experience sudden pain, please travel to the closest health center or talk to a local community nurse.
                """)
                
    st.markdown("---")
    
    # 4. Home Button to Go Back
    if st.button("🏠 Return to Home Page"):
        # Reset everything back to the beginning
        st.session_state.page = 1
        st.session_state.user_name = ""
        st.session_state.user_address = ""
        st.session_state.fingerprint_done = False
        st.rerun()
