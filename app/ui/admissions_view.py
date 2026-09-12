"""
Admissions section for the IPU University Information Hub.
"""
import streamlit as st
from agents.admission_agent import admission_agent
from app.ui.components import render_page_banner, render_agent_response


def render_admissions():
    """Renders the Admissions portal view."""
    render_page_banner(
        badge="IPU Admissions & Enrollments",
        title="University Admissions & Counseling Hub",
        description="Comprehensive information on admissions criteria, CET/CUET eligibility, registration deadlines, counseling schedules, and fee structures sourced from official IPU brochures."
    )
    
    # 5-Stage Admission Journey Roadmap
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            The IPU Admission Process Roadmap
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">Key steps from application registration to final seat confirmation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st1, st2, st3, st4, st5 = st.columns(5)
    stages = [
        ("1", "Eligibility Check", "Review 10+2 / Diploma criteria and minimum aggregate requirements."),
        ("2", "Registration & CET", "Submit application on the IPU admission portal and pay registration fee."),
        ("3", "Merit & Cutoffs", "Check JEE / CUET / CET ranks and participate in online counseling rounds."),
        ("4", "Document Verification", "Provide marksheets, migration, caste/category certificate, & medical fitness."),
        ("5", "Seat Allotment & Fee", "Confirm allotted institute, submit part academic fee, and report to campus.")
    ]
    for col, (num, title, desc) in zip([st1, st2, st3, st4, st5], stages):
        with col:
            st.markdown(f"""
            <div class="ipu-step-card">
                <div class="ipu-step-badge">{num}</div>
                <div class="ipu-step-title">{title}</div>
                <div class="ipu-step-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Admission Agent Query Console
    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">🎓 Admission Agent</div>
            <div class="ipu-ai-title">Consult the IPU Admission Agent</div>
        </div>
        <div class="ipu-ai-desc">
            Ask specific questions regarding B.Tech Code 131, spot rounds, CUET merit lists, reservation policies, or brochure guidelines.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if "adm_last_response" not in st.session_state:
        st.session_state.adm_last_response = None
    if "adm_last_query" not in st.session_state:
        st.session_state.adm_last_query = None
    if "adm_pending_query" not in st.session_state:
        st.session_state.adm_pending_query = None

    def set_adm_query(q_text: str):
        st.session_state.admission_input = q_text
        st.session_state.adm_pending_query = q_text

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_query = st.text_input(
            "Admission Query",
            placeholder="e.g., What is the eligibility for B.Tech admission at IPU / DTC?",
            label_visibility="collapsed",
            key="admission_input"
        )
    with col_btn:
        search_clicked = st.button("Search 🔍", type="primary", use_container_width=True, key="adm_search_btn")
        
    st.markdown('<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 12px;"><b>Suggested inquiries:</b></p>', unsafe_allow_html=True)
    q_cols = st.columns(4)
    suggested = [
        "What is the eligibility for B.Tech admission?",
        "What are the rules for spot round counseling?",
        "Explain CUET merit list criteria for B.Tech",
        "What documents are required during counseling?"
    ]
    for i, prompt in enumerate(suggested):
        with q_cols[i]:
            st.button(
                prompt,
                key=f"adm_prompt_{i}",
                use_container_width=True,
                on_click=set_adm_query,
                args=(prompt,)
            )

    # Determine query to execute
    query_to_run = None
    if st.session_state.adm_pending_query:
        query_to_run = st.session_state.adm_pending_query
        st.session_state.adm_pending_query = None
    elif search_clicked and user_query.strip():
        query_to_run = user_query.strip()

    if query_to_run:
        with st.spinner("Searching official IPU admission brochures and circulars..."):
            try:
                response = admission_agent(query_to_run)
                st.session_state.adm_last_response = response
                st.session_state.adm_last_query = query_to_run
            except Exception as e:
                st.error(f"Error consulting Admission Agent: {e}")

    if st.session_state.adm_last_response:
        render_agent_response(
            st.session_state.adm_last_response,
            "IPU Admission Agent",
            st.session_state.adm_last_query or ""
        )
                
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Program Categories Overview
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Key Academic Streams & Program Details
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">Core undergraduate and postgraduate admissions covered under IPU regulations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #EFF6FF; color: #2563EB;">💻</div>
                <div class="ipu-card-title">B.Tech Engineering</div>
                <div class="ipu-card-text">
                    Admissions conducted on the basis of <b>JEE Main Paper 1</b> merit. Streams include Computer Science, IT, AI & Data Science, Electronics, and Mechanical.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>CET Code:</b> 131 • <b>Eligibility:</b> 55% in PCM</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F0FDF4; color: #16A34A;">📊</div>
                <div class="ipu-card-title">Management (BBA / MBA)</div>
                <div class="ipu-card-text">
                    Undergraduate management programs admit students through <b>CET / CUET</b>. MBA admissions prioritize <b>CAT / CMAT</b> scores followed by university CET.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>CET Code:</b> 125 (BBA) • <b>Eligibility:</b> 50% in 10+2</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #FEF3C7; color: #D97706;">⚡</div>
                <div class="ipu-card-title">B.Tech Lateral Entry</div>
                <div class="ipu-card-text">
                    Direct entry into the 2nd year (3rd semester) for 3-year Engineering Diploma holders or B.Sc graduates with Mathematics.
                </div>
            </div>
            <div style="font-size: 12px; color: #64748B;"><b>CET Code:</b> 128 / 129 • <b>Eligibility:</b> 60% in Diploma</div>
        </div>
        """, unsafe_allow_html=True)
