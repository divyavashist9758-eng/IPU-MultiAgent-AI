import streamlit as st

st.set_page_config(
    page_title="IPU AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background: #f5f7fb;
}

/* Navbar */

.navbar {
    background: #ffffff;
    border-bottom: 1px solid #e6e9f0;
    padding: 16px 35px;
    border-radius: 0 0 14px 14px;
    margin-bottom: 35px;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: #172554;
}

.logo span {
    color: #2563eb;
}

.nav-text {
    text-align: right;
    color: #475569;
    font-size: 14px;
    padding-top: 7px;
}

/* Hero */

.hero {
    background: linear-gradient(
        135deg,
        #172554 0%,
        #1e40af 55%,
        #2563eb 100%
    );
    border-radius: 28px;
    padding: 65px 55px;
    color: white;
    margin-bottom: 35px;
    box-shadow: 0 20px 50px rgba(30,64,175,0.18);
}

.hero-small {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    opacity: 0.8;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 18px;
}

.hero-description {
    font-size: 17px;
    line-height: 1.7;
    max-width: 700px;
    color: #dbeafe;
}

/* Search */

.search-box {
    background: white;
    border-radius: 15px;
    padding: 5px;
    margin-top: 30px;
    max-width: 760px;
}

/* Section */

.section-title {
    font-size: 25px;
    font-weight: 800;
    color: #172033;
    margin-top: 25px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 20px;
}

/* Cards */

.card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 25px;
    min-height: 175px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.04);
    transition: 0.2s;
}

.card-icon {
    font-size: 30px;
    margin-bottom: 12px;
}

.card-title {
    color: #172033;
    font-size: 18px;
    font-weight: 750;
    margin-bottom: 7px;
}

.card-text {
    color: #64748b;
    font-size: 13px;
    line-height: 1.6;
}

.card-arrow {
    color: #2563eb;
    font-size: 13px;
    font-weight: 700;
    margin-top: 15px;
}

/* AI strip */

.ai-section {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 22px;
    padding: 35px;
    margin-top: 40px;
}

.ai-title {
    color: #172033;
    font-size: 25px;
    font-weight: 800;
}

.ai-text {
    color: #64748b;
    line-height: 1.6;
}

/* Features */

.feature {
    text-align: center;
    padding: 25px;
}

.feature-icon {
    font-size: 32px;
    margin-bottom: 10px;
}

.feature-title {
    color: #172033;
    font-weight: 750;
    font-size: 16px;
}

.feature-text {
    color: #64748b;
    font-size: 13px;
    margin-top: 6px;
}

/* Footer */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 45px 0 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# NAVBAR
# =========================

st.markdown("""
<div class="navbar">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div class="logo">
🎓 <span>IPU</span> AI
</div>

<div class="nav-text">
Home &nbsp;&nbsp;&nbsp;
Admissions &nbsp;&nbsp;&nbsp;
Academics &nbsp;&nbsp;&nbsp;
Notices &nbsp;&nbsp;&nbsp;
Student Services &nbsp;&nbsp;&nbsp;
🤖 AI Assistant
</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">

<div class="hero-small">
GURU GOBIND SINGH INDRAPRASTHA UNIVERSITY
</div>

<div class="hero-title">
Your IPU Information Hub
</div>

<div class="hero-description">
Find information about admissions, academic rules,
programs, university notices and student services
with the help of an AI-powered information assistant.
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# QUICK ACCESS
# =========================

st.markdown(
    '<div class="section-title">Explore IPU Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Quick access to the information students need most.</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">📝</div>
        <div class="card-title">Admissions</div>
        <div class="card-text">
            Eligibility, application process,
            registration and admission information.
        </div>
        <div class="card-arrow">Explore →</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">📚</div>
        <div class="card-title">Academics</div>
        <div class="card-text">
            Exams, marks, syllabus, academic
            rules and university regulations.
        </div>
        <div class="card-arrow">Explore →</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">📢</div>
        <div class="card-title">Notices</div>
        <div class="card-text">
            University notifications,
            circulars and important announcements.
        </div>
        <div class="card-arrow">Explore →</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🎫</div>
        <div class="card-title">Student Services</div>
        <div class="card-text">
            Certificates, documents, fees,
            scholarships and student facilities.
        </div>
        <div class="card-arrow">Explore →</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# AI ASSISTANT
# =========================

st.markdown("""
<div class="ai-section">

<div class="ai-title">
🤖 Ask the IPU AI Assistant
</div>

<div class="ai-text">
Have a question about IPU? Ask our AI assistant about
admissions, academics, notices or student services.
</div>

</div>
""", unsafe_allow_html=True)

st.text_input(
    "",
    placeholder="🔍  What would you like to know about IPU?",
    label_visibility="collapsed"
)


# =========================
# FEATURES
# =========================

st.markdown(
    '<div class="section-title">Why use IPU AI?</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Multi-Agent AI</div>
        <div class="feature-text">
            Specialized agents handle different types of queries.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">📚</div>
        <div class="feature-title">RAG Powered</div>
        <div class="feature-text">
            Information is retrieved from university documents.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🔎</div>
        <div class="feature-title">Source Based</div>
        <div class="feature-text">
            Answers can be supported by relevant sources.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Quick Answers</div>
        <div class="feature-text">
            Find useful university information quickly.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

────────────────────────────────────────

🎓 <b>IPU AI</b><br><br>

Admission & Student Information Assistant<br><br>

Admissions • Academics • Notices • Student Services<br><br>

AI Powered University Information System

</div>
""", unsafe_allow_html=True)
