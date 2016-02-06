#find the pythagorean triplet that a^2 + b^2 + c^2 = 1000

#just gonna do a nested for loop for this and brute force it
#it works, it's just slow as hell

def is_triplet(a, b, c):
    if (a < b and b < c):
        return True
    else:
        return False

for a in range(0, 999):
    for b in range(0, 999):
        for c in range(0, 999):
            if is_triplet(a, b, c):
                if a*a + b*b == c*c:
                    if (a+b+c == 1000):
                        print(a*b*c)
                        break