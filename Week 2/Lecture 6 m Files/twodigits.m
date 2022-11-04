function [x] = twodigits(y)
x = 0;
while x^3 - x - 1 <= y
    x = x + 0.01;
end

