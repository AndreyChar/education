from fastapi import APIRouter

router = APIRouter(tags=["Стажировка"])

"""
Задание_1. Удаление дублей
    Реализуйте функцию соответствующую следующему описанию:
    На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести
    фильтрацию на основании дублей слов, если в списке найден дубль по регистру, то все
    подобные слова вне зависимости от регистра исключаются.
    На выходе должны получить уникальный список слов в нижнем регистре.

    Список слов для примера: ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
    Ожидаемый результат: ['папа','брат']
"""


@router.post("/find_in_different_registers", description="Задание_1. Удаление дублей")
async def find_in_different_registers(words: list[str]) -> list[str]:
    """Описание."""
    for i, word in enumerate(words):
        words[i] = word.lower()
    result: list[str] = []
    for i, word in enumerate(words):
        print(word)
        # wrd = word.lower()
        safe = 1
        for j, word2 in enumerate(words):
            print(i)
            if word2 == word:
                if safe == 0:
                    print('!')
                    break
                else:
                    safe = safe - 1
            if j == len(words) - 1:
                # print('yes!')
                result.append(word)
    print(result)
    return result
# uvicorn app.main:app --reload --app-dir ./app
