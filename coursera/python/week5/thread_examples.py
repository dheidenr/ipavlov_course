from threading import Thread


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print("hello", self.name)


def f(name):
    print("hello", name)


if __name__ == '__main__':
    # th = Thread(target=f, args=("Bob", ))
    th = PrintThread("Mike")
    th.start()
    th.join()