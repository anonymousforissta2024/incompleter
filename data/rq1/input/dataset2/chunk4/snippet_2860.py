#Source: https://stackoverflow.com/questions/70395860/how-to-fix-typeerror-a-bytes-like-object-is-required-not-str
lines = subprocess.check_output(
    [
        "git",
        "log",
        "--all",
        "--no-merges",
        "--shortstat",
        "--reverse",
        "--pretty=format:'%ad;%an'",
    ]
).splitlines()

for line in lines:
    print(line)
    if "file changed" in line or "files changed" in line:
        print("do something")