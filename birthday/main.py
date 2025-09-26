import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2026, 1, 1)

days_away = today - next_birthday

if next_birthday == today:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')