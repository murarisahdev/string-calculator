class StringCalculator:
    def add(self, num):
        if num == "":
            return 0
        numbers_liss = num.split(",")
        if len(numbers_liss) == 1:
            return int(numbers_liss[0])
        return int(numbers_liss[0]) + int(numbers_liss[1])
