function [b] = wrand(w)
%w is a number between 0 and 100
%Returns 1 with probability w and -1 with probability 1-w
x = rand(1);
if x <= w*10^-2
    b = 1;
else 
    b = -1;
end
end