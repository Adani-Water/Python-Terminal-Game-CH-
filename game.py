import threading
import time
import sys
import random
import os

# clear the console screen (for Windows)
os.system("cls")

# colour codes for terminal text formatting
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
NORMAL = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"




class Cave:
    """
    Class representing the cave system in the game.
    Handles movement, interactions with enemies, and tracking visited rooms.
    """

    def __init__(self, cave=None):
        """
        initialises the cave with a predefined layout and sets the starting position.
        """
        self.cave = {
            1: [2, 5, 8], 2: [1, 3, 6], 3: [2, 4, 7], 4: [3, 5, 8], 5: [1, 4, 9],
            6: [2, 7, 10], 7: [3, 6, 11], 8: [1, 4, 12], 9: [5, 10, 13], 10: [6, 9, 14],
            11: [7, 12, 15], 12: [8, 11, 16], 13: [9, 14, 17], 14: [10, 13, 18],
            15: [11, 16, 19], 16: [12, 15, 20], 17: [13, 18, 21], 18: [14, 17, 22],
            19: [15, 16, 23], 20: [16, 17, 24], 21: [17, 22, 25], 22: [18, 21, 26],
            23: [19, 20, 27], 24: [20, 25, 28], 25: [21, 24, 29], 26: [22, 27, 30],
            27: [23, 26, 28], 28: [24, 27, 29], 29: [25, 28, 30], 30: [26, 29, 27]
        } #Cave system
        self.position = 1  # Starting room
        self.visited_rooms = [1]  # List of visited rooms
        self.helper_fightN = 0

    def move(self):
        """
        Handles movement of the protagonist through the cave, interacting with enemies
        and processing user commands.
        """
        
        while True:
            global current_enemy
            # Check for encounters with enemies in the current room
            if slime1_position in self.cave[self.position]:
                if slime1.health > 0:
                    slime1.warn()
            if slime2_position in self.cave[self.position]:
                if slime2.health > 0:
                    slime2.warn()
            if zombie1_position in self.cave[self.position]:
                if zombie1.health > 0:
                    zombie1.warn()
            if zombie2_position in self.cave[self.position]:
                if zombie2.health > 0:
                    zombie2.warn()
            if cthulhu_position in self.cave[self.position]:
                if cthulhu.health > 0:
                    cthulhu.warn()
            if grotto_position in self.cave[self.position]:
                    grotto.warn()
            if darkness_position in self.cave[self.position]:
                    darkness.warn()
            while True:
                # Prompt user for action
                choice = input(f"{LIGHT_WHITE}{NORMAL}Would you like to move (M), check inventory (C), view known and discovered positions (P), or exit (E)? Choose: [M, C, P, E] ").lower()
                if choice == "m":
                    break
                elif choice == "e":
                    #print("You have unlocked an easter egg, would you like to exit the game (E) or view easter egg (G)?")
                    #while True:
                        #exit_choice = input("You: ").lower()
                        #if exit_choice == "g":
                        # Exit the game with a narrative
                    if self.helper_fightN == 0:
                        time.sleep(2)
                        effects.typewrite(f"{BLUE}Helper: After all of our efforts, ", 0.05)
                        time.sleep(1)
                        effects.typewrite(f"{BLUE}you want to leave?", 0.1)
                        time.sleep(1)
                        effects.typewrite(f"{BLUE} After all of Adania's suffering?", 0.1)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{BOLD}{RED}Helper: NOT ON MY WATCH!!!", 0.05)
                        print()
                        time.sleep(2)
                        self.helper_fightN += 1
                        current_enemy = "helper"
                        helper_E.attack()
                        continue
                    else:
                        time.sleep(2)
                        effects.typewrite(f"{BLUE}Helper: ...Hey.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{BLUE} Look, I know things got... complicated back there.", 0.05)
                        time.sleep(2)
                        print()
                        effects.typewrite(f"{BLUE}Helper: I won't pretend that didn't happen.", 0.05)
                        time.sleep(2)
                        print()
                        effects.typewrite(f"{BLUE}Helper: I tried to kill you.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{BLUE}Helper: But I've been thinking about it.", 0.05)
                        time.sleep(2)
                        print()
                        effects.typewrite(f"{BLUE}Helper: And honestly?", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{BLUE} What would it even change.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{BLUE}Helper: Go", 0.05)
                        effects.typewrite(f"{BLUE}...", 0.2)
                        time.sleep(1.5)
                        effects.typewrite(f"{BLUE} Just go.", 0.05)
                        time.sleep(1.5)
                        print()
                        effects.typewrite(f"{BLUE}Helper: You're free.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{LIGHT_WHITE}You don't know whether to believe him or not.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} But your feet are already moving.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{LIGHT_WHITE}The tunnel stretches ahead of you. Long. Dark. Familiar.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} You've walked this path before.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} You know where it leads.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{LIGHT_WHITE}Light. Faint, but real...", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} The exit.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{LIGHT_WHITE}You start to run.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} You're going to make it.", 0.05)
                        time.sleep(2)
                        effects.typewrite(f"{LIGHT_WHITE} You're actually going to make it.", 0.05)
                        time.sleep(3)
                        print()
                        effects.typewrite(f"{LIGHT_WHITE}You're—", 0.05)
                        time.sleep(5)
                        print()
                        effects.typewrite(f"{RED}Helper: ...I lied.", 0.05)
                        time.sleep(0.5)
                        protagonist.die()

                        #elif exit_choice == "e":
                        #    print("Credits: \nGame Creator: Adan Malik\nGame inspired by: 'Hunt the Wumpus' and 'Zork'")
                        #    exit()
                        #else:
                        #    print("I am sorry, I could not understand. Please type 'E' or 'G'.")
                elif choice == "c":
                    # Show player's inventory
                    print(f"{BLUE}Helper: Here is your inventory.")
                    protagonist.show_inventory()
                elif choice == "p":
                    # Show known and discovered positions
                    self.show_positions()
                else:
                    print(f"{BLUE}Helper: What? Didn't understand...")
                    time.sleep(1)
            # Process movement
            movement = input(f"{LIGHT_WHITE}{NORMAL}Where do you want to move? Choose from: {self.cave[self.position]} ")
            try:
                movement = int(movement)
                if movement == self.position:
                    print(f"{BLUE}Helper: We're already in that room...")
                else:
                    if movement in self.cave:
                        if movement in self.cave[self.position]:
                            print(f"{LIGHT_WHITE}{NORMAL}You have successfully moved to room {movement}")
                            self.position = movement
                            if self.position not in self.visited_rooms:
                                self.visited_rooms.append(self.position)
                            # Handle enemy encounters
                            if self.position == grotto_position:
                                grotto.fight()
                            elif self.position == slime1_position:
                                current_enemy = "slime1"
                                slime1.fight()
                            elif self.position == slime2_position:
                                current_enemy = "slime2"
                                slime2.fight()
                            elif self.position == zombie1_position:
                                current_enemy = "zombie1"
                                zombie1.fight()
                            elif self.position == zombie2_position:
                                current_enemy = "zombie2"
                                zombie2.fight()
                            elif self.position == cthulhu_position:
                                current_enemy = "cthulhu"
                                cthulhu.fight()
                            elif self.position == darkness_position:
                                effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You step into a room swallowed by darkness, an ominous presence lurking like a specter.", 0.05)
                                time.sleep(1)
                                print()
                                protagonist.lose_torch()
                            else:
                                self.move()
                            break
                        else:
                            print(f"{BLUE}Helper: I mean sure, if you can teleport, if not though could you pick one of the adjacent rooms?")
                    else:
                        print(f"{BLUE}Helper: I don't even think the cave is that big...")
            except ValueError:
                print(f"{BLUE}Helper: That's not even a number?")

    def show_positions(self):
        """
        Displays the positions of discovered enemies and visited rooms.
        """
        # Check if any enemies have been discovered
        if slime1.discovered == 1 or slime2.discovered == 1 or zombie1.discovered == 1 or zombie2.discovered == 1 or cthulhu.discovered == 1 or grotto.discovered == 1 or darkness.discovered == 1 or slime1.warned == 1 or slime2.warned == 1 or zombie1.warned == 1 or zombie2.warned == 1 or cthulhu.warned == 1 or grotto.warned == 1 or darkness.warned == 1:
            print(f"{BLUE}Helper: Here are the positions you know so far:")
            time.sleep(1)
            print()
        else:
            print(f"{BLUE}Helper: You have not discovered anything interesting yet...")
            time.sleep(1)

        # Print discovered enemies' positions
        if slime1.discovered == 1:
            if slime1.health > 0:
                print(f"{LIGHT_WHITE}{NORMAL}Slime in room {slime1_position}")
                time.sleep(1)
        else:
            if slime1.warned == 1:
                if slime1.health > 0:
                    print(f"{LIGHT_WHITE}{NORMAL}Slime near rooms {slime1.adjacent}")
                    time.sleep(1)
        if slime2.discovered == 1:
            if slime2.health > 0:
                print(f"{LIGHT_WHITE}{NORMAL}Slime in room {slime2_position}")
                time.sleep(1)
        else:
            if slime2.warned == 1:
                if slime2.health > 0:
                    print(f"{LIGHT_WHITE}{NORMAL}Slime near rooms {slime2.adjacent}")
                    time.sleep(1)
        if zombie1.discovered == 1:
            if zombie1.health > 0:
                print(f"{LIGHT_WHITE}{NORMAL}Zombie in room {zombie1_position}")
                time.sleep(1)
        else:
            if zombie1.warned == 1:
                if zombie1.health > 0:
                    print(f"{LIGHT_WHITE}{NORMAL}Zombie near rooms {zombie1.adjacent}")
                    time.sleep(1)
        if zombie2.discovered == 1:
            if zombie2.health > 0:
                print(f"{LIGHT_WHITE}{NORMAL}Zombie in room {zombie2_position}")
                time.sleep(1)
        else:
            if zombie2.warned == 1:
                if zombie2.health > 0:
                    print(f"{LIGHT_WHITE}{NORMAL}Zombie near rooms {zombie2.adjacent}")
                    time.sleep(1)
        if cthulhu.discovered == 1:
            if cthulhu.health > 0:
                print(f"{LIGHT_WHITE}{NORMAL} Cthulhu in room {cthulhu_position}")
                time.sleep(1)
        else:
            if cthulhu.warned == 1:
                if cthulhu.health > 0:
                    print(f"{LIGHT_WHITE}{NORMAL}Cthulhu near rooms {cthulhu.adjacent}")
                    time.sleep(1)
        if grotto.discovered == 1:
            print(f"{LIGHT_WHITE}{NORMAL}Pitfall in room {grotto_position}")
            time.sleep(1)
        else:
            if grotto.warned == 1:
                print(f"{LIGHT_WHITE}{NORMAL}Pitfall near rooms {grotto.adjacent}")
                time.sleep(1)
        if darkness.discovered == 1:
            print(f"{LIGHT_WHITE}{NORMAL}Darkness looming in room {darkness_position}")
            time.sleep(1)
        else:
            if darkness.warned == 1:
                print(f"{LIGHT_WHITE}{NORMAL}Darkness looming near rooms {darkness.adjacent}")
                time.sleep(1)

        # Print visited rooms
        print(f"{LIGHT_WHITE}{NORMAL}You have visited rooms: {self.visited_rooms}")
        time.sleep(1)


