function [c] = leadzero(v)
%Returns number of zeros at the start of v
c = 0;
for i = v
    if i == 0
        c = c+1;
    else 
        return
    end
end
end