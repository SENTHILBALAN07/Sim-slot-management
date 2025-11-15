from Sim import Sim
class Mobile:
  Slot=None
  Owner="Senthilbalan"
  def __init__(self,name=None,price=None,sname=None,sprice=None):
    self.name=name
    self.price=price
  @classmethod
  def isSimPresent(cls):
    if cls.Slot is None:
      print("sim not Present give details to add" if (cls.Slot is None) else "Present")
      return False
    return True
  @classmethod
  def addSim(cls):
    if  not cls.isSimPresent():
      sname=str(input("Enter sim name..."))
      sprice=str(input("Enter sim Price..."))
      cls.Slot=Sim(sname,sprice)
      print("Sim inserted")
    else:
      print("Sim Already present")
  @classmethod
  def removeSim(cls):
    if cls.isSimPresent():
      cls.Slot=None
      print("Sim removed")
    else:
      print("Sim not present")
  def details(self):
    print("Name: ",self.name)
    print("Price: ",self.price)
    print("Owner: ",Mobile.Owner)
  def sdetails(cls):
    if cls.isSimPresent():
      print("Name: ",Mobile.Slot.sname)
      print("Price: ",Mobile.Slot.sprice)
      print("Owner: ",Sim.owner)
    else:
      print("Sim not present")
  