from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

def save_jd_as_pdf(jd_text: str, folder_path: str) -> str:
    jd_path = Path(folder_path) / "jd.pdf"

    # Create PDF doc
    doc = SimpleDocTemplate(
        str(jd_path),
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    # Optional: make "Job Description" a title
    content = [Paragraph("<b>Job Description</b>", styles["Heading2"]), Spacer(1, 0.2 * inch)]

    # Split JD into paragraphs using double newlines or sections
    paragraphs = jd_text.strip().split("\n\n")

    for para in paragraphs:
        cleaned = para.strip().replace("\n", " ")  # flatten internal lines
        content.append(Paragraph(cleaned, style))
        content.append(Spacer(1, 0.2 * inch))

    doc.build(content)
    return str(jd_path)