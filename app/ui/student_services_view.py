"""
Student Services & Welfare section for the IPU University Information Hub.
"""
import streamlit as st
from agents.student_services_agent import student_services_agent
from app.ui.components import render_page_banner, render_agent_response


def render_student_services():
    """Renders the Student Services portal view."""
    render_page_banner(
        badge="Student Welfare & Administrative Facilitation",
        title="Student Services & Documentation Hub",
        description="Guidelines for acquiring bonafide certificates, official transcripts, migration certificates, scholarship assistance, identity cards, and student welfare support."
    )
    
    # 6 Core Student Service Cards
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Key Student Administrative Services
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">Procedures for acquiring documents and institutional support from the university.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #EFF6FF; color: #2563EB;">📄</div>
                <div class="ipu-card-title">Bonafide Certificate</div>
                <div class="ipu-card-text">
                    Issued by the college/university for passport applications, visa, education loans, and bus pass concessions.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Requirements:</b> Fee receipt & ID card copy</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F0FDF4; color: #16A34A;">📜</div>
                <div class="ipu-card-title">Transcripts & Degree</div>
                <div class="ipu-card-text">
                    Official consolidated marksheets and university transcripts required for higher studies in India or abroad.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Issued by:</b> Examination Division, GGSIPU</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #FEF3C7; color: #D97706;">🪪</div>
                <div class="ipu-card-title">Student ID Cards</div>
                <div class="ipu-card-text">
                    Issued to newly enrolled candidates with permanent enrollment number, or duplicate replacement upon loss.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Verification:</b> Institute Administrative Cell</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #FDF2F8; color: #DB2777;">💰</div>
                <div class="ipu-card-title">Scholarships & EWS</div>
                <div class="ipu-card-text">
                    University financial assistance schemes including Merit-cum-Means and Delhi Government fee waiver portals.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Portal:</b> Directorate of Student Welfare</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F5F3FF; color: #7C3AED;">✈️</div>
                <div class="ipu-card-title">Migration Certificate</div>
                <div class="ipu-card-text">
                    Formal certificate provided upon program completion or transfer to another recognized university.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Processing:</b> Online IPU Academic Portal</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F0FDFA; color: #0D9488;">🛡️</div>
                <div class="ipu-card-title">Grievance Redressal</div>
                <div class="ipu-card-text">
                    Ombudsperson and Student Grievance Redressal Committee for resolving student issues impartially.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>Statute:</b> University Regulations</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Student Services Agent Console
    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">🎫 Student Services Agent</div>
            <div class="ipu-ai-title">Ask the Student Services AI Assistant</div>
        </div>
        <div class="ipu-ai-desc">
            Ask about how to obtain certificates, submit fee refund requests, check scholarship criteria, or resolve student documentation questions.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if "services_last_response" not in st.session_state:
        st.session_state.services_last_response = None
    if "services_last_query" not in st.session_state:
        st.session_state.services_last_query = None
    if "services_pending_query" not in st.session_state:
        st.session_state.services_pending_query = None

    def set_services_query(q_text: str):
        st.session_state.services_input = q_text
        st.session_state.services_pending_query = q_text

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_query = st.text_input(
            "Student Services Query",
            placeholder="e.g., What is the procedure to get a bonafide certificate or student scholarship?",
            label_visibility="collapsed",
            key="services_input"
        )
    with col_btn:
        search_clicked = st.button("Search 🔍", type="primary", use_container_width=True, key="services_search_btn")
        
    st.markdown('<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 12px;"><b>Suggested inquiries:</b></p>', unsafe_allow_html=True)
    q_cols = st.columns(4)
    suggested = [
        "How can I get a student certificate?",
        "What scholarship information is available for students?",
        "What is the procedure for obtaining a migration certificate?",
        "How do I apply for a duplicate ID card?"
    ]
    for i, prompt in enumerate(suggested):
        with q_cols[i]:
            st.button(
                prompt,
                key=f"services_prompt_{i}",
                use_container_width=True,
                on_click=set_services_query,
                args=(prompt,)
            )

    # Determine query to execute
    query_to_run = None
    if st.session_state.services_pending_query:
        query_to_run = st.session_state.services_pending_query
        st.session_state.services_pending_query = None
    elif search_clicked and user_query.strip():
        query_to_run = user_query.strip()

    if query_to_run:
        with st.spinner("Searching student services guidelines and documents..."):
            try:
                response = student_services_agent(query_to_run)
                st.session_state.services_last_response = response
                st.session_state.services_last_query = query_to_run
            except Exception as e:
                st.error(f"Error consulting Student Services Agent: {e}")

    if st.session_state.services_last_response:
        render_agent_response(
            st.session_state.services_last_response,
            "IPU Student Services Agent",
            st.session_state.services_last_query or ""
        )
