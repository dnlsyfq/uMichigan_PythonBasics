def computepay(h, r):
    if h <= 40:
        return h * r 
    else:
        return (40 * r) + ((h - 40) * (r * 1.5))

hrs = input("Enter Hours:")
r = input("Enter Rate: ")
p = computepay(float(hrs), float(r))
print("Pay", p)
