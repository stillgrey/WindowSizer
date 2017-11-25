# WindowSizer
Quick scripts to get and set sizes of windows (Windows only)

Requires Python 2.7

The window resized is determined by the window title. This can be passed as a command line argument to setsize/getsize. If multiple windows share the same title you can't choose which one is resized (currently).

Run getsize.py to get the x and y positions of the top-left corner of the window as well as the width and height. This information is written to a file (default: size.txt).

The size file can be manually edited.

Run setsize.py to read from the file and set the window size/position. If x and y are set to -1 then the window position is ignored.