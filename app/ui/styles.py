"""
Design system and CSS styles for the IPU University Information Hub.
"""

def get_custom_css() -> str:
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

/* Global Reset & Streamlit Chrome Overrides */
#MainMenu, footer, header {
    visibility: hidden;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: #F8FAFC;
    color: #1E293B;
}

.block-container {
    max-width: 1240px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* =========================================================
   TOP UNIVERSITY NAVBAR
   ========================================================= */
.ipu-header-strip {
    background: linear-gradient(90deg, #0F172A 0%, #1E3A8A 100%);
    color: #93C5FD;
    font-size: 11.5px;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    padding: 7px 18px;
    border-radius: 12px 12px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.ipu-navbar {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-top: none;
    border-radius: 0 0 16px 16px;
    padding: 16px 24px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.ipu-brand-logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.ipu-emblem {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #1E3A8A, #2563EB);
    color: #FFFFFF;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}

.ipu-brand-title {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.1;
}

.ipu-brand-title span {
    color: #2563EB;
}

.ipu-brand-subtitle {
    font-size: 11.5px;
    color: #64748B;
    font-weight: 500;
    letter-spacing: 0.3px;
}

/* =========================================================
   NAVIGATION BUTTONS
   ========================================================= */
div[data-testid="stHorizontalBlock"]:has(.nav-anchor) {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 6px 10px;
    margin-bottom: 24px;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
}

.stButton > button {
    font-family: 'Plus Jakarta Sans', sans-serif;
    border-radius: 10px;
    border: 1px solid #E2E8F0;
    background: #FFFFFF;
    color: #334155;
    font-weight: 600;
    font-size: 14px;
    min-height: 44px;
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    border-color: #3B82F6;
    color: #1D4ED8;
    background: #EFF6FF;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
}

.stButton > button:active {
    transform: translateY(0);
}

/* Primary Button Styling */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #1E40AF 0%, #2563EB 100%);
    border: none;
    color: #FFFFFF;
    font-weight: 700;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #1E3A8A 0%, #1D4ED8 100%);
    color: #FFFFFF;
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
    transform: translateY(-1px);
}

/* =========================================================
   HERO BANNER
   ========================================================= */
.ipu-hero {
    background: linear-gradient(135deg, #0A1128 0%, #1E3A8A 50%, #2563EB 100%);
    border-radius: 24px;
    padding: 48px 44px;
    color: #FFFFFF;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 36px rgba(14, 30, 80, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.ipu-hero::after {
    content: "";
    position: absolute;
    top: -50px;
    right: -50px;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(96, 165, 250, 0.2) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.ipu-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #BFDBFE;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    padding: 6px 14px;
    border-radius: 30px;
    margin-bottom: 16px;
    text-transform: uppercase;
}

.ipu-hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 40px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 14px;
    color: #FFFFFF;
    letter-spacing: -0.5px;
}

.ipu-hero-desc {
    font-size: 16px;
    line-height: 1.65;
    color: #DBEAFE;
    max-width: 720px;
    font-weight: 400;
}

/* Inner Page Banner */
.ipu-page-banner {
    background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 65%, #2563EB 100%);
    border-radius: 20px;
    padding: 36px 40px;
    color: #FFFFFF;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.ipu-page-badge {
    color: #93C5FD;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.ipu-page-title {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.ipu-page-desc {
    color: #DBEAFE;
    font-size: 15px;
    line-height: 1.6;
    max-width: 680px;
}

/* =========================================================
   PORTAL CARDS & INTERACTIVE TILES
   ========================================================= */
.ipu-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 24px;
    height: 100%;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.ipu-card:hover {
    border-color: #93C5FD;
    transform: translateY(-3px);
    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.08);
}

.ipu-card-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 16px;
}

.ipu-card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 750;
    color: #0F172A;
    margin-bottom: 8px;
}

.ipu-card-text {
    font-size: 13.5px;
    color: #64748B;
    line-height: 1.6;
    margin-bottom: 14px;
}

.ipu-card-link {
    font-size: 13px;
    font-weight: 700;
    color: #2563EB;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

/* Metric / Stat Box */
.ipu-stat-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px 22px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
}

.ipu-stat-value {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #1E3A8A;
    margin-bottom: 4px;
}

.ipu-stat-label {
    font-size: 12px;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* =========================================================
   AI QUERY CONSOLE & ANSWER CARDS
   ========================================================= */
.ipu-ai-console {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 20px;
    padding: 28px 32px;
    margin-top: 24px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
}

.ipu-ai-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}

.ipu-ai-badge {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    color: #1D4ED8;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.ipu-ai-title {
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 750;
    color: #0F172A;
}

.ipu-ai-desc {
    font-size: 13.5px;
    color: #64748B;
    margin-bottom: 18px;
    line-height: 1.5;
}

/* Answer Presentation Box */
.ipu-answer-container {
    background: #FFFFFF;
    border: 1px solid #BFDBFE;
    border-left: 5px solid #2563EB;
    border-radius: 16px;
    padding: 24px 28px;
    margin-top: 24px;
    box-shadow: 0 8px 25px rgba(37, 99, 235, 0.06);
}

.ipu-answer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid #F1F5F9;
}

