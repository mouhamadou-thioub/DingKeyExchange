
from cmath import exp
from math import pi

# A simple class to simulate n-th root of unity
# This class is by no means complete and is implemented
# merely for FFT and FPM algorithms
class NthRootOfUnity:
    def __init__(self, n, k = 1):
        self.k = k
        self.n = n

    def __pow__(self, other):
        if type(other) is int:
            n = NthRootOfUnity(self.n, self.k * other)
            return n

    def __eq__(self, other):
        if other == 1:
            return abs(self.n) == abs(self.k)

    def __mul__(self, other):
        return exp(2*1j*pi*self.k/self.n)*other

    def __repr__(self):
        return str(self.n) + "-th root of unity to the " + str(self.k)

    @property
    def th(self):
        return abs(self.n // self.k)


# The Fast Fourier Transform Algorithm
#
# Input: A, An array of integers of size n representing a polynomial
#        omega, a root of unity
# Output: [A(omega), A(omega^2), ..., A(omega^(n-1))]
# Complexity: O(n logn)
def FFT(A, omega):
    if omega == 1:
        return [sum(A)]
    B = [[],[]]
    i = 0
    for a in A:
        B[i%2].append(a)
        i+=1
    o2 = omega**2
    C1 = FFT(B[0], o2)
    C2 = FFT(B[1], o2)
    C3 = [None]*omega.th
    for i in range(omega.th//2):
        C3[i] = C1[i] + omega**i * C2[i]
        C3[i+omega.th//2] = C1[i] - omega**i * C2[i]
    return C3

# The Fast Polynomial Multiplication Algorithm
#
# Input: A,B, two arrays of integers representing polynomials
#        their length is in O(n)
# Output: Coefficient representation of AB
# Complexity: O(n logn)
def FPM(A,B):
    n = 1<<(len(A)+len(B)-2).bit_length()
    o = NthRootOfUnity(n)
    AT = FFT(A, o)
    BT = FFT(B, o)
    C = [AT[i]*BT[i] for i in range(n)]
    nm = (len(A)+len(B)-1)
    D = [int((a/n).real) for a in FFT(C, o ** -1)]
    while True:
        if D[-1] != 0:
            return D
        else:
            del D[-1]