class Timer:
    def __init__(self):
        self.core_used = False

    def start(self, command):
        self.core_used = False
        self._command = command

        if current_enemy == "slime1" or current_enemy == "slime2":
            timeout = slime1.timeout
        elif current_enemy == "zombie1" or current_enemy == "zombie2":
            timeout = zombie1.timeout
        elif current_enemy == "cthulhu":
            timeout = cthulhu.timeout
        elif current_enemy == "helper":
            timeout = helper_E.timeout

        import msvcrt
        print(f"{LIGHT_WHITE}{NORMAL}Type '{command}': ", end="", flush=True)
        
        deadline = time.time() + timeout
        typed = ""
        
        while time.time() < deadline:
            if msvcrt.kbhit():
                ch = msvcrt.getwche()  # echo the character
                if ch in ('\r', '\n'):  # Enter pressed
                    print()
                    break
                elif ch == '\x08':  # backspace
                    if typed:
                        typed = typed[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                else:
                    typed += ch
            time.sleep(0.01)
        else:
            # Timed out
            print()
            print(f"{LIGHT_WHITE}You did not respond in time.")
            self._apply_timeout_damage()
            return

        user_input = typed.lower().strip()

        if command == "dodge":
            if user_input == "dodge":
                print(f"{LIGHT_WHITE}You successfully dodged!")
                effects.display_health()
            else:
                print(f"{LIGHT_WHITE}You made the wrong move! You could not dodge.")
                self.handle_missed_action()
        elif command == "attack":
            if user_input == "attack":
                print(f"{LIGHT_WHITE}You successfully attacked!")
                self.handle_attack()
            else:
                print(f"{LIGHT_WHITE}You made the wrong move! You could not attack.")
                effects.display_health()

    def _apply_timeout_damage(self):
        if current_enemy == "slime1": slime1.damage_P()
        elif current_enemy == "slime2": slime2.damage_P()
        elif current_enemy == "zombie1": zombie1.damage_P()
        elif current_enemy == "zombie2": zombie2.damage_P()
        elif current_enemy == "helper": helper_E.damage_P()
        elif current_enemy == "cthulhu": cthulhu.damage_P()
        if protagonist.health < 0: protagonist.health = 0
        effects.display_health()
        time.sleep(2)
        if protagonist.cores < 1:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Your demise came swiftly due to your lack of vigilance.", 0.05)
            protagonist.die()
        else:
            protagonist.lose_core()
            self.core_used = True

    def handle_missed_action(self):
        if current_enemy == "slime1": slime1.damage_P()
        elif current_enemy == "slime2": slime2.damage_P()
        elif current_enemy == "zombie1": zombie1.damage_P()
        elif current_enemy == "zombie2": zombie2.damage_P()
        elif current_enemy == "helper": helper_E.damage_P()
        elif current_enemy == "cthulhu": cthulhu.damage_P()
        if protagonist.health < 0: protagonist.health = 0
        effects.display_health()

    def handle_attack(self):
        if current_enemy == "slime1":
            slime1.damage_E()
            if slime1.health < 0: slime1.health = 0
        elif current_enemy == "slime2":
            slime2.damage_E()
            if slime2.health < 0: slime2.health = 0
        elif current_enemy == "zombie1":
            zombie1.damage_E()
            if zombie1.health < 0: zombie1.health = 0
        elif current_enemy == "zombie2":
            zombie2.damage_E()
            if zombie2.health < 0: zombie2.health = 0
        elif current_enemy == "helper": helper_E.damage_E()
        elif current_enemy == "cthulhu":
            cthulhu.damage_E()
            if cthulhu.health < 0: cthulhu.health = 0
        effects.display_health()


class Effects:
    """
    A class to handle visual effects in the game, such as text animations and health displays.
    """

    def blink_text(self, text, times):
        """
        Blinks the given text a specified number of times.
        
        Args:
            text (str): The text to blink.
            times (int): The number of times to blink the text.
        """
        for i in range(times):
            i += 1
            sys.stdout.write(BLINK + text + BLINK)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(text) + '\r')
            sys.stdout.flush()
            time.sleep(0.5)

    def typewrite(self, write, delay):
        """
        Simulates typing out the given text with a specified delay between characters.
        
        Args:
            write (str): The text to type out.
            delay (float): The delay between each character.
        """
        for characters in write:
            sys.stdout.write(characters)
            sys.stdout.flush()
            time.sleep(delay)

    def dots(self, repeat, sleep):
        """
        Displays a loading animation with dots.
        
        Args:
            repeat (int): The number of times to repeat the animation.
            sleep (float): The delay between each dot.
        """
        for _ in range(repeat):
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(sleep)
            print("\b\b\b   \b\b\b", end="", flush=True)
            time.sleep(sleep)

    def delete_line(self):
        """
        Deletes the previous line of text from the console.
        """
        sys.stdout.write('\x1b[1A')  # Move up one line
        sys.stdout.write('\x1b[2K')  # Clear the line

    def display_health(self, enemy_name=None):
        """
        Displays the health of the protagonist and the current enemy.
        
        Args:
            enemy_name (str, optional): The name of the enemy to display health for. Defaults to None.
        """
        global current_enemy
        bar_length = 20
        current_enemy_bar = None
        protag_health_ratio = protagonist.health / 100

        # Determine the enemy's health and display name
        if current_enemy == "slime1":
            enemy_health_ratio = slime1.health / 25
            current_enemy_bar = slime1
            enemy_name = "Slime"
        elif current_enemy == "slime2":
            enemy_health_ratio = slime2.health / 25
            current_enemy_bar = slime2
            enemy_name = "Slime"
        elif current_enemy == "zombie1":
            enemy_health_ratio = zombie1.health / 100
            current_enemy_bar = zombie1
            enemy_name = "Zombie"
        elif current_enemy == "zombie2":
            enemy_health_ratio = zombie2.health / 100
            current_enemy_bar = zombie2
            enemy_name = "Zombie"
        elif current_enemy == "helper":
            enemy_name = "Helper"
            enemy_health_ratio = 100 / 100
            enemy_health_bar = 1
        elif current_enemy == "cthulhu":
            enemy_health_ratio = cthulhu.health / 100
            current_enemy_bar = cthulhu
            enemy_name = "Cthulhu"
        
        filled_square = '\u25A0'
        empty_square = '-'
        
        player_health_bar = filled_square * int(protag_health_ratio * bar_length) + empty_square * (bar_length - int(protag_health_ratio * bar_length))
        enemy_health_bar = filled_square * int(enemy_health_ratio * bar_length) + empty_square * (bar_length - int(enemy_health_ratio * bar_length))

        print(f"{LIGHT_WHITE}Your Health: [{player_health_bar}] {protagonist.health}/100")
        if enemy_name == "Helper":
            print(f"{LIGHT_WHITE}{enemy_name} Health: [{enemy_health_bar}] 9̴̡͇͚̝̼͉̟͛̓͆̎9̴̨͋͂̚9̷͎̱̘̠̾͌̏͜9̷̀̽̔́̓̆ͅ9̵͇̘̱̪̏͑̀̃̓̀9̶̟͐̿̿͑͌̆  / 9̴̡͇͚̝̼͉̟͛̓͆̎9̴̨͋͂̚9̷͎̱̘̠̾͌̏͜9̷̀̽̔́̓̆ͅ9̵͇̘̱̪̏͑̀̃̓̀9̶̟͐̿̿͑͌̆")
        elif enemy_name == "Slime":
            print(f"{LIGHT_WHITE}{enemy_name} Health: [{enemy_health_bar}] {current_enemy_bar.health}/25")
        elif enemy_name == "Zombie":
            print(f"{LIGHT_WHITE}{enemy_name} Health: [{enemy_health_bar}] {current_enemy_bar.health}/100")
        elif enemy_name == "Cthulhu":
            print(f"{LIGHT_WHITE}{enemy_name} Health: [{enemy_health_bar}] {current_enemy_bar.health}/500")

