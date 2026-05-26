class Random:
    def __init__(self, seed=228):
        self.seed = seed

    def next(self):
        self.seed = (self.seed * 4242 + 5252) % (2**31)

        return self.seed

    def randint(self, start, end):
        return start + self.next() % (end - start + 1)

    def random(self):
        return self.next() / (2**31)


rng = Random(1337)

print("Для генерации случайного числа введите диапозон: ")
start = int(input("от:"))
end = int(input("до: "))

print(f"Случайное число: {rng.randint(start, end)}")