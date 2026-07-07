import nltk

RESOURCES = [
    "punkt",
    "punkt_tab",      # Required for NLTK 3.9+
    "stopwords",
    "wordnet",
    "omw-1.4",
]

for resource in RESOURCES:
    print(f"Downloading {resource}...")
    nltk.download(resource)

print("All NLTK resources downloaded successfully.")