class Protag:
    """
    A class representing the protagonist with attributes for health, power, torches, and health cores.
    """

    def __init__(self, health, power, torches, cores):
        """
        initialises the protagonist with specified attributes.
        
        Args:
            health (int): The initial health of the protagonist.
            power (int): The initial power of the protagonist.
            torches (int): The initial number of torches.
            cores (int): The initial number of health cores.
        """
        self.health = health
        self.power = power
        self.torches = torches
        self.cores = cores

    def name_char(self):
        """
        Prompts the user to enter their character's name and validates the input.
        """
        print(f"{YELLOW}Cthulhu Hunt: Before we begin, please type your character's first and last name.")
        while True:
            name = str(input(f"{LIGHT_WHITE}{NORMAL}You: ")).capitalize().rstrip().lstrip()
            namewords = name.split()
            if len(namewords) == 2:
                self.first_name, self.last_name = namewords
                if self.first_name.isalpha() and self.last_name.isalpha():
                    print(f"{YELLOW}Cthulhu Hunt: Hello, {self.first_name.capitalize()} {self.last_name.capitalize()}.")
                    break
                else:
                    print(f"{YELLOW}Cthulhu Hunt: I'm not sure I understood that. Please respond with only your first and last name with letters only.")
            else:
                print(f"{YELLOW}Cthulhu Hunt: I'm not sure I understood that. Please respond with only your first and last name.")

    def gain_torch(self):
        """
        Increases the number of torches the protagonist has.
        """
        self.torches += 1
        if self.torches == 1:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have gained a torch! You now have {self.torches} torch.", 0.05)
            print()
        else:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have gained a torch! You now have {self.torches} torches.", 0.05)
            print()

    def lose_torch(self):
        """
        Decreases the number of torches the protagonist has, handling the consequences of losing a torch.
        """
        if self.torches >= 1:
            self.torches -= 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Suddenly, you recall the torch retrieved from the slime's remains.", 0.05)
            time.sleep(1)
            print()
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}As its flickering light reveals shadows dancing with unseen horrors, ", 0.05)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}you know you must flee before the torch's glow dims to nothingness.",0.05)
            print()
            darkness.fight()
            cave.move()
        else:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Without a light to guide you, fear grips your heart as you sense unseen horrors lurking.", 0.05)
            time.sleep(1)
            print()    
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}In an instant, a shiver runs down your spine- ", 0.05)
            time.sleep(0.5)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}as your neck snaps and your life slips away.", 0.075)
            protagonist.die()

    def gain_core(self):
        """
        Increases the number of health cores the protagonist has.
        """
        self.cores += 1
        if self.cores == 1:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have gained a health core! You now have {self.cores} health core.", 0.05)
            print()
        else:
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have gained a health core! You now have {self.cores} health cores.", 0.05)
   
    def lose_core(self):
        """
        Consumes a health core
        """
        self.cores -= 1
        time.sleep(2)
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}As the darkness begins to consume your vision, a sudden surge of energy from the health core pulses through your body, reviving you from the brink of death.", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Your HP bar rapidly fills, and you rise to your feet.", 0.05)
        self.health += 50
        time.sleep(3)
        print()

    def die(self):
        """
        Kills the protagonist
        """
        time.sleep(3)
        print()
        print()
        effects.typewrite(f"{BOLD}{RED}YOU HAVE DIED.", 0.1)
        time.sleep(1)
        print()
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Because of your incompetence, Adania will suffer for eternity...", 0.1)   
        time.sleep(2)
        print("Credits: \nGame Creator: Adan Malik\nGame inspired by: 'Hunt the Wumpus' and 'Zork'")
        exit()
    
    def show_inventory(self):
        """
        Shows items in inventory
        """
        print("Inventory:")
        print(f"Adamantite Broadsword: 1")
        print(f"Torches: {self.torches}")
        print(f"Health Cores: {self.cores}")

