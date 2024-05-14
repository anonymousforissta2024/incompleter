for row in zip(*([key] + value for key, value in sorted(my_dict.items()))):
    print(*row)