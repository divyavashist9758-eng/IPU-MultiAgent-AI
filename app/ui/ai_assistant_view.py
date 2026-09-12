"""
AI Assistant section for the IPU University Information Hub.
"""
import streamlit as st
from agents.supervisor_agent import supervisor_agent
from agents.router_agent import router_agent
from app.ui.components import render_page_banner, render_agent_response


def render_ai_assistant():
    """Renders the AI Assistant multi-agent consultation view."""
    render_page_banner(
        badge="Multi-Agent University Advisory System",
        title="🤖 IPU AI Multi-Agent Advisory Center",
        description="Ask any question regarding admissions, academic regulations, examination schedules, circulars, or student services. The supervisor agent intelligently directs your request to the appropriate specialist agent."
    )
    
    # Architecture Overview Cards
    c1, c2, c3, c4 = st.columns(4)
    agents_info = [
        ("📝 Admission Agent", "B.Tech CET Codes, CUET, counseling rounds, documents & eligibility."),
        ("📚 Academic Agent", "Ordinance 11, passing criteria, grace marks, CGPA & exams."),
        ("📢 Notice Agent", "Circulars, internship schemes, date sheets & official announcements."),
        ("🎫 Services Agent", "Bonafide, migration, transcripts, scholarships & student welfare.")
    ]
    for col, (name, role) in zip([c1, c2, c3, c4], agents_info):
        with col:
            st.markdown(f"""
            <div class="ipu-card" style="min-height: 120px; padding: 16px;">
                <div style="font-weight: 750; font-size: 14px; color: #0F172A; margin-bottom: 4px;">{name}</div>
                <div style="font-size: 12px; color: #64748B; line-height: 1.4;">{role}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize conversation history in session state
    if "ai_chat_history" not in st.session_state:
        st.session_state.ai_chat_history = []
        
    # AI Query Input Console
    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">⚡ Full Multi-Agent Assistant</div>
            <div class="ipu-ai-title">What would you like to know about IPU?</div>
        </div>
        <div class="ipu-ai-desc">
            Type your question below. Our routing intelligence will classify the intent and formulate a grounded answer.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if "ai_pending_query" not in st.session_state:
        st.session_state.ai_pending_query = None

    def set_ai_query(q_text: str):
        st.session_state.ai_assistant_input = q_text
        st.session_state.ai_pending_query = q_text

    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_query = st.text_input(
            "AI Assistant Query",
            placeholder="Ask anything about IPU (e.g., 'What are the passing marks for B.Tech?', 'Tell me about PM internship scheme')",
            label_visibility="collapsed",
            key="ai_assistant_input"
        )
    with col_btn:
        ask_clicked = st.button("Consult AI 🚀", type="primary", use_container_width=True, key="ai_assistant_search_btn")
        
    st.markdown('<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 12px;"><b>Example prompts:</b></p>', unsafe_allow_html=True)
    q_cols = st.columns(4)
    examples = [
        "What are the passing marks in IPU?",
        "How is B.Tech admission eligibility decided?",
        "Tell me about the Prime Minister Internship Scheme.",
        "How do I apply for a student certificate?"
    ]
    for i, prompt in enumerate(examples):
        with q_cols[i]:
            st.button(
                prompt,
                key=f"ai_ex_{i}",
                use_container_width=True,
                on_click=set_ai_query,
                args=(prompt,)
            )

    # Determine query to execute
    query_to_run = None
    if st.session_state.ai_pending_query:
        query_to_run = st.session_state.ai_pending_query
        st.session_state.ai_pending_query = None
    elif ask_clicked and user_query.strip():
        query_to_run = user_query.strip()

    if query_to_run:
        with st.spinner("Analyzing question intent & consulting specialist agent..."):
            try:
                # Detect route for transparency
                detected_route = "GENERAL"
                try:
                    detected_route = router_agent(query_to_run)
                except Exception:
                    pass
                
                response = supervisor_agent(query_to_run)
                
                # Save into history
                st.session_state.ai_chat_history.append({
                    "query": query_to_run,
                    "response": response,
                    "route": detected_route
                })
            except Exception as e:
                st.error(f"Error during AI Consultation: {e}")
                
    # Display Chat History / Latest Answers
    if st.session_state.ai_chat_history:
        st.markdown("<br>", unsafe_allow_html=True)
        h_col1, h_col2 = st.columns([5, 1])
        with h_col1:
            st.markdown("""
            <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 4px;">
                Consultation Responses
            </h3>
            """, unsafe_allow_html=True)
        with h_col2:
            if st.button("Clear History 🗑️", key="clear_chat_hist", use_container_width=True):
                st.session_state.ai_chat_history = []
                st.session_state.ai_active_query = None
                st.rerun()
                
        for item in reversed(st.session_state.ai_chat_history):
            st.markdown(f"""
            <div style="background: #F1F5F9; border-radius: 12px; padding: 12px 18px; margin-top: 14px; margin-bottom: 8px;">
                <span style="font-size: 11px; font-weight: 700; color: #64748B; text-transform: uppercase;">You Asked:</span>
                <div style="font-weight: 700; font-size: 15px; color: #0F172A; margin-top: 2px;">{item['query']}</div>
                <div style="margin-top: 6px;">
                    <span style="background: #E2E8F0; color: #334155; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 700;">
                        ROUTED TO: {item.get('route', 'MULTI-AGENT')}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_agent_response(item['response'], f"IPU AI ({item.get('route', 'Supervisor')})", item['query'])
