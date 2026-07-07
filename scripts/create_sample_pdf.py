from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("tests/data/sample_resume.pdf")

styles = getSampleStyleSheet()

story = [
    Paragraph("John Doe", styles["Normal"]),
    Paragraph("Software Engineer", styles["Normal"]),
    Paragraph("Skills: Python, SQL, Docker, AWS", styles["Normal"]),
    Paragraph("Experience: 5 years", styles["Normal"]),
]

doc.build(story)

print("PDF created successfully.")