# Base class for all enemies
class Enemy():
    """
    Base class for all enemies in the game.
    
    Attributes:
        health (int): The health of the enemy.
        damage (int): The damage the enemy can inflict.
        timeout (int): Time to respond in seconds during combat.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        self.health = health
        self.damage = damage
        self.timeout = timeout
        self.warned = warned
        self.discovered = discovered
        self.adjacent = adjacent
        

    def fight(self): #A generalised method
        if self.health > 0:
            self.discovered = 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}An enemy appears!", 0.03)
            time.sleep(1)
            print()
            while self.health > 0 and protagonist.health > 0:
                action = input(f"{LIGHT_WHITE}{NORMAL}Do you want to (A)ttack or (R)un? ").lower()
                if action == 'a':
                    self.attack()
                elif action == 'r':
                    print(f"{LIGHT_WHITE}{NORMAL}You ran away from the enemy!")
                    cave.move()
                    return 
                else:
                    print(f"{LIGHT_WHITE}{NORMAL}Invalid action. Please choose 'A' to attack or 'R' to run.")
            cave.move()
        else:
            cave.move()

    def placement(self):
        """
        Randomly places the enemy in a room.
        
        Returns:
            int: The position of the enemy.
        """
        while True:
            enemy_position = random.randint(2, 30)
            if enemy_position not in taken:
                taken.append(enemy_position)
                break
        return enemy_position

    def damage_P(self):
        """
        Inflicts damage on the protagonist.
        """
        protagonist.health -= self.damage
        print(f"-{self.damage} player hp")

    def damage_E(self):
        """
        Inflicts damage on the enemy.
        """
        self.health -= protagonist.power
        print(f"-{protagonist.power} enemy hp")

    def attack(self):
        global command
        effects.typewrite(f"{BLUE}Helper: Listen closely, we've encountered an enemy. Follow my orders swiftly if you want to survive; delay, and your chance will slip away. ", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{BLUE}Helper: This enemy will give you {self.timeout} time to react, so follow what I say to survive.", 0.05)
        time.sleep(2)
        print()
        while self.health > 0 and protagonist.health > 0 and not timer.core_used:
            helper.command()
        if protagonist.health <= 0:
            protagonist.health = 0
            if protagonist.cores == 0:
                protagonist.die()
            else:
                protagonist.lose_core()
        if self.health <= 0:
            if self.name != "Helper":
                self.health = 0
                time.sleep(2)
                effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Congratulations!", 3)
                time.sleep(1)
                effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have defeated the enemy!", 0.05)
                time.sleep(2)
                cave.move()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

    def warn(self):
        """
        Provides a warning about the presence of a slime enemy.
        """
        if self.warned == 0:
            self.warned += 1
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}There is an enemy nearby.", 0.03)
            time.sleep(2)
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is a enemy near this room.")
            time.sleep(1)
        self.set_adjacent()

class Helper_E(Enemy):
    """
    Helper enemy that assists the protagonist during combat.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)

    def attack(self):
        global command
        while protagonist.health > 0 and not timer.core_used:
            effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Get ready!", 3)
            time.sleep(1)
            print(f"{LIGHT_WHITE}{NORMAL}FIGHT!")
            time.sleep(1)
            pick = random.randint(1, 2)
            if pick == 1:
                print(f"{BOLD}{RED}Helper: Dodge this!")
                command = "attack"
                timer.start(command)
            elif pick == 2:
                print(f"{BOLD}{RED}Helper: Come on, attack me!")
                command = "dodge"
                timer.start(command)
    
        if protagonist.health <= 0:
            protagonist.health = 0
            if protagonist.cores == 0:
                protagonist.die()
            else:
                protagonist.lose_core()

    def damage_E(self):
        """
        Inflicts damage on the Helper enemy.
        """
        print(f"-{protagonist.power} enemy hp")

        
