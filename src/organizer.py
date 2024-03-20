from transformers import pipeline

def organizar_lista(lista, assunto):
    classifier = pipeline("zero-shot-classification")
    result = classifier(assunto, lista)
    return result['labels']
