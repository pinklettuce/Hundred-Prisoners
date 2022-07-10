#! /usr/bin/env python3
import sys
import math
import random

class game:
    def __init__(self):
        self.players = int(sys.argv[1])
        self.num_log = []

    def gen_containers(self):
        self.containers = {}
        for i in range(1, self.players+1):
            self.containers["Box-%s"%str(i)] = str(self.gen_slip())
    
    def gen_slip(self):
        try:
            while num in self.num_log:
                num = random.randint(1,100)
            self.num_log += [num]
            return num
        except:
            num = random.randint(1,100)
            self.num_log+= [num]
            return num
            


def main():
    test=game()
    test.gen_containers()
    containers = test.containers
    player = [None] * int(test.players)
    for i in range(1,101):
        player[i],l = {'opened': 0, 'found': False},[]
        while player[i]['opened'] < int(test.players/2):
            selected = input("Player-%i Select a box number: "%(i))
            if str(i) == containers["Box-%s"%selected]:
                player[i]['opened'] += 1
                player[i]['found'] = True
                print("YOU FOUND IT!!")
                break
            else:
                print("Result: ",containers["Box-%s"%selected])
                print("YOU HAVE %s TRIES LEFT!"%(str(50 - player[i]['opened'])))
                print("Nums Tried: %s"%l)
                l+=[containers["Box-%s"%selected]]
                player[i]['opened'] += 1

if __name__ == '__main__':
    main()
