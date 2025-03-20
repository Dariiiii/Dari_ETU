from transformers import pipeline

# Загружаем zero-shot классификатор
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_water(text):
    labels = ["вода (размытые формулировки, канцеляризмы)", "четкий и информативный текст"]
    result = classifier(text, candidate_labels=labels)
    return result["labels"][0], result["scores"][0]  # Возвращает самый вероятный класс

text = """На основании результатов обзора, можно сделать вывод, что существующие решения недостаточно хороши, как могли бы быть."""
label, confidence = detect_water(text)

print(f"Классификация: {label}, Уверенность: {confidence:.2f}")
