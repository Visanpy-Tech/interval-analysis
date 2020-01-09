# Interval analysis

In this project, a class for representing intervals is implemented as well as basic arithmetic operations on them.  
Four basic arithmetic operators that were implemented:
1) addition --> [a, b] + [c, d] = [a + c, b + d],
2) subtraction --> [a, b] − [c, d] = [a − d, b − c],
3) multiplication --> [a, b] · [c, d] = [min(ac, ad, bc, bd), max(ac, ad, bc, bd)],
4) divison --> [a, b] / [c, d] = [min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d)]

Besides these basic arithmetic operations,  the power functions of intervals [a, b]^n is implemented as well. 
If n is odd, power function is implemented as follows:
[a, b]^n = [a^n, b^n]

If n is even, we have:
[a, b]^n = [a^n, b^n] for a>=0;
[a, b]^n = [b^n, a^n] for b<0;
[a, b]^n = [0, max(a^n, b^n)] othervise.

