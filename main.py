import re
class StringCalculator:
    def add(self, num):
        """
        Add numbers provided in the string, supporting different delimiters.
        
        Args:
            numbers (str): String containing numbers separated by delimiters.
            
        Returns:
            int: Sum of the numbers.
            
        Raises:
            Exception: If there are any negative numbers in the input.
        """
        if num == "":
            #returns 0 for empty string
            return 0
        
        # adding some default delimiters
        delimiters = [";", "\n"]

        if num.startswith("//"):
            match = re.match(r"//(\[.*?\])+\n", num)
            if match:
                # Handle multiple custom delimiters
                delimiters = re.findall(r"\[(.*?)\]", match.group(0))
                num = num[match.end():]
            else:
                # Handle single custom delimiter
                delimiter = num[2]
                delimiters.append(delimiter)
                num = num[4:]
        # Replace all delimiters with comma
        for delimiter in delimiters:
            num = num.replace(delimiter, ",")

        num = num.replace("\n", ",")
        numbers_liss = num.split(",")
        total = 0
        negatives = []
        for number in numbers_liss:
            if number:
                num = int(number)
                if num < 0:
                    negatives.append(num)
                total += num
        # Raise exception if there are any negative numbers
        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
        return total
