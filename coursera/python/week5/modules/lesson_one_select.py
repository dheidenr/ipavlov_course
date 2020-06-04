"""
Есть несколько механизмов опроса файловых дескрипторов у модуля select:
    select.select()
    select.poll()
    select.epoll()
    select.kqueue
Выбираются в зависимости от например операционной системы, Linux -> epoll()

Socket - Создать новый сокет
Bind - Связать сокет с IP адресом и портом
Listen - Объявить о желании принимать соединения
Accept - Принять запрос на установку соединения
Connect - Установить соединение
Send - Отправить данные по сети
Receive - Получить данные из сети
Close - Закрыть соединение
"""

# Неблокирующий ввод/вывод, обучающий пример

import socket
import select

sock = socket.socket()
# Выбираем пустой хост "" чтобы сокет был доступен всем интерфейсам,
# Так же устанавливаем порт, который следует оправшивать
# Или же по простому связываем ip адрес с портом
sock.bind(("", 1001))
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0) # перевод соединения в не блокирующий режим равносильно settimeout(0)
conn2.setblocking(0)

epoll = select.select()
# epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}
