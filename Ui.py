from Mobile import Mobile
import time
class Ui:
  flag=True
  a=Mobile("Moto",150000)
  while flag==True:
    time.sleep(0.51)
    print("Welcome...")
    print("Enter your input")
    print("1.Sim Details \n 2.Mobile Details \n 3.Sim Present \n 4.Add Sim \n 5.Remove Sim \n 6.exit")
    inpu=int(input("Enter value: "))
    match inpu:
      case 1:
        a.sdetails()
      case 2:
        a.details()
      case 3:
        a.isSimPresent()
      case 4:
        a.addSim()
      case 5:
        a.removeSim()
      case 6:
        print("Thank you")
        print("__________")
        flag=False     