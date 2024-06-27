class StringCalculator:
    def add(self, num):
        if num == "":
            return 0
        num = num.replace("\n", ",")
        numbers_liss = num.split(",")
        total = 0
        for number in numbers_liss:
            total+=int(number)
        return total
