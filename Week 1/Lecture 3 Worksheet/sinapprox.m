x1 = linspace(-6,6,1000);
x2 = -6:0.5:6;
y1 = sin(x1);
y2 = x2 - 1/6*x2.^3;
plot(x1,y1,'b',x2,y2,'r.-')
legend("sin(x)", "x-1/6x^3")
xlabel("x")
title("A plot of sin(x) and an approximation")
axis([-6,6,-7,7])
grid on