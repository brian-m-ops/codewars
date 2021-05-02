def abbrev_name(name):
    return ".".join(word[0].capitalize() for word in name.split(" "))
