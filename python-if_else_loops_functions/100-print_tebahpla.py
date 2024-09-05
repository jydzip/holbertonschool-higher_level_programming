#!/usr/bin/python3
for ascii_letter in range(122, 96, -1):
    print("{:s}".format(
        chr(
            ascii_letter - (0 if (ascii_letter % 2) == 0 else 32)
        )),
        end=""
    )
