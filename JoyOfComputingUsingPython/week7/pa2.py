queue = []

while True:
    operation = input().split(',')
    if operation[0] == 'JOIN':
        token = int(operation[1])
        queue.append(token)
    elif operation[0] == 'LEAVE':
        if queue:
            queue.pop(0)
    elif operation[0] == 'MOVE':
        token = int(operation[1])
        position = operation[2]
        if token in queue:
            queue.remove(token)
            if position == 'HEAD':
                queue.insert(0, token)
            elif position == 'TAIL':
                queue.append(token)
    elif operation[0] == 'PRINT':
        print(','.join(map(str, queue)))
    elif operation[0] == 'END':
        break
