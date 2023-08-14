from random import randint
from time import sleep
from operator import itemgetter

thrown = dict()
for c in range(1, 5):
    thrown[f'Player {c}'] = randint(1, 6)
ranking = list()
print('Drawn numbers: ')
for j, r in thrown.items():
    print(f'{j}: {r}')
    sleep(0.5)
print()
print('Ranking: ')
ranking = sorted(thrown.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º: {v[0]} with {v[1]}')
    sleep(0.5)
