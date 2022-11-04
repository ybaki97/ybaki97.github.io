function [c] = smallrange(v)
c = false;

if abs(max(v) - min(v)) < 1
    c = true;
end

end