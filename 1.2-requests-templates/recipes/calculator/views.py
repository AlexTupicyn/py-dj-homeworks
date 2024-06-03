from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_page(request):
    return HttpResponse('Вас приветствует наша книга рецептов: omlet, pasta, buter.')


def get_ingredients(request, dishes):
    servings = int(request.GET.get("servings", 1))
    recipe = DATA.get(dishes)
    if recipe:
        context = {
            'recipe': {key: round(value * servings, 2) for key, value in recipe.items()},
            'name_recipe': dishes,
            'porc_recipe': servings
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Такого рецепта к сожалению нет :(')