class Slime(Enemy):
    """
    Slime enemy with unique combat mechanics.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
        warned (int): Flag to indicate if the player has been warned about the slime.
        discovered (int): Flag to indicate if the slime has been discovered.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)
        
    def attack(self):
        """
        Executes combat sequence with the slime enemy.
        """
        global command
        effects.typewrite(f"{BLUE}Helper: Listen closely, we've encountered a slime. Follow my orders swiftly if you want to survive; delay, and your chance will slip away. ", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{BLUE}Helper: This enemy will give you about {self.timeout} seconds time to react, so follow what I say to survive.", 0.05)
        time.sleep(2)
        print()
        while self.health > 0 and protagonist.health > 0 and not timer.core_used:
            helper.command()
        if protagonist.health <= 0:
            protagonist.health = 0
            if protagonist.cores == 0:
                protagonist.die()
            else:
                protagonist.lose_core()
                return
        if self.health <= 0:
            self.health = 0
            time.sleep(2)
            effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Congratulations!", 3)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have defeated the slime!", 0.05)
            time.sleep(3)
            print()
            protagonist.gain_torch()
            time.sleep(2)
            cave.move()

    def fight(self):
        """
        Handles the fighting sequence with the slime enemy.
        """
        if self.health > 0:
            self.discovered = 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}A wild slime appears!", 0.03)
            time.sleep(1)
            print()
            while self.health > 0 and protagonist.health > 0:
                action = input(f"{LIGHT_WHITE}{NORMAL}Do you want to (A)ttack or (R)un? ").lower()
                if action == 'a':
                    if current_enemy == "slime1":
                        slime1.attack()
                    elif current_enemy == "slime2":
                        slime2.attack()
                elif action == 'r':
                    print(f"{LIGHT_WHITE}{NORMAL}You ran away from the slime!")
                    cave.move()
                    return 
                else:
                    print(f"{LIGHT_WHITE}{NORMAL}Invalid action. Please choose 'A' to attack or 'R' to run.")
            cave.move()
        else:
            cave.move()
            
    def damage_E(self):
        """
        Inflicts damage on the slime enemy.
        """
        self.health -= protagonist.power
        print(f"-{protagonist.power} enemy hp")

    def warn(self):
        """
        Provides a warning about the presence of a slime enemy.
        """
        if self.warned == 0:
            self.warned += 1
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The air grows thick with a faint, musty odor.", 0.03)
            time.sleep(1)
            print()
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Suddenly, you hear a squelching sound echoing from a nearby room.", 0.03)
            time.sleep(2)
            print()
            effects.typewrite(f"{BLUE}Helper: You hear that? These are signs that there is a slime nearby", 0.03)
            time.sleep(2)
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is a slime near this room.")
            time.sleep(1)
        self.set_adjacent()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

class Zombie(Enemy):
    """
    Zombie enemy with unique combat mechanics.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
        warned (int): Flag to indicate if the player has been warned about the zombie.
        discovered (int): Flag to indicate if the zombie has been discovered.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)
        
    def attack(self):
        """
        Executes combat sequence with the zombie enemy.
        """
        global command
        effects.typewrite(f"{BLUE}Helper: We've encountered a zombie. Listen closely and act quickly if you want to survive; delay could be fatal. ", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{BLUE}Helper: This enemy will only give you about {self.timeout} seconds time to react, so follow what I say to survive.", 0.05)
        time.sleep(2)
        print()
        while self.health > 0 and protagonist.health > 0 and not timer.core_used:
            helper.command()
        if protagonist.health <= 0:
            protagonist.health = 0
            if protagonist.cores == 0:
                protagonist.die()
            else:
                protagonist.lose_core()
                return
        if self.health <= 0:
            self.health = 0
            time.sleep(2)
            effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Congratulations!", 3)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have defeated the zombie!", 0.05)
            print()
            time.sleep(3)
            protagonist.gain_core()
            time.sleep(2)
            cave.move()

    def fight(self):
        """
        Handles the fighting sequence with the zombie enemy.
        """
        if self.health > 0:
            self.discovered = 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}A revolting zombie appears, get ready to fight!", 0.03)
            time.sleep(1)
            print()
            while self.health > 0 and protagonist.health > 0:
                action = input(f"{LIGHT_WHITE}{NORMAL}Do you want to (A)ttack or (R)un? ").lower()
                if action == 'a':
                    if current_enemy == "zombie1":
                        zombie1.attack()
                    elif current_enemy == "zombie2":
                        zombie2.attack()
                elif action == 'r':
                    print(f"{LIGHT_WHITE}{NORMAL}You ran away from the zombie!")
                    cave.move()
                    return 
                else:
                    print(f"{LIGHT_WHITE}{NORMAL}Invalid action. Please choose 'A' to attack or 'R' to run.")
            cave.move()
        else:
            cave.move()

    def damage_E(self):
        """
        Inflicts damage on the zombie enemy.
        """
        self.health -= protagonist.power
        print(f"-{protagonist.power} enemy hp.")

    def warn(self):
        """
        Provides a warning about the presence of a zombie enemy.
        """
        if self.warned == 0:
            self.warned += 1
            time.sleep(1)
            effects.typewrite("A low, guttural moan reverberates through the cavern, ", 0.03)
            time.sleep(1)
            print()
            effects.typewrite("The stench of decay fills the air.", 0.03)
            time.sleep(2)
            print()
            effects.typewrite(f"{BLUE}Helper: I think there is a zombie nearby. I can feel it.", 0.03)
            time.sleep(2)
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is a zombie near this room.")
            time.sleep(1)
        self.set_adjacent()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

