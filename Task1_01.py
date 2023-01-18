class Calculator:

    def __init__(self, actions = []):
        self.actions = actions


    def add(self, add1, add2):
        # self.add1 = add1
        # self.add2 = add2
        result = add1 + add2
        self.actions.append(f"added {add1} to {add2} got {result}")
        return result

    def multiply(self, num1, num2):
        # self.num1 = num1
        # self.num2 = num2
        result = num1 * num2
        self.actions.append(f"multiplied {num1} with {num2} got {result}")
        return result

    def print_operations(self):
        print(self.actions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Calculator().add(4, 5)
    Calculator().add(4, 9)
    Calculator().add(9, 13)
    Calculator().multiply(5, 7)
    Calculator().multiply(9, 15)
    Calculator().multiply(510, 5245)
    Calculator().print_operations()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
