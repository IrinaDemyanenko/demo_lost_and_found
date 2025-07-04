"""Здесь описана логика поиска потеряной вещи."""
from finditem.models import FoundItem
from finditem.utils.text_processing import normalize_text


def find_similar_items(description, date, station, category):
    """Ищет в БД потерянные вещи.

    Принимает описание, дату, станцию и категорию — и ищет в базе те
    найденные вещи, которые:

    - найдены не раньше указанной даты,
    - находятся на нужной станции и в нужной категории,
    - и по описанию максимально похожи на запрос пользователя.

    Аргументы:
    description — текст, который ввёл пользователь (например, "черный зонт с деревянной ручкой");
    date — дата потери;
    station — объект модели Station (внешний ключ);
    category — объект модели Category.

    Пример:
    search_words = ["черный", "зонт", "ручка"]
    item_words = ["найден", "зонт", "черный", "с", "деревянный", "ручка"]
    Все три слова входят → совпадение
    """
    search_words = normalize_text(description)  # список лемм от пользователя

    candidates = FoundItem.objects.filter(
        found_date__gte=date,
        station=station,
        category=category,
    )

    matched = []  # вещи, которые прошли текстовое сравнение

    for item in candidates:  # перебираем все объекты FoundItem, отобранные по дате, станции и категории
        # для каждой вещи из базы: берём item.description
        # нормализуем его точно так же, как и ввод пользователя

        item_words = normalize_text(item.description)  # список лемм от БД

        # все слова из запроса пользователя должны входить в описание вещи
        # иначе — вещь отбрасывается
        # if all(word in item_words for word in search_words):
        #     matched.append(item)

        # считаем, сколько слов из запроса входит в описание
        common_count = sum(1 for word in search_words if word in item_words)

        # если совпадает не менее 2/3 слов — добавляем
        if common_count / len(search_words) >= 2/3:
            matched.append(item)

    return matched
