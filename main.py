from sympy import *

N = symbols("N", integer=True, positive=True)
n1, n2 = symbols("n1 n2", integer=True, nonnegative=True)
m1, m2, r1, q, l, x = symbols("m1 m2 r1 q l x", positive=True)
def R(k1, k2):
    c = factorial(N)/factorial(k1+k2)*binomial(k1+k2, k1)
    return c*(m1*m2*(1-r1))**(N-k1-k2)*(m1*(1-q))**k2*(m2*q)**k1*(l+x)**(k1+k2)

simplify(-R(0,0)*(l+x)+R(1,0)*m1*(1-r1)+R(0,1)*m2*(1-r1))


K1=R(0,n2)*(-(l+n2*m2+x) + n2*m2*r1*(1-q))
K2=R(0, n2-1)*(1-q)*(l+x)
K3=R(1,n2)*(1-r1)*m1
K4=R(0,n2+1)*(1-r1)*m2*(n2+1)
K5=r1*m1*(1-q)*R(1, n2 -1)
simplify(K1+K2+K3+K4+K5)


K1=R(n1,0)*(-(l+n1*m1+x) + n1*m1*r1*q)
K2=R(n1-1, 0)*q*(l+x)
K3=R(n1, 1)*(1-r1)*m2
K4=R(n1+1,0)*(1-r1)*m1*(n1+1)
K5=r1*m2*q*R(1, n2 -1)
simplify(K1+K2+K3+K4+K5)


K1=R(n1,n2)*(-(l+n1*m1+n2*m2+x)+n1*m1*r1*q + n2*m2*r1*(1-q))
K2=R(n1-1,n2)*q*(l+x)
K3=R(n1, n2-1)*(1-q)*(l+x)
K4=R(n1+1,n2)*(1-r1)*m1*(n1+1)
K5=R(n1,n2+1)*(1-r1)*m2*(n2+1)
K6=r1*((n1+1)*m1*(1-q)*R(n1+1, n2 -1)+(n2+1)*m2*q*R(n1-1, n2+1))
simplify(K1+K2+K3+K4+K5+K6)

B1=R(0,N)*(-N*m2+ N*m2*r1*(1-q))
B2=R(0, N-1)*(1-q)*(l+x)
B3=m1*r1*(1-q)*R(1,N-1)
simplify(B1+B2+B3)
(m1*q*(m1*(1-q))**(N - 1)*(l + x)**N - m1*(m1*(1-q))**(N - 1)*(l + x)**N + (m1*(1-q)*(l+x))**N)
(m1*(1-q))**(N - 1)*(l + x)**N*(m1*q - m1) + (m1*(1-q)*(l+x))**N
-(m1*(1-q))**N*(l + x)**N + (m1*(1-q)*(l+x))**N
0

B1=R(N,0)*(-N*m1+ N*m1*r1*q)
B2=R(N-1, 0)*q*(l+x)
B3=m2*r1*q*R(N-1,1)
simplify(B1+B2+B3)

B1=R(n1,n2)*(-(n1*m1+n2*m2)+n1*m1*r1*q+n2*m2*r1*(1-q))
B2=R(n1-1, n2)*q*(l+x)
B3= R(n1, n2-1)*(1-q)*(l+x)
B4= (n1+1)*m1*r1*(1-q)*R(n1+1, n2-1)
B5=(n2+1)*m2*r1*q*R(n1-1, n2+1)
simplify(B1+B2+B3+B4+B5)