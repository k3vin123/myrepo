class Cal:
    def __init__(self, num):
        self.num = num

    def __add__(self, sec_num):
        self.num = self.num + sec_num

    def __sub__(self, sec_num):
        self.num = self.num - sec_num

    def __divmod__(self, sec_num):
        self.num = self.num / sec_num

    def __mod__(self, sec_num):
        self.num = self.num * sec_num

    def __pow__(self, sec_num):
        self.num = self.num ** sec_num

    def __str__(self):
        return str(self.num)

if __name__ == "__main__":
    a  =10
    a = Cal(a)
    while True:
        operator = input("operator").strip()
        sec_num = int(input("Input second number: \n"))
        a = eval(f"{a}{operator}{sec_num}")
        print(a)