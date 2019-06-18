import random, curses

s= curses.initscr()
curses.curs_set(0)
ht, wd = s.getmaxyx()
w= curses.newwin(ht, wd, 0, 0)
w.keypad(1)
w.timeout(100)

snkx= int(wd/3)
snky= int(ht/3)

snk= [ [snky, snkx], [snky, snkx-1], [snky, snkx-2] ]

food= [int(ht/2), int(wd/2)]
w.addch(food[0], food[1], curses.ACS_PI)

key= curses.KEY_RIGHT

while True:
    next_key= w.getch()
    key= key if next_key == -1 else next_key

    if snk[0][0] in [0,ht] or snk[0][1] in [0, wd] or snk[0][0] in snk[1:]:
        curses.endwin()
        quit()

    new_head =[snk[0][0], snk[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] +=1
    if key == curses.KEY_RIGHT:
        new_head[1] +=1
    if key == curses.KEY_LEFT:
        new_head[1] -=1
    if key == curses.KEY_UP:
        new_head[0] -=1

    snk.insert(1, new_head)
    if snk[0] == food:
        food= None
        while food is None:
            nf= [ random.randint(1, ht-1), random.randint(1, wd-1)  ]
            food= nf if nf not in snk else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail= snk.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snk[0][0], snk[0][1], curses.ACS_CKBOARD)
