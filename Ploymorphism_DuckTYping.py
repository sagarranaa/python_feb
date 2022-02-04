class Pycharm:

    def execute(self): #Duck Method
        print("Compling time")
        print("Runtime")
class Myeditor: #we are changing the editor but it doesn't effect anything ,when you have execute method in it

    def execute(self):
        print("spelling check")
        print("Convention Check")
        print("Compling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()
# ide=Pycharm()
ide=Myeditor()
lap=laptop()
lap.code(ide)
