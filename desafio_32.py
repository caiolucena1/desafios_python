# URI 1828
from datetime import timedelta


winner = 'Bazinga!'
loser = 'Raj trapaceou!'
tied = 'De novo!'

rules = {
    'tesoura':{
        'papel': winner,
        'Spock': loser,
        'tesoura': tied,
        'lagarto': winner,
        'pedra': loser
    },
    'papel':{
        'papel': tied,
        'Spock': winner,
        'tesoura': loser,
        'lagarto': loser,
        'pedra': winner
    },
    'pedra':{
        'papel': loser,
        'Spock': loser,
        'tesoura': winner,
        'lagarto': winner,
        'pedra': tied
    },
    'lagarto':{
        'papel': winner,
        'Spock': winner,
        'tesoura': loser,
        'lagarto': tied,
        'pedra': loser
    },
    'Spock':{
        'papel': loser,
        'Spock': tied,
        'tesoura': winner,
        'lagarto': loser,
        'pedra': winner
    }
}

entry = int(input())

for i in range(entry):
    sheldon, raj = input().split()
    result = rules[sheldon][raj]
    print(f'Caso #{i+1}: {result}')

