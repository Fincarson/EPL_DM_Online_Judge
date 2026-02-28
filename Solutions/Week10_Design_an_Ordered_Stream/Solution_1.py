class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.list = [""] * n
        self.cur_index = 0

    def insert(self, idKey: int, value: str):
        self.list[idKey-1] = value
        output = []
        while(self.cur_index < self.n and self.list[self.cur_index] != ""):
            output += [self.list[self.cur_index]]
            self.cur_index += 1
        return output


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))