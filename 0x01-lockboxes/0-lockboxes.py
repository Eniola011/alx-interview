#!usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    """
    opened_boxes = set()
    opened_boxes.add(0)
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    return len(opened_boxes) == len(boxes)