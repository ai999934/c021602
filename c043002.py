# 1 / 9801 = ?
i = 0;
A = 0;
a = 1;
b = 9801;
while(i < 202):
    A = a/ b;
    if(A != 0):
        a = a - A * b;
    a = a * 10;
    print A;
    # i++; SyntaxError: invalid syntax
    # Added
    i = i + 1;
# python c043002.py > c043002.txt
