class pycharm:
    def excute(self):
        print("running")
        print("exucting")


class MyEditor:
    def excute(self):
        print("running")
        print("exucting")


class Laptop:
    def code(self, ide):
        ide.excute()


ide = MyEditor()
lap = Laptop()
lap.code(ide)
