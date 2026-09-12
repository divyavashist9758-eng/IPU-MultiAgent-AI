"""
University Notices & Circulars section for the IPU University Information Hub.
"""

import streamlit as st

from agents.notice_agent import notice_agent
from app.ui.components import render_page_banner, render_agent_response
from utils.live_notices import fetch_live_notices


def render_notices():
    """Renders the University Notices view."""

    render_page_banner(
        badge="Official Notifications & Circulars",
        title="University Notices & Announcements Hub",
        description="View the latest official IPU notices and search the verified university knowledge base."
    )

    # ---------------------------------------------------------
    # LIVE IPU NOTICES
    # ---------------------------------------------------------
    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px;
        font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Latest Live IPU Notices
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">
            These notices are fetched directly from the official IPU website.
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        live_notices = fetch_live_notices(10)

        if live_notices:
            for i, notice in enumerate(live_notices):
                col_left, col_right = st.columns([5, 1])

                with col_left:
                    st.markdown(
                        f"""
                        <div class="ipu-notice-card" style="margin-bottom: 10px;">
                            <div>
                                <div class="ipu-notice-meta">
                                    LIVE · OFFICIAL IPU
                                </div>
                                <div class="ipu-notice-title">
                                    {notice["title"]}
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col_right:
                    st.link_button(
                        "Open PDF",
                        notice["url"],
                        use_container_width=True
                    )
        else:
            st.info("No live notices were found right now.")

    except Exception as e:
        st.warning(
            f"Live IPU notices could not be loaded right now. "
            f"The AI notice search is still available below."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # NOTICE AI SEARCH
    # ---------------------------------------------------------

    st.markdown("""
    <div class="ipu-ai-console">
        <div class="ipu-ai-header">
            <div class="ipu-ai-badge">Notice Agent</div>
            <div class="ipu-ai-title">Search University Circulars with AI</div>
        </div>
        <div class="ipu-ai-desc">
            Ask questions about examinations, internships, deadlines,
            circulars, or official university instructions.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "notice_last_response" not in st.session_state:
        st.session_state.notice_last_response = None

    if "notice_last_query" not in st.session_state:
        st.session_state.notice_last_query = None

    if "notice_pending_query" not in st.session_state:
        st.session_state.notice_pending_query = None

    def set_notice_query(q_text: str):
        st.session_state.notice_input = q_text
        st.session_state.notice_pending_query = q_text

    col_input, col_btn = st.columns([5, 1])

    with col_input:
        user_query = st.text_input(
            "Notice Query",
            placeholder="e.g., What are the latest examination notices?",
            label_visibility="collapsed",
            key="notice_input"
        )

    with col_btn:
        search_clicked = st.button(
            "Search",
            type="primary",
            use_container_width=True,
            key="notice_search_btn"
        )

    st.markdown(
        '<p style="font-size: 13px; color: #64748B; margin-top: -10px; margin-bottom: 12px;">'
        '<b>Frequently searched notices:</b></p>',
        unsafe_allow_html=True
    )

    q_cols = st.columns(4)

    suggested = [
        "Tell me about the Prime Minister Internship Scheme.",
        "What are the latest examination notices?",
        "What is the date sheet for B.Tech theory and practical exams?",
        "What are the circulars regarding answer book inspection?"
    ]

    for i, prompt in enumerate(suggested):
        with q_cols[i]:
            st.button(
                prompt,
                key=f"notice_prompt_{i}",
                use_container_width=True,
                on_click=set_notice_query,
                args=(prompt,)
            )

    query_to_run = None

    if st.session_state.notice_pending_query:
        query_to_run = st.session_state.notice_pending_query
        st.session_state.notice_pending_query = None

    elif search_clicked and user_query.strip():
        query_to_run = user_query.strip()

    if query_to_run:
        with st.spinner("Searching university notice knowledge base..."):
            try:
                response = notice_agent(query_to_run)

                st.session_state.notice_last_response = response
                st.session_state.notice_last_query = query_to_run

            except Exception as e:
                st.error(f"Error consulting Notice Agent: {e}")

    if st.session_state.notice_last_response:
        render_agent_response(
            st.session_state.notice_last_response,
            "IPU Notice Agent",
            st.session_state.notice_last_query or ""
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # EXISTING INDEXED NOTICE CATEGORIES
    # ---------------------------------------------------------

    st.markdown("""
    <div style="margin-bottom: 14px;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px;
        font-weight: 800; color: #0F172A; margin-bottom: 4px;">
            Indexed Notice Categories
        </h3>
        <p style="font-size: 13.5px; color: #64748B;">
            Existing notices and official documents stored in the IPU knowledge base.
        </p>
    </div>
    """, unsafe_allow_html=True)

    notices = [
        {
            "cat": "Career & Internships",
            "title": "Prime Minister's Internship Scheme — Pilot Project Guidelines & Eligibility",
            "tag": "OPPORTUNITY",
            "tag_class": "tag-adm",
            "query": "What are the eligibility criteria and stipend for the Prime Minister Internship Scheme?"
        },
        {
            "cat": "Examination Division",
            "title": "Final Date Sheet for End Term Theory & Practical Examinations for Affiliated Institutes",
            "tag": "EXAMINATION",
            "tag_class": "tag-exam",
            "query": "Tell me about the final date sheet for B.Tech theory and practical examinations."
        },
        {
            "cat": "Student Welfare",
            "title": "Procedures for Rechecking, Re-evaluation & Inspection of Evaluated Answer Sheets",
            "tag": "EVALUATION",
            "tag_class": "tag-gen",
            "query": "What are the regulations and fees for inspection of evaluated answer books?"
        }
    ]

    for item in notices:
        c_left, c_right = st.columns([4, 1])

        with c_left:
            st.markdown(
                f"""
                <div class="ipu-notice-card" style="margin-bottom: 0px;">
                    <div>
                        <div class="ipu-notice-meta">{item["cat"]}</div>
                        <div class="ipu-notice-title">{item["title"]}</div>
                    </div>
                    <span class="ipu-notice-tag {item["tag_class"]}">
                        {item["tag"]}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c_right:
            st.button(
                "Query Notice",
                key=f"btn_notice_{item['tag']}",
                use_container_width=True,
                on_click=set_notice_query,
                args=(item["query"],)
            )

        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
