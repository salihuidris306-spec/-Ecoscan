<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoScan - Advanced AI Medical Diagnostics</title>
    <!-- Google Fonts for Professional Look -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome for Premium Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --primary-green: #2ecc71;
            --dark-green: #1b4d3e;
            --light-green: #e8f5e9;
            --accent-green: #27ae60;
            --bg-dark: #0f201b;
            --text-light: #ffffff;
            --text-dark: #2c3e50;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            height: 90vh;
            background: linear-gradient(135deg, #142c24 0%, #0b1a15 100%);
            border: 2px solid var(--primary-green);
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(46, 204, 113, 0.2);
            overflow-y: auto;
            position: relative;
            padding: 30px 20px;
            display: flex;
            flex-direction: column;
        }

        /* Hide scrollbars but keep functionality */
        .app-container::-webkit-scrollbar {
            width: 4px;
        }
        .app-container::-webkit-scrollbar-thumb {
            background: var(--primary-green);
            border-radius: 10px;
        }

        .page {
            display: none;
            flex-direction: column;
            height: 100%;
            animation: fadeIn 0.5s ease-in-out forwards;
        }

        .page.active {
            display: flex;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Reusable Components */
        .brand-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .brand-logo {
            font-size: 2.5rem;
            color: var(--primary-green);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .brand-logo i {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }

        .btn {
            background: linear-gradient(135deg, var(--primary-green) 0%, var(--accent-green) 100%);
            color: white;
            border: none;
            padding: 14px 28px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(46, 204, 113, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: auto;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(46, 204, 113, 0.5);
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: var(--primary-green);
            font-weight: 600;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 14px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(46, 204, 113, 0.3);
            border-radius: 10px;
            color: white;
            font-size: 1rem;
            transition: all 0.3s;
        }

        .form-group input:focus, .form-group select:focus {
            outline: none;
            border-color: var(--primary-green);
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 10px rgba(46, 204, 113, 0.2);
        }

        /* Page 1: Welcome */
        #page1 {
            justify-content: center;
            text-align: center;
        }
        .tagline {
            color: #a2b4af;
            font-size: 1rem;
            margin-bottom: 40px;
        }
        .dev-badge {
            background: rgba(46, 204, 113, 0.1);
            border: 1px solid var(--primary-green);
            padding: 12px;
            border-radius: 15px;
            margin-top: 30px;
        }
        .dev-badge p {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #a2b4af;
        }
        .dev-name {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--primary-green);
        }

        /* Page 3: Symptoms Grid */
        .symptoms-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 15px;
            max-height: 320px;
            overflow-y: auto;
            padding-right: 5px;
        }
        .symptom-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(46, 204, 113, 0.2);
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
        }
        .symptom-card i {
            font-size: 1.5rem;
            color: var(--primary-green);
            margin-bottom: 8px;
        }
        .symptom-card.selected {
            background: rgba(46, 204, 113, 0.2);
            border-color: var(--primary-green);
            transform: scale(1.02);
        }

        /* Page 4: Scanner */
        .scanner-box {
            position: relative;
            width: 200px;
            height: 250px;
            margin: 40px auto;
            background: rgba(46, 204, 113, 0.05);
            border: 2px dashed rgba(46, 204, 113, 0.4);
            border-radius: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .biometric-icon {
            font-size: 6rem;
            color: rgba(46, 204, 113, 0.4);
            z-index: 1;
        }
        .scan-laser {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: var(--primary-green);
            box-shadow: 0 0 15px var(--primary-green);
            animation: scanning 2s linear infinite;
            z-index: 2;
        }
        @keyframes scanning {
            0% { top: 0%; }
            50% { top: 100%; }
            100% { top: 0%; }
        }
        .scan-status {
            text-align: center;
            font-weight: bold;
            color: var(--primary-green);
            letter-spacing: 1px;
        }

        /* Page 5: Report Dashboard */
        .dashboard-card {
            background: rgba(255, 255, 255, 0.05);
            border-left: 4px solid var(--primary-green);
            padding: 15px;
            border-radius: 0 12px 12px 0;
            margin-bottom: 15px;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 15px;
        }
        .metric-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(46, 204, 113, 0.1);
            padding: 10px;
            text-align: center;
            border-radius: 10px;
        }
        .metric-box span {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary-green);
            display: block;
        }

        /* Records History Panel */
        .records-btn {
            background: transparent;
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 8px 15px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.8rem;
            margin-top: 10px;
        }
        .history-panel {
            background: rgba(11, 26, 21, 0.95);
            border-top: 2px solid var(--primary-green);
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-in-out;
            z-index: 10;
            border-radius: 20px 20px 0 0;
            padding: 0 20px;
        }
        .history-panel.open {
            max-height: 70%;
            padding: 20px;
            overflow-y: auto;
        }
    </style>
