class myClass:
  __myprivate=27
  def __privmeth(self):
    print("im inside class myClass")
  def hello(self):
    print("variable value",myClass.__myprivate)
  def show(self):
    self.__privmeth()
foo=myClass()
foo.hello()
foo.show()
