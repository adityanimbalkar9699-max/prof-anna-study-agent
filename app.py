"""
Prof. Anna Universal Academic Sovereign Web Application
=======================================================
Deployable Turnkey Web Application & REST API
Supports 1-click cloud deployment on Render, Railway, Streamlit Cloud,
Hugging Face Spaces, Docker, Google Cloud Run, and Localhost.
"""

import os
import sys
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from anna.core.professor import ProfAnna

# Ensure current directory is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

app = Flask(__name__, template_folder="templates", static_folder="static")
anna = ProfAnna(base_output_dir=os.path.join(PROJECT_ROOT, "anna_output"))


@app.route("/")
def index():
    """Main Web Application Dashboard."""
    return render_template("index.html")


@app.route("/health")
def health():
    """Cloud Healthcheck Probe."""
    return jsonify({
        "status": "healthy",
        "service": "Prof. Anna Academic Sovereign Agent",
        "version": "1.0.0",
        "engines": 10,
        "mode": "all-rounder"
    })


# 1. Omni-Disciplinary Answer Formulator API
@app.route("/api/omni-solve", methods=["POST"])
def api_omni_solve():
    data = request.get_json() or {}
    question = data.get("question", "").strip()
    marks = int(data.get("marks", 8))
    domain = data.get("domain", None)
    if not question:
        return jsonify({"error": "Question statement cannot be empty"}), 400

    ans = anna.solve_omni(question, target_marks=marks, domain_hint=domain)
    return jsonify(ans.to_dict())


# 2. Assignment Solver & Proofs API
@app.route("/api/solve", methods=["POST"])
def api_solve():
    data = request.get_json() or {}
    problem = data.get("problem", "").strip()
    subject = data.get("subject", "Computer Science & Engineering")
    marks = int(data.get("marks", 10))
    if not problem:
        return jsonify({"error": "Problem statement cannot be empty"}), 400

    sol = anna.solve_assignment(problem, subject=subject, total_marks=marks)
    return jsonify(sol.to_dict())


# 3. Solution Auditor & Rubric Checker ("Cheque") API
@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json() or {}
    problem = data.get("problem", "").strip()
    solution = data.get("solution", "").strip()
    marks = float(data.get("marks", 10.0))
    if not problem or not solution:
        return jsonify({"error": "Both problem and student solution are required"}), 400

    audit = anna.check_solution(problem, solution, total_marks=marks)
    return jsonify(audit.to_dict())


# 4. Universal Diagram Studio API
@app.route("/api/diagram", methods=["POST"])
def api_diagram():
    data = request.get_json() or {}
    topic = data.get("topic", "").strip()
    if not topic:
        return jsonify({"error": "Diagram topic is required"}), 400

    diag = anna.render_omni_diagram(topic)
    
    # Read SVG content if available for inline embedding
    svg_content = None
    if diag.get("svg_file") and os.path.exists(diag["svg_file"]):
        with open(diag["svg_file"], "r", encoding="utf-8") as f:
            svg_content = f.read()

    return jsonify({
        "topic": diag["topic"],
        "diagram_type": diag["diagram_type"],
        "svg_content": svg_content,
        "png_available": bool(diag.get("png_file")),
        "fallback_info": diag["fallback_info"]
    })


# 5. Anti-AI PDF Generator API
@app.route("/api/pdf", methods=["POST"])
def api_pdf():
    data = request.get_json() or {}
    topic = data.get("topic", "Academic Report").strip()
    marks = int(data.get("marks", 10))
    subject = data.get("subject", "Engineering Science")

    sol = anna.solve_assignment(topic, subject=subject, total_marks=marks)
    diag = anna.render_omni_diagram(topic)
    pdf_filename = f"report_{topic.lower().replace(' ', '_')[:25]}.pdf"
    
    pdf_path = anna.generate_pdf(
        solution_data=sol.to_dict(),
        filename=pdf_filename,
        diagram_image_path=diag.get("png_file")
    )

    return jsonify({
        "success": True,
        "pdf_filename": os.path.basename(pdf_path),
        "download_url": f"/download/reports/{os.path.basename(pdf_path)}"
    })


