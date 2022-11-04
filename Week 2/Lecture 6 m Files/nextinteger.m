function [n] = nextinteger(v)
% If m is the largest positive integer that appears in v returns m+1 if 
% every positive integer less than m also appears. Returns the smallest
% positive integer that does not appear otherwise.
% If no such positive integer exists returns 1
n = 1;

if sum(v <= 0) == length(v)
    return;

else 
    while sum(v == n) ~= 0
        
        n = n+1;
        
    end
    
end

end

