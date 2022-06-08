# Умова
5.2.1 Розглянемо діаграму класів,
що наведена на рисунку 5.2.1 (див. методичку), яка описує структуру напоїв,
що виготовляються у деякій невеликій кав’ярні. Вихідний код на мові програмування Java наведено за
посиланням

https://github.com/krenevych/patterns/tree/main/Java/labs/lab5/task_3_1.
Проведіть рефакторинг класів, цього проекту з застосуванням

шаблону проектування Міст. По тому, додайте відповідні класи для можливості готування
напоїв для вживання їх як в
ресторані, так і «на винос».
# Резульат
```
Prepearing coffee.
Making your bevrage darker.
Adding 1 hot water.
This bevrage will be served indoors.
Cost of beverage: 13
Drinking black coffee with 0 sugar indoors.

Prepearing coffee.
Adding 0.5 milk.
Adding 1 hot water.
Adding 2 pieces of sugar.
This bevrage will be served indoors.
Cost of beverage: 11.5
Drinking milk coffee with 2 sugar indoors.

Prepearing a tee.
Making your bevrage darker.
Adding 2 hot water.
This bevrage will be served outdoors.
Cost of beverage: 10
Drinking black tee with 0 sugar outdoors.

Prepearing a tee.
Adding 0.5 milk.
Adding 2 hot water.
Adding 2 pieces of sugar.
This bevrage will be served indoors.
Cost of beverage: 8.5
Drinking milk tee with 2 sugar indoors.

Prepearing cacao.
Making your bevrage darker.
Adding 1 hot water.
This bevrage will be served outdoors.
Cost of beverage: 18
Drinking black chocolate with 0 sugar outdoors.

Prepearing cacao.
Adding 1 milk.
Adding 2 hot water.
Adding 2 pieces of sugar.
This bevrage will be served indoors.
Cost of beverage: 18
Drinking milk chocolate with 2 sugar indoors.
```

