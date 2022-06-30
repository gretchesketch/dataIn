def data_Analyst(input):
    if input % 3 == 0 and input % 7 == 0:
        return "DataAnalyst"
    if input % 3 == 0:
        return "data"
    if input % 7 == 0:
        return "analyst"
    return input


print(data_Analyst(21))

