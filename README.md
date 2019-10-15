# CitraRNG

RNG assistant developed with Python 3.7 and pyside2 for use with Pokémon XY v1.5, ORAS 1.4, and SM/USUM v1.2. Support for XY and ORAS is WIP.

Last tested on Citra Canary 1492.

### Citra Setup

 1. Install the latest release of Python 3: https://www.python.org/downloads/
 2. Open a command prompt anywhere and type `pip install pyside2`
    * Note: If the command prompt says pip is not recognized then Python needs to be added to Path. The command prompt may also need to be ran in administrative mode.
 3. Download the latest release of Citra: https://citra-emu.org/download/
 4. Copy all the `.py` files in the `CitraRNG` folder of this repo into `<your Citra directory>/scripting`
 5. Open Citra and your Pokemon game, and load your save file
 6. Double-click the `main.py` file to run the script
 	  * Note: If this does not work then right click `main.py` and select `Edit with IDLE`. Make sure that you open with Python 3.7 if you have both Python2 and Python3 installed. Then hit `F5` to run the script.
 
 ## Known Issues
  * None currently. Please report problems by creating a Github Issue.
 
 ## Credits
 
 * EverOddish for their [great example](https://github.com/EverOddish/PokeStreamer-Tools/) of how to use scripting in Citra
