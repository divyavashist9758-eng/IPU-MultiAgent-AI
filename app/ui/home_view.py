"""
Home section for the IPU University Information Hub.
"""
import streamlit as st
from agents.supervisor_agent import supervisor_agent
from app.ui.components import render_hero, render_agent_response


def render_home():
    """Renders the comprehensive Home section."""
    if "home_last_response" not in st.session_state:
        st.session_state.home_last_response = None
    if "home_last_query" not in st.session_state:
        st.session_state.home_last_query = None
    if "home_pending_query" not in st.session_state:
        st.session_state.home_pending_query = None

    def set_home_query(q_text: str):
        st.session_state.home_global_input = q_text
        st.session_state.home_pending_query = q_text

    render_hero(
        badge="Guru Gobind Singh Indraprastha University",
        title="Your Official IPU Information Hub",
        description="Navigate admissions, academic rules, official university circulars, and student documentation with the help of a dedicated multi-agent AI system grounded in verified university documents."
    )
    
    # Global AI Quick Search Bar
    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">⚡ Quick AI Search</div>
            <div class="ipu-ai-title">Ask Any Question Across the University</div>
        </div>
        <div class="ipu-ai-desc">
            Type your inquiry below. The multi-agent supervisor will analyze your question, route it to the best specialist agent, and retrieve verified document context.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        home_query = st.text_input(
            "Global Question",
            placeholder="e.g., What are the passing criteria in IPU? Or when does B.Tech counseling start?",
            label_visibility="collapsed",
            key="home_global_input"
        )
    with col_btn:
        search_clicked = st.button("Ask AI 🚀", type="primary", use_container_width=True, key="home_global_search_btn")
        
    # Quick prompt chips for home
    st.markdown('<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 15px;"><b>Popular questions:</b></p>', unsafe_allow_html=True)
    chip_cols = st.columns(4)
    quick_queries = [
        "What are the passing marks for B.Tech in IPU?",
        "How is B.Tech admission eligibility decided?",
        "Tell me about the Prime Minister Internship Scheme.",
        "How do I apply for a student certificate?"
    ]
    
    for i, q_text in enumerate(quick_queries):
        with chip_cols[i]:
            st.button(
                q_text,
                key=f"home_chip_{i}",
                use_container_width=True,
                on_click=set_home_query,
                args=(q_text,)
            )

    # Determine if a search needs to be executed
    query_to_run = None
    if st.session_state.home_pending_query:
        query_to_run = st.session_state.home_pending_query
        st.session_state.home_pending_query = None
    elif search_clicked and home_query.strip():
        query_to_run = home_query.strip()

    if query_to_run:
        with st.spinner("🤖 IPU Multi-Agent Supervisor is routing and synthesizing verified information..."):
            try:
                response = supervisor_agent(query_to_run)
                st.session_state.home_last_response = response
                st.session_state.home_last_query = query_to_run
            except Exception as e:
                st.error(f"Error consulting agents: {e}")

    # Render latest answer if available
    if st.session_state.home_last_response:
        render_agent_response(
            st.session_state.home_last_response,
            "IPU Multi-Agent Supervisor",
            st.session_state.home_last_query or ""
        )
                
    st.markdown("<br>", unsafe_allow_html=True)
    
    # University Metrics Strip
    s1, s2, s3, s4 = st.columns(4)
    metrics = [
        ("120+", "Affiliated Institutes & DTC"),
        ("15+", "University Schools of Study"),
        ("100+", "Undergraduate & Postgrad Programs"),
        ("4 Specialized", "AI Agents & Vector Knowledge")
    ]
    for col, (val, lbl) in zip([s1, s2, s3, s4], metrics):
        with col:
            st.markdown(f"""
            <div class="ipu-stat-card">
                <div class="ipu-stat-value">{val}</div>
                <div class="ipu-stat-label">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Explore IPU Hub Sections
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 24px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Explore IPU Knowledge Portals
        </h2>
        <p style="font-size: 14px; color: #64748B;">
            Direct access to dedicated sections powered by specialized RAG agents.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #EFF6FF; color: #2563EB;">📝</div>
                <div class="ipu-card-title">Admissions</div>
                <div class="ipu-card-text">
                    Eligibility requirements, B.Tech CET/CUET codes, counseling stages, fee structures, and seat allocations.
                </div>
            </div>
            <div class="ipu-card-link">Explore Admissions →</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Admissions Portal", key="home_nav_adm", use_container_width=True):
            st.session_state.page = "Admissions"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F0FDF4; color: #16A34A;">📚</div>
                <div class="ipu-card-title">Academics</div>
                <div class="ipu-card-text">
                    IPU Ordinance 11 regulations, passing marks criteria, grading system, grace marks, and end-term exam rules.
                </div>
            </div>
            <div class="ipu-card-link">Explore Academics →</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Academics Portal", key="home_nav_acad", use_container_width=True):
            st.session_state.page = "Academics"
            st.rerun()

    with c3:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #FEF3C7; color: #D97706;">📢</div>
                <div class="ipu-card-title">University Notices</div>
                <div class="ipu-card-text">
                    Official circulars, exam date sheets, internship notices (PM Scheme), and institutional notifications.
                </div>
            </div>
            <div class="ipu-card-link">Explore Notices →</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Notices Portal", key="home_nav_not", use_container_width=True):
            st.session_state.page = "University Notices"
            st.rerun()

    with c4:
        st.markdown("""
        <div class="ipu-card">
            <div>
                <div class="ipu-card-icon" style="background: #F5F3FF; color: #7C3AED;">🎫</div>
                <div class="ipu-card-title">Student Services</div>
                <div class="ipu-card-text">
                    Bonafide certificates, migration cards, transcripts, scholarship schemes, and student grievance procedures.
                </div>
            </div>
            <div class="ipu-card-link">Explore Services →</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Services Portal", key="home_nav_serv", use_container_width=True):
            st.session_state.page = "Student Services"
            st.rerun()
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Why Use IPU AI / Multi-Agent Architecture
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 24px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            How the Multi-Agent AI System Works
        </h2>
        <p style="font-size: 14px; color: #64748B;">
            Engineered with modern LLMs and semantic vector search for verified, non-hallucinated university information.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    f1, f2, f3, f4 = st.columns(4)
    features = [
        ("🤖", "Router & Supervisor", "Incoming queries are classified into domain intents via Qwen3-8B with heuristic fallbacks."),
        ("📚", "Vector Store (ChromaDB)", "Ingested official IPU brochures, ordinances, and circulars embedded with semantic vectors."),
        ("🔍", "Grounded RAG", "Context-filtered chunks with strict page/source references prevent fabricated information."),
        ("⚡", "Sub-Second Answers", "Fast, high-precision answers with direct citations for reliable academic planning.")
    ]
    for col, (icon, title, desc) in zip([f1, f2, f3, f4], features):
        with col:
            st.markdown(f"""
            <div class="ipu-card" style="min-height: 160px;">
                <div>
                    <div style="font-size: 28px; margin-bottom: 8px;">{icon}</div>
                    <div style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 750; color: #0F172A; margin-bottom: 6px;">{title}</div>
                    <div style="font-size: 13px; color: #64748B; line-height: 1.5;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    # Quick FAQ Accordion
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 12px;">
        Frequently Consulted University Topics
    </h3>
    """, unsafe_allow_html=True)
    
    with st.expander("📌 How do I check minimum passing marks for B.Tech under Ordinance 11?"):
        st.write("""
        Under IPU regulations (Ordinance 11), a candidate must obtain at least **40% marks in Theory** and **40% marks in Practical/Internal** separately to pass a subject course. Aggregate requirements and credit promotion criteria also apply.
        """)
        
    with st.expander("📌 Where can I find information on the Prime Minister's Internship Scheme?"):
        st.write("""
        The Prime Minister's Internship Scheme circular is part of the university notices. It outlines eligible batches, registration steps, and monthly stipend guidelines for student internships.
        """)
        
    with st.expander("📌 What is the procedure for obtaining a Bonafide Certificate?"):
        st.write("""
        Students must apply through their respective institute or department with proof of fee receipt and student ID. The Student Services agent can assist with specific documentation requirements.
        """)