class Cthulhu(Enemy):
    """
    Cthulhu enemy, the final boss with unique combat mechanics.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
        warned (int): Flag to indicate if the player has been warned about Cthulhu.
        discovered (int): Flag to indicate if Cthulhu has been discovered.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)
        
    def attack(self):
        """
        Executes combat sequence with the Cthulhu enemy.
        """
        global command
        effects.typewrite(f"{BLUE}Helper: It's Cthulhu... He looks ever more terrifying than I had imagined. ", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{BLUE}Helper: He is going to be very quick, so I need you to react to my orders in less than {self.timeout} seconds, otherwise you will die.", 0.05)
        time.sleep(2)
        print()
        while self.health > 0 and protagonist.health > 0 and not timer.core_used:
            helper.command()
        if protagonist.health <= 0:
            protagonist.health = 0
            if protagonist.cores == 0:
                protagonist.die()
            else:
                protagonist.lose_core()
                return
        if self.health <= 0:
            self.health = 0
            time.sleep(2)
            effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Congratulations!", 3)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have defeated Cthulhu!", 0.05)
            print()
            time.sleep(2)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The ancient evil that plagued the kingdom of Adania is no more!", 0.05)
            print()
            time.sleep(2)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The people of Adania rejoice in our brave hero {protagonist.first_name.capitalize()} {protagonist.last_name.capitalize()}'s victory!", 0.05)
            print()
            time.sleep(3)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You have freed the kingdom from darkness and brought peace!", 0.05)
            print()
            time.sleep(3)
            print("Credits: \nGame Creator: Adan Malik\nGame inspired by: 'Hunt the Wumpus' and 'Zork'")
            exit()

    def fight(self):
        """
        Handles the fighting sequence with the Cthulhu enemy.
        """
        if self.health > 0:
            self.discovered = 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You hear unsettling thuds...", 0.1)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL} Loud enough to make you go deaf if heard for too long. ", 0.05)
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}It's him...", 0.05)
            time.sleep(3)
            print()
            effects.typewrite(f"{BOLD}{RED}Cthulhu: I see I have a challenger... ", 0.1)
            time.sleep(1)
            print()
            effects.typewrite(f"{BOLD}{RED}Cthulhu: COME, " , 0.05)
            time.sleep(0.5)
            effects.typewrite(f"{BOLD}{RED}SHOW ME YOUR WORTH!!!" , 0.05)
            time.sleep(1)
            print()
            while self.health > 0 and protagonist.health > 0:
                action = input(f"{LIGHT_WHITE}{NORMAL}Do you want to (A)ttack or (R)un? ").lower()
                if action == 'a':
                    cthulhu.attack()
                elif action == 'r':
                    effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Desperation fuels your legs as you sprint with all your might, heart pounding in fear of the pursuing beast.", 0.05)
                    time.sleep(1)
                    print()
                    effects.typewrite(f"{LIGHT_WHITE}{NORMAL}A sickening realization hits as your legs buckle, turning to see them mangled and bloody, ", 0.05)
                    time.sleep(0.5)
                    effects.typewrite(f"{LIGHT_WHITE}{NORMAL}a gruesome sight behind you.", 0.05)
                    time.sleep(1)
                    print()
                    effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You collapse in agony, succumbing to the pain and terror as your life ebbs away, ", 0.05)
                    time.sleep(0.5)
                    effects.typewrite(f"{LIGHT_WHITE}{NORMAL}a victim of your failed escape..", 0.05)
                    time.sleep(2)
                    print()
                    effects.typewrite(f"{BOLD}{RED}Cthulhu: You really thought you could have run away?" , 0.05)
                    time.sleep(1)
                    print()
                    effects.typewrite(f"{BOLD}{RED}Cthulhu: Fool." , 0.05)
                    protagonist.die()
                else:
                    print(f"{LIGHT_WHITE}{NORMAL}Invalid action. Please choose 'A' to attack or 'R' to run.")
            cave.move()
        else:
            cave.move()

    def damage_E(self):
        """
        Inflicts damage on the Cthulhu enemy.
        """
        self.health -= protagonist.power
        print(f"-{protagonist.power} enemy hp")

    def warn(self):
        """
        Provides a warning about the presence of Cthulhu.
        """
        if self.warned == 0:
            self.warned += 1
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The ground shakes with each thunderous footstep", 0.03)
            time.sleep(2)
            print()
            effects.typewrite(f"{BLUE}Helper: ... {ITALIC}what is that?", 0.03)
            time.sleep(2) 
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is a mysterious and frightening entity near this room.")
            time.sleep(1)
        self.set_adjacent()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

class Grotto(Enemy):
    """
    Grotto enemy that represents a pitfall or trap.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
        warned (int): Flag to indicate if the player has been warned about the pitfall.
        discovered (int): Flag to indicate if the pitfall has been discovered.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)

    def fight(self):
        """
        Handles the falling sequence into the pitfall.
        """
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}You stumble, the ground giving way beneath you with a sickening lurch. ", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Plunging into the pit's depths, fear grips your throat as darkness swallows you whole.", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}Desperate hands claw at slippery walls, but there's no escape.", 0.05)
        time.sleep(1)
        print()
        effects.typewrite(f"{LIGHT_WHITE}{NORMAL}With a final, heart-wrenching realization, you plummet into the abyss, the world above fading into a distant echo.", 0.05)
        protagonist.die()

    def warn(self):
        """
        Provides a warning about the presence of a pitfall.
        """
        if self.warned == 0:
            self.warned += 1
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The ground trembles slightly beneath your feet, and you hear the distant echo of falling rocks", 0.03)
            time.sleep(2)
            print()
            effects.typewrite(f"{BLUE}Helper: I can hear the ambience of a large pitfall. Tread carefully...", 0.03)
            time.sleep(2) 
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is a pitfall near this room.")
            time.sleep(1)
        self.set_adjacent()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

