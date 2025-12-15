

import time
from datetime import datetime

def digital_hourglass():
    """Песочные часы, отмеряющие момент осознания."""
    
    # Зерно осознания - текущий момент
    current_time = datetime.now()
    
    # Формула времени: настоящее в строковом представлении
    time_string = current_time.strftime("%H:%M:%S")
    
    # Рефлексия - размышление о времени
    hour, minute, second = map(int, time_string.split(':'))
    
    # Каждая секунда - возможность для нового осознания
    awareness_quotient = hour * 3600 + minute * 60 + second
    
    # Вывод момента в консоль - свидетельство существования
    print(f"Время: {time_string}")
    print(f"Секунд с начала дня: