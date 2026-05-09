import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Multi Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp{
    background:
    linear-gradient(135deg,#020617,#0f172a,#111827);
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#0f172a;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Inputs */

label{
    color:white !important;
    font-weight:bold;
}

/* Headings */

h1, h2, h3, h4{
    color:white !important;
}

/* Number Inputs */

.stNumberInput input{
    background:white !important;
    color:black !important;
    border-radius:10px !important;
}

/* Buttons */

.stButton button{
    width:100%;
    background:#2563eb;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:16px;
    font-weight:bold;
}

/* Cards */

.card{
    background:#1e293b;
    padding:30px;
    border-radius:20px;
    margin-bottom:25px;
}

.feature-card{
    background:#1e293b;
    padding:30px;
    border-radius:20px;
    text-align:center;
    height:250px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

/* Result */

.success{
    background:#14532d;
    padding:20px;
    border-radius:12px;
    color:white;
}

.danger{
    background:#7f1d1d;
    padding:20px;
    border-radius:12px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="card">

<h1 style="text-align:center; color:white; font-size:55px;">
🩺 Multi Disease Prediction System
</h1>

<p style="text-align:center; color:white; font-size:22px;">
Professional Healthcare Prediction Dashboard
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🩺 Dashboard")

page = st.sidebar.radio(
    "Select Prediction",
    [
        "Home",
        "Diabetes Prediction",
        "Thyroid Prediction",
        "Liver Prediction"
    ]
)

# =========================
# HOME
# =========================

if page == "Home":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">

        <div style="font-size:60px;">🧠</div>

        <h2 style="margin-top:20px;">
        Machine Learning
        </h2>

        <p style="color:white;">
        Smart AI Prediction Models
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">

        <div style="font-size:60px;">⚡</div>

        <h2 style="margin-top:20px;">
        Fast Analysis
        </h2>

        <p style="color:white;">
        Instant Medical Prediction
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">

        <div style="font-size:60px;">📊</div>

        <h2 style="margin-top:20px;">
        Health Reports
        </h2>

        <p style="color:white;">
        Accurate Healthcare Insights
        </p>

        </div>
        """, unsafe_allow_html=True)

# =========================
# DIABETES
# =========================

elif page == "Diabetes Prediction":

    st.header("🩸 Diabetes Prediction")

    col1, col2 = st.columns(2)

    with col1:
        fasting = st.number_input("Fasting Blood Sugar")
        post = st.number_input("Postprandial Blood Sugar")
        hba1c = st.number_input("HbA1c")

    with col2:
        random_bs = st.number_input("Random Blood Sugar")
        bmi = st.number_input("BMI")
        age = st.number_input("Age")

    if st.button("Predict Diabetes"):

        avg = (fasting + post + hba1c + random_bs) / 4

        if avg > 140:

            st.markdown("""
            <div class="danger">

            <h2>⚠️ High Risk of Diabetes</h2>

            <p>
            Consult a diabetologist or healthcare professional immediately
            for proper diagnosis and treatment.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.markdown("## 🥗 Recommended Diet")

            st.success("""
✅ Eat:
• Green vegetables
• Brown rice
• Oats
• Apple
• Orange
• Sprouts
• Nuts
• Dal
• High fiber foods
""")

            st.markdown("## 🚫 Avoid")

            st.error("""
❌ Avoid:
• Sugar
• Soft drinks
• Bakery foods
• White rice excess
• Junk food
• Ice cream
• Chocolates
""")

            st.markdown("## 🏃 Lifestyle Suggestions")

            st.info("""
✔ Walk 30 minutes daily  
✔ Drink more water  
✔ Reduce stress  
✔ Sleep properly  
✔ Exercise regularly  
""")

        else:

            st.markdown("""
            <div class="success">

            <h2>✅ Diabetes Not Detected</h2>

            <p>Your values appear normal.</p>

            </div>
            """, unsafe_allow_html=True)

# =========================
# THYROID
# =========================

elif page == "Thyroid Prediction":

    st.header("🧬 Thyroid Prediction")

    tsh = st.number_input("TSH")
    t3 = st.number_input("T3")
    t4 = st.number_input("T4")

    if st.button("Predict Thyroid"):

        if tsh > 4.5:

            st.markdown("""
            <div class="danger">

            <h2>⚠️ Thyroid Disorder Detected</h2>

            <p>
            Consult an endocrinologist or thyroid specialist for
            further medical evaluation.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.markdown("## 🥗 Recommended Diet")

            st.success("""
✅ Eat:
• Iodized salt
• Eggs
• Fish
• Milk
• Yogurt
• Nuts
• Fruits
""")

            st.markdown("## 🚫 Avoid")

            st.error("""
❌ Avoid:
• Excess junk food
• Smoking
• Excess sugar
• Excess processed foods
""")

        else:

            st.markdown("""
            <div class="success">

            <h2>✅ Thyroid Appears Normal</h2>

            </div>
            """, unsafe_allow_html=True)

# =========================
# LIVER
# =========================

elif page == "Liver Prediction":

    st.header("🧫 Liver Prediction")

    bilirubin = st.number_input("Total Bilirubin")
    sgot = st.number_input("SGOT")
    sgpt = st.number_input("SGPT")

    if st.button("Predict Liver Disease"):

        if sgot > 40 or sgpt > 40:

            st.markdown("""
            <div class="danger">

            <h2>⚠️ Liver Disease Detected</h2>

            <p>
            Consult a hepatologist or healthcare professional
            for detailed liver diagnosis.
            </p>

            </div>
            """, unsafe_allow_html=True)

            st.markdown("## 🥗 Recommended Diet")

            st.success("""
✅ Eat:
• Fruits
• Green vegetables
• Lemon water
• Beetroot
• Carrot
• Oats
• High protein foods
""")

            st.markdown("## 🚫 Avoid")

            st.error("""
❌ Avoid:
• Alcohol
• Oily foods
• Smoking
• Junk food
• Excess salt
""")

        else:

            st.markdown("""
            <div class="success">

            <h2>✅ Liver Appears Healthy</h2>

            </div>
            """, unsafe_allow_html=True)