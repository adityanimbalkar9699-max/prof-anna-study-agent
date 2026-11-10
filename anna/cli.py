"""
Prof. Anna CLI - Academic Sovereign Command Line Interface
==========================================================
Usage:
  python -m anna.cli solve "problem statement"
  python -m anna.cli check --problem "..." --solution "..."
  python -m anna.cli pdf --topic "..."
  python -m anna.cli diagram --topic "..."
  python -m anna.cli ppt --title "..."
  python -m anna.cli sih --title "..." --ps "SIH-1234"
  python -m anna.cli paper --topic "..."
  python -m anna.cli exam --subject "..."
  python -m anna.cli feynman --concept "..."
  python -m anna.cli flashcards --subject "..."
  python -m anna.cli web
"""

import sys
import json
import click
import subprocess
from anna.core.professor import ProfAnna


@click.group()
def cli():
    """Prof. Anna - Academic Sovereign Agent & Pedagogical Guide."""
    pass


@cli.command()
@click.argument("problem")
@click.option("--subject", default="Computer Science & Engineering", help="Course subject")
@click.option("--marks", default=10, type=int, help="Total marks")
def solve(problem, subject, marks):
    """Solve an assignment problem with 100% formal mathematical proof."""
    anna = ProfAnna()
    click.secho("\n🎓 Prof. Anna: Formulating Rigorous Mathematical Solution...", fg="cyan", bold=True)
    sol = anna.solve_assignment(problem, subject=subject, total_marks=marks)
    
    click.secho(f"\n[ASSIGNMENT ID]: {sol.assignment_id} | {sol.title}", fg="green", bold=True)
    click.echo(f"Subject: {sol.subject} | Marks: {sol.total_marks}")
    click.secho("\n--- Step-by-Step Derivation ---", fg="yellow")
    for s in sol.derivation_steps:
        click.secho(f"Step {s.step_number}: {s.heading}", bold=True)
        click.echo(f"  Explanation: {s.explanation}")
        click.echo(f"  KaTeX Math:  {s.math_latex}")
        click.echo(f"  Result:      {s.intermediate_result}\n")
    
    click.secho(f"FINAL ANSWER: {sol.final_answer}", fg="green", bold=True)
    click.secho(f"FORMAL PROOF: {sol.formal_proof.get('method', 'Axiomatic Induction')}", fg="cyan")


@cli.command()
@click.option("--problem", required=True, help="Original problem statement")
@click.option("--solution", required=True, help="Student's drafted answer to check")
@click.option("--marks", default=10.0, type=float, help="Maximum marks")
def check(problem, solution, marks):
    """Audit and grade student work against university rubrics ('City & Cheque')."""
    anna = ProfAnna()
    click.secho("\n🔍 Prof. Anna: Conducting Academic Rubric & Proof Audit...", fg="cyan", bold=True)
    audit = anna.check_solution(problem, solution, total_marks=marks)
    
    click.secho(f"\n[AUDIT CERTIFICATE]: {audit.submission_id}", fg="green", bold=True)
    click.secho(f"Overall Score: {audit.overall_score} / {audit.total_marks} ({audit.percentage}%) - Grade: {audit.grade}", bold=True)
    click.echo(f"Soundness: {audit.mathematical_soundness}")
    click.echo(f"Exam Ready: {'YES' if audit.is_exam_ready else 'NEEDS REMEDIATION'}")
    
    click.secho("\nRubric Breakdown:", fg="yellow")
    for r in audit.rubric_breakdown:
        click.echo(f"• {r.criterion_name}: {r.awarded_marks}/{r.max_marks} [{r.status}] - {r.feedback}")
    
    if audit.detected_traps_or_fallacies:
        click.secho("\n⚠️ Examiner Traps Detected:", fg="red")
        for t in audit.detected_traps_or_fallacies:
            click.echo(f"  - {t}")


