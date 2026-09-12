"""
Guru Gobind Singh Indraprastha University (GGSIPU / DTC)
Official Multi-Agent AI Information Hub

A unified Streamlit application connecting students to institutional knowledge,
admissions, academic regulations, official notices, and student welfare services.
"""
import sys
import os

# Ensure the root project directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.ui.styles import get_custom_css
from app.ui.components import render_header, render_navigation, render_footer
from app.ui.home_view import render_home
from app.ui.admissions_view import render_admissions
from app.ui.academics_view import render_academics
from app.ui.notices_view import render_notices
from app.ui.student_services_view import render_student_services
from app.ui.ai_assistant_view import render_ai_assistant


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="IPU University Information Hub | Multi-Agent AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS design system
st.markdown(get_custom_css(), unsafe_allow_html=True)


# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Home"


# =========================================================
# HEADER & UNIFIED NAVIGATION
# =========================================================
render_header()
render_navigation(st.session_state.page)


# =========================================================
# SECTION DISPATCHER
# =========================================================
current_page = st.session_state.page

if current_page == "Home":
    render_home()

elif current_page == "Admissions":
    render_admissions()

elif current_page == "Academics":
    render_academics()

elif current_page == "University Notices":
    render_notices()

elif current_page == "Student Services":
    render_student_services()

elif current_page == "AI Assistant":
    render_ai_assistant()

else:
    # Default fallback
    st.session_state.page = "Home"
    render_home()


# =========================================================
# FOOTER
# =========================================================
render_footer()
