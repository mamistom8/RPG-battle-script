from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#create black magic
fire = Spell("Fire",10,100,"black")
thunder = Spell("Thunder",10,100,"black")
blizzard = Spell("Blizzard",10,100,"black")
meteor = Spell("Meteor",20,200,"black")
quake = Spell("Quake",14,140,"black")

#create white magic
cure = Spell("Cure",12,120,"white")
cura = Spell("Cura",18,200,"white")

#create items
posion = Item("Potion","potion","Heals 50 HP",50)
hiposion = Item("Hi-Potion","potion","Heals 100 HP",100)
superposion = Item("Super-Potion","potion","Heals 500 HP",500)
elixer = Item("Elixer","elixer","Fully restores HP/MP of one party member",9999)
hielixer = Item("Hi-Elixer","elixer","Fully restores party's HP/MP",9999)
grenade = Item("Grenade","attack", "Deals 500 damage", 500)


player_spells = [fire,thunder,blizzard,meteor,cure,cura]
player_items = [{"item":posion,"quantity":15},{"item":hiposion,"quantity":15},
                {"item":superposion,"quantity":15},{"item":elixer,"quantity":15},
                {"item":hielixer,"quantity":15},{"item":grenade,"quantity":15}]

#init players
player1 = Person("Tommy  :",3260,300,60,34,player_spells,player_items)
player2 = Person("Mike   :",4160,311,60,34,player_spells,player_items)
player3 = Person("Lebron :",3089,288,60,34,player_spells,player_items)
enemy = Person("The Haters",11200,500,500,25,[],[])

players = [player1,player2,player3]

running = True
i = 0

print(bcolors.FAIL+bcolors.BOLD +"AN ENEMY ATTACKS!" +bcolors.ENDC)



while running:
    print("============")
    print("\n\n")
    print("NAME                  HP                                 MP")
    for player in players:
    
        player.get_stats()

    print("\n")

    enemy.get_enemy_stats()

    for player in players:
        
        player.choose_action()
        choice = input("choose action:")
        index=int(choice)-1

        if index == 0:
            dmg=player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg,"points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choise = int(input("choose magic:"))-1
            
            if magic_choise == -1:
                continue

            spell = player.magic[magic_choise]
            magic_dmg = spell.generate_damage()
            current_mp =player.get_mp()
        
            if spell.cost > current_mp:
                print(bcolors.FAIL + " \nNot enough MP\n"+ bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.typ == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name , "heals for", str(magic_dmg), "HP." + bcolors.ENDC)

            elif spell.typ == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name ,"deals",str(magic_dmg),"points of damage" +bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("choose item:"))-1
            
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "None left.." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" +bcolors.ENDC)

            elif item.type == "elixer":
                if item.name == "Hi-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP and MP" + bcolors.ENDC)
            

            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals" +  str(item.prop)+"points of damage"+ bcolors.ENDC)



        elif index == -1:
            continue

    enemy_choise = 1
    target = random.randrange(0,2)
    enemy_dmg = enemy.generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg,"points of damage.")

    

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN+ "YOU WIN!"+ bcolors.ENDC)
        running =False
    elif player.get_hp() == 0:
        print(bcolors.FAIL+ "YOU LOST!"+ bcolors.ENDC)
        running =False
