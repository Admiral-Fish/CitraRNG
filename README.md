# CitraRNG

Work in progress RNG assistant developed with Python 3.7 and pyside2 for use with Pokémon Sun/Moon v1.2 and Pokémon Ultra Sun/Ultra Moon v1.2. 

For the time being there will be no support for X/Y or Omega Ruby/Alpha Sapphire.

### Citra Setup

 1. Install the latest release of Python 3: https://www.python.org/downloads/
 2. Open a command prompt and run `pip install pyzmq pyside2`
 3. Download the latest release of Citra: https://citra-emu.org/download/
 4. Copy the `CitraRNG` folder of this repo into `<your Citra directory>/scripting/CitraRNG`
 5. Make sure to also copy citra.py into the CitraRNG folder
	* Note: citra.py should be located in `<your Citra directory>/scripting/`
 6. Open Citra and your Gen 7 Pokemon ROM, and load your save file
 7. Double-click the `main.py` file to run the script
 	* Note: If this does not work then right click `main.py` and select `Edit with IDLE`. Make sure that you open with Python 3.7 if             you have both Python2 and Python3 installed. Then hit `F5` to run the script.
 
 ## Known Issues
  * None currently. Please report problems by creating a Github Issue.
 
 ## Credits
 
 * EverOddish for their [great example](https://github.com/EverOddish/PokeStreamer-Tools/) of how to use scripting in Citra
