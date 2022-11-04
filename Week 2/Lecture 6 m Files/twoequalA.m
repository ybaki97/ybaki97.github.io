function [b] = twoequalA(v)

for i = 1:length(v)-1
    if v(i) == v(i + 1)
        b = true;

    else 
        b = false;
    end
end 

end