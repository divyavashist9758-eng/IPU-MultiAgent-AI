"""
Reusable UI components for the IPU University Information Hub.
"""
import streamlit as st
import re


def render_header():
    """Renders the top institutional strip and branding bar."""
    st.markdown("""
    <div class="ipu-header-strip">
        <span>🏛️ Guru Gobind Singh Indraprastha University (GGSIPU)</span>
        <span>⚡ Multi-Agent AI Information System</span>
    </div>
    <div class="ipu-navbar">
        <div class="ipu-brand-logo">
            <div class="ipu-emblem">🎓</div>
            <div>
                <div class="ipu-brand-title">IPU <span>Hub</span></div>
                <div class="ipu-brand-subtitle">Official Student Knowledge & Multi-Agent Advisory Center</div>
            </div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <span style="background: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; padding: 4px 12px; border-radius: 20px; font-size: 11.5px; font-weight: 700;">
                ● RAG System Live
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_navigation(active_page: str):
    """
    Renders the unified 6-section navigation bar.
    """
    st.markdown('<div class="nav-anchor" style="display:none;"></div>', unsafe_allow_html=True)
    
    sections = [
        ("Home", "🏠 Home"),
        ("Admissions", "📝 Admissions"),
        ("Academics", "📚 Academics"),
        ("University Notices", "📢 Notices"),
        ("Student Services", "🎫 Student Services"),
        ("AI Assistant", "🤖 AI Assistant")
    ]
    
    cols = st.columns(len(sections))
    for i, (key, label) in enumerate(sections):
        with cols[i]:
            is_active = (active_page == key)
            btn_type = "primary" if is_active else "secondary"
            if st.button(label, key=f"nav_btn_{key}", use_container_width=True, type=btn_type):
                if st.session_state.get("page") != key:
                    st.session_state.page = key
                    st.rerun()


def render_hero(badge: str, title: str, description: str):
    """Renders the home hero banner."""
    st.markdown(f"""
    <div class="ipu-hero">
        <div class="ipu-hero-badge">🏛️ {badge}</div>
        <div class="ipu-hero-title">{title}</div>
        <div class="ipu-hero-desc">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def render_page_banner(badge: str, title: str, description: str):
    """Renders an inner page banner."""
    st.markdown(f"""
    <div class="ipu-page-banner">
        <div class="ipu-page-badge">{badge}</div>
        <div class="ipu-page-title">{title}</div>
        <div class="ipu-page-desc">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def render_agent_response(response_text: str, agent_name: str, query: str = ""):
    """
    Nicely renders agent response with citation separation.
    """
    if not response_text:
        return
        
    # Check if there are sources mentioned in the response
    source_match = re.search(r"(Source:.*?|Page:.*)", response_text, re.IGNORECASE | re.DOTALL)
    
    body_text = response_text
    citation_text = ""
    
    if "Source:" in response_text:
        parts = response_text.split("Source:", 1)
        body_text = parts[0].strip()
        citation_text = "Source: " + parts[1].strip()
    elif "Sources:" in response_text:
        parts = response_text.split("Sources:", 1)
        body_text = parts[0].strip()
        citation_text = "Sources: " + parts[1].strip()
        
    st.markdown(f"""
    <div class="ipu-answer-container">
        <div class="ipu-answer-header">
            <div class="ipu-answer-agent-tag">
                <span>🤖</span> <b>{agent_name}</b> Verified Answer
            </div>
            <div style="font-size: 11.5px; color: #64748B; font-weight: 600;">
                Retrieved from Ingested University Documents
            </div>
        </div>
        <div class="ipu-answer-body">
    """, unsafe_allow_html=True)
    
    # Write the body using streamlit markdown for proper formatting of bullet points, tables, bold text
    st.markdown(body_text)
    
    if citation_text:
        st.markdown(f"""
        <div class="ipu-citation-box">
            <span class="ipu-citation-tag">📄 CITATION</span>
            <span>{citation_text}</span>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("</div></div>", unsafe_allow_html=True)


def render_footer():
    """Renders standard university portal footer."""
    st.markdown("""
    <div class="ipu-footer">
        <div class="ipu-footer-brand">🎓 GGSIPU Multi-Agent Knowledge Hub</div>
        <div class="ipu-footer-sub">
            Intelligent Information Assistance for Guru Gobind Singh Indraprastha University & Affiliated Colleges (DTC)
        </div>
        <div class="ipu-footer-links">
            <span>Admissions Hub</span> • 
            <span>Academic Regulations</span> • 
            <span>University Circulars</span> • 
            <span>Student Welfare</span> • 
            <span>AI Consultation</span>
        </div>
        <div class="ipu-footer-note">
            ⚠️ Disclaimer: Information is retrieved via AI agents from official university documents and circulars. For legal confirmations, refer to official notifications at <a href="http://www.ipu.ac.in" target="_blank" style="color: #2563EB; text-decoration: none;">ipu.ac.in</a>.
        </div>
    </div>
    """, unsafe_allow_html=True)
