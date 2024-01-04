#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    func = dir()
    for i in range(0, len(func)):
        if func[i][:2] != "__":
            print("{:s}".format(func[i]))
