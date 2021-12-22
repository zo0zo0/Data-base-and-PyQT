"""
4. Продолжаем работать над проектом «Мессенджер»:
a) Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него. Уместно использовать
модуль subprocess).
b) Реализовать скрипт, запускающий указанное количество клиентских приложений.
"""

from subprocess import call, Popen
import threading


def create_client():
    COMMAND = "python .\message_proj\client.py"
    Popen(COMMAND, shell=False)


def start_clients(qty:int):
    threads = []
    for i in range(qty):
        threads.append( threading.Thread(target=create_client))
        threads[i].start()
    return threads


def start_two_clients():
    start_clients(2)


def start_server():
    COMMAND = "python .\message_proj\server.py"
    call(COMMAND, shell=False)


if __name__ == "__main__":
    threading.Thread(target=start_server).start()
    threading.Thread(target=start_two_clients).start()