.ipu-answer-agent-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #EFF6FF;
    color: #1E40AF;
    font-size: 12.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 30px;
    border: 1px solid #DBEAFE;
}

.ipu-answer-body {
    font-size: 15px;
    line-height: 1.75;
    color: #1E293B;
}

.ipu-answer-body p, .ipu-answer-body li {
    color: #1E293B !important;
}

.ipu-citation-box {
    margin-top: 20px;
    padding: 14px 18px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    font-size: 12.5px;
    color: #475569;
    display: flex;
    align-items: center;
    gap: 10px;
}

.ipu-citation-tag {
    background: #E2E8F0;
    color: #334155;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
}

/* =========================================================
   PROCESS ROADMAP / STEPS
   ========================================================= */
.ipu-step-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    height: 100%;
    position: relative;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.02);
}

.ipu-step-badge {
    width: 36px;
    height: 36px;
    background: #EFF6FF;
    color: #2563EB;
    border: 2px solid #BFDBFE;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 12px auto;
    font-weight: 800;
    font-size: 15px;
}

.ipu-step-title {
    font-weight: 750;
    font-size: 15px;
    color: #0F172A;
    margin-bottom: 6px;
}

.ipu-step-text {
    font-size: 12px;
    color: #64748B;
    line-height: 1.5;
}

/* =========================================================
   NOTICE ITEM CARDS
   ========================================================= */
.ipu-notice-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s ease;
}

.ipu-notice-card:hover {
    border-color: #BFDBFE;
    background: #F8FAFC;
    transform: translateX(4px);
}

.ipu-notice-meta {
    font-size: 11.5px;
    color: #64748B;
    font-weight: 600;
    margin-bottom: 4px;
}

.ipu-notice-title {
    font-size: 14.5px;
    font-weight: 700;
    color: #0F172A;
}

.ipu-notice-tag {
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    white-space: nowrap;
}

.tag-exam { background: #FEF3C7; color: #92400E; }
.tag-adm { background: #E0E7FF; color: #3730A3; }
.tag-gen { background: #E0F2FE; color: #075985; }

/* =========================================================
   FOOTER
   ========================================================= */
.ipu-footer {
    background: #FFFFFF;
    border-top: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 36px 32px 24px;
    margin-top: 48px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.02);
}

.ipu-footer-brand {
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 8px;
}

.ipu-footer-sub {
    font-size: 13px;
    color: #64748B;
    margin-bottom: 18px;
}

.ipu-footer-links {
    display: flex;
    justify-content: center;
    gap: 24px;
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 20px;
}

.ipu-footer-note {
    font-size: 11.5px;
    color: #94A3B8;
    border-top: 1px solid #F1F5F9;
    padding-top: 16px;
}
</style>
"""
