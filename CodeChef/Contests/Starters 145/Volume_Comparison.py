https://www.codechef.com/problems/CABLE

def volume(A, B, C, X):
    v_cuboid = A * B * C
    v_cube = X ** 3
    
    if v_cuboid > v_cube:
        print("Cuboid")
    elif v_cuboid < v_cube:
        print("Cube")
    else:
        print("Equal")