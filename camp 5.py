import random 
def run():
    print (" you die of starvation")
    print (" you went extinct...\n the end")
def fight ():
    choice= input ("you look for a weapon...\n1.bow and arrow\n2.fist\n3.rock\nchoice:")
    if choice=="1":
        print ( " you snipe it in the brain, it tumbles to the ground. you make a dagger from its skull, a coat out of bones and hide. plus bone weapons.")
        print (" the rescue never comes but you sucsessfully live in the world of the dinos. \n the end")
    elif choice=="2":
        print (" you try to punch it. it dodges and cuts your throat")
        print (" you went extinct...\n the end")
    elif choice=="3":
        print ( " you pick up a rock and throw it at the raptor and it hits the fule cell of the machine you explode")
        print (" you went extinct ")
def scower_jungle():
    print (" you find food,water and the materials to make a bow and some arrows")
    print ("a dakotaraptor finds you and runs at you")
    choice=input("what do you do?\n1. fight \n2.run\nchoice:")
    if choice=="1":
        print ("you are NOT about to give up all these supplies AND your ride out of here you fight")
        fight()
    elif choice=="2":
        print (" you run as fast as you can as far as you can leaving your shot outta here behind")
        run()
    else:
        print ( " you cant do that sorry")


def make_camp():
    luck= random.randint(1,2)
    if luck==1:
        print ("a dakotaraptor finds your camp and kills you.")
        print ("you went extinct...\n the end")
    elif luck==2:
        print (" you realize you dont have enough supplies and venture into the jungle")
        scower_jungle()



def start():
    print("you volentered to go back in time and study dinosaurs")
    print ("you go inside the time machine and it starts up. when it stops you crash in the creatacous period and your time machine is busted")
    choice= input ("what do you do?:\n1. make camp and rest...\n2. explore for resorces")
    if choice=="1":
        print (" you make camp in the jungle")
        make_camp()
    elif choice == "2":
        print ("you scower the jungle for supplies")
        scower_jungle()
    else:
        print("you cant do that sorry")
        start()



def main ():
    print (" welcome to creatacous rpg!!!click enter to start")
    input()
    start()


main()
