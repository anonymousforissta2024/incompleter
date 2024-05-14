#Source: https://stackoverflow.com/questions/65931348/nameerror-name-is-not-defined-only-for-test-case-2
for i in sys.stdin.readlines():
    lines = i.strip()
for j in range(3): 
    sys.stdout.write(lines + '\n')