% % clear;
% % %EO1
% % x = 11:30;
% x(2:2:end) = 4+(1:length(x(1:2:end)));
% y = ones(1,length(x));
% y(1:2:end) = 0;
% plot(x,y,'-o','LineWidth',2);
% axis([0,30,0,1]);
% %EO3 
% a = [0 1 2;2 1 0];
% b1 = a(1,1) < a(2,1);
% b2 = a(2,2) && a(2,3);
% b3 = a(1,1)+a(2,3)||a(2,2)-a(2,1);
% 
% %EO6
% d = 0;
% for i = 1:10000
%    if randsuit() == "diamonds"
%        d = d+1;
%    end
% end
% 
% p = d/10000;
% 
% %GOMa1
% A = 7*ones(10,10);
% A(3:8,3:8) = 0;
% A(5:6,5:6) = 3;

%GOMa2

% for i = 1:1000
%     if randsuit() == "diamonds"
%         d = d+1;
%     end
% end
% 
% p = d/1000;
% for j = 1:10
% t = tiledlayout(5,2);
% t.TileSpacing = 'compact';
% t.Padding = 'compact';
x = [0];
y = [0];
n = 100;
for i = 1:n
    x = [x, x(end) + randi([-1,1])];
    y = [y,y(end) + randi([-1,1])];
end 
    plot(x,y);

