# 1 / 9801 = ?
i = 0;
A = 0;
a = 1;
b = 9801;
while(i < 202):
    A = a / b;
    if(A != 0):
        a = a - A * b;
    a = a * 10;
    print A;
    # i++ -> SyntaxError: invalid syntax
    i = i + 1;
# -> Comment -> '//' is SyntaxError: invalid syntax
# python c043005.py > c043005.txt
