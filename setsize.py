import ctypes
import argparse

def ResizeWindow(windowName, cx, cy, x=0, y=0):
    hWnd = ctypes.windll.user32.FindWindowA(0, windowName)
    print cx
    print cy
    if (x==-1 and y==-1):
        print cx
        print cy
        ctypes.windll.user32.SetWindowPos(hWnd, 0, x, y, cx, cy, 2) #handle, hWndInsertAfter, xpos, ypos, width, height, SWP_NOMOVE
    else:
        ctypes.windll.user32.SetWindowPos(hWnd, 0, x, y, cx, cy, 0) #handle, hWndInsertAfter, xpos, ypos, width, height

def ParseFile(filename):
    f = open(filename)
    size = f.readlines()
    f.close()
    
    size_dict = {}
    for line in size:
        size_dict[line.split(":")[0]] = int(line.split(":")[1].strip("\r").strip("\n"))
    print size_dict
    return size_dict
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Window Name", default="Untitled - Notepad")
    parser.add_argument("-f", "--file", help="File Name", default="size.txt")
    
    args = parser.parse_args()
    
    size_dict = ParseFile(args.file)
    ResizeWindow(args.name, size_dict["width"], size_dict["height"], size_dict["x"], size_dict["y"])