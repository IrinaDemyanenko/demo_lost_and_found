"""Инструменты для нормализации текста с использованием Natasha."""
import re
from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    MorphVocab,
    Doc,
)


# инициализируем компоненты Natasha
# Segmenter — разбивает текст на токены
# MorphTagger — определяет часть речи и грамматические признаки
# MorphVocab — нужен для лемматизации
segmenter = Segmenter()
morph_tagger = NewsMorphTagger(NewsEmbedding())
morph_vocab = MorphVocab()


def normalize_text(text: str) -> list:
    """
    Нормализует текст:
    • приводит к нижнему регистру;
    • удаляет все лишние знаки (оставляет только буквы и цифры);
    • разбивает на слова (токены);
    • определяет часть речи;
    • лемматизирует (приводит к начальной форме);
    • оставляет только содержательные слова: существительные, прилагательные, глаголы и т.п.

    Возвращает список лемм.

    Пример:
        normalize_text("Потерял чёрную куртку в поезде!")
        → ['потерять', 'чёрный', 'куртка', 'поезд']
    """

    # в нижний регистр
    text = text.lower()

    # re.sub() заменяет всё, что не входит в набор [а-яa-z0-9 ], на пробел
    # удаляем знаки препинания, лишние символы, латиница — допускается
    text = re.sub(r'[^а-яa-z0-9 ]', ' ', text)

    # создаём объект Doc — Natasha будет с ним работать
    doc = Doc(text)

    # сегментация: делим текст на токены (слова)
    doc.segment(segmenter)

    # морфологическая разметка: определяем часть речи, род, падеж и т.п.
    doc.tag_morph(morph_tagger)

    lemmas = []

    for token in doc.tokens:
        # лемматизация — определяем словарную форму
        token.lemmatize(morph_vocab)

        # Добавляем лемму, если она не пуста и не состоит из одного символа
        if token.lemma and len(token.lemma.strip()) > 1:
            lemmas.append(token.lemma)

    # список лемм — готов к сравнению, фильтрации, поиску по БД
    return lemmas
