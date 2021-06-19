def open_or_senior(data):
    result = []
    [result.append("Senior") if person[0] >= 55 and person[1] > 7 else result.append("Open") for person in data]
    return result

# Long way
# def open_or_senior(data):
# #     result = []
# #
# #     for person in data:
# #         if person[0] >= 55 and person[1] > 7:
# #             result.append("Senior")
# #         else:
# #             result.append("Open")
# #
# #     return result

