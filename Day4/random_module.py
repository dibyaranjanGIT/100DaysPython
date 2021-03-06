# >>> random()                             # Random float:  0.0 <= x < 1.0
# 0.37444887175646646
#
# >>> uniform(2.5, 10.0)                   # Random float:  2.5 <= x <= 10.0
# 3.1800146073117523
# 
# >>> expovariate(1 / 5)                   # Interval between arrivals averaging 5 seconds
# 5.148957571865031
#
# >>> randrange(10)                        # Integer from 0 to 9 inclusive
# 7
#
# >>> randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
# 26
#
# >>> choice(['win', 'lose', 'draw'])      # Single random element from a sequence
# 'draw'
#
# >>> deck = 'ace two three four'.split()
# >>> shuffle(deck)                        # Shuffle a list
# >>> deck
# ['four', 'two', 'ace', 'three']
#
# >>> sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement
# [40, 10, 50, 30]