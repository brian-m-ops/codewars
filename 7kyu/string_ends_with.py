def solution(string, ending):
    if not ending:
        return True
    else:
        return ending == string[-len(ending):]
