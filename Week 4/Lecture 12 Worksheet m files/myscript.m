clear;
s = 0;
t = 0;
for i = 1:10000
    v = rwalk(10,55);
    t = t + length(v);
    if v(end) == 10;
        s = s+1;
    end 
end 
p10 = s/10000;
e10 = t/10000;
s = 0;
t = 0;
for i = 1:10000
    v = rwalk(30,55);
    t = t + length(v);
    if v(end) == 10;
        s = s+1;
    end 
p30 = s/10000;
e30 = t/10000;
end 
 