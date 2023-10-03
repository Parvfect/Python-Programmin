
""" Given s indice convert to 3D coordinates. Input three dimensions length and index """


index = int(input("Enter index"))

first_dim_length = int(input("Enter first dimension length"))
second_dim_length = int(input("Enter second dimension length"))
third_dim_length = int(input("Enter third dimension length"))


dim1, dim2, dim3 = 0, 0, 0

while True:

    index -= third_dim_length
    dim2+=1

    if dim3 == third_dim_length:
        dim3 == 0
        dim2 += 1
        if dim2 == second_dim_length:
            dim2 = 0
            dim1 += 1

    if index <= third_dim_length:
        break

dim3 += index
if dim3 == third_dim_length:
        dim3 == 0
        dim2 += 1
        if dim2 == second_dim_length:
            dim2 = 0
            dim1 += 1


print("Three coordinate index is ({},{},{})".format(dim1, dim2, dim3))


