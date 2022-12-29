C = input()

if C[0] == "A":
    if C[1] == "+":
        print("4.3")
    elif C[1] == "0":
        print("4.0")
    else:
        print("3.7")
elif C[0] == "B":
    if C[1] == "+":
        print("3.3")
    elif C[1] == "0":
        print("3.0")
    else:
        print("2.7")
elif C[0] == "C":
    if C[1] == "+":
        print("2.3")
    elif C[1] == "0":
        print("2.0")
    else:
        print("1.7")
elif C[0] == "D":
    if C[1] == "+":
        print("1.3")
    elif C[1] == "0":
        print("1.0")
    else:
        print("0.7")
else:
    print("0.0")