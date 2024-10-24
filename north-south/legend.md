# Задача: Окраска двудольного графа

## Суть

Дан двудольный граф и необходимо покрасить его в два цвета.
По сути это просто делается через поиск в ширину, но это первая задача их серии, дальше будут задачи на раскраску в **n** цветов

## Легенда

В волшебном королевстве Зеландия два соседних королевства: Севера и Юга. Они разделены широкой рекой, но между ними построены мосты, соединяющие города обоих королевств.

Каждый город в королевстве Севера может быть связан только с городом в королевстве Юга, и наоборот. Правители решили, что для улучшения взаимопонимания между королевствами, города должны быть окрашены в два цвета: красный и синий.

Однако они заметили, что два соседних города не должны быть одного цвета, чтобы избежать конфликтов.

Помоги правителю Зеландии раскрасить города Севера и Юга.

## Описание входных данных

Входные данные состоят из:

- Двух чисел **n** и **m**:
  - **n** (1 ≤ n ≤ 1000) — суммарное количество городов в каждом королевстве
- Далее следует **m** строк, каждая из которых содержит два числа:
  - **u** (1 ≤ u ≤ n) — номер города в котором начинается мост
  - **v** (1 ≤ v ≤ n) — номер города в котором мост заканчивается

### Пример входных данных

6 5 \
4 3 \
2 3 \
4 5 \
2 6 \
1 6

## Описание выходных данных

- Выходные данные должны содержать два числа **n** и **m**
  - **n** - кол-во городов, окрашенных в красный
  - **m** - кол-во городов, окрашенных в синий
- Далее должно иди две строки, содержащие **n** и **m** чисел соответственно в порядке возрастания, разделенных пробелами. Числа в первой строке соответствуют номерам городов, окрашенных в красный, числа второй - в синий.

### Пример выходных данных

3 3 \
1 2 4 \
3 5 6

### Пояснение

В данном примере имеется 3 города в Северном королевстве (1, 2, 4) и 3 города в Южном королевстве (3, 5, 6). Мосты соединяют:

- Город 4 с городом 5
- Город 4 с городом 5
- Город 2 с городом 3
- Город 2 с городом 6
- Город 1 с городом 6