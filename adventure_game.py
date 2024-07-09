import time
import random


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(prompt, option_1, option_2):
    response = ""
    while response != option_1 and response != option_2:
        response = input(prompt).lower()
    return response


def play_again():
    response = valid_input("Would you like to play again? (y/n) ", "y", "n")
    if response == "y":
        print_sleep("Excellent! Restarting the game ...")
        adventure_game()
    elif response == "n":
        print_sleep("Thanks for playing! See you next time.")


def fight(player):
    if not player["cave_visited"]:
        print_sleep(
            "You feel a bit under-prepared for this, "
            "what with only having a dagger.")
        want_fight = valid_input(
            "Would you like to (1) fight or (2) run away? ", "1", "2")
        if want_fight == "1":
            print_sleep("You do your best...")
            print_sleep("but your dagger is no match for the "
                        f"{player["villain"]}.")
            print_sleep("You have been defeated!")
            play_again()
        elif want_fight == "2":
            print_sleep(
                "You run back into the field. Luckily, "
                "you don't seem to have been followed.")
            outside_choices(player)
    elif player["cave_visited"]:
        want_fight = valid_input(
            "Would you like to (1) fight or (2) run away? ", "1", "2")
        if want_fight == "1":
            print_sleep(
                f"As the {player['villain']} moves to attack, "
                "you unsheathe your new sword.")
            print_sleep(
                "The Sword of Ogoroth shines brightly in your hand "
                "as you brace yourself for the attack.")
            print_sleep(
                f"But the {player['villain']} takes one look "
                "at your shiny new toy and runs away!")
            print_sleep("You have rid the town of the "
                        f"{player['villain']}. You are victorious!")
            play_again()
        elif want_fight == "2":
            print_sleep(
                "You run back into the field. Luckily, "
                "you don't seem to have been followed.")
            outside_choices(player)


def intro(player):
    print_sleep(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers.")
    print_sleep(
        f"Rumor has it that a {player["villain"]} is somewhere around here, "
        "and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep(
        "In your hand you hold your trusty (but not very effective) dagger.")


def house(player):
    print_sleep("You approach the door of the house.")
    print_sleep(
        "You are about to knock when the door opens "
        f"and out steps a {player["villain"]}.")
    print_sleep(f"Eep! This is the {player["villain"]}'s house!")
    print_sleep(f"The {player['villain']} attacks you!")
    fight(player)


def cave(player):
    print_sleep("You peer cautiously into the cave.")
    if player["cave_visited"]:
        print_sleep(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now.")
    elif not player["cave_visited"]:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical sword of Ogoroth!")
        print_sleep(
            "You discard your silly old dagger and take the sword with you.")
        player["cave_visited"] = True
    print_sleep("You walk back out to the field.")
    outside_choices(player)


def outside_choices(player):
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    decision_1 = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if decision_1 == "1":
        house(player)
    elif decision_1 == "2":
        cave(player)


def adventure_game():
    villains = ['troll', 'wicked fairie',
                'pirate', 'gorgon', 'dragon', 'vampire']
    player = {
        "cave_visited": False,
        "villain": random.choice(villains),
    }
    intro(player)
    outside_choices(player)


adventure_game()