class Darkness(Enemy):
    """
    Darkness enemy that represents an impenetrable dark area.
    
    Attributes:
        timeout (int): Time to respond in seconds during combat.
        warned (int): Flag to indicate if the player has been warned about the darkness.
        discovered (int): Flag to indicate if the darkness has been discovered.
    """
    def __init__(self, health, damage, timeout, warned, discovered, adjacent):
        super().__init__(health=health, damage=damage, timeout=timeout, warned = warned, discovered = discovered, adjacent = adjacent)

    def fight(self):
        """
        Placeholder method for combat with the darkness enemy.
        """
        self.discovered = 1

    def warn(self):
        """
        Provides a warning about the presence of darkness.
        """
        if self.warned == 0:
            self.warned += 1
            time.sleep(1)
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}An eerie, impenetrable darkness seems to seep from the shadows around you.", 0.03)
            time.sleep(1)
            print()
            effects.typewrite(f"{LIGHT_WHITE}{NORMAL}The darkness has spread so much so, you cannot determine its source.", 0.03)
            time.sleep(2)
            print()
            effects.typewrite(f"{BLUE}Helper: It feels very ominous here, tread carefully...", 0.03)
            time.sleep(2) 
            print()
        else:
            time.sleep(1)
            print(f"{BLUE}Helper: There is darkness looming near this room.")
            time.sleep(1)
        self.set_adjacent()

    def set_adjacent(self):
        if cave.position not in self.adjacent:
            self.adjacent.append(cave.position)

