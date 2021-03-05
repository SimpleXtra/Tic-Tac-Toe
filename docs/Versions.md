# Versions Docs
As of version 2.0.0, there are two versions with slightly different displays. It depends on whether the program is running in a terminal or not. The program will be automatically configured to a version on startup.

## The New Version
This version is a new addition to update 2.0.0. If the program is running in a terminal, this is the version that you will see.

Below are the list of some differences with the old version.
- The board, the prompt, and other text displays are refreshed instead of printing repeatedly which creates a long line of text.
- The `Options` info are not displayed.
- The `Computer's move` will not be displayed to make the board update more seamless.

## The Old Version (Classic)
This is the version where the display is the same before version 2.0.0. If the program is not running in a terminal, this is the version that you will see.

The reason the Classic version exists is because some features such as display refresh doesn't work without running the program through a terminal. Some operating systems, such as Android, doesn't have a terminal. Because of this, the Classic version is made to be compatible to all running environments.

The main functions are still present in the Classic version, however features mentioned in the new version is not available in this version.