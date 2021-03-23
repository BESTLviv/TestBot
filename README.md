# TestBot
Test task for besties to attend the bot development

- Створити бота через BotFather. Скопіювати API токен новоствореного бота у код
- При запуску команди /start - бот відправляє наступне повідомлення: “Привіт {username}! Це повідомлення було відправлено о {time}” 
  - username - це твій нік в телеграмі який виглядає так - @dora
  - time та username потрібно взяти з об’єкта message, який повертаєтся при надсиланні повідомлення. Про це можна почитати тут або просто вивести message через print() і побачити як він побудований.
- При надсиланні фотографії - бот надсилає photo_id.
  Наприклад photo_id можна получити так message.json['photo'][0]['file_id']
- При надсиланні слова “Фото” - бот надсилає останню фотографію яку ви кинули (через photo_id). Якщо ж її немає тоді надіслати повідомлення про її відсутність.
- *Після запуску команди /start - бот прикріпляє до повідомлення кнопку (InlineButton), після натиску на яку бот надішле callback стрічку цієї кнопки.
- *Після запуску команди /location - бот показує дві прості кнопки (KeyboardButton) 
  - Кнопка яка запрошує локацію користувача
  - Кнопка яка запрошує контакт користувача
