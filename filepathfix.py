import os

directory = os.fsencode("_build/features/notebooks")

skurk1 = "![png](C%3A/Users/KarlH/Dropbox/GitHubRepositories/Jupyter-Book-Showroom/_build/"
skurk2 = "C:\\Users\\KarlH\\Dropbox\\GitHubRepositories\\Jupyter-Book-Showroom\\content\\"

for filename in os.listdir(directory):
    if filename.endswith(b".md"):
        myfile = os.path.join(directory, filename)

        with open(myfile, "r") as f:
            lines = f.readlines()
        with open(myfile, "w") as f:
            for line in lines:
                if (skurk1 in line):
                    f.write(line.replace(skurk1, "![png](../../"))
                elif (skurk2 in line):
                    f.write(line.replace(skurk2, ""))
                else:
                    f.write(line)
        continue
    else:
        continue