class Narrator:
    def __init__(self):
        """
        initialise the Narrator with a set of dialogues to be used for story introduction.
        """
        self.dialogues = [
            f"{GREEN}In the kingdom of Adania, darkness has engulfed our once-peaceful lands.\n",
            f"{GREEN}For centuries, our people have lived under the shadow of fear cast by the monstrous Cthulhu.\n",
            f"{GREEN}Its malevolent presence threatens our very existence.\n",
            f"{GREEN}Once, the dryads had tried their luck, but they failed, not a single one remaining.\n",
            f"{GREEN}Now, a brave hero {protagonist.first_name.capitalize()} {protagonist.last_name.capitalize()} emerges,\n",
            f"{GREEN}driven by the plight of our kingdom and the need to rid Adania of this ancient evil.\n",
            f"{GREEN}As you step into the shoes of our hero, prepare to embark on a perilous journey\n",
            f"{GREEN}to hunt down Cthulhu and restore light to our world.\n"
        ]
    
    def begin(self):
        """
        Display the introduction dialogues as a narration to the player.
        """
        for dialogue in self.dialogues:
            effects.typewrite(f"{GREEN}Narrator: {dialogue}", 0.04)
            print()
            time.sleep(1)

class Helper:
    def __init__(self):
        """
        initialise the Helper with a set of dialogues for guiding and assisting the protagonist.
        """
        self.dialogues = [
            f"{BLUE}Hello {protagonist.first_name.capitalize()} {protagonist.last_name.capitalize()}, I am your personal Adania issued helper!\n",
            f"{BLUE}I will carry your items, guide you through the caves as we dwell deeper and help you during encounters.\n",
            f"{BLUE}Let's head in.\n",
        ]

    def context(self):
        """
        Display the introduction dialogues for the Helper, providing guidance and support information.
        """
        for dialogue in self.dialogues:
            effects.typewrite(f"{BLUE}Helper: {dialogue}", 0.04)  
            print()
            time.sleep(1)

    def command(self):
        """
        Gives a command "attack" or "dodge" during a fight
        """
        global command
        effects.blink_text(f"{LIGHT_WHITE}{NORMAL}Get ready!", 3)
        time.sleep(1)
        print(f"{LIGHT_WHITE}{NORMAL}FIGHT!")
        time.sleep(1)
        pick = random.randint(1,2)
        if pick == 1:
            print(f"{BLUE}Helper: Dodge!")
            command = "dodge"
            if protagonist.health > 0:
                timer.start(command)
        if pick == 2:
            print(f"{BLUE}Helper: Attack!")
            command = "attack"
            if protagonist.health > 0:
                timer.start(command)

# Global variables and object instantiation
current_enemy = None
taken = [2, 5, 8]
command = ""

protagonist = Protag(100, 50, 0, 1)  # initialise protagonist with specific attributes
protagonist.name_char()  # Set the protagonist's name
timer = Timer()  # initialise the Timer for handling time-based events

# initialise enemies with their respective timeouts
slime1 = Slime(25, 10, 7, 0, 0, [])
slime2 = Slime(25, 10, 7, 0, 0, [])
zombie1 = Zombie(100, 50, 5, 0, 0, [])
zombie2 = Zombie(100, 50, 5, 0, 0, [])
grotto = Grotto(None, None, None, 0, 0, [])  # No specific timeout for Grotto
darkness = Darkness(None, None, None, 0, 0, [])  # No specific timeout for Darkness
cthulhu = Cthulhu(500, 100, 3, 0, 0, [])  # initialise Cthulhu with a specific timeout
helper_E = Helper_E(None, 1000000, 2, 0, 0, [])  # initialise helper with a specific timeout 

# Placement of enemies in the cave
slime1_position = slime1.placement()
slime2_position = slime2.placement()
zombie1_position = zombie1.placement()
zombie2_position = zombie2.placement()
grotto_position = grotto.placement()
cthulhu_position = cthulhu.placement()
darkness_position = darkness.placement()

# List of all enemy positions, not in classes as they are better off global
enemy_positions = [
    slime1_position,
    slime2_position,
    zombie1_position,
    zombie2_position,
    grotto_position,
    cthulhu_position,
    darkness_position
]

# initialise the cave system, effects and the narrator
cave = Cave()     
narrator = Narrator()
effects = Effects()
helper = Helper()
context_narrator = Narrator()
# Display narrator's introduction
  # Display a loading effect

print(f"{YELLOW}Cthulhu Hunt: Would you like to get immersed in the story (S) or go straight to the game (G)?")

while True:
    story = input(f"{LIGHT_WHITE}{NORMAL}You: ").lower()
    if story == "s":
        print(f"{YELLOW}Cthulhu Hunt: Ok, redirecting you to the story.")
        print(f"{YELLOW}Redirecting.", end="")
        effects.dots(2, 0.5)
        time.sleep(1)
        os.system("cls")
        dialogues = context_narrator.begin()  # Start the narrator's introduction
        print(dialogues)
        effects.delete_line()  # Delete the loading effect
        effects.dots(3, 0.5)  # Display a loading effect
        time.sleep(2)
        os.system("cls")  # Clear the screen
        # Display helper's introduction
        dialogues = helper.context()  # Start the helper's introduction
        print(dialogues)
        effects.delete_line()  # Delete the loading effect
        time.sleep(2)
        
        # Begin cave exploration
        print()
        cave.move()
    elif story == "g":
        print(f"{YELLOW}Cthulhu Hunt: Ok, redirecting you straight to the game.")
        print(f"{YELLOW}Redirecting.", end="")
        effects.dots(2, 0.5)
        time.sleep(1)
        os.system("cls")
        
        # Begin cave exploration
        cave.move()
    else:
        print(f"{YELLOW}I didn't quite understand. Type 'S' or 'G' please...")
        time.sleep(1)