</head>
<body>

    <div class="app-container">
        
        <!-- PAGE 1: WELCOME PAGE -->
        <div id="page1" class="page active">
            <div class="brand-header">
                <div class="brand-logo"><i class="fa-solid fa-leaf"></i> EcoScan</div>
                <p class="tagline">Next-Generation AI Bio-Diagnostics</p>
            </div>
            
            <button class="btn" onclick="navigateTo(2)">Launch Assessment</button>
            
            <div class="dev-badge">
                <p>Designed & Developed By</p>
                <div class="dev-name">Salihu Idris</div>
                <small style="color: var(--primary-green); font-size: 0.7rem;">Young Innovation Challenge Competitor</small>
            </div>
        </div>

        <!-- PAGE 2: PATIENT INFO -->
        <div id="page2" class="page">
            <div class="brand-header">
                <h3>Patient Intake</h3>
                <p style="color: #a2b4af; font-size: 0.85rem;">Please enter authentication details</p>
            </div>
            
            <div class="form-group" style="margin-top: 20px;">
                <label><i class="fa-solid fa-user"></i> Full Name</label>
                <input type="text" id="patientName" placeholder="e.g. John Doe" required>
            </div>
            <div class="form-group">
                <label><i class="fa-solid fa-location-dot"></i> Residential Address</label>
                <input type="text" id="patientAddress" placeholder="e.g. State Road, Kano" required>
            </div>
            <div class="form-group">
                <label><i class="fa-solid fa-venus-mars"></i> Gender</label>
                <select id="patientGender">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
            </div>

            <button class="btn" onclick="validateAndProceedToSymptoms()">Proceed to Symptoms</button>
        </div>

        <!-- PAGE 3: SYMPTOMS SELECTION -->
        <div id="page3" class="page">
            <div class="brand-header">
                <h3>Symptom Matrix</h3>
                <p style="color: #a2b4af; font-size: 0.85rem;">Select all indicators currently experienced</p>
            </div>

            <div class="symptoms-container">
                <div class="symptom-card" data-symptom="Fever" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-temperature-high"></i>
                    <p>High Fever</p>
                </div>
                <div class="symptom-card" data-symptom="Cough" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-head-side-cough"></i>
                    <p>Dry Cough</p>
                </div>
                <div class="symptom-card" data-symptom="Headache" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-brain"></i>
                    <p>Headache</p>
                </div>
                <div class="symptom-card" data-symptom="Fatigue" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-battery-empty"></i>
                    <p>Fatigue</p>
                </div>
                <div class="symptom-card" data-symptom="Nausea" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-stomach"></i>
                    <p>Nausea</p>
                </div>
                <div class="symptom-card" data-symptom="Chills" onclick="toggleSymptom(this)">
                    <i class="fa-solid fa-snowflake"></i>
                    <p>Chills</p>
                </div>
            </div>

            <button class="btn" onclick="startAutomatedScan()">Initiate Diagnostic Scan</button>
        </div>

        <!-- PAGE 4: BIOMETRIC SCANNING -->
        <div id="page4" class="page" style="justify-content: center;">
            <div class="brand-header">
                <h3>Biometric Analysis</h3>
                <p style="color: #a2b4af; font-size: 0.85rem;">Place finger onto device screen area</p>
            </div>

            <div class="scanner-box">
                <div class="scan-laser"></div>
                <i class="fa-solid fa-fingerprint biometric-icon"></i>
            </div>

            <div class="scan-status" id="scanStatus">DETECTING BIOMETRICS...</div>
            <p style="text-align: center; font-size: 0.8rem; color:#a2b4af; margin-top: 10px;">Keep still. AI is capturing pulse & oxygenation trends automatically.</p>
        </div>

        <!-- PAGE 5: AI DIAGNOSIS REPORT -->
        <div id="page5" class="page">
            <div class="brand-header">
                <h3 style="color: var(--primary-green);"><i class="fa-solid fa-square-poll-horizontal"></i> Diagnostic Report</h3>
                <p id="reportMeta" style="color: #a2b4af; font-size: 0.8rem;"></p>
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <p style="font-size:0.75rem; color:#a2b4af;">HEART RATE</p>
                    <span id="resBpm">-- BPM</span>
                </div>
                <div class="metric-box">
                    <p style="font-size:0.75rem; color:#a2b4af;">SPO2 LEVELS</p>
                    <span id="resSpo2">-- %</span>
                </div>
            </div>

            <div class="dashboard-card">
                <h4 style="color: var(--primary-green); font-size:0.9rem; margin-bottom: 5px;">Primary Assessment</h4>
                <p id="resDiagnosis" style="font-size: 0.95rem; font-weight:600;"></p>
            </div>

            <div class="dashboard-card" style="border-left-color: #f1c40f;">
                <h4 style="color: #f1c40f; font-size:0.9rem; margin-bottom: 5px;">Clinical Recommendations</h4>
                <p id="resAdvice" style="font-size: 0.85rem; color:#e0e0e0;"></p>
            </div>

            <div class="dashboard-card" style="border-left-color: #3498db;">
                <h4 style="color: #3498db; font-size:0.9rem; margin-bottom: 5px;">Preventative Measures</h4>
                <p id="resPrevention" style="font-size: 0.85rem; color:#e0e0e0;"></p>
            </div>

            <div style="display: flex; gap: 10px; margin-top: auto;">
                <button class="btn" style="flex: 2;" onclick="resetApp()">New Scan</button>
                <button class="records-btn" style="margin: 0;" onclick="toggleHistory()"><i class="fa-solid fa-history"></i> Records</button>
            </div>
        </div>

        <!-- HIDDEN RECORDS HISTORY DRAWER -->
        <div id="historyPanel" class="history-panel">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <h4 style="color: var(--primary-green);"><i class="fa-solid fa-database"></i> Local Patient Database</h4>
                <i class="fa-solid fa-times" style="cursor:pointer;" onclick="toggleHistory()"></i>
            </div>
            <div id="historyLogs">
                <!-- Data dynamically inserted here -->
            </div>
        </div>

    </div>

    <!-- AUDIO FOR SCI-FI EFFECT -->
    <script>
        let selectedSymptoms = [];
        let currentPatient = {};

        function navigateTo(pageNumber) {
            document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
            document.getElementById(`page${pageNumber}`).classList.add('active');
        }

        function validateAndProceedToSymptoms() {
            const name = document.getElementById('patientName').value.trim();
            const address = document.getElementById('patientAddress').value.trim();
            const gender = document.getElementById('patientGender').value;

            if(!name || !address) {
                alert('Please provide complete patient demographics before scanning.');
                return;
            }

            currentPatient = { name, address, gender };
            navigateTo(3);
        }

        function toggleSymptom(element) {
            const symptom = element.getAttribute('data-symptom');
            if(element.classList.contains('selected')) {
                element.classList.remove('selected');
                selectedSymptoms = selectedSymptoms.filter(s => s !== symptom);
            } else {
                element.classList.add('selected');
                selectedSymptoms.push(symptom);
            }
        }

        function startAutomatedScan() {
            navigateTo(4);
            const statusText = document.getElementById('scanStatus');
            
            // Step 1: Simulating automatic detection (No interaction needed)
            setTimeout(() => {
                statusText.innerText = "BIOMETRIC FINGERPRINT LOCKED...";
                statusText.style.color = "#f1c40f";
            }, 1500);

            // Step 2: Processing algorithms
            setTimeout(() => {
                statusText.innerText = "RUNNING CLINICAL DIAGNOSIS...";
                statusText.style.color = "#3498db";
            }, 3000);

            // Step 3: Compile Report
            setTimeout(() => {
                compileDiagnosticReport();
            }, 5000);
        }

        function compileDiagnosticReport() {
            // Smart AI Engine Logic based on Combinations
            let diagnosis = "General Fatigue & Exhaustion";
            let advice = "Increase fluid intake, prioritize 8 hours of clinical sleep, and monitor body metrics.";
            let prevention = "Engage in routine aerobic exercise, balance nutrition, and optimize workspace ergonomics.";
            
            // Clinical variations
            if (selectedSymptoms.includes('Fever') && selectedSymptoms.includes('Chills')) {
                diagnosis = "Suspected Acute Malaria or Viral Infection";
                advice = "Urgent clinical validation required. Administer antipyretics under medical guidance.";
                prevention = "Utilize insecticide-treated bed nets, clear stagnant water reservoirs, and use insect repellents.";
            } else if (selectedSymptoms.includes('Cough') && selectedSymptoms.includes('Fever')) {
                diagnosis = "Upper Respiratory Tract Infection Indicators";
                advice = "Isolate temporarily, consume warm fluids, and consult for possible antibiotic/antiviral protocols.";
                prevention = "Maintain meticulous hand hygiene, wear masks in congested spaces, and take annual influenza vaccinations.";
            } else if (selectedSymptoms.includes('Headache') && selectedSymptoms.includes('Nausea')) {
                diagnosis = "Acute Migraine vs Neurological Stress Response";
                advice = "Rest in dark, noise-isolated environments. Avoid blue-light triggers immediately.";
                prevention = "Track nutritional dietary triggers, strictly maintain hydration, and regulate stress levels.";
            } else if (selectedSymptoms.length > 0) {
                diagnosis = `Mild Symptomatic Strain (${selectedSymptoms.join(', ')})`;
                advice = "Symptomatic treatment advised. Rest and high-protein nutrition.";
                prevention = "Boost natural immunity via Vitamin C and Zinc supplements.";
            }

            // Generate randomized realistic biometrics
            const bpm = Math.floor(Math.random() * (105 - 68 + 1)) + 68;
            const spo2 = Math.floor(Math.random() * (100 - 94 + 1)) + 94;

            // Update UI Elements
            document.getElementById('reportMeta').innerText = `Patient: ${currentPatient.name} | ${currentPatient.gender}`;
            document.getElementById('resBpm').innerText = `${bpm} BPM`;
            document.getElementById('resSpo2').innerText = `${spo2}%`;
            document.getElementById('resDiagnosis').innerText = diagnosis;
            document.getElementById('resAdvice').innerText = advice;
            document.getElementById('resPrevention').innerText = prevention;

            // Commit to Local History Database
            const record = {
                id: Date.now(),
                name: currentPatient.name,
                address: currentPatient.address,
                gender: currentPatient.gender,
                symptoms: selectedSymptoms.join(', ') || 'None Reported',
                diagnosis: diagnosis,
                bpm: bpm,
                spo2: spo2,
                date: new Date().toLocaleString()
            };

            let localHistory = JSON.parse(localStorage.getItem('ecoscan_history')) || [];
            localHistory.unshift(record);
            localStorage.setItem('ecoscan_history', JSON.stringify(localHistory));

            // Proceed to Output View
            navigateTo(5);
        }

        function toggleHistory() {
            const panel = document.getElementById('historyPanel');
            panel.classList.toggle('open');
            if(panel.classList.contains('open')) {
                renderHistory();
            }
        }

        function renderHistory() {
            const container = document.getElementById('historyLogs');
            let localHistory = JSON.parse(localStorage.getItem('ecoscan_history')) || [];
            
            if(localHistory.length === 0) {
                container.innerHTML = `<p style="color:#a2b4af; font-size:0.85rem; text-align:center; padding:20px;">No patient records registered on this cloud instance.</p>`;
                return;
            }

            container.innerHTML = localHistory.map(item => `
                <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(46,204,113,0.2); padding:12px; border-radius:8px; margin-bottom:10px; font-size:0.8rem;">
                    <div style="display:flex; justify-content:space-between; color:var(--primary-green); font-weight:bold;">
                        <span>${item.name} (${item.gender})</span>
                        <span style="font-size:0.7rem; color:#a2b4af;">${item.date}</span>
                    </div>
                    <p style="color:#e0e0e0; margin-top:4px;"><strong>Diagnosis:</strong> ${item.diagnosis}</p>
                    <p style="color:#a2b4af; font-size:0.75rem;">Vitals: ${item.bpm}BPM | ${item.spo2}% SpO2 | Address: ${item.address}</p>
                </div>
            `).join('');
        }

        function resetApp() {
            // Reset input values
            document.getElementById('patientName').value = '';
            document.getElementById('patientAddress').value = '';
            document.getElementById('patientGender').selectedIndex = 0;
            document.getElementById('scanStatus').innerText = "DETECTING BIOMETRICS...";
            document.getElementById('scanStatus').style.color = "var(--primary-green)";
            
            // Clear selections
            document.querySelectorAll('.symptom-card').forEach(card => card.classList.remove('selected'));
            selectedSymptoms = [];
            currentPatient = {};
            
            // Close drawer if open and return home
            document.getElementById('historyPanel').classList.remove('open');
            navigateTo(1);
        }
    </script>
</body>
</html>
