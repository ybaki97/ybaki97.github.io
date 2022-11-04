function [v] = count_heads(n)
v = [0,0];
for i = 1:n
if coin_flip() == "heads"
    v(1) = v(1)+1;
elseif coin_flip() == "tails"
    v(2) = v(2)+1;
end
end
end