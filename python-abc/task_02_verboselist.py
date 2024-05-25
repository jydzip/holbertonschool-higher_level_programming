#!/usr/bin/python3


class VerboseList(list):
    def append(self, el):
        print(f"Added [{el}] to the list.")
        super().append(el)

    def extend(self, els):
        print(f"Extended the list with [{len(els)}] items.")
        super().extend(els)

    def remove(self, el):
        print(f"Removed [{el}] from the list.")
        super().remove(el)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        super().pop(index)
