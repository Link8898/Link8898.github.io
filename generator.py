import random

rn0i = random.randrange(0,10)
ra0i = random.randrange(0,10)
rv0i = random.randrange(0,10)
ra1i = random.randrange(0,10)
si = random.randrange(0,6)
mi = random.randrange(0,6)
ei = random.randrange(0,6)

rn0 = ""
ra0 = ""
rv0 = ""
ra1 = ""
rs = ""
rm = ""
re = ""

n0 = "spider"
n1 = "penguin"
n2 = "knight"
n3 = "wizard"
n4 = "monkey"
n5 = "demon"
n6 = "ghost"
n7 = "turtle"
n8 = "dog"
n9 = "cat"

a0 = "happy"
a1 = "sad"
a2 = "curious"
a3 = "strange"
a4 = "noisy"
a5 = "hilarious"
a6 = "unique"
a7 = "brave"
a8 = "heroic"
a9 = "silent"

v0 = "running"
v1 = "jumping"
v2 = "sleeping"
v3 = "climbing"
v4 = "flying"
v5 = "fighting"
v6 = "swimming"
v7 = "coding"
v8 = "programming"
v9 = "reading"

s0 = "Once upon a time, there was a"
s1 = "There once was a"
s2 = "I used to know a"
s3 = "Back in my day, there was a"
s4 = "There was an old tale about a"
s5 = "This is the legend of a"
m0 = " was very "
m1 = " used to be "
m2 = " was known to be really "
m3 = " was always "
m4 = " was usually "
m5 = " was mostly "
e0 = " and extremely awful at"
e1 = " and surprisingly good at"
e2 = " and really bored of"
e3 = " and tired of"
e4 = " and excellent at"
e5 = " and bad at"

if rn0i == 0:
    rn0 = n0
elif rn0i == 1:
    rn0 = n1
elif rn0i == 2:
    rn0 = n2
elif rn0i == 3:
    rn0 = n3
elif rn0i == 4:
    rn0 = n4
elif rn0i == 5:
    rn0 = n5
elif rn0i == 6:
    rn0 = n6
elif rn0i == 7:
    rn0 = n7
elif rn0i == 8:
    rn0 = n8
elif rn0i == 9:
    rn0 = n9

if ra0i == 0:
    ra0 = a0
elif ra0i == 1:
    ra0 = a1
elif ra0i == 2:
    ra0 = a2
elif ra0i == 3:
    ra0 = a3
elif ra0i == 4:
    ra0 = a4
elif ra0i == 5:
    ra0 = a5
elif ra0i == 6:
    ra0 = a6
elif ra0i == 7:
    ra0 = a7
elif ra0i == 8:
    ra0 = a8
elif ra0i == 9:
    ra0 = a9

if ra1i == 0:
    ra1 = a0
elif ra1i == 1:
    ra1 = a1
elif ra1i == 2:
    ra1 = a2
elif ra1i == 3:
    ra1 = a3
elif ra1i == 4:
    ra1 = a4
elif ra1i == 5:
    ra1 = a5
elif ra1i == 6:
    ra1 = a6
elif ra1i == 7:
    ra1 = a7
elif ra1i == 8:
    ra1 = a8
elif ra1i == 9:
    ra1 = a9

if rv0i == 0:
    rv0 = v0
elif rv0i == 1:
    rv0 = v1
elif rv0i == 2:
    rv0 = v2
elif rv0i == 3:
    rv0 = v3
elif rv0i == 4:
    rv0 = v4
elif rv0i == 5:
    rv0 = v5
elif rv0i == 6:
    rv0 = v6
elif rv0i == 7:
    rv0 = v7
elif rv0i == 8:
    rv0 = v8
elif rv0i == 9:
    rv0 = v9

if si == 0:
    rs = s0
elif si == 1:
    rs = s1
elif si == 2:
    rs = s2
elif si == 3:
    rs = s3
elif si == 4:
    rs = s4
elif si == 5:
    rs = s5

if mi == 0:
    rm = m0
elif mi == 1:
    rm = m1
elif mi == 2:
    rm = m2
elif mi == 3:
    rm = m3
elif mi == 4:
    rm = m4
elif mi == 5:
    rm = m5

if ei == 0:
    re = e0
elif ei == 1:
    re = e1
elif ei == 2:
    re = e2
elif ei == 3:
    re = e3
elif ei == 4:
    re = e4
elif ei == 5:
    re = e5

start = rs + " " + ra0 + " " + rn0 + "."
middle = " The " + rn0 + rm + ra1
end = re + " " + rv0 + "."
finalStory = start + middle + end
print(finalStory)