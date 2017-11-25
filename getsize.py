import ctypes
import argparse

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), 
                ("right", ctypes.c_long), ("bottom", ctypes.c_long)]


def GetWindowSize(windowName):
    hWnd = ctypes.windll.user32.FindWindowA(0, windowName)
    
    windowSizeRect = RECT()
    
    ctypes.windll.user32.GetWindowRect(hWnd, ctypes.pointer(windowSizeRect))
    
    size = [windowSizeRect.left, windowSizeRect.top, windowSizeRect.right-windowSizeRect.left, windowSizeRect.bottom-windowSizeRect.top]
    return size

def WriteSizeToFile(size, filename):
    f = open(filename, 'wb')
    f.write("x:" + str(size[0]) + "\r\n" +
            "y:" + str(size[1]) + "\r\n" +
            "width:" + str(size[2]) + "\r\n" +
            "height:" + str(size[3]))
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Window Name", default="Untitled - Notepad")
    parser.add_argument("-f", "--file", help="File Name", default="size.txt")
    args = parser.parse_args()
    
    size = GetWindowSize(args.name)
    
    WriteSizeToFile(size, args.file)