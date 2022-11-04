function [v] = fibb(n)
v = [0,1];

for i = 2:n
    v = [v, v(end-1) + v(end)];
end