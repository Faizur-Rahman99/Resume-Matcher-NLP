from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("tests/data/sample_resume.pdf")

styles = getSampleStyleSheet()

story = [
    Paragraph("John Doe", styles["Normal"]),
    Paragraph("Software Engineer", styles["Normal"]),
    Paragraph("", styles["Normal"]),

    Paragraph("Email: john.doe@example.com", styles["Normal"]),
    Paragraph("Phone: +8801712345678", styles["Normal"]),
    Paragraph("", styles["Normal"]),

    Paragraph("Skills:", styles["Normal"]),
    Paragraph("Python", styles["Normal"]),
    Paragraph("SQL", styles["Normal"]),
    Paragraph("Docker", styles["Normal"]),
    Paragraph("AWS", styles["Normal"]),
    Paragraph("", styles["Normal"]),

    Paragraph("Experience: 3 years", styles["Normal"]),

    Paragraph("Projects:", styles["Normal"]),
    Paragraph("AI Resume Matcher", styles["Normal"]),
    Paragraph("Customer Churn Prediction", styles["Normal"]),
]

doc.build(story)

print("PDF created successfully.")