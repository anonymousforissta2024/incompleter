def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2) / 2
    return list_of_dicts
print(sum_math_v_vi_average(student_details))