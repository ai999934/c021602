# External reference https://twitter.com/funmath_bot/status/255638822438703106
# 1 / 9801 = ?
i = 0;
A = 0;
a = 1;
b = 9801;
while(i < 203):
    A = a / b;
    if(A != 0):
        a = a - A * b;
    a = a * 10;
    print A;
    i = i + 1;
    # i++ -> SyntaxError: invalid syntax
# -> comment -> '//' is SyntaxError: invalid syntax
# python c043006.py > c043006.txt
