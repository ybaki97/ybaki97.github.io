function [w] = replaceA(v,a)
w = [];
for x = v
    if x > a
        w = [w,x];
    else
        w = [w,0];
    end
end
end
