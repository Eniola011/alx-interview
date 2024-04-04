#!/usr/bin/python3
"""
UTF-8 encoding
"""


def validUTF8(data):
    """
        A method that determines if a given data set
        represents a valid UTF-8 encoding.
    """
    def check_continuation_bytes(start_index, count):
        for i in range(start_index + 1, start_index + count + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        leading_byte = data[i]
        if (leading_byte >> 7) == 0:  # Single-byte character
            i += 1
        elif (leading_byte >> 5) == 0b110:  # Two-byte character
            if not check_continuation_bytes(i, 1):
                return False
            i += 2
        elif (leading_byte >> 4) == 0b1110:  # Three-byte character
            if not check_continuation_bytes(i, 2):
                return False
            i += 3
        elif (leading_byte >> 3) == 0b11110:  # Four-byte character
            if not check_continuation_bytes(i, 3):
                return False
            i += 4
        else:  # Invalid leading byte
            return False
    return True
