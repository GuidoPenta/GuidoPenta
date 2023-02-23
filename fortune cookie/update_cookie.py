import random
import time
from git import Repo
import os

# Opens the fortunes file and reads a random line
with open('./fortune_cookie/fortunes.cookie', encoding='utf-8') as f:
    lines = f.readlines()

random_line_number = random.randint(2, len(lines) - 1)
fortune = lines[random_line_number]
print('Today fortune is: ' + fortune)

# Replace the fortune cookie sentence in the README
with open('./README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('> '):
        lines[i] = '> 🥠 ' + fortune
    elif line.startswith('Last update:'):
        lines[i] = 'Last update: ' + time.ctime() + '\n'

with open('./README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# Commits the updated files
remote_url = os.getenv('REMOTE_URL')
repo = Repo(".")
repo.git.add(update=True)
repo.index.commit("Updated fortune cookie message")
origin = repo.remote(name='origin')
origin.set_url(remote_url)
origin.push("HEAD:main")
