function [v] = rwalk(n,w)
%Weighted random walk where we end at a distance of n from origin 
% steps determined by wrand(w)
v = [0];

while abs(v(end)) ~= n
    v = [v,v(end) + wrand(w)];
end 

end