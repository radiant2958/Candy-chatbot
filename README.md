#Игра "Конфеты" с ботом

Это игра, написанная на Python с использованием библиотеки aiogram.

Как это работает
При запуске программы создается экземпляр бота с использованием токена. Затем создается диспетчер, который связывает обработчики команд с функциями-обработчиками. Далее, бот начинает работу в режиме polling, ожидая входящие сообщения.

Когда пользователь отправляет команду /start, бот предлагает пользователю сыграть в игру "Конфеты". В игре пользователь должен ввести общие количество конфет на столе. Далее по очереди пользователь с ботом забирает со стола от 1 до 28 конфет за раз. Выигрывает тот, кто заберет последнюю конфету со стола.


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#"Candies" game with a bot
This is a game written in Python using the aiogram library.

How it works
When the program is launched, an instance of the bot is created using a token. Then a dispatcher is created that links command handlers to processing functions. Then the bot starts working in polling mode, waiting for incoming messages.

When the user sends the /start command, the bot suggests the user play the "Candies" game. In the game, the user must enter the total number of candies on the table. Then, one by one, the user and the bot take from 1 to 28 candies from the table at a time. The winner is the one who takes the last candy from the table.
