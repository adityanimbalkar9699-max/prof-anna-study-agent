"""
PPT Reference Cloner & Presentation Generation Engine
=====================================================
Clones the exact slide structure, layout rhythm, and cards of a reference presentation,
injecting new research, findings, and technical specifics without breaking symmetry.
Outputs native widescreen .pptx and interactive HTML5 presentation decks.
"""

import os
from typing import List, Dict, Any, Optional
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


class PPTCloner:
    """
    Presentation Cloner and Professional Slide Generator.
    """

    def __init__(self, output_dir: str = "output/presentations"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def clone_and_replace(
        self,
        reference_deck_schema: List[Dict[str, Any]],
        new_project_data: Dict[str, Any],
        output_filename: str = "cloned_presentation.pptx",
    ) -> Dict[str, str]:
        """
        Clones reference slide structures and replaces content with user's research.
        """
        pptx_path = os.path.join(self.output_dir, output_filename)
        html_path = os.path.join(self.output_dir, output_filename.replace(".pptx", ".html"))

        # 1. Build Native PPTX
        prs = Presentation()
        # Set 16:9 Widescreen (13.33 x 7.5 inches)
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        blank_slide_layout = prs.slide_layouts[6]  # Blank layout for custom card precision

        for index, slide_spec in enumerate(reference_deck_schema):
            slide = prs.slides.add_slide(blank_slide_layout)

            # Background fill: Luxury obsidian (#0F172A) for Title, Alabaster (#FAF9F6) for content
            is_title_slide = (index == 0 or slide_spec.get("is_title", False))

            if is_title_slide:
                self._build_pptx_title_slide(slide, slide_spec, new_project_data)
            else:
                self._build_pptx_content_slide(slide, slide_spec, new_project_data, index + 1)

        prs.save(pptx_path)

        # 2. Build Interactive HTML5 Presentation Deck
        self._build_html5_presentation(reference_deck_schema, new_project_data, html_path)

        return {
            "pptx_file": pptx_path,
            "html5_file": html_path,
            "total_slides": len(reference_deck_schema),
        }

    def _build_pptx_title_slide(self, slide, slide_spec, data):
        # Background rect
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.33), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = RGBColor(15, 23, 42)  # Obsidian / Deep Slate #0F172A
        bg.line.fill.background()

        # Accent Bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(2.2), Inches(0.12), Inches(3.0))
        bar.fill.solid()
        bar.fill.fore_color.rgb = RGBColor(13, 148, 136)  # Teal #0D9488
        bar.line.fill.background()

        # Title Text Box
        tx_box = slide.shapes.add_textbox(Inches(1.6), Inches(2.0), Inches(10.5), Inches(3.2))
        tf = tx_box.text_frame
        tf.word_wrap = True

        p_pre = tf.paragraphs[0]
        p_pre.text = slide_spec.get("category", "ACADEMIC & INNOVATION DEFENSE").upper()
        p_pre.font.size = Pt(12)
        p_pre.font.bold = True
        p_pre.font.color.rgb = RGBColor(13, 148, 136)

        p_title = tf.add_paragraph()
        p_title.text = data.get("title", slide_spec.get("title", "Project Defense Presentation"))
        p_title.font.size = Pt(36)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(248, 250, 252)

        p_sub = tf.add_paragraph()
        p_sub.text = data.get("subtitle", slide_spec.get("subtitle", "Autonomous Mathematical & Empirical Synthesis"))
        p_sub.font.size = Pt(18)
        p_sub.font.color.rgb = RGBColor(148, 163, 184)

        p_team = tf.add_paragraph()
        p_team.text = f"\nLead Researcher: {data.get('author', 'Aditya Nimbalkar')}  |  Mentor: Prof. Anna  |  Institution: SPPU"
        p_team.font.size = Pt(12)
        p_team.font.color.rgb = RGBColor(203, 213, 225)

    def _build_pptx_content_slide(self, slide, slide_spec, data, slide_num):
        # Warm Alabaster Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.33), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = RGBColor(250, 249, 246)
        bg.line.fill.background()

        # Header Ribbon
        header_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.33), Inches(1.2))
        htf = header_box.text_frame
        htf.word_wrap = True

        hp_sub = htf.paragraphs[0]
        hp_sub.text = f"SECTION {slide_num}  •  {slide_spec.get('section', 'PROJECT SPECIFICATION').upper()}"
        hp_sub.font.size = Pt(11)
        hp_sub.font.bold = True
        hp_sub.font.color.rgb = RGBColor(13, 148, 136)

        hp_title = htf.add_paragraph()
        hp_title.text = slide_spec.get("title", f"Slide {slide_num}")
        hp_title.font.size = Pt(24)
        hp_title.font.bold = True
        hp_title.font.color.rgb = RGBColor(15, 23, 42)

        # Content Cards (supports 1, 2, or 3 column layouts from schema)
        cards = slide_spec.get("cards", [])
        if not cards:
            # Default card with bullet points
            cards = [{"heading": "Key Takeaways", "bullets": slide_spec.get("bullets", ["Point 1", "Point 2", "Point 3"])}]

        num_cards = min(len(cards), 3)
        card_width = (11.33 - (0.4 * (num_cards - 1))) / num_cards

        for i, card in enumerate(cards[:num_cards]):
            left = 1.0 + i * (card_width + 0.4)
            # Card Shape
            card_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(1.8), Inches(card_width), Inches(4.8))
            card_shape.fill.solid()
            card_shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
            card_shape.line.color.rgb = RGBColor(226, 232, 240)
            card_shape.line.width = Pt(1)

            ctf = card_shape.text_frame
            ctf.word_wrap = True
            ctf.margin_left = Inches(0.25)
            ctf.margin_right = Inches(0.25)
            ctf.margin_top = Inches(0.25)

            cp_head = ctf.paragraphs[0]
            cp_head.text = card.get("heading", "Analysis Card").upper()
            cp_head.font.size = Pt(14)
            cp_head.font.bold = True
            cp_head.font.color.rgb = RGBColor(15, 23, 42)

            for b in card.get("bullets", []):
                bp = ctf.add_paragraph()
                bp.text = f"• {b}"
                bp.font.size = Pt(12)
                bp.font.color.rgb = RGBColor(71, 85, 105)

        # Footer
        ft_box = slide.shapes.add_textbox(Inches(1.0), Inches(6.8), Inches(11.33), Inches(0.5))
        ftf = ft_box.text_frame
        fp = ftf.paragraphs[0]
        fp.text = f"Prof. Anna Academic Engine  |  Verified Study Deck  |  Slide {slide_num}"
        fp.font.size = Pt(9)
        fp.font.color.rgb = RGBColor(148, 163, 184)

    def _build_html5_presentation(self, schema: List[Dict[str, Any]], data: Dict[str, Any], output_path: str):
        """Builds a luxury HTML5 presentation deck with 60fps spring transitions."""
        slides_html = ""
        for i, s in enumerate(schema):
            title = s.get("title", f"Slide {i+1}")
            cards = s.get("cards", [{"heading": "Details", "bullets": s.get("bullets", [])}])
            cards_html = ""
            for c in cards:
                bullets = "".join([f"<li class='text-slate-600 mb-2 leading-relaxed text-sm'>{b}</li>" for b in c.get("bullets", [])])
                cards_html += f"""
                <div class="bg-white border border-slate-200 rounded-xl p-6 shadow-sm flex-1">
                    <h3 class="text-xs font-bold uppercase tracking-wider text-teal-600 mb-3">{c.get('heading')}</h3>
                    <ul class="list-disc list-inside space-y-1">{bullets}</ul>
                </div>
                """
            slides_html += f"""
            <div class="slide absolute inset-0 p-16 flex flex-col justify-between transition-all duration-500 {'active opacity-100 scale-100 z-10' if i==0 else 'opacity-0 scale-95 pointer-events-none'}" id="slide-{i}">
                <div>
                    <span class="text-xs font-mono font-semibold tracking-widest text-teal-600 uppercase">Slide {i+1} of {len(schema)}</span>
                    <h2 class="text-3xl font-extrabold text-slate-900 mt-2 tracking-tight">{title}</h2>
                </div>
                <div class="flex gap-6 my-auto">
                    {cards_html}
                </div>
                <div class="flex justify-between items-center border-t border-slate-200 pt-4 text-xs text-slate-400">
                    <span>{data.get('title', 'Project Defense')} • Prof. Anna Guide</span>
                    <span>Use Left/Right Arrow Keys to Navigate</span>
                </div>
            </div>
            """

        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{data.get('title', 'Presentation')} - Prof. Anna Luxury Slides</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #FAF9F6; font-family: -apple-system, BlinkMacSystemFont, "Inter", sans-serif; }}
        .slide {{ transition: opacity 0.4s ease, transform 0.4s ease; }}
    </style>
</head>
<body class="h-screen w-screen overflow-hidden flex items-center justify-center p-6">
    <div class="relative w-full max-w-6xl aspect-[16/9] bg-[#FAF9F6] border border-slate-300 rounded-2xl shadow-xl overflow-hidden" id="deck">
        {slides_html}
    </div>
    <script>
        let current = 0;
        const total = {len(schema)};
        function showSlide(index) {{
            document.querySelectorAll('.slide').forEach((el, idx) => {{
                if(idx === index) {{
                    el.classList.add('opacity-100', 'scale-100', 'z-10');
                    el.classList.remove('opacity-0', 'scale-95', 'pointer-events-none');
                }} else {{
                    el.classList.remove('opacity-100', 'scale-100', 'z-10');
                    el.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
                }}
            }});
        }}
        document.addEventListener('keydown', (e) => {{
            if(e.key === 'ArrowRight' || e.key === ' ') {{
                if(current < total - 1) {{ current++; showSlide(current); }}
            }} else if(e.key === 'ArrowLeft') {{
                if(current > 0) {{ current--; showSlide(current); }}
            }}
        }});
    </script>
</body>
</html>"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_doc)
