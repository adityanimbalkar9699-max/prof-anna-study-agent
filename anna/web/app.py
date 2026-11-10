"""
Prof. Anna Interactive Web Studio
=================================
A world-class luxury web dashboard for academic & competitive examination excellence.
Features:
- Universal Omni-Disciplinary Solver (UPSC, NEET, JEE, CA/Commerce, Law, AI)
- Mark-Targeted Answer Formulator (2M, 5M, 8M, 10M, 15M)
- 60fps Kinetic Video Storyboard & Presentation Studio
- Spatial Memory Palace & Mnemonic Generator ("Smart Work over Hard Work")
- Universal Diagram Studio with Verified External Reference Links (PubMed, NCERT, Nature, UPSC)
- Anti-AI Luxury PDF Publisher, SIH Pitch Optimizer & IEEE Access Paper Synthesizer
"""

import os
import streamlit as st
from anna.core.professor import ProfAnna

# Page Configuration
st.set_page_config(
    page_title="Prof. Anna • World-Class All-Rounder Professor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Anti-AI Aesthetic, Apple/Linear Luxury Tone)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background-color: #FAF9F6;
        color: #0F172A;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 2rem;
        border-radius: 14px;
        color: white;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
    }
    
    .metric-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    
    .badge-teal { background: #CCFBF1; color: #0F766E; }
    .badge-amber { background: #FEF3C7; color: #92400E; }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
</style>
""", unsafe_allow_html=True)

if "anna" not in st.session_state:
    st.session_state.anna = ProfAnna()

anna = st.session_state.anna

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🎓 **PROF. ANNA**")
    st.caption("World-Class All-Rounder Sovereign Professor")
    st.markdown("---")
    
    nav = st.radio(
        "Sovereign Academic Engines",
        [
            "🌍 Universal Answer Formulator (UPSC/NEET/JEE/CA)",
            "🎬 Kinetic Video Script & 60fps Deck",
            "🧠 Mnemonic & Memory Palace Studio",
            "📐 Universal Diagram Studio + Fallbacks",
            "📄 Anti-AI Luxury PDF Studio",
            "📊 PPT Cloner & SIH Hackathon",
            "📜 IEEE Access Research Paper",
            "🎯 Exam Forensics (Pareto 80/20)",
            "🔍 Solution Grader & 'Cheque'",
        ],
    )
    st.markdown("---")
    st.caption("Disciplines: Civil Services • Pre-Med • Pure Sciences • Commerce • Engineering • AI")
    st.caption("Standard: 100% Mark-Securing Full Proofs")

# Header
st.markdown("""
<div class="main-header">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <span class="metric-badge badge-teal">World-Class All-Rounder Sovereign Professor</span>
            <h1 style="margin: 0.5rem 0 0 0; font-size: 2.1rem; font-weight: 800; letter-spacing: -0.03em;">Prof. Anna Universal Academic Studio</h1>
            <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                Reverse-engineered study excellence for UPSC, MPSC, NEET, JEE, CA/Commerce, Engineering, AI &amp; Law.
            </p>
        </div>
        <div style="text-align:right;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #38BDF8;">All-Rounder</div>
            <div style="font-size: 0.75rem; color: #94A3B8; text-transform:uppercase; letter-spacing:0.05em;">Multi-Discipline</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 1. Universal Answer Formulator
if nav == "🌍 Universal Answer Formulator (UPSC/NEET/JEE/CA)":
    st.subheader("🌍 Universal Mark-Targeted Answer Formulator")
    st.write("Generates 100% full, mark-securing answers with Definitions, Diagrams, Mechanisms, Case Studies, and Conclusions.")

    col1, col2 = st.columns([2, 1])
    with col1:
        q_input = st.text_area(
            "Enter Examination Question:",
            value="Examine the doctrine of Separation of Powers under the Indian Constitution and its contemporary judicial developments.",
            height=120,
        )
    with col2:
        domain = st.selectbox("Exam / Academic Domain", ["Auto-Detect", "UPSC_CIVIL_SERVICES", "MEDICAL_NEET", "COMMERCE_ACCOUNTING", "JEE_PHYSICAL_SCIENCES", "AI_MACHINE_LEARNING", "LAW_LEGAL"])
        target_marks = st.select_slider("Target Question Marks", options=[2, 5, 8, 10, 15], value=8)
        submit_btn = st.button("Synthesize Full Mark Answer", type="primary")

    if submit_btn or q_input:
        domain_hint = None if domain == "Auto-Detect" else domain
        with st.spinner("Prof. Anna is structuring complete mark-securing answer..."):
            ans = anna.solve_omni(q_input, target_marks=target_marks, domain_hint=domain_hint)

        st.success(f"Formulated for {ans.target_marks} Marks ({ans.rubric_strategy.recommended_words}) • Domain: {ans.field_domain}")
        
        st.markdown(f"**Scoring Strategy:** {ans.rubric_strategy.scoring_focus}")

        st.markdown("### I. Introduction & Governing Foundation")
        st.write(ans.introduction)
        st.info(f"**Governing Principle / Article / Axiom:** {ans.governing_statute_or_theory}")

        st.markdown("### II. Required Schematic / Diagram Blueprint")
        st.markdown(f"**Concept:** `{ans.diagram_concept}`")
        st.caption(f"**Visual Description for Examiner:** {ans.diagram_description}")

        st.markdown("### III. Comprehensive Working & Dimensional Breakdown")
        for dim in ans.core_working_or_provisions:
            with st.expander(dim.get("dimension"), expanded=True):
                for p in dim.get("details", []):
                    st.write(f"- {p}")

        if ans.step_calculations:
            st.markdown("### IV. Step-by-Step Calculations & Invariants")
            for c in ans.step_calculations:
                st.code(c)

        st.markdown("### V. Real-World Applications & Landmark Case Laws")
        for app in ans.applications_and_case_laws:
            st.write(f"✓ **{app}**")

        st.warning(f"⚠️ **{ans.examiner_trap_warning}**")

        st.markdown(f"""
        <div style="background:#F0FDF4; border:1.5px solid #10B981; border-radius:8px; padding:1.2rem; margin-top:1rem;">
            <div style="font-size:0.8rem; font-weight:700; color:#065F46; text-transform:uppercase;">Conclusion &amp; Way Forward (Max Marks Secured)</div>
            <div style="font-size:1.05rem; color:#0F172A; margin-top:0.4rem; line-height:1.6;">{ans.conclusion_way_forward}</div>
        </div>
        """, unsafe_allow_html=True)

# 2. Kinetic Video Script & 60fps Deck
elif nav == "🎬 Kinetic Video Script & 60fps Deck":
    st.subheader("🎬 Kinetic Video Lecture Script & 60fps Storyboard Studio")
    st.write("Generates timestamped video scripts with visual prompts, spoken voiceover, and interactive 60fps animated web decks.")

    col1, col2 = st.columns([2, 1])
    with col1:
        vid_topic = st.text_input("Lecture / Presentation Topic:", value="Transformer Multi-Head Attention Mechanism")
    with col2:
        vid_domain = st.selectbox("Topic Category", ["Deep Learning / AI", "UPSC Polity", "Medical Physiology", "JEE Physics", "Corporate Accounting"])
        vid_dur = st.number_input("Target Duration (Minutes)", min_value=1, max_value=15, value=3)
        gen_vid_btn = st.button("Generate Video Storyboard", type="primary")

    if gen_vid_btn or vid_topic:
        with st.spinner("Writing cinematic pedagogical video script..."):
            pkg = anna.generate_video_package(vid_topic, domain=vid_domain, total_minutes=vid_dur)

        st.success(f"Video Production Package Ready: {len(pkg.scenes)} Scenes ({pkg.estimated_duration})")

        for s in pkg.scenes:
            with st.expander(f"Scene {s.scene_number}: {s.scene_title} ({s.timestamp_range})", expanded=True):
                st.markdown(f"**Pedagogical Goal:** *{s.pedagogical_purpose}*")
                st.code(f"📹 VISUAL: {s.on_screen_visual_direction}\n⚡ KINETIC CUE: {s.kinetic_animation_cue}")
                st.info(f"🗣️ **SPOKEN VOICEOVER:**\n\n\"{s.voiceover_dialogue}\"")

        with open(pkg.script_markdown_path, "r", encoding="utf-8") as f:
            st.download_button("📥 Download Full Script Markdown (.md)", f.read(), file_name=os.path.basename(pkg.script_markdown_path), mime="text/markdown")

        with open(pkg.interactive_html5_deck_path, "r", encoding="utf-8") as f:
            st.download_button("📥 Download 60fps Kinetic Animated Presentation (.html)", f.read(), file_name=os.path.basename(pkg.interactive_html5_deck_path), mime="text/html")

# 3. Mnemonic & Memory Palace Studio
elif nav == "🧠 Mnemonic & Memory Palace Studio":
    st.subheader("🧠 Mnemonic & Spatial Memory Palace (Method of Loci) Studio")
    st.write("Convert complex lists, articles, anatomical nerves, and formulas into unforgettable phonetic mnemonics and mental palaces.")

    m_topic = st.text_input("Enter Topic or Concept to Memorize:", value="12 Schedules of Indian Constitution")
    m_btn = st.button("Construct Memory Palace", type="primary")

    if m_btn or m_topic:
        m_pkg = anna.construct_memory_palace(m_topic)
        st.success(f"Mnemonic Acronym: {m_pkg.phonetic_acronym}")
        st.info(f"**Story Hook:** {m_pkg.rhyming_or_story_hook}")

        st.markdown("### Phonetic Letter Breakdown")
        for k, v in m_pkg.breakdown.items():
            st.write(f"- **{k}**: {v}")

        st.markdown("### Spatial Memory Palace Rooms (Walkthrough Journey)")
        for r in m_pkg.memory_palace_rooms:
            with st.expander(f"{r.room_name} ➔ Anchor: {r.physical_anchor}", expanded=True):
                st.write(f"**Concept:** {r.concept_to_remember}")
                st.write(f"**Vivid Story:** {r.vivid_sensory_story}")
                st.caption(f"**Exam Cue:** {r.exam_cue}")

        st.warning(f"💡 **Examiner Recall Secret:** {m_pkg.examiner_recall_secret}")

# 4. Universal Diagram Studio + Fallbacks
elif nav == "📐 Universal Diagram Studio + Fallbacks":
    st.subheader("📐 Universal Publication Diagram Studio with Direct Authoritative Links")
    st.write("Renders vector SVGs and scientific plots across Medical, UPSC, Commerce, JEE, and Computer Science.")

    d_topic = st.selectbox(
        "Select Concept Diagram:",
        [
            "Nephron Counter-Current Multiplier (Medical)",
            "Action Potential Curve (Neurophysiology)",
            "Separation of Powers Triad (UPSC Polity)",
            "Balance Sheet T-Account Architecture (Commerce/CA)",
            "Cost-Volume-Profit Break-Even Chart (Finance)",
            "Carnot Cycle Indicator Diagram (JEE Physics)",
            "Transformer Multi-Head Attention (Computer Science)",
        ],
    )
    render_btn = st.button("Render High-Res Diagram", type="primary")

    if render_btn or d_topic:
        res = anna.render_omni_diagram(d_topic)
        st.success(f"Generated Diagram: {res.get('diagram_type')}")

        if res.get("png_file") and os.path.exists(res.get("png_file")):
            st.image(res.get("png_file"))
        elif res.get("svg_file") and os.path.exists(res.get("svg_file")):
            with open(res.get("svg_file"), "r", encoding="utf-8") as f:
                st.image(f.read())

        fb = res.get("fallback_info", {})
        st.markdown("### 🌐 Authoritative Reference Documentation")
        st.markdown(f"**Source:** {fb.get('source')}")
        st.markdown(f"**Title:** {fb.get('title')}")
        st.markdown(f"**Description:** {fb.get('description')}")
        st.markdown(f"[🔗 Direct Authoritative Reference Page]({fb.get('primary_url')})")
        st.markdown(f"[🖼️ Direct High-Definition Blueprint Link]({fb.get('diagram_url')})")

# 5. Anti-AI Luxury PDF Studio
elif nav == "📄 Anti-AI Luxury PDF Studio":
    st.subheader("📄 Anti-AI Luxury Publication PDF Generator")
    pdf_topic = st.text_input("Topic for Publication Report", value="Divide and Conquer Master Theorem Analysis")
    if st.button("Generate Handcrafted PDF", type="primary"):
        with st.spinner("Compiling publication PDF..."):
            sol = anna.solve_assignment(pdf_topic)
            diag = anna.generate_diagram(pdf_topic)
            pdf_path = anna.generate_pdf(sol.to_dict(), filename=f"solution_{pdf_topic.replace(' ', '_')}.pdf", diagram_image_path=diag.get("png_file"))
        st.success(f"PDF Compiled: {pdf_path}")
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download Handcrafted PDF", f.read(), file_name=os.path.basename(pdf_path), mime="application/pdf")

# 6. PPT Cloner & SIH Hackathon
elif nav == "📊 PPT Cloner & SIH Hackathon":
    st.subheader("📊 PPT Cloner & Smart India Hackathon (SIH) Optimizer")
    sih_t = st.text_input("Hackathon Title", value="Autonomous Rural Water Leakage Detector")
    sih_ps = st.text_input("Problem Statement ID", value="SIH-2024-PS1482")
    if st.button("Optimize SIH Deck", type="primary"):
        opt = anna.optimize_sih_deck([{"title": "Overview", "bullets": ["AI Solution"]}], ps_id=sih_ps, project_title=sih_t)
        st.metric("SIH Readiness Score", f"{opt.overall_sih_readiness_score}/100")
        st.json(opt.rubric_scores)
        deck_res = anna.clone_presentation(opt.optimized_slides_schema, {"title": sih_t, "author": "Aditya Nimbalkar"}, output_filename="sih_winning_deck.pptx")
        with open(deck_res.get("pptx_file"), "rb") as f:
            st.download_button("📥 Download Winning SIH PPTX (16:9)", f.read(), file_name="sih_winning_deck.pptx")

# 7. IEEE Access Research Paper
elif nav == "📜 IEEE Access Research Paper":
    st.subheader("📜 IEEE Access Research Paper Generator")
    paper_top = st.text_input("Research Topic", value="Decentralized Edge Federated Learning")
    if st.button("Synthesize IEEE Paper", type="primary"):
        p_res = anna.generate_ieee_paper(paper_top)
        st.success(f"Paper Synthesized: {p_res.get('title')}")
        with open(p_res.get("latex_file"), "r", encoding="utf-8") as f:
            st.download_button("📥 Download LaTeX (.tex)", f.read(), file_name=os.path.basename(p_res.get("latex_file")), mime="text/plain")

# 8. Exam Forensics (Pareto 80/20)
elif nav == "🎯 Exam Forensics (Pareto 80/20)":
    st.subheader("🎯 Pareto 80/20 Exam Forensics")
    sub = st.selectbox("Subject", ["Operating Systems", "Design and Analysis of Algorithms"])
    rep = anna.analyze_exam_readiness(subject_name=sub)
    st.metric("Predicted Success Rate", f"{rep.predicted_success_rate}%")
    for t in rep.pareto_80_20_topics:
        st.checkbox(f"[{t.recurrence_probability*100:.0f}% Prob] {t.concept_name} ({t.typical_marks}M)", value=t.is_mastered, key=t.topic_id)

# 9. Solution Grader & "Cheque"
elif nav == "🔍 Solution Grader & 'Cheque'":
    st.subheader("🔍 Solution Grader & Rubric Checker")
    prob_text = st.text_input("Problem Statement", value="Solve recurrence T(n) = 2T(n/2) + n")
    draft_text = st.text_area("Student's Draft Solution:", value="Given T(n)=2T(n/2)+n. By Master Theorem Case 2, T(n)=Theta(n log n). Q.E.D.")
    if st.button("Run Audit", type="primary"):
        audit = anna.check_solution(prob_text, draft_text)
        st.metric("Score", f"{audit.overall_score} / {audit.total_marks}")
        st.info(f"Grade: {audit.grade}")
        for r in audit.rubric_breakdown:
            st.write(f"- **{r.criterion_name}**: {r.awarded_marks}/{r.max_marks} ({r.status})")
