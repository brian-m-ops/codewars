import re


def validate_pin(pin):
    if re.findall("\D", pin):
        return False

    if re.findall("[0-9]{4}", pin) and len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False

# Better way
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()