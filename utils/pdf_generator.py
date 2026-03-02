from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
import re

def clean_resume_text(text):
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"^Here.*?resume.*?\n", "", text, flags=re.IGNORECASE)
    lines = text.split("\n")

    cleaned_lines = []
    name_found = False

    for line in lines:
        if not name_found:
            if re.match(r"^[A-Za-z\s]+$", line.strip()):
                name_found = True
                cleaned_lines.append(line.strip())
        else:
            cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)
    stop_pattern = r"CERTIFICATIONS[\s\S]*?(?:Completed:.*?\n)"
    match = re.search(stop_pattern, text, flags=re.IGNORECASE)

    if match:
        text = text[:match.end()]

    return text.strip()

def generate_resume_pdf(resume_text, file_path="optimized_resume.pdf"):

    resume_text = clean_resume_text(resume_text)

    doc = SimpleDocTemplate(
        file_path,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontSize=18,
        spaceAfter=12,
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.black,
    )

    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=4
    )

    elements = []
    lines = resume_text.split("\n")

    is_first_line = True

    for line in lines:
        line = line.strip()

        if not line:
            elements.append(Spacer(1, 0.15 * inch))
            continue

        # First line → Name
        if is_first_line:
            elements.append(Paragraph(line, name_style))
            elements.append(Spacer(1, 0.2 * inch))
            is_first_line = False
            continue

        if line.upper() in [
            "PROFILE SUMMARY", "SUMMARY",
            "EDUCATION",
            "EXPERIENCE",
            "PERSONAL PROJECTS", "PROJECTS",
            "TECHNICAL SKILLS",
            "SOFT SKILLS",
            "CERTIFICATIONS"
        ]:
            elements.append(Spacer(1, 0.25 * inch))
            elements.append(Paragraph(line.upper(), header_style))
            elements.append(Spacer(1, 0.1 * inch))
            continue

        if line.startswith("-") or line.startswith("*"):
            bullet_text = line[1:].strip()
            bullet = ListFlowable(
                [ListItem(Paragraph(bullet_text, normal_style))],
                bulletType='bullet'
            )
            elements.append(bullet)
        else:
            elements.append(Paragraph(line, normal_style))

    doc.build(elements)

    return file_path