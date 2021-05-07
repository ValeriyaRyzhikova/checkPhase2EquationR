from sympy import *

N = symbols("N", integer=True, positive=True)
n1, n2 = symbols("n1 n2", integer=True, nonnegative=True)
m1, m2, r1, q, l, x = symbols("m1 m2 r1 q l x", positive=True)
def R(k1, k2):
    c = factorial(N)/factorial(k1+k2)*binomial(k1+k2, k1)
    return c*(m1*m2*(1-r1))**(N-k1-k2)*(m1*(1-q))**k2*(m2*q)**k1*(l+x)**(k1+k2)

simplify(-(l+x)*R(0,0)+m1*(1-r1)*R(1,0)+m2*(1-r1)*R(0,1))


A1=(-(l+n2*m2+x) + n2*m2*r1*(1-q))
A2=(1-q)*(l+x)
A3=(1-r1)*m1
A4=(1-r1)*m2*(n2+1)
A5=r1*m1*(1-q)
simplify(A1*R(0,n2)+A2*R(0, n2-1)+A3*R(1,n2)+A4*R(0,n2+1)+A5*R(1, n2 -1))


B1=(-(l+n1*m1+x) + n1*m1*r1*q)
B2=q*(l+x)
B3=(1-r1)*m2
B4=(1-r1)*m1*(n1+1)
B5=r1*m2*q
simplify(R(n1,0)*B1+R(n1-1, 0)*B2+R(n1, 1)*B3+R(n1+1,0)*B4+R(n1-1, 1)*B5)


C1=(-(l+n1*m1+n2*m2+x)+n1*m1*r1*q + n2*m2*r1*(1-q))
C2=q*(l+x)
C3=(1-q)*(l+x)
C4=(1-r1)*m1*(n1+1)
C5=(1-r1)*m2*(n2+1)
C6=r1*(n1+1)*m1*(1-q)
C7=r1*(n2+1)*m2*q
simplify(C1*R(n1,n2)+C2*R(n1-1,n2)+C3*R(n1, n2-1)+C4*R(n1+1,n2)+C5*R(n1,n2+1)+C6*R(n1+1, n2 -1)+C7*R(n1-1, n2+1))

D1=(-N*m2+ N*m2*r1*(1-q))
D2=(1-q)*(l+x)
D3=m1*r1*(1-q)
simplify(D1*R(0,N)+D2*R(0, N-1)+D3*R(1,N-1))
#(m1*q*(m1*(1-q))**(N - 1)*(l + x)**N - m1*(m1*(1-q))**(N - 1)*(l + x)**N + (m1*(1-q)*(l+x))**N)
#(m1*(1-q))**(N - 1)*(l + x)**N*(m1*q - m1) + (m1*(1-q)*(l+x))**N
#-(m1*(1-q))**N*(l + x)**N + (m1*(1-q)*(l+x))**N
#0

E1=(-N*m1+ N*m1*r1*q)
E2=q*(l+x)
E3=m2*r1*q
simplify(E1*R(N,0)+E2*R(N-1, 0)+E3*R(N-1,1))

F1=(-(n1*m1+n2*m2)+n1*m1*r1*q+n2*m2*r1*(1-q))
F2=q*(l+x)
F3= (1-q)*(l+x)
F4= (n1+1)*m1*r1*(1-q)
F5=(n2+1)*m2*r1*q
simplify(F1*R(n1,n2)+F2*R(n1-1, n2)+F3*R(n1, n2-1)+F4*R(n1+1, n2-1)+F5*R(n1-1, n2+1))