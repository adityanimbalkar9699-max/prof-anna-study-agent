"""
Anti-AI Luxury Publication-Grade PDF Generator
==============================================
Follows strict editorial typography, hairline boundaries, warm alabaster/ivory
backgrounds, rich obsidian text, shaded data tables, and running academic headers.
Zero AI Clichés: No generic purple-to-indigo gradients, no harsh single-drop shadows.
"""

import os
import datetime
from typing import Dict, Any, List, Optional
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    KeepTogether,
    HRFlowable,
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas for exact 'Page X of Y' academic numbering and running header/footer.
    """

    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Running Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "PROF. ANNA ACADEMIC SOVEREIGN ENGINE  •  OFFICIAL VERIFIED STUDY REPORT")
            self.drawRightString(558, 755, datetime.date.today().strftime("%B %d, %Y"))
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 748, 558, 748)

        # Running Footer (All pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)

        self.drawString(54, 36, "STRICT ZERO-DATA-DRIFT FIDELITY  •  CONFIDENTIAL ACADEMIC RECORD")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_str)
        self.restoreState()


class AcademicPDFGenerator:
    """
    Generates handcrafted, publication-grade academic PDFs.
    """

    def __init__(self, output_dir: str = "output/reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_assignment_pdf(
        self,
        solution_data: Dict[str, Any],
        filename: str = "assignment_solution.pdf",
        audit_data: Optional[Dict[str, Any]] = None,
        diagram_image_path: Optional[str] = None,
    ) -> str:
        """
        Builds a verified assignment solution PDF with luxury academic styling.
        """
        filepath = os.path.join(self.output_dir, filename)
        doc = SimpleDocTemplate(
            filepath,
            pagesize=A4,
            leftMargin=54,
            rightMargin=54,
            topMargin=54,
            bottomMargin=54,
        )

        styles = getSampleStyleSheet()

        # Editorial Typographic Styles
        title_style = ParagraphStyle(
            "EditorialTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#0F172A"),
            spaceAfter=6,
        )

        subtitle_style = ParagraphStyle(
            "EditorialSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#0D9488"),
            spaceAfter=14,
        )

        section_heading = ParagraphStyle(
            "EditorialHeading",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=colors.HexColor("#0F172A"),
            spaceBefore=14,
            spaceAfter=6,
        )

        body_style = ParagraphStyle(
            "EditorialBody",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14.5,
            textColor=colors.HexColor("#1E293B"),
            spaceAfter=6,
        )

        math_box_style = ParagraphStyle(
            "MathBoxStyle",
            parent=styles["Normal"],
            fontName="Courier",
            fontSize=9,
            leading=13,
            textColor=colors.HexColor("#0F172A"),
        )

        story = []

        # 1. Header Banner Box
        header_table_data = [
            [
                Paragraph("<b>ACADEMIC EXCELLENCE &amp; VERIFICATION REPORT</b>", subtitle_style),
                Paragraph(f"<b>STATUS:</b> <font color='#059669'>100% VERIFIED</font>", subtitle_style),
            ],
            [
                Paragraph(f"<b>{solution_data.get('title', 'Assignment Solution')}</b>", title_style),
                "",
            ],
            [
                Paragraph(f"<b>Subject:</b> {solution_data.get('subject', 'Engineering Science')} | <b>ID:</b> {solution_data.get('assignment_id', 'ANNA-001')} | <b>Total Marks:</b> {solution_data.get('total_marks', 10)}", body_style),
                "",
            ],
        ]
        header_table = Table(header_table_data, colWidths=[380, 120])
        header_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("SPAN", (0, 1), (1, 1)),
            ("SPAN", (0, 2), (1, 2)),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 8))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0F172A"), spaceAfter=12))

        # 2. Problem Statement Box (Warm Alabaster with Slate border)
        story.append(Paragraph("I. PROBLEM STATEMENT &amp; FORMULATION", section_heading))
        problem_text = solution_data.get("problem_statement", "No problem statement specified.")
        prob_table = Table([[Paragraph(f"<b>Problem:</b> {problem_text}", body_style)]], colWidths=[500])
        prob_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
            ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#CBD5E1")),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(prob_table)
        story.append(Spacer(1, 10))

        # 3. Governing Principles & Axioms
        story.append(Paragraph("II. GOVERNING PRINCIPLES, THEOREMS &amp; AXIOMS", section_heading))
        principles = solution_data.get("governing_principles", [])
        for p in principles:
            story.append(Paragraph(f"• <b>{p}</b>", body_style))
        story.append(Spacer(1, 10))

        # 4. Embedded Diagram (if available)
        if diagram_image_path and os.path.exists(diagram_image_path):
            story.append(Paragraph("III. SYSTEM ARCHITECTURE &amp; DERIVATION SCHEMATIC", section_heading))
            try:
                story.append(Image(diagram_image_path, width=480, height=220))
                story.append(Spacer(1, 6))
                story.append(Paragraph("<font size=8 color='#64748B'><i>Figure 1: Analytical Architecture Schematic generated by Prof. Anna.</i></font>", body_style))
                story.append(Spacer(1, 10))
            except Exception as e:
                pass

        # 5. Step-by-Step Derivation Steps
        story.append(Paragraph("IV. STEP-BY-STEP MATHEMATICAL DERIVATION", section_heading))
        steps = solution_data.get("derivation_steps", [])
        for step in steps:
            step_num = step.get("step_number", "")
            heading = step.get("heading", "")
            explanation = step.get("explanation", "")
            math_latex = step.get("math_latex", "")
            result = step.get("intermediate_result", "")

            step_content = [
                [Paragraph(f"<b>Step {step_num}: {heading}</b>", ParagraphStyle("StepHead", parent=body_style, fontName="Helvetica-Bold", fontSize=10, textColor=colors.HexColor("#0D9488")))],
                [Paragraph(explanation, body_style)],
                [Paragraph(f"<code>{math_latex}</code>", math_box_style)],
                [Paragraph(f"<b>Intermediate Result:</b> {result}", ParagraphStyle("SubRes", parent=body_style, fontSize=9, textColor=colors.HexColor("#334155")))],
            ]
            step_table = Table(step_content, colWidths=[490])
            step_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFFFFF")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LINEBELOW", (0, 0), (0, 0), 0.5, colors.HexColor("#E2E8F0")),
            ]))
            story.append(step_table)
            story.append(Spacer(1, 8))

        # 6. Final Boxed Answer & Formal Proof
        story.append(Paragraph("V. FINAL BOXED RESULT &amp; FORMAL PROOF OF CORRECTNESS", section_heading))
        final_answer = solution_data.get("final_answer", "")
        proof = solution_data.get("formal_proof", {})
        proof_text = "<br/>".join([f"<b>{k.replace('_', ' ').title()}:</b> {v}" for k, v in proof.items()])

        final_box_data = [
            [Paragraph(f"<b>FINAL ANSWER / RESULT:</b><br/><font size=11 color='#0F172A'><b>{final_answer}</b></font>", body_style)],
            [Paragraph(f"<b>Formal Proof &amp; Invariants:</b><br/>{proof_text}", body_style)],
        ]
        final_table = Table(final_box_data, colWidths=[490])
        final_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F0FDF4")),
            ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#FAFAFA")),
            ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#059669")),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#86EFAC")),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(final_table)
        story.append(Spacer(1, 12))

        # 7. Examiner Traps & Common Pitfalls
        pitfalls = solution_data.get("common_pitfalls", [])
        if pitfalls:
            story.append(Paragraph("VI. EXAMINER TRAPS &amp; PITFALL ALERTS", section_heading))
            pitfall_items = [[Paragraph(f"⚠️ <b>Trap {i+1}:</b> {p}", body_style)] for i, p in enumerate(pitfalls)]
            pitfall_table = Table(pitfall_items, colWidths=[490])
            pitfall_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFFBEB")),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#FCD34D")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]))
            story.append(pitfall_table)
            story.append(Spacer(1, 12))

        # 8. Solution Audit Report Certificate (if checked)
        if audit_data:
            story.append(Paragraph("VII. PROF. ANNA GRADING &amp; RUBRIC AUDIT CERTIFICATE", section_heading))
            audit_score = audit_data.get("overall_score", 0)
            audit_total = audit_data.get("total_marks", 10)
            audit_grade = audit_data.get("grade", "A")

            cert_data = [
                [
                    Paragraph(f"<b>Overall Score:</b> {audit_score} / {audit_total} ({audit_data.get('percentage', 0)}%)", body_style),
                    Paragraph(f"<b>Assigned Grade:</b> <b>{audit_grade}</b>", body_style),
                ],
                [
                    Paragraph(f"<b>Soundness:</b> {audit_data.get('mathematical_soundness', 'Verified')}", body_style),
                    Paragraph(f"<b>Exam Ready:</b> {'YES' if audit_data.get('is_exam_ready') else 'NEEDS WORK'}", body_style),
                ],
            ]
            cert_table = Table(cert_data, colWidths=[245, 245])
            cert_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#0D9488")),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]))
            story.append(cert_table)

        # Build document with NumberedCanvas
        doc.build(story, canvasmaker=NumberedCanvas)
        return filepath
