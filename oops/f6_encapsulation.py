
class Animals:
    __emid = 10

    def getemid(self, eid):
        self.__emid == eid

    def disemid(self):
        print(self.__emid)


obj = Animals()
obj.getemid(20)
obj.disemid()
# print(obj.__a)
