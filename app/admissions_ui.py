import streamlit as st

st.set_page_config(
    page_title="IPU AI | Admissions",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

.stApp {
    background:#f5f7fb;
}

/* NAVBAR */

.navbar {
    background:white;
    border-bottom:1px solid #e5e7eb;
    padding:16px 35px;
    border-radius:0 0 14px 14px;
    margin-bottom:30px;
}

.logo {
    font-size:25px;
    font-weight:800;
    color:#172554;
}

.logo span {
    color:#2563eb;
}

.nav {
    text-align:right;
    color:#475569;
    font-size:14px;
    padding-top:7px;
}

/* PAGE HEADER */

.page-header {
    background:linear-gradient(
        135deg,
        #172554,
        #1e40af,
        #2563eb
    );
    padding:45px 50px;
    border-radius:25px;
    color:white;
    margin-bottom:35px;
    box-shadow:0 18px 45px rgba(30,64,175,0.15);
}

.page-label {
    font-size:12px;
    font-weight:700;
    letter-spacing:2px;
    opacity:.8;
}

.page-title {
    font-size:42px;
    font-weight:800;
    margin:10px 0;
}

.page-description {
    color:#dbeafe;
    font-size:16px;
    line-height:1.7;
    max-width:700px;
}

/* SEARCH */

.search-title {
    font-size:23px;
    font-weight:800;
    color:#172033;
    margin-top:10px;
}

/* CARDS */

.card {
    background:white;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:25px;
    min-height:175px;
    box-shadow:0 7px 24px rgba(15,23,42,.04);
    margin-bottom:20px;
}

.icon {
    font-size:30px;
    margin-bottom:12px;
}

.card-title {
    color:#172033;
    font-size:18px;
    font-weight:750;
    margin-bottom:8px;
}

.card-text {
    color:#64748b;
    font-size:13px;
    line-height:1.6;
}

.arrow {
    color:#2563eb;
    font-size:13px;
    font-weight:700;
    margin-top:14px;
}

/* PROCESS */

.process-section {
    background:white;
    border:1px solid #e5e7eb;
    border-radius:22px;
    padding:35px;
    margin-top:20px;
}

.process-title {
    color:#172033;
    font-size:24px;
    font-weight:800;
}

.step {
    text-align:center;
    padding:20px 10px;
}

.step-number {
    background:#eff6ff;
    color:#2563eb;
    width:45px;
    height:45px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
    font-weight:800;
    font-size:17px;
}

.step-title {
    color:#172033;
    font-weight:750;
    margin-top:12px;
}

.step-text {
    color:#64748b;
    font-size:12px;
    margin-top:5px;
}

/* AI BOX */

.ai-box {
    background:#eff6ff;
    border:1px solid #bfdbfe;
    border-radius:20px;
    padding:30px;
    margin-top:30px;
}

.ai-title {
    color:#172554;
    font-size:23px;
    font-weight:800;
}

.ai-text {
    color:#475569;
    font-size:14px;
    line-height:1.6;
}

/* FOOTER */

.footer {
    text-align:center;
    color:#64748b;
    font-size:12px;
    padding:45px 0 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVBAR
# =========================================================

st.markdown("""
<div class="navbar">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div class="logo">
🎓 <span>IPU</span> AI
</div>

<div class="nav">
Home &nbsp;&nbsp;&nbsp;
<b>Admissions</b> &nbsp;&nbsp;&nbsp;
Academics &nbsp;&nbsp;&nbsp;
Notices &nbsp;&nbsp;&nbsp;
Student Services &nbsp;&nbsp;&nbsp;
🤖 AI Assistant
</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="page-header">

<div class="page-label">
ADMISSION INFORMATION
</div>

<div class="page-title">
📝 Admissions
</div>

<div class="page-description">
Everything you need to understand the IPU admission process —
from eligibility and application to documents, fees and important dates.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SEARCH
# =========================================================

st.markdown(
    '<div class="search-title">What do you want to know?</div>',
    unsafe_allow_html=True
)

st.text_input(
    "",
    placeholder="🔍  Search admission information...",
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# ADMISSION CARDS
# =========================================================

st.markdown(
    '<div class="search-title">Admission Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:#64748b;font-size:14px;">Explore the most important admission topics.</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">

        <div class="icon">🎓</div>

        <div class="card-title">
        Eligibility
        </div>

        <div class="card-text">
        Check eligibility requirements,
        qualifications and admission criteria.
        </div>

        <div class="arrow">
        View eligibility →
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

        <div class="icon">📝</div>

        <div class="card-title">
        Application Process
        </div>

        <div class="card-text">
        Understand registration,
        application steps and submission process.
        </div>

        <div class="arrow">
        View process →
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">

        <div class="icon">📄</div>

        <div class="card-title">
        Required Documents
        </div>

        <div class="card-text">
        Find the documents required
        during the admission process.
        </div>

        <div class="arrow">
        View documents →
        </div>

    </div>
    """, unsafe_allow_html=True)


col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="card">

        <div class="icon">💰</div>

        <div class="card-title">
        Fees
        </div>

        <div class="card-text">
        Explore admission fees,
        tuition information and related charges.
        </div>

        <div class="arrow">
        View fees →
        </div>

    </div>
    """, unsafe_allow_html=True)


with col5:

    st.markdown("""
    <div class="card">

        <div class="icon">📅</div>

        <div class="card-title">
        Important Dates
        </div>

        <div class="card-text">
        Keep track of application deadlines,
        registration and admission dates.
        </div>

        <div class="arrow">
        View dates →
        </div>

    </div>
    """, unsafe_allow_html=True)


with col6:

    st.markdown("""
    <div class="card">

        <div class="icon">❓</div>

        <div class="card-title">
        Admission FAQs
        </div>

        <div class="card-text">
        Get answers to common questions
        students ask about admissions.
        </div>

        <div class="arrow">
        View FAQs →
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# APPLICATION PROCESS
# =========================================================

st.markdown("""
<div class="process-section">

<div class="process-title">
🛣️ Admission Process
</div>

<p style="color:#64748b;font-size:14px;">
A simple overview of the admission journey.
</p>

</div>
""", unsafe_allow_html=True)


p1, p2, p3, p4, p5 = st.columns(5)

steps = [
    ("1", "Check Eligibility", "Understand the requirements"),
    ("2", "Register", "Create your application"),
    ("3", "Apply", "Submit the application"),
    ("4", "Upload Documents", "Provide required documents"),
    ("5", "Admission", "Complete the admission process")
]

for col, step in zip([p1,p2,p3,p4,p5], steps):

    with col:

        st.markdown(f"""
        <div class="step">

            <div class="step-number">
            {step[0]}
            </div>

            <div class="step-title">
            {step[1]}
            </div>

            <div class="step-text">
            {step[2]}
            </div>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# AI ADMISSION ASSISTANT
# =========================================================

st.markdown("""
<div class="ai-box">

<div class="ai-title">
🤖 Need help with admission?
</div>

<div class="ai-text">
Ask the IPU AI Assistant about eligibility, applications,
documents, fees or any other admission-related question.
</div>

</div>
""", unsafe_allow_html=True)

st.text_input(
    "",
    placeholder="Ask an admission question...",
    label_visibility="collapsed"
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

────────────────────────────────────────

🎓 <b>IPU AI</b><br><br>

Admission & Student Information Assistant<br><br>

Admissions • Academics • Notices • Student Services

</div>
""", unsafe_allow_html=True)

