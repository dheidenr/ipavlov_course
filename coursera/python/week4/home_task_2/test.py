from coursera.python.week4.home_task_2.solution import Value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


bobs_account = Account(0.1)
bobs_account.amount = 100
print(bobs_account.amount)
# with open('log.txt', 'r') as f:
#     print(f.read())
