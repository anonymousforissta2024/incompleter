#Source: https://stackoverflow.com/questions/53549356/trying-to-write-file-to-my-working-directory-error-typeerror-expected-str-by
# Read both text files and join them together
if os.path.exists('list1.txt'):
    with open('list1.txt') as f:
        list1 = f.read().splitlines()
        f.close()

if os.path.exists('list2.txt'):
    with open('list2.txt') as f:
        list2 = f.read().splitlines()
        f.close()

# Combine these into a MASTERLIST
MASTERLIST = list1 + list2

# Remove duplicates
MASTERLIST = list(set(MASTERLIST))
print('\n\n[+] MASTERLIST created!\n')
with open(MASTERLIST, "w") as f:
    f.write('../conf/ignore.txt')