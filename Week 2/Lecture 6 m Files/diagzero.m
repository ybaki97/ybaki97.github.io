function [A] = diagzero(n)
%Returns an nxn matrix with zeros along diagonal and 1s everywhere else
A = ones(n);
for i = 1:n
    A(i,i) = 0;
end
end