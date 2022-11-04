function [s] = coin_flip( )
x = rand();
if x <= 0.51
    s = "heads";
elseif x > 0.51
    s = "tails";
end