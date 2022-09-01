"""script to manipulate game save files in Songs of Conquest"""

import os
import json
import random
import sys


class GameState:
    """
    Class to hold the GameState Dict
    """
    def __init__(self):
        """
        Initialize as empty
        """
        self.game_state = {}

    def load_from_file(self, path):
        """
        Load from file
        :param path: the full path to the save file
        """
        with open(path, "r") as f:
            line = f.read()
            line = line.strip()

        state = json.loads(line)
        for key in state:
            tmp = state[key]
            tmp = json.loads(tmp)
            state[key] = tmp

        self.game_state = state

    def save_to_file(self, path):
        """
        Save to file
        :param path: the full path of where to save
        """
        string = json.dumps({
            "File": json.dumps(self.game_state["File"]),
            "Metadata": json.dumps(self.game_state["Metadata"])
        })

        # opening in append mode will create file if necessary
        with open(path, "a") as f:
            pass

        with open(path, "w") as f:
            f.write(string)


class Cheat:
    """
    Superclass for all cheats, contains different subclasses for the individual cheats grouped by type
    """

    class MapManipulation:
        """
        All cheats that are related to the map file itself
        """
        def set_water_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Water"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Water"]))]

        def set_road_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Roads"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Roads"]))]

        def set_elevation_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Elevations"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Elevations"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Themes"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Themes"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Types"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Types"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Decoration"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Decoration"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Effects"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Effects"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["StandaloneDecorations"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["StandaloneDecorations"]))]

        def set_theme_level(gamestate, level):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Variations"] = [level for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Variations"]))]

        def scramble_map(gamestate):
            state = gamestate.game_state
            state["File"]["_level"]["_map"]["Contents"]["Water"] = [0 for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Water"]))]
            state["File"]["_level"]["_map"]["Contents"]["Roads"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Roads"]))]
            state["File"]["_level"]["_map"]["Contents"]["Elevations"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Elevations"]))]
            state["File"]["_level"]["_map"]["Contents"]["Themes"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Themes"]))]
            state["File"]["_level"]["_map"]["Contents"]["Types"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Types"]))]
            # state["File"]["_level"]["_map"]["Contents"]["Decoration"] = [random.randint(0, 4) for _ in range(len(state["File"]["_level"]["_map"]["Contents"]["Decoration"]))]
            state["File"]["_level"]["_map"]["Contents"]["Effects"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Effects"]))]
            # state["File"]["_level"]["_map"]["Contents"]["StandaloneDecorations"] = [random.randint(0, 4) for _ in range(len(state["File"]["_level"]["_map"]["StandaloneDecorations"]["Water"]))]
            state["File"]["_level"]["_map"]["Contents"]["Variations"] = [random.randint(0, 1) for _ in range(
                len(state["File"]["_level"]["_map"]["Contents"]["Variations"]))]

    class PlayerManipulation:
        """
        All cheats that are related to setting player values
        """
        def set_resource_count(gamestate, player_id, resource_id, target_amount):
            # 0 = gold, 1 = wood, 2 = stone, 3 = ancient Amber, 4 = glimmerweave, 5 = Celestial Ore
            state = gamestate.game_state
            tmp = state["File"]["_teamsSerializable"][player_id]["_resources"]["_resources"]
            # print(tmp)
            for r in tmp:
                if r["Type"] == resource_id:
                    r["_amount"] = target_amount
            state["File"]["_teamsSerializable"][player_id]["_resources"]["_resources"] = tmp

        def set_alive(gamestate, player_id, is_alive):
            state = gamestate.game_state
            state["File"]["_teamsSerializable"][player_id]["_isAlive"] = is_alive

        def set_building_constructions_per_base(gamestate, player_id, amount):
            state = gamestate.game_state
            state["File"]["_teamsSerializable"][player_id]["_stats"]["_buildingConstructionsPerBase"] = amount

        def set_all_dwellings_increase(gamestate, player_id, percentage):
            state = gamestate.game_state
            state["File"]["_teamsSerializable"][player_id]["_stats"]["_allDwellingIncrease"] = percentage

        def make_overpowered(gamestate, player_id):
            state = gamestate.game_state
            tmp = state["File"]["_teamsSerializable"][player_id]["_resources"]["_resources"]
            for r in tmp:
                r["_amount"] = 99999999
            state["File"]["_teamsSerializable"][player_id]["_resources"]["_resources"] = tmp
            state["File"]["_teamsSerializable"][player_id]["_isAlive"] = True
            state["File"]["_teamsSerializable"][player_id]["_stats"]["_buildingConstructionsPerBase"] = 9999
            state["File"]["_teamsSerializable"][player_id]["_stats"]["_allDwellingIncrease"] = 999999

    class CommanderManipulation:
        """
        All cheats that are related to setting hero values
        """
        def get_index_from_name(gamestate, name):
            state = gamestate.game_state
            for i in range(len(state["File"]["_commandersSerializable"])):
                if state["File"]["_commandersSerializable"][i]["_reference"]["Name"] == name:
                    return i

        def get_all_heros(gamestate):
            state = gamestate.game_state
            lookup = {}
            for i in range(len(state["File"]["_commandersSerializable"])):
                lookup[state["File"]["_commandersSerializable"][i]["_reference"]["Name"]] = i
            return lookup

        def set_experience(gamestate, index, target_value):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_stats"]["_experience"] = target_value

        def set_view_radius(gamestate, index, target_value):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_stats"]["_viewRadius"] = target_value

        def set_offense(gamestate, index, target_value):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_stats"]["_offense"] = target_value

        def set_defense(gamestate, index, target_value):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_stats"]["_defense"] = target_value

        def set_movement(gamestate, index, target_value):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_stats"]["_movement"] = target_value

        def make_overpowered(gamestate, index):
            state = gamestate.game_state
            state["File"]["_commandersSerializable"][index]["_unspentSkillPoints"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_experience"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_viewRadius"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_movement"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_offense"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_defense"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_xpMultiplier"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceLeech"] = 10
            state["File"]["_commandersSerializable"][index]["_stats"]["_diplomacyBonus"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_tutorPercent"] = 100
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceStats"]["_order"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceStats"]["_creation"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceStats"]["_chaos"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceStats"]["_arcana"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_essenceStats"]["_destruction"] = 999
            state["File"]["_commandersSerializable"][index]["_stats"]["_command"] = 9
            state["File"]["_commandersSerializable"][index]["_stats"]["_spellDamagePowerPercent"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_pillageBonusPercent"] = 99999999
            state["File"]["_commandersSerializable"][index]["_stats"]["_woodcutterRadius"] = 9
            state["File"]["_commandersSerializable"][index]["_skills"] = [{'Skill': 2, 'Level': 3},
                                                                          {'Skill': 12, 'Level': 9},
                                                                          {'Skill': 8, 'Level': 3},
                                                                          {'Skill': 5, 'Level': 3},
                                                                          {'Skill': 40, 'Level': 2},
                                                                          {'Skill': 11, 'Level': 3},
                                                                          {'Skill': 10, 'Level': 3},
                                                                          {'Skill': 39, 'Level': 3},
                                                                          {'Skill': 25, 'Level': 3},
                                                                          {'Skill': 15, 'Level': 2},
                                                                          {'Skill': 9, 'Level': 3},
                                                                          {'Skill': 7, 'Level': 3}]


class UI:
    """
    A simple console interface for the user to select cheats
    """

    def print_banner():
        """
        Welcome banner
        """
        print("")
        print("          .d88b.       .d88b             ")
        print("          YPwww. .d8b. 8P                ")
        print("  wwww        d8 8' .8 8b       wwww     ")
        print("          `Y88P' `Y8P' `Y88P             ")
        print("                                       ")
        print("  .d88b 8   8 8888    db    88888 .d88b. ")
        print("  8P    8www8 8www   dPYb     8   YPwww. ")
        print("  8b    8   8 8     dPwwYb    8       d8 ")
        print("  `Y88P 8   8 8888 dP    Yb   8   `Y88P' ")

    def map_menu():
        print("TODO: come back later\n")

    def player_menu():
        print("TODO: come back later\n")

    def hero_menu(gamestate):
        """
        For manipulating hero values
        """
        while True:
            print("Available heros: ")
            all_heros = Cheat.CommanderManipulation.get_all_heros(gamestate)
            print(all_heros)
            print("Which hero do you want to manipulate? Enter the ID")
            hero_id = input("> ")
            if int(hero_id) not in all_heros.values():
                print("ERROR: ID not found!\n")
                return

            print("\nOptions: [1] Make Overpowered, [2] Back to Main Menu")
            selection = input("> ")

            if selection == "1":
                Cheat.CommanderManipulation.make_overpowered(gamestate, hero_id)
                print(f"Set all values the max for hero {all_heros[hero_id]}")
            elif selection == "2":
                return
            else:
                print("Undefined input! Try again\n")

    def quitting():  # can't call it quit because that name is reserved
        """
        Shuts down the script
        """
        print("Quitting...")
        print("Thank you for using this script")
        sys.exit()

    def main_menu(gamestate):
        """
        Main menu to choose sub menus from
        :param gamestate: the state of the save
        """
        while True:
            print("Options: [1] Map Manipulation, [2] Player Manipulation, [3] Hero Manipulation, [4] Quit")
            selection = input("> ")

            if selection == "1":
                UI.map_menu()
            elif selection == "2":
                UI.player_menu()
            elif selection == "3":
                UI.hero_menu(gamestate)
            elif selection == "4":
                UI.quitting()
            else:
                print("Undefined input! Try again\n")


if __name__ == '__main__':
    print(f"called with {len(sys.argv) - 1} arguments: {sys.argv[1:]}")

    if len(sys.argv) < 4:
        print("ERROR: expected 3 arguments!\n"
              " - Save game folder (usually C:/Users/<USER>/AppData/LocalLow/Lavapotion/SongsOfConquest/Savegames),\n"
              " - input file name (something like mysave.sav),\n"
              " - output file name (something like mysave-cheated.sav)")
    else:
        UI.print_banner()

        folder = sys.argv[1]
        in_file = sys.argv[2]
        out_file = sys.argv[3]

        print(f"\n\nLoading file {os.path.join(folder, in_file)} ...")
        gamestate = GameState()
        gamestate.load_from_file(os.path.join(folder, in_file))
        print("successful!\n")

        UI.main_menu(gamestate)

        print(Cheat.CommanderManipulation.get_all_heros(gamestate))

        # Cheat.MapManipulation.set_water_level(gamestate, 0)
        # Cheat.MapManipulation.set_road_level(gamestate, 0)
        # Cheat.MapManipulation.set_elevation_level(gamestate, 0)
        # Cheat.MapManipulation.set_theme_level(gamestate, 0)

        Cheat.PlayerManipulation.set_resource_count(gamestate, 0, 0, 100)
        # Cheat.PlayerManipulation.set_alive(gamestate, 0, False)

        Cheat.CommanderManipulation.make_overpowered(gamestate, 22)
        Cheat.PlayerManipulation.make_overpowered(gamestate, 0)
        Cheat.MapManipulation.scramble_map(gamestate)

        gamestate.save_to_file(os.path.join(folder, out_file))
