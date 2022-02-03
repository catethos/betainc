import numpy as np
cimport numpy as np
cimport cython
from cython.parallel import prange

cdef extern from "math.h":
    double lgamma(double x) nogil
    double exp(double x) nogil
    double log(double x) nogil
    double fabs(double x) nogil

cdef double STOP = 1.0e-8
cdef double TINY =  1.0e-30

@cython.cdivision(True)
cdef double incbeta(double a, double b, double x) nogil:
    # x cannot be greater than 1 or less than 0
    if (x<0.0) or (x>1.0):

        return 1.0/0.0 # return inf as inf is a double too :)

    if x > (a+1)/(a+b+2):
        return 1 - incbeta(b, a, 1-x)

    cdef double lbeta_ab = lgamma(a) + lgamma(b) - lgamma(a+b)
    cdef double front = exp(log(x)*a + log(1-x)*b - lbeta_ab) / a 

    cdef double f=1.0, c=1.0, d=0.0

    cdef int i, m
    cdef double numerator
    for i in range(200):
        m = i/2
        if i == 0:
            numerator = 1.0
        elif i%2 == 0:
            numerator = (m*(b-m)*x)/((a+2.0*m-1.0)*(a+2.0*m))
        else:
            numerator = -((a+m)*(a+b+m)*x)/((a+2.0*m)*(a+2.0*m+1))
        d = 1.0 + numerator * d
        if (fabs(d) < TINY):
            d = TINY
        d = 1.0/d 
        c = 1.0 + numerator / c
        if (fabs(c) < TINY):
            c = TINY
        f *= c*d

        if (fabs(1.0-c*d) < STOP):
            return front * (f - 1.0)
    
    return 1.0/0.0

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def betacdf(np.ndarray[np.double_t, ndim=1] xs, double p, double q):
    cdef int N = xs.shape[0]
    cdef int i = 0
    cdef np.ndarray[np.double_t, ndim=1] result = np.zeros(N)
    cdef double x
    for i in prange(N, nogil=True, num_threads=10):
        x = xs[i]
        result[i] += incbeta(p, q, x)
    return np.asarray(result)