# Умова
14.2.2. Реалізуйте симулятор,
що опрацьовує запити на виконання арифметичних операцій. Кожен запит
складається з двох чисел та типу операції, що має над ними виконатися.
Реалізацію симулятора здійсніть з використанням шаблону проектування Ланцюжок
обов’язків.
# Результат
```
DivHandler is queued after AddHandler
MulHandler is queued after DivHandler
SubHandler is queued after MulHandler
AddHandler is handling operation + for 1 and 1
Result: 2
MulHandler is handling operation * for 2 and 2
Result: 4
SubHandler is handling operation - for 10.0 and 20.5
Result: -10.5
DivHandler is handling operation / for 100 and 10
Result: 10.0
MulHandler is handling operation * for 0 and 0
Result: 0
```