"""
Academics section for the IPU University Information Hub.
"""
import streamlit as st
from agents.academic_agent import academic_agent
from app.ui.components import render_page_banner, render_agent_response


def render_academics():
    """Renders the Academics & Regulations portal view."""
    render_page_banner(
        badge="IPU Academic Governance & Ordinances",
        title="Academics, Ordinances & Examination Regulations",
        description="Official academic rules governing curricula, credit schemes, passing standards (Ordinance 11), evaluation procedures, rechecking, and grace mark policies."
    )
    
    # Quick Regulatory Pillars Cards
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Key Academic Regulations at a Glance
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">Core statutes under GGSIPU Ordinance 11 and academic guidelines.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    pillars = [
        ("40% Pass Rule", "Passing Standard", "Minimum 40% in End-Term Theory and 40% in Continuous Internal Assessment independently."),
        ("Ordinance 11", "Grading & Evaluation", "Semester credit system, relative/absolute marking scales, SGPA, and cumulative CGPA formulas."),
        ("Grace Marks", "Policy Guidelines", "Provision of up to 5 grace marks per academic year for passing or class award where permissible."),
        ("Inspection / Rechecking", "Answer Book Review", "Defined procedures and deadlines for certified copy inspection or marks re-totaling.")
    ]
    for col, (title, sub, desc) in zip([c1, c2, c3, c4], pillars):
        with col:
            st.markdown(f"""
            <div class="ipu-card" style="min-height: 170px;">
                <div>
                    <div style="font-size: 11px; font-weight: 700; color: #2563EB; text-transform: uppercase; margin-bottom: 4px;">{sub}</div>
                    <div style="font-family: 'Outfit', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; margin-bottom: 8px;">{title}</div>
                    <div style="font-size: 12.5px; color: #64748B; line-height: 1.5;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Academic Agent Query Console
    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">📚 Academic Agent</div>
            <div class="ipu-ai-title">Consult the IPU Academic & Regulations Agent</div>
        </div>
        <div class="ipu-ai-desc">
            Ask specific questions about passing requirements, grade points, attendance eligibility (75% rule), exam rules, or course promotions.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if "acad_last_response" not in st.session_state:
        st.session_state.acad_last_response = None
    if "acad_last_query" not in st.session_state:
        st.session_state.acad_last_query = None
    if "acad_pending_query" not in st.session_state:
        st.session_state.acad_pending_query = None

    def set_acad_query(q_text: str):
        st.session_state.academic_input = q_text
        st.session_state.acad_pending_query = q_text

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_query = st.text_input(
            "Academic Query",
            placeholder="e.g., What are the passing marks for theory and practical exams in IPU?",
            label_visibility="collapsed",
            key="academic_input"
        )
    with col_btn:
        search_clicked = st.button("Search 🔍", type="primary", use_container_width=True, key="acad_search_btn")
        
    st.markdown('<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 12px;"><b>Suggested questions:</b></p>', unsafe_allow_html=True)
    q_cols = st.columns(4)
    suggested = [
        "What are the passing marks in IPU?",
        "Explain grace marks rules under IPU Ordinance",
        "What are the rules for rechecking an examination?",
        "What is the minimum attendance required for exams?"
    ]
    for i, prompt in enumerate(suggested):
        with q_cols[i]:
            st.button(
                prompt,
                key=f"acad_prompt_{i}",
                use_container_width=True,
                on_click=set_acad_query,
                args=(prompt,)
            )

    # Determine query to execute
    query_to_run = None
    if st.session_state.acad_pending_query:
        query_to_run = st.session_state.acad_pending_query
        st.session_state.acad_pending_query = None
    elif search_clicked and user_query.strip():
        query_to_run = user_query.strip()

    if query_to_run:
        with st.spinner("Retrieving academic statutes and examination regulations..."):
            try:
                response = academic_agent(query_to_run)
                st.session_state.acad_last_response = response
                st.session_state.acad_last_query = query_to_run
            except Exception as e:
                st.error(f"Error consulting Academic Agent: {e}")

    if st.session_state.acad_last_response:
        render_agent_response(
            st.session_state.acad_last_response,
            "IPU Academic Agent",
            st.session_state.acad_last_query or ""
        )
                
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Division & CGPA Reference Table
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Division Awards under Ordinance 11
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">Classification of results upon completion of undergraduate and postgraduate programs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.markdown("""
        <div class="ipu-card" style="border-top: 4px solid #10B981;">
            <div style="font-family: 'Outfit', sans-serif; font-size: 18px; font-weight: 800; color: #065F46; margin-bottom: 4px;">First with Distinction</div>
            <div style="font-size: 14px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">CGPA ≥ 7.50 / 75%+</div>
            <div style="font-size: 12.5px; color: #64748B;">Provided the student has passed all examinations within the minimum prescribed duration of the program.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_t2:
        st.markdown("""
        <div class="ipu-card" style="border-top: 4px solid #3B82F6;">
            <div style="font-family: 'Outfit', sans-serif; font-size: 18px; font-weight: 800; color: #1D4ED8; margin-bottom: 4px;">First Division</div>
            <div style="font-size: 14px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">6.50 ≤ CGPA &lt; 7.50 / 60%+</div>
            <div style="font-size: 12.5px; color: #64748B;">Awarded to candidates who clear all requirements with an overall CGPA meeting the first division threshold.</div>
        </div>
        """, unsafe_allow_html=True)

    with col_t3:
        st.markdown("""
        <div class="ipu-card" style="border-top: 4px solid #F59E0B;">
            <div style="font-family: 'Outfit', sans-serif; font-size: 18px; font-weight: 800; color: #B45309; margin-bottom: 4px;">Second Division / Pass</div>
            <div style="font-size: 14px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">5.00 ≤ CGPA &lt; 6.50 / 50%+</div>
            <div style="font-size: 12.5px; color: #64748B;">Awarded to candidates fulfilling all credit and passing criteria with a passing aggregate.</div>
        </div>
        """, unsafe_allow_html=True)
