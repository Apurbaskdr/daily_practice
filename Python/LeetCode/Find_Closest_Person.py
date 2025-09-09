"""You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly."""


def Find_Closest_Person(x,y,z):
    dist_x=abs(z-x)
    dist_y=abs(z-y)
    if dist_x > dist_y:
        return 2
    elif dist_y > dist_x:
        return 1
    else:
        return 0
    



x = 1
y = 5
z = 7
res=Find_Closest_Person(x,y,z)
print (res)