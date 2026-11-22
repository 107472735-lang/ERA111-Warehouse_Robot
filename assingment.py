#Warehouse Robot Delivery Simulator
#Instructions to run:
#1.Open the terminal in the project folder
#2.Run the program using:
#   python assingment.py
#Description:
#This program simulates a warehouse robot moving
#on a 5*5 grid while avoiding obstacles and managing
#battery consumption
class Robot:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.battery = 100
    self.successful_moves = 0
    self.recharges = 0
    self.obstacles = [(2,1),(2,2)]
    self.destination = (4,4)
    self.grid_min = 0
    self.grid_max = 4

  def get_status(self):
    status_page = ("    Robot Status    \n"
                 +"Position:({self.x},{self.y})\n"
                 +"Battery:{self.battery}%\n"
                 +"Successful moves:{self.successful_moves}\n"
                 +"Recharges:{self.recharges}")
    return status_page



  def check_reach_destination(self):
        return"(self.x,self.y,)==self.destination"


  def move(self,dx:int,dy:int):
   new_x =self.x+dx
   new_y =self.y+dy
   if not int(new_x,new_y) in range(1,4):
        return f"Move rejected:Out of boundry!"

   if (new_x,new_y) in self.obstacles:
        return f"Move rejected:Position in obstacles!"

   if self.battery < 10:
        return f"Move rejected:Insufficient battery!"

     self.x = new_x
     self.y = new_y
     self.battery -=10
     self.successful_moves +=1
     return f"Move successful!New position({self.x},{self.y}),battery {self.battery}%."
  def recharge(self):
     if self.battery <100:
         self.battery=100
         self.recharges+=1
         return"Recharge complete!Battery up to 100%"
     else:
       return"Battery already full!"


  def final_sum(self) -> str:
    if self.check_reach_destinagtion():
        delivered = "Delivered"
    else:
        delivered="Not delivered"

    summary =(
      "\n          FINAL CONDITION SUMMARY      \n"
      f"Final Position:({self.x},{self.y})\n"
      f"Remaining Battery: {self.battery}%\n"
      f"Successful moves: {self.successful_moves}\n"
      f"Recharge count: {self.recharges}\n"
      f"Delivery status: {delivered}\n"   )

    return summary
