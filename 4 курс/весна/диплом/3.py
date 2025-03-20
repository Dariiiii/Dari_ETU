import re
from transformers import pipeline

# Загружаем zero-shot классификатор
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_water(text):
    labels = ["вода (размытые формулировки, канцеляризмы)", "четкий и информативный текст"]
    result = classifier(text, candidate_labels=labels)
    return result["labels"][0], result["scores"][0]  # Возвращает самый вероятный класс

# text = """На основании результатов обзора, можно сделать вывод, что существующие решения недостаточно хороши, как могли бы быть."""
# label, confidence = detect_water(text)

# print(f"Классификация: {label}, Уверенность: {confidence:.2f}")

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)  # Разбиваем текст по точкам

text = """На основании результатов обзора, можно сделать вывод, что существующие решения недостаточно хороши. К сожалению, иногда в системе все же случаются разного рода сбои."""
sentences = split_sentences(text)

for sentence in sentences:
    label, confidence = detect_water(sentence)
    print(f"Предложение: {sentence}")
    print(f" -> Классификация: {label} (уверенность {confidence:.2f})\n")
