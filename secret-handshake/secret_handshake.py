d = ['wink',
     'double blink',
     'close your eyes',
     'jump'
     ]

def handshake(code):
    l = [d[i] for i in range(4) if code & 1 << i]
    if code & 1 << 4:
        return list(reversed(l))
    return l


def secret_code(actions):
    l = [1 << d.index(action) for action in actions]
    if len(l) > 1 and l[1] < l[0]:
        l.append(1 << 4)
    return sum(l)
