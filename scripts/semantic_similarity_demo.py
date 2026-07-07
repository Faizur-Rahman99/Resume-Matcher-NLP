from src.ml.semantic_similarity import SemanticSimilarity

similarity = SemanticSimilarity()

score = similarity.calculate(
    "Python Machine Learning TensorFlow",
    "Python Deep Learning PyTorch"
)

print(score)