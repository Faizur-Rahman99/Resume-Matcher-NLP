from src.components.contact_extractor import ContactExtractor
from src.components.name_extractor import NameExtractor
from src.components.project_extractor import ProjectExtractor
from src.components.education_extractor import EducationExtractor

text = """
John Doe

Software Engineer

Email:
john.doe@example.com

Phone:
+8801712345678

Skills:
Python
SQL
Docker
AWS

Experience:
3 years

Projects:
AI Resume Matcher
Customer Churn Prediction
"""

print("NAME:", NameExtractor().extract(text))
print("EMAIL:", ContactExtractor().extract_email(text))
print("PHONE:", ContactExtractor().extract_phone(text))
print("PROJECTS:", ProjectExtractor().extract(text))
print("EDUCATION:", EducationExtractor().extract(text))