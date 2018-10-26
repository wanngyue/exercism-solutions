from string import ascii_uppercase as letters


def make_diamond(letter):
    N = letters.find(letter)
    rows =[]
    for i,c in enumerate(letters[:N+1]):
        row = [' ']*(2*N+1)
        row[N+i]=row[N-i]=c
        rows.append(''.join(row))
    rows.extend(reversed(rows[:N]))
    return '\n'.join(rows)+'\n'
