from multiprocessing import Process


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


def f(name):
    print("hello", name)


if __name__ == '__main__':
    # p = Process(target=f, args=("Bob",))
    p = PrintProcess("Mike")

    p.start()
    p.join()
