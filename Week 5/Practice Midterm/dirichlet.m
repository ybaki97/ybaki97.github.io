function [p] = dirichlet(a,s)
n = 0;
while ~isprime(a + s*n)
    disp(a + s*n)
    n = n + 1;
end
p = a + s*n;