@cli.command()
@click.option("--topic", required=True, help="Topic for assignment report")
@click.option("--marks", default=10, type=int, help="Total marks")
def pdf(topic, marks):
    """Generate an Anti-AI publication-grade PDF report."""
    anna = ProfAnna()
    click.secho("\n📄 Prof. Anna: Generating Luxury Publication-Grade PDF...", fg="cyan", bold=True)
    sol = anna.solve_assignment(topic, total_marks=marks)
    diag = anna.generate_diagram(topic, diagram_type="architecture", filename_prefix="pdf_diagram")
    pdf_path = anna.generate_pdf(sol.to_dict(), filename=f"solution_{topic.replace(' ', '_')}.pdf", diagram_image_path=diag.get("png_file"))
    click.secho(f"✅ Luxury PDF Generated: {pdf_path}", fg="green", bold=True)


@cli.command()
@click.option("--topic", required=True, help="Diagram concept / architecture")
@click.option("--type", "diag_type", default="architecture", help="architecture | flowchart | benchmark_chart")
def diagram(topic, diag_type):
    """Generate publication vector diagram with authoritative web fallback links."""
    anna = ProfAnna()
    click.secho("\n📐 Prof. Anna: Rendering Vector Architectural Diagram...", fg="cyan", bold=True)
    res = anna.generate_diagram(topic, diagram_type=diag_type, filename_prefix="cli_diagram")
    click.secho(f"✅ Generated: {res.get('svg_file') or res.get('png_file')}", fg="green")
    fb = res.get("fallback_info", {})
    click.secho(f"🌐 Authoritative Fallback Source: {fb.get('title')}", fg="yellow")
    click.echo(f"  Primary Reference: {fb.get('primary_url')}")
    click.echo(f"  Direct High-Res Diagram: {fb.get('diagram_url')}")


@cli.command()
@click.option("--title", default="Autonomous Multi-Agent AI Grid", help="Project Title")
def ppt(title):
    """Clone presentation structure and generate widescreen PPTX & HTML5 slides."""
    anna = ProfAnna()
    click.secho("\n📊 Prof. Anna: Cloning Presentation Structure & Generating PPTX...", fg="cyan", bold=True)
    schema = [
        {"is_title": True, "category": "ACADEMIC DEFENSE", "title": title, "subtitle": "System Architecture"},
        {"is_title": False, "section": "PROBLEM", "title": "Problem Statement", "cards": [{"heading": "Pain Point", "bullets": ["High latency", "Single point of failure"]}]},
        {"is_title": False, "section": "SOLUTION", "title": "Proposed Solution", "cards": [{"heading": "Architecture", "bullets": ["Decentralized edge mesh", "Sub-linear O(log n)"]}]},
    ]
    res = anna.clone_presentation(schema, {"title": title, "author": "Aditya Nimbalkar"})
    click.secho(f"✅ Widescreen PPTX: {res.get('pptx_file')}", fg="green", bold=True)
    click.secho(f"✅ Interactive HTML5 Deck: {res.get('html5_file')}", fg="green")


@cli.command()
@click.option("--title", required=True, help="Hackathon Project Title")
@click.option("--ps", default="SIH-2024-PS1482", help="Problem Statement ID")
@click.option("--ministry", default="Ministry of Electronics and Information Technology", help="Ministry")
def sih(title, ps, ministry):
    """Analyze and optimize Smart India Hackathon (SIH) presentation pitch deck."""
    anna = ProfAnna()
    click.secho("\n🏆 Prof. Anna: Optimizing Pitch Deck for Smart India Hackathon (SIH)...", fg="cyan", bold=True)
    sample_slides = [
        {"title": "Our Project", "bullets": ["We solve the problem using AI", "It is very good and disruptive", "We have a website"]},
    ]
    opt = anna.optimize_sih_deck(sample_slides, ps_id=ps, project_title=title, ministry=ministry)
    click.secho(f"SIH Readiness Score: {opt.overall_sih_readiness_score}/100", fg="yellow", bold=True)
    click.secho(f"Shortlist Worthy: {'YES' if opt.is_shortlist_worthy else 'NO'}", fg="green" if opt.is_shortlist_worthy else "red")
    click.secho("\nSynthesized Winning 7-Slide Schema Generated!", fg="cyan")
    
    # Save optimized PPTX directly
    res = anna.clone_presentation(opt.optimized_slides_schema, {"title": title, "author": "Aditya Nimbalkar"}, output_filename="sih_winning_deck.pptx")
    click.secho(f"✅ Saved Winning SIH PPTX: {res.get('pptx_file')}", fg="green", bold=True)


