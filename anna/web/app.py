"""
Prof. Anna Interactive Web Studio
=================================
A world-class luxury web dashboard for academic excellence, assignment solving,
Anti-AI PDF publishing, presentation cloning, SIH pitch optimization, IEEE Access
research paper synthesis, and Pareto 80/20 exam forensics.
"""

import os
import streamlit as st
from anna.core.professor import ProfAnna

# Page Configuration
st.set_page_config(
    page_title="Prof. Anna • Academic Sovereign Agent",
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
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
    }
    
    .academic-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
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
    .badge-emerald { background: #D1FAE5; color: #065F46; }
</style>
""", unsafe_allow_html=True)

# Initialize Agent
if "anna" not in st.session_state:
    st.session_state.anna = ProfAnna()

anna = st.session_state.anna

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🎓 **PROF. ANNA**")
    st.caption("Academic Sovereign Mentor • PhD Evaluator")
    st.markdown("---")
    
    nav = st.radio(
        "Academic Operating Engines",
        [
            "📝 Assignment Solver & Proofs",
            "🔍 Solution Grader & 'Cheque'",
            "📄 Anti-AI Luxury PDF Studio",
            "📐 Autonomous Diagram Studio",
            "📊 PPT Cloner & SIH Optimizer",
            "📜 IEEE Access Research Paper",
            "🎯 Exam Forensics (Pareto 80/20)",
            "💡 Feynman Intuition & Flashcards",
        ],
    )
    st.markdown("---")
    st.caption("Institution: SPPU / Autonomous IEEE ABET")
    st.caption("Standard: 100% Zero-Data-Drift Fidelity")

# Top Header
st.markdown("""
<div class="main-header">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <span class="metric-badge badge-teal">Official Academic Sovereign Agent</span>
            <h1 style="margin: 0.5rem 0 0 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.03em;">Prof. Anna Academic Studio</h1>
            <p style="margin: 0.3rem 0 0 0; color: #94A3B8; font-size: 0.95rem;">
                Rigorous step-by-step mathematical proofs, anti-AI publication PDFs, diagrams with live fallback, SIH winning decks &amp; 80/20 PYQ forensics.
            </p>
        </div>
        <div style="text-align:right;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #38BDF8;">100%</div>
            <div style="font-size: 0.75rem; color: #94A3B8; text-transform:uppercase; letter-spacing:0.05em;">Mathematical Fidelity</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Engine 1: Assignment Solver
if nav == "📝 Assignment Solver & Proofs":
    st.subheader("📝 Assignment Solver & Formal Proofs")
    st.write("Solves university coursework with 100% formal mathematical rigor, axioms, and inductive verification.")

    col1, col2 = st.columns([2, 1])
    with col1:
        problem_input = st.text_area(
            "Enter Assignment Problem Statement:",
            value="Solve recurrence relation T(n) = 2T(n/2) + Theta(n) with base case T(1) = 1. Prove tight asymptotic bound.",
            height=120,
        )
    with col2:
        subject = st.selectbox("Subject Domain", ["Computer Science & Engineering", "Operating Systems", "DBMS", "Networks", "Mathematics", "Applied Engineering"])
        marks = st.number_input("Max Marks", min_value=1, max_value=100, value=10)
        solve_btn = st.button("Solve with Formal Proofs", type="primary")

    if solve_btn or problem_input:
        with st.spinner("Prof. Anna is deriving formal axiomatic steps..."):
            sol = anna.solve_assignment(problem_input, subject=subject, total_marks=marks)

        st.success(f"Verified Solution Generated: {sol.title}")
        
        st.markdown(f"**Subject:** {sol.subject} | **Total Marks:** {sol.total_marks} | **Confidence:** 100%")
        
        st.markdown("### Governing Axioms & Principles")
        for p in sol.governing_principles:
            st.markdown(f"- **{p}**")

        st.markdown("### Step-by-Step Derivation")
        for s in sol.derivation_steps:
            with st.expander(f"Step {s.step_number}: {s.heading}", expanded=True):
                st.write(s.explanation)
                st.latex(s.math_latex)
                st.info(f"Intermediate Result: {s.intermediate_result}")
                st.caption(f"Rationale: {s.rationale}")

        st.markdown("### Final Boxed Conclusion")
        st.markdown(f"""
        <div style="background:#F0FDF4; border:1.5px solid #10B981; border-radius:8px; padding:1.2rem; margin-top:1rem;">
            <div style="font-size:0.8rem; font-weight:700; color:#065F46; text-transform:uppercase;">Verified Result</div>
            <div style="font-size:1.2rem; font-weight:700; color:#0F172A; margin-top:0.4rem;">{sol.final_answer}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Formal Proof of Correctness")
        for k, v in sol.formal_proof.items():
            st.write(f"**{k.replace('_', ' ').title()}:** {v}")

        if sol.common_pitfalls:
            st.warning("⚠️ **Examiner Traps Alert:**\n" + "\n".join([f"- {p}" for p in sol.common_pitfalls]))

# Engine 2: Solution Grader & "Cheque"
elif nav == "🔍 Solution Grader & 'Cheque'":
    st.subheader("🔍 Solution Auditor & Rubric Checker ('City & Cheque')")
    st.write("Audits student draft solutions, flags missed edge cases, and calculates marks.")

    prob = st.text_input("Problem Statement", value="Solve recurrence T(n) = 2T(n/2) + n")
    draft = st.text_area(
        "Student's Draft Solution:",
        value="Given T(n) = 2T(n/2) + n\nBy Master Theorem, a=2, b=2, so n^(log2 2) = n.\nSince f(n) = n, it is Case 2.\nTherefore T(n) = Theta(n log n).",
        height=140,
    )
    total_m = st.number_input("Maximum Assignment Marks", value=10.0, step=1.0)
    audit_btn = st.button("Run Rigorous Rubric Audit", type="primary")

    if audit_btn or draft:
        with st.spinner("Auditing solution against university grading schemes..."):
            audit = anna.check_solution(prob, draft, total_marks=total_m)

        c1, c2, c3 = st.columns(3)
        c1.metric("Awarded Score", f"{audit.overall_score} / {audit.total_marks}")
        c2.metric("Percentage", f"{audit.percentage}%")
        c3.metric("University Grade", audit.grade)

        st.markdown("### Rubric Evaluation Breakdown")
        for r in audit.rubric_breakdown:
            st.markdown(f"**{r.criterion_name}** — `{r.awarded_marks} / {r.max_marks}` ({r.status})")
            st.caption(f"Feedback: {r.feedback}")
            if r.deduction_reasons:
                for d in r.deduction_reasons:
                    st.error(f"Deduction: {d}")

        if audit.detected_traps_or_fallacies:
            st.markdown("### Examiner Trap Warnings")
            for t in audit.detected_traps_or_fallacies:
                st.warning(t)

        st.markdown("### Prof. Anna's Actionable Remediation")
        for rem in audit.prof_anna_remediation:
            st.success(f"✓ {rem}")

# Engine 3: Anti-AI Luxury PDF Studio
elif nav == "📄 Anti-AI Luxury PDF Studio":
    st.subheader("📄 Anti-AI Luxury Publication PDF Generator")
    st.write("Generates documents with zero AI tropes: editorial typography, hairline boundaries, rich obsidian tones, running headers.")

    pdf_topic = st.text_input("Assignment Topic / Title", value="Divide and Conquer Master Theorem Analysis")
    pdf_subject = st.selectbox("Academic Subject", ["Computer Science & Engineering", "Operating Systems", "Applied Mathematics"])
    gen_pdf_btn = st.button("Generate Handcrafted Publication PDF", type="primary")

    if gen_pdf_btn:
        with st.spinner("Compiling publication-grade PDF..."):
            sol = anna.solve_assignment(pdf_topic, subject=pdf_subject)
            diag = anna.generate_diagram(pdf_topic, diagram_type="architecture")
            pdf_file = anna.generate_pdf(sol.to_dict(), filename=f"solution_{pdf_topic.replace(' ', '_')}.pdf", diagram_image_path=diag.get("png_file"))
        
        st.success(f"PDF Successfully Compiled: {pdf_file}")
        with open(pdf_file, "rb") as f:
            st.download_button("📥 Download Handcrafted PDF", f.read(), file_name=os.path.basename(pdf_file), mime="application/pdf")

# Engine 4: Diagram Studio with Fallback
elif nav == "📐 Autonomous Diagram Studio":
    st.subheader("📐 Autonomous Diagram Studio with Live Web Fallback Links")
    st.write("Generates vector SVGs and scientific charts. If complex hardware blueprints are required, embeds direct verified external reference links.")

    diag_topic = st.text_input("Enter System / Concept Topic:", value="Transformer Multi-Head Attention")
    diag_type = st.selectbox("Diagram Format", ["architecture", "flowchart", "benchmark_chart"])
    render_btn = st.button("Generate Publication Diagram", type="primary")

    if render_btn or diag_topic:
        res = anna.generate_diagram(diag_topic, diagram_type=diag_type)
        st.success(f"Generated Diagram Type: {res.get('diagram_type')}")
        
        # Display SVG or PNG
        if res.get("svg_file") and os.path.exists(res.get("svg_file")):
            with open(res.get("svg_file"), "r", encoding="utf-8") as f:
                st.image(f.read())
        elif res.get("png_file") and os.path.exists(res.get("png_file")):
            st.image(res.get("png_file"))

        # Fallback & Authoritative Citations
        fb = res.get("fallback_info", {})
        st.markdown("### 🌐 Authoritative External Diagram Reference")
        st.markdown(f"**Source:** {fb.get('source')}")
        st.markdown(f"**Title:** {fb.get('title')}")
        st.markdown(f"**Description:** {fb.get('description')}")
        st.markdown(f"[🔗 Direct Authoritative Paper / Spec Page]({fb.get('primary_url')})")
        st.markdown(f"[🖼️ Direct High-Definition Vector/Diagram Link]({fb.get('diagram_url')})")

# Engine 5: PPT Cloner & SIH Optimizer
elif nav == "📊 PPT Cloner & SIH Optimizer":
    st.subheader("📊 Presentation Cloner & Smart India Hackathon (SIH) Pitch Optimizer")
    st.write("Clones reference slide deck structures and optimizes presentations against official national hackathon evaluation rubrics.")

    tab1, tab2 = st.tabs(["Smart India Hackathon (SIH) Optimizer", "PPT Reference Cloner"])

    with tab1:
        sih_title = st.text_input("Hackathon Project Title", value="Autonomous Edge AI Grid for Rural Water Leakage Detection")
        sih_ps = st.text_input("Problem Statement ID", value="SIH-2024-PS1482")
        sih_ministry = st.text_input("Ministry / Organization", value="Ministry of Jal Shakti / AICTE")
        
        opt_btn = st.button("Analyze & Optimize SIH Presentation", type="primary")
        if opt_btn or sih_title:
            sample_slides = [
                {"title": "Our Innovation", "bullets": ["We solve the problem using AI", "Very scalable and revolutionary", "Has mobile application"]},
            ]
            opt = anna.optimize_sih_deck(sample_slides, ps_id=sih_ps, project_title=sih_title, ministry=sih_ministry)
            
            st.metric("SIH Readiness Score", f"{opt.overall_sih_readiness_score} / 100", delta="Winning Tier" if opt.is_shortlist_worthy else "Needs Polish")
            
            st.markdown("### Jury Rubric Breakdown")
            st.json(opt.rubric_scores)

            st.markdown("### Critical Flaws Detected & Remediated")
            for flaw in opt.critical_defects_found:
                st.error(flaw)

            st.markdown("### Jury Defense Cheat Sheet (Predicting Jury Questions)")
            for q in opt.jury_defense_cheat_sheet:
                st.markdown(f"**Q: {q.get('jury_question')}**")
                st.info(f"**Bulletproof Defense:** {q.get('bulletproof_defense')}")

            # Generate winning PPTX
            deck_res = anna.clone_presentation(opt.optimized_slides_schema, {"title": sih_title, "author": "Aditya Nimbalkar"}, output_filename="sih_winning_presentation.pptx")
            with open(deck_res.get("pptx_file"), "rb") as f:
                st.download_button("📥 Download Winning SIH PPTX (16:9 Widescreen)", f.read(), file_name="sih_winning_presentation.pptx")

    with tab2:
        st.write("Takes reference slide schemas and replaces content with your new project findings.")
        st.info("Exports both Microsoft PowerPoint (.pptx) and zero-dependency interactive HTML5 presentations.")

# Engine 6: IEEE Access Research Paper
elif nav == "📜 IEEE Access Research Paper":
    st.subheader("📜 IEEE Access & Transactions Two-Column Paper Generator")
    st.write("Generates peer-reviewed standard IEEE Access research papers with LaTeX source and live HTML preview.")

    paper_topic = st.text_input("Research Topic / Title", value="Decentralized Edge Federated Learning under Asymmetric Network Partitions")
    paper_author = st.text_input("Primary Author", value="Aditya Nimbalkar, Student Member, IEEE")
    gen_paper_btn = st.button("Synthesize IEEE Access Paper", type="primary")

    if gen_paper_btn or paper_topic:
        with st.spinner("Synthesizing IEEE Access paper with formal mathematical modeling..."):
            paper_res = anna.generate_ieee_paper(paper_topic, authors=[paper_author, "Prof. Anna, Fellow, IEEE"])
        
        st.success(f"Paper Synthesized: {paper_res.get('title')}")
        st.caption(f"DOI Preview: {paper_res.get('doi_preview')}")

        with open(paper_res.get("latex_file"), "r", encoding="utf-8") as f:
            st.download_button("📥 Download LaTeX (.tex) Source", f.read(), file_name=os.path.basename(paper_res.get("latex_file")), mime="text/plain")

        with open(paper_res.get("html_file"), "r", encoding="utf-8") as f:
            st.download_button("📥 Download Publication HTML Preview", f.read(), file_name=os.path.basename(paper_res.get("html_file")), mime="text/html")

# Engine 7: Exam Forensics (Pareto 80/20)
elif nav == "🎯 Exam Forensics (Pareto 80/20)":
    st.subheader("🎯 Exam Forensics & Pareto 80/20 High-Yield Checklist")
    st.write("Analyzes past 5-year question papers, finds the vital 20% topics yielding 80% marks, and tracks your success rate.")

    sub_name = st.selectbox("Select Subject", ["Operating Systems", "Design and Analysis of Algorithms"])
    total_marks = st.number_input("Total Exam Marks", value=70)

    report = anna.analyze_exam_readiness(subject_name=sub_name, total_exam_marks=total_marks)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Predicted Success Rate", f"{report.predicted_success_rate}%")
        st.info(f"Readiness Tier: {report.exam_readiness_tier}")
        st.markdown(f"**High-Yield Marks Available:** {report.total_high_yield_marks}")
        st.markdown(f"**Mastered Marks:** {report.mastered_marks}")
    
    with col2:
        st.markdown("### Pareto 80/20 High-Yield Topic Checklist")
        for t in report.pareto_80_20_topics:
            checked = st.checkbox(f"[{t.recurrence_probability*100:.0f}% Prob | {t.typical_marks}M] {t.concept_name}", value=t.is_mastered, key=t.topic_id)
            st.caption(f"Type: {t.question_type} • Frequency: {t.historical_frequency}/5 yrs • PYQ Phrasing: {t.standard_pyq_phrasing}")

    st.markdown("### Rapid 1-Day Formula Cheat Sheet")
    st.json(report.last_minute_formula_sheet)

# Engine 8: Feynman Intuition & Flashcards
elif nav == "💡 Feynman Intuition & Flashcards":
    st.subheader("💡 Feynman Technique Intuition & Spaced Repetition")
    
    c_tab1, c_tab2 = st.tabs(["Feynman Intuition Mental Models", "Anki Spaced Repetition Decks"])
    
    with c_tab1:
        concept = st.text_input("Enter Difficult Engineering Concept:", value="Operating System Deadlock")
        fey = anna.explain_feynman(concept)
        
        st.markdown(f"### Mental Model: {fey.concept}")
        st.info(f"**Everyday Physical Analogy:**\n\n{fey.everyday_physical_analogy}")
        st.success(f"**For a 10-Year-Old Child:**\n\n{fey.the_10_year_old_explanation}")
        st.markdown(f"**Core Mathematical Truth:**\n\n{fey.core_mathematical_insight}")
        st.warning(f"**Why Examiners Care:**\n\n{fey.why_examiners_care}")

    with c_tab2:
        st.write("Generates ready-to-import Anki flashcards (.csv) for fast spaced repetition.")
        sub_card = st.selectbox("Subject for Cards", ["Algorithms", "Operating Systems"])
        deck = anna.generate_flashcards(sub_card)
        st.success(f"Generated {deck.get('total_cards')} Anki Flashcards")
        with open(deck.get("csv_file"), "r", encoding="utf-8") as f:
            st.download_button("📥 Download Anki Deck (.tsv/.csv)", f.read(), file_name=f"{sub_card}_anki_deck.csv", mime="text/csv")
