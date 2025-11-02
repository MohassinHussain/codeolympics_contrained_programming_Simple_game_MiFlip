# MiFlip
# Constraints; 1. Variable limit to <= 3charcaters, 2. No external libraries, 3. A simple game

import random, os, time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def mkb(sz):
    sy = list("!@#$%&*+=?")
    brd = sy[: sz * sz // 2] * 2
    random.shuffle(brd)
    g = []
    for i in range(sz):
        g.append(brd[i * sz:(i + 1) * sz])
    return g

def mkm(sz):
    return [["#" for _ in range(sz)] for _ in range(sz)]

def dsp(g):
    for r in g:
        print(" ".join(r))
    print()

def fin(m):
    for r in m:
        if "#" in r:
            return False
    return True

def val(p, sz):
    if len(p) != 2: return False
    if not p[0].isdigit() or not p[1].isdigit(): return False
    x, y = int(p[0]), int(p[1])
    return 0 <= x < sz and 0 <= y < sz

def ply():
    sz = 4
    win = 0
    los = 0
    att = 0
    scr = 0

    while True:
        brd = mkb(sz)
        msk = mkm(sz)
        print("=== FLIPMIND+ ===\n")
        print("Find pairs. Input rowcol (ex: 01)")
        input("Press Enter to start...")
        while True:
            cls()
            print("=== FLIPMIND+ ===")
            print(f"Score:{scr}  Wins:{win}  Losses:{los}  Attempts:{att}\n")
            dsp(msk)
            if fin(msk):
                win += 1
                print(">>>>You found all pairs!<<<<<")
                print(f"Final Score: {scr}, Attempts: {att}")
                ch = input("Play again? (y/n): ").lower()
                if ch == 'y':
                    break
                else:
                    print("Thanks for playing!")
                    return

            p1 = input("Pick 1st (rc): ")
            if not val(p1, sz): continue
            x1, y1 = int(p1[0]), int(p1[1])
            if msk[x1][y1] != "#": continue
            msk[x1][y1] = brd[x1][y1]
            cls(); print(f"Score:{scr}  Wins:{win}  Losses:{los}  Attempts:{att}\n"); dsp(msk)

            p2 = input("Pick 2nd (rc): ")
            if not val(p2, sz):
                msk[x1][y1] = "#"; continue
            x2, y2 = int(p2[0]), int(p2[1])
            if (x1==x2 and y1==y2) or msk[x2][y2] != "#":
                msk[x1][y1] = "#"; continue
            msk[x2][y2] = brd[x2][y2]
            cls(); print(f"Score:{scr}  Wins:{win}  Losses:{los}  Attempts:{att}\n"); dsp(msk)
            time.sleep(1)

            att += 1
            if brd[x1][y1] == brd[x2][y2]:
                scr += 10
                print("======Match! +10 pts\n")
                time.sleep(0.8)
            else:
                los += 1
                print("------Wrong! Try again.\n")
                time.sleep(1)
                msk[x1][y1] = "#"
                msk[x2][y2] = "#"

        continue

if __name__ == "__main__":
    ply()
