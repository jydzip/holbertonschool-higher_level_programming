#!/usr/bin/python3
from os import open, close, write, O_WRONLY

if __name__ == "__main__":
    fd = open('/dev/stdout', O_WRONLY)
    write(fd, b"#pythoniscool\n")
    close(fd)
