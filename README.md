# Songs of Conquest - Save file editor

A simple edit script for manipulating values in your save files for the game Songs of Conquest.

_**WORK IN PROGRESS!**_

The script is functional but lacks core features.
It can be seen as more of a proof of work.
If you know how to code, feel free to poke around in the code and see what you can do.
Pull requests and feature requests are always welcome.

## Features
- load, manipulate and save .sav files
- simple console menu to pick cheats
- Level cheats:
  - change elevations
  - change water levels
  - change roads
- Player cheats:
  - change resource values (Gold, wood, etc...)
  - make overpowered (= increase spawn rates and buildings per base)
- Hero cheats:
  - change stats like offense and defense
  - change stats like movement and view distance
  - set level and skill points
  - make overpowered (= incredible stats and level)

## How to run
Open a console in the folder where you have the script.
Call the script
```commandline
python  python soc_cheat.py C:/Users/<USER>/AppData/LocalLow/Lavapotion/SongsOfConquest/Savegames cheat-test.sav cheat-test-2.sav
```
The parameters behind the script name will define the following:
- Save game folder (usually C:/Users/USER/AppData/LocalLow/Lavapotion/SongsOfConquest/Savegames)
- input file name (something like mysave.sav)
- output file name (something like mysave-cheated.sav)

The input file name can be equal to the output file name, but it would make sense to have different file names just so you have a backup.

## Installation
No installation necessary!
Just download the script and run it.
This will need a version of python 3 to be installed though.