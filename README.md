# CitraRNG

RNG assistant developed with Python 3.9 and PySide6 for use with Pokémon XY v1.5, ORAS 1.4, and SM/USUM v1.2.

Last tested on Citra Canary 1928.

### Citra Setup

 1. Install the latest release of [Python 3.9](https://www.python.org/downloads/)
 2. Open a command prompt anywhere and type `pip install pyside6`
    * Note: If the command prompt says pip is not recognized then Python needs to be added to Path. The command prompt may also need to be ran in administrative mode.
 3. Download the latest release of [Citra](https://citra-emu.org/download/)
 4. Download the latest release of [CitraRNG](https://github.com/Admiral-Fish/CitraRNG/releases/latest) and copy all the `.py` files into `<your Citra directory>/scripting`
    * Note: If you are using XY or ORAS read the note below about the game patch
 5. Open Citra and your Pokemon game, and load your save file
 6. Double-click the `citrarng.py` file to run the script
 	  * Note: If this does not work then right click `citrarng.py` and select `Edit with IDLE`. Make sure that you open with Python 3.9 if you have both Python2 and Python3 installed. Then hit `F5` to run the script.
 
XY and ORAS require a patch to work. This does not modify the gamecode in anyway that would result in illegal pokemon. All it does is write the initial seed of the game to a unused part of memory that the script has access to later. You can read this [guide](https://pokemonrng.com/guides/tools/en/Using%20IPS%20Patches%20with%20Luma%20and%20Citra/) for information on how to setup the patch correctly.

## Credits
 
 * EverOddish for their [great example](https://github.com/EverOddish/PokeStreamer-Tools/) of how to use scripting in Citra
