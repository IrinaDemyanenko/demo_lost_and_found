"""Views для вэб-сервиса поиска потерянных вещей."""
from django.shortcuts import render
from finditem.forms import FoundItemForm
from finditem.services.item_search import find_similar_items


def find_item_view(request):
    """Обрабатывает GET-запрос (когда пользователь зашёл на страницу)
    и POST-запрос (когда он отправил форму).
    """
    results = None  # подходящие найденные вещи
    query = None  # то, что ввёл пользователь (чтобы отобразить обратно в шаблоне)

    if request.method == 'POST':
        form = FoundItemForm(request.POST)  # request.POST — это словарь со всеми введёнными данными
        if form.is_valid():
            # После успешной валидации Django возвращает очищенные данные в виде словаря
            cleaned = form.cleaned_data
            description = cleaned['description']
            date = cleaned['found_date']
            station = cleaned['station']
            category = cleaned['category']

            query = cleaned  # Сохраняем данные формы — чтобы потом в шаблоне отобразить «ваш запрос: …»
            results = find_similar_items(description, date, station, category)

    # Если пользователь только открыл страницу, а не отправил форму (GET-запрос)
    # мы создаём пустую форму, чтобы отрисовать её на странице
    else:
        form = FoundItemForm()

    context = {
        'form': form,
        'results': results,
        'query': query,
    }

    return render(request, 'finditem/found_item_form.html', context)