# 6. SIH Pitch Deck Optimizer API
@app.route("/api/sih", methods=["POST"])
def api_sih():
    data = request.get_json() or {}
    title = data.get("title", "Autonomous Innovation System").strip()
    ps_id = data.get("ps_id", "SIH-2024-PS1482").strip()
    ministry = data.get("ministry", "Ministry of Electronics & IT").strip()
    draft_slides = data.get("slides", [{"title": "Overview", "bullets": ["AI Solution"]}])

    opt = anna.optimize_sih_deck(draft_slides, ps_id=ps_id, project_title=title, ministry=ministry)
    
    # Generate presentation files
    deck_filename = f"sih_deck_{title.lower().replace(' ', '_')[:20]}.pptx"
    deck_res = anna.clone_presentation(opt.optimized_slides_schema, {"title": title, "author": "Student Innovator"}, output_filename=deck_filename)

    return jsonify({
        "audit": opt.to_dict(),
        "pptx_download_url": f"/download/presentations/{os.path.basename(deck_res['pptx_file'])}",
        "html5_download_url": f"/download/presentations/{os.path.basename(deck_res['html5_file'])}"
    })


# 7. IEEE Access Research Paper API
@app.route("/api/paper", methods=["POST"])
def api_paper():
    data = request.get_json() or {}
    topic = data.get("topic", "Decentralized Edge Intelligence").strip()
    author = data.get("author", "Aditya Nimbalkar, Student Member, IEEE")

    paper_res = anna.generate_ieee_paper(topic, authors=[author, "Prof. Anna, Fellow, IEEE"])
    return jsonify({
        "title": paper_res["title"],
        "doi_preview": paper_res["doi_preview"],
        "latex_download_url": f"/download/papers/{os.path.basename(paper_res['latex_file'])}",
        "html_download_url": f"/download/papers/{os.path.basename(paper_res['html_file'])}"
    })


# 8. Exam Forensics & Pareto 80/20 API
@app.route("/api/exam", methods=["POST"])
def api_exam():
    data = request.get_json() or {}
    subject = data.get("subject", "Operating Systems")
    total_marks = int(data.get("marks", 70))
    mastered = data.get("mastered_ids", None)

    rep = anna.analyze_exam_readiness(subject_name=subject, total_exam_marks=total_marks, mastered_topic_ids=mastered)
    return jsonify(rep.to_dict())


# 9. 60fps Video Script & Storyboard API
@app.route("/api/video-script", methods=["POST"])
def api_video_script():
    data = request.get_json() or {}
    topic = data.get("topic", "Transformer Attention Mechanism").strip()
    domain = data.get("domain", "Deep Learning / AI")
    duration = int(data.get("duration", 3))

    pkg = anna.generate_video_package(topic, domain=domain, total_minutes=duration)
    return jsonify({
        "topic": pkg.topic,
        "estimated_duration": pkg.estimated_duration,
        "scenes": [
            {
                "scene_number": s.scene_number,
                "timestamp": s.timestamp_range,
                "title": s.scene_title,
                "voiceover": s.voiceover_dialogue,
                "visual_direction": s.on_screen_visual_direction,
                "kinetic_cue": s.kinetic_animation_cue,
                "purpose": s.pedagogical_purpose,
            }
            for s in pkg.scenes
        ],
        "script_download_url": f"/download/video_scripts/{os.path.basename(pkg.script_markdown_path)}",
        "deck_download_url": f"/download/video_scripts/{os.path.basename(pkg.interactive_html5_deck_path)}"
    })


# 10. Mnemonic & Spatial Memory Palace API
@app.route("/api/mnemonic", methods=["POST"])
def api_mnemonic():
    data = request.get_json() or {}
    topic = data.get("topic", "12 Schedules of Indian Constitution").strip()
    pkg = anna.construct_memory_palace(topic)
    return jsonify({
        "topic": pkg.topic,
        "acronym": pkg.phonetic_acronym,
        "breakdown": pkg.breakdown,
        "hook": pkg.rhyming_or_story_hook,
        "rooms": [
            {
                "room": r.room_name,
                "anchor": r.physical_anchor,
                "concept": r.concept_to_remember,
                "story": r.vivid_sensory_story,
                "cue": r.exam_cue
            }
            for r in pkg.memory_palace_rooms
        ],
        "examiner_secret": pkg.examiner_recall_secret
    })


# File Download Route
@app.route("/download/<folder>/<filename>")
def download_file(folder, filename):
    folder_path = os.path.join(PROJECT_ROOT, "anna_output", folder)
    if os.path.exists(os.path.join(folder_path, filename)):
        return send_from_directory(folder_path, filename, as_attachment=True)
    return jsonify({"error": f"File {filename} not found"}), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Prof. Anna Academic Sovereign Application starting on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=False)
