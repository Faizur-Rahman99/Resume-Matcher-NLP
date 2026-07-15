# 🤖 AI Resume Matcher

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.49-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Live-success)

An AI-powered Applicant Tracking System (ATS) that automatically parses resumes, extracts candidate information, and ranks applicants against a job description using Natural Language Processing (NLP).

> Designed for recruiters and hiring teams to quickly identify the strongest candidates.
<p align="center">
  <img src="docs/images/home.png" alt="AI Resume Matcher Home" width="100%">
</p>

---
# 🎯 Project Goals

This project was built to demonstrate the design and deployment of a modern AI-powered Applicant Tracking System using Natural Language Processing.

The focus was on creating a production-style application featuring:

- Modular software architecture
- RESTful API design
- Interactive web interface
- Docker-based deployment
- Explainable candidate ranking

---

## 🌐 Live Demo

**Live Demo:** https://resume-matcher-nlp.onrender.com

> **Note**
>
> The live demo uses Rule-Based Matching and TF-IDF Similarity to fit within the memory limits of free cloud hosting.
>
> The full version on the `main` branch additionally includes Semantic Similarity using Sentence Transformers.

---

# ✨ Features

- 📄 Resume Parsing
- 🧠 Job Description Parsing
- 🎯 Automatic Candidate Ranking
- ✅ Skill Matching
- 💼 Experience Matching
- 📊 Overall Match Score
- 📈 Candidate Comparison Dashboard
- 👤 Candidate Information Extraction
- 🎓 Education Extraction
- 📂 Project Extraction
- 💡 Match Explanation
- ⚡ FastAPI REST API
- 🎨 Interactive Streamlit Dashboard
- 🐳 Docker Support

---

# ⭐ Key Highlights

- AI-powered Applicant Tracking System (ATS)
- Supports PDF and DOCX resumes
- Automatic candidate ranking
- Multi-factor NLP matching
- Interactive recruiter dashboard
- REST API built with FastAPI
- Dockerized for easy deployment
- Live cloud deployment on Render

---

# 📸 Screenshots

## Upload Documents

<p align="center">
  <img src="docs/images/upload.png" width="100%">
</p>

---

## Candidate Rankings

<p align="center">
  <img src="docs/images/rankings.png" width="100%">
</p>

---

## Candidate Details

<p align="center">
  <img src="docs/images/candidate-details.png" width="100%">
</p>

---

## Candidate Comparison

<p align="center">
  <img src="docs/images/comparison.png" width="100%">
</p>

---

## Full AI Version

The complete implementation available on the `main` branch includes transformer-based semantic similarity.

<p align="center">
  <img src="docs/images/semantic-version.png" width="100%">
</p>
---

# 🏗️ System Architecture

```mermaid
flowchart TD

    A[💻 Streamlit Frontend]
    B[⚙️ FastAPI Backend]
    C[📄 Resume Parser]
    D[📝 Information Extraction]
    E[🧠 Matching Engine]
    F[🏆 Candidate Ranking]
    G[📊 Dashboard]

    A -->|HTTP API| B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G

    E --> E1[Rule-Based]
    E --> E2[TF-IDF]
    E --> E3["Semantic Similarity (Full Version)"]
```

---

# 🧠 Matching Engine

```mermaid
flowchart LR

    JD[📋 Job Description]
    R[📄 Resume]

    JD --> RB
    R --> RB

    JD --> TF
    R --> TF

    JD --> SM
    R --> SM

    RB[Rule-Based Matching]
    TF[TF-IDF Similarity]
    SM["Semantic Similarity (Full Version)"]

    RB --> SCORE
    TF --> SCORE
    SM --> SCORE

    SCORE[Weighted Overall Score]

    SCORE --> EXP[Explanation Engine]
    EXP --> DASH[Dashboard]
```
> **Note**
>
> The live demo uses **Rule-Based Matching** and **TF-IDF Similarity**.
>
> The complete implementation on the `main` branch additionally includes **Sentence Transformer–based Semantic Similarity**.
---

# ⚙️ Tech Stack

## Programming Language

- Python 3.11

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

## Machine Learning & NLP

- scikit-learn
- TF-IDF Vectorizer
- Sentence Transformers *(Full Version)*
- spaCy
- NLTK

## Document Processing

- PyMuPDF
- pdfplumber
- python-docx

## Data Processing

- NumPy
- Pandas

## Deployment & DevOps

- Docker
- Render

## Development Tools

- Git
- GitHub
- PyCharm

---

# 📊 Matching Algorithm

The overall candidate score is calculated using multiple NLP techniques.

### Rule-Based Matching

Compares:

- Skills
- Experience

### TF-IDF Similarity

Measures textual similarity between:

- Resume
- Job Description

### Semantic Similarity *(Full Version)*

Uses transformer embeddings to understand contextual similarity between resumes and job descriptions.

---

# 📂 Project Structure

```text
Resume-Matcher-NLP
│
├── frontend/
├── src/
│   ├── api/
│   ├── entity/
│   ├── matching/
│   ├── parser/
│   ├── similarity/
│   └── ...
│
├── tests/
├── Dockerfile
├── Dockerfile.render
├── requirements.txt
└── README.md
```

---

# 🛠️ Installation

## Prerequisites

- Python 3.11+
- Git
- Docker *(optional)*

## Clone Repository

```bash
git clone ...
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run frontend/app.py
```

---

# 🚀 Running with Docker

```bash
docker build -t resume-matcher .

docker run -p 8501:8501 resume-matcher
```

---

# 🔌 API Overview

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/match` | Analyze a single resume |
| POST | `/match/batch` | Analyze multiple resumes |
| GET | `/health` | Health check |

---

# 📈 Future Improvements

## AI Enhancements

- LLM-powered resume analysis
- RAG-based candidate search
- Skill ontology matching

## Platform Features

- User authentication
- Recruiter dashboard
- PostgreSQL integration
- Export reports

## Deployment

- AWS deployment
- Azure deployment
- CI/CD pipeline
- Kubernetes support

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- NLP pipelines
- Machine learning similarity algorithms
- REST API development
- Docker containerization
- Cloud deployment
- Modular software architecture
- Interactive data visualization

---

# 📄 License

This project is licensed under the **MIT License**, which allows you to use, modify, and distribute the software with proper attribution.

See the [LICENSE](LICENSE) file for details.

---

# 👨‍💻 Author

## Faizur Rahman

Computer Science & Engineering graduate with a strong interest in **Artificial Intelligence**, **Machine Learning**, and **Software Engineering**.

### Connect with me

- **GitHub:** https://github.com/Faizur-Rahman99
- **LinkedIn:** www.linkedin.com/in/faizur-rahman99

---

## ⭐ Support

If you found this project helpful or interesting, please consider giving it a ⭐ on GitHub.

Your support helps showcase the project and motivates future improvements.

Thank you for visiting!
