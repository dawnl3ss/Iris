def pascals_triangle(limit = 10):
    data = {0: {0: 0, 1: 1, 2: 0}}

    for i in range(0, limit):
        next = {}

        if i in data.keys():
            for j in data[i]:
                if j + 1 in data[i].keys():
                    next[i] = j + (j+1)
        print(next)

pascals_triangle(10)