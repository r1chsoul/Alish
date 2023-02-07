import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def main():
    X = (x1, x2, x3) = tuple(map(int, input("Coordinates of X: ").split()))
    Y = (y1, y2, y3) = tuple(map(int, input("Coordinates of Y: ").split()))
    Z = (z1, z2, z3) = tuple(map(int, input("Coordinates of Z: ").split()))
    T = (t1, t2, t3) = tuple(map(int, input("Coordinates of T: ").split()))

    d_xy = distance(*X, *Y)
    d_xz = distance(*X, *Z)
    d_xt = distance(*X, *T)
    d_yz = distance(*Y, *Z)
    d_yt = distance(*Y, *T)
    d_zt = distance(*Z, *T)

    min_dist = min(d_xy, d_xz, d_xt, d_yz, d_yt, d_zt)
    print("Minimalnaya distancia:", min_dist)

if __name__ == "__main__":
    main()