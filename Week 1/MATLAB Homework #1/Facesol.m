face = figure();
%Head
t1 = linspace(0,2*pi,1000);
x1 = cos(t1);
y1 = sin(t1);
%Left/right eyes
t2 = linspace(0,2*pi,10);
x2 = 0.1*cos(t2) - 0.5;
y2 = 0.1*sin(t2) + 0.5;

t3 = linspace(0,2*pi,10);
x3 = 0.1*cos(t2) + 0.5;
y3 = 0.1*sin(t2) + 0.5;

%Mouth
t4 = linspace(0,2*pi,100);
x4 = 0.75*cos(t4);
y4 = 0.15*sin(t4)-0.25;

plot(x1,y1,'b',x2,y2,'kx',x3,y3,'kx',x4,y4,'ro')
title("Face")
legend("Head","Left Eye","Right Eye","Mouth")
axis([-1.5,1.5,-1.5,1.5])

saveas(face,"face.png","png");