@cli.command()
@click.option("--topic", required=True, help="Research domain / topic")
def paper(topic):
    """Synthesize IEEE Access two-column compliant research paper."""
    anna = ProfAnna()
    click.secho(f"\n📝 Prof. Anna: Synthesizing IEEE Access Paper for '{topic}'...", fg="cyan", bold=True)
    res = anna.generate_ieee_paper(topic)
    click.secho(f"✅ LaTeX File: {res.get('latex_file')}", fg="green", bold=True)
    click.secho(f"✅ Publication HTML Preview: {res.get('html_file')}", fg="green")


@cli.command()
@click.option("--subject", default="Operating Systems", help="Subject Name")
def exam(subject):
    """Run Pareto 80/20 PYQ forensics and generate exam readiness checklist."""
    anna = ProfAnna()
    click.secho(f"\n🎯 Prof. Anna: Mining Pareto 80/20 High-Yield PYQs for {subject}...", fg="cyan", bold=True)
    rep = anna.analyze_exam_readiness(subject_name=subject)
    click.secho(f"Predicted Success Rate: {rep.predicted_success_rate}% - Tier: {rep.exam_readiness_tier}", fg="yellow", bold=True)
    click.secho("\nHigh-Yield Topics (80% Marks):", fg="cyan")
    for t in rep.pareto_80_20_topics:
        click.echo(f"• [{t.recurrence_probability * 100:.0f}% Prob] {t.concept_name} ({t.typical_marks} marks) - {t.question_type}")


@cli.command()
@click.argument("concept")
def feynman(concept):
    """Explain complex concepts with Feynman physical mental models."""
    anna = ProfAnna()
    click.secho(f"\n💡 Prof. Anna: Unpacking Feynman Mental Model for '{concept}'...", fg="cyan", bold=True)
    fey = anna.explain_feynman(concept)
    click.secho(f"Concept: {fey.concept}", fg="green", bold=True)
    click.secho(f"\nEveryday Physical Analogy:\n{fey.everyday_physical_analogy}", fg="yellow")
    click.secho(f"\nFor a 10-Year-Old:\n{fey.the_10_year_old_explanation}", fg="cyan")
    click.secho(f"\nMathematical Insight:\n{fey.core_mathematical_insight}", fg="white")


@cli.command()
@click.option("--subject", default="DAA", help="Subject")
def flashcards(subject):
    """Generate Anki-compatible spaced repetition CSV flashcards."""
    anna = ProfAnna()
    click.secho(f"\n🗂️ Prof. Anna: Synthesizing Spaced Repetition Anki Deck for {subject}...", fg="cyan", bold=True)
    res = anna.generate_flashcards(subject)
    click.secho(f"✅ Created {res.get('total_cards')} cards at: {res.get('csv_file')}", fg="green", bold=True)


@cli.command()
def web():
    """Launch the interactive Prof. Anna Web Dashboard."""
    click.secho("\n🚀 Launching Prof. Anna Interactive Web Studio...", fg="cyan", bold=True)
    app_path = os.path.join(os.path.dirname(__file__), "web", "app.py")
    subprocess.run(["streamlit", "run", app_path])


if __name__ == "__main__":
    cli()
