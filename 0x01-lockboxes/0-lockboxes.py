#!/usr/bin/python3
"""
  LockBoxes
"""


def canUnlockAll(boxes):
    """
        A method that determines if all the boxes can be opened.
        Return True if all boxes can be opened, else return False
    """
    # first: what is in the box?
    opened_boxes = [0]
    for idx in opened_boxes:
        for box in boxes[idx]:
            if box < len(boxes):
                if box not in opened_boxes:
                    opened_boxes.append(box)
    # check the length of the opened boxes and all the boxes.
    if len(boxes) == len(opened_boxes):
        return True
    else:
        return False
