#Source: https://stackoverflow.com/questions/74903021/typeerror-not-supported-between-instances-of-str-and-int
New_MS = 41313137
str_ms = str(New_MS)
n = 2
split_str_ms = [str_ms[i : i + n] for i in range(0, len(str_ms), n)]
ms_txt_list = [f"0x{d.ljust(2, '0')}" for d in split_str_ms]
p=(f"({','.join(ms_txt_list)})") 