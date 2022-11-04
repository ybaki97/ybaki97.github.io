%@author Yasmeen Baki <ybaki@uci.edu>
%September 2022
%These are solutions to Lecture #2 Worksheet
function [v] = lecture2sol(n,i)
if i == 1
    v = ["Yasmeen Baki", "Peter Anteater"];
    
elseif i == 2    
    % This answer has been provided for you as an example.    
    % Most but not all of these answers will depend on n.    
    % Most answers will be longer than this.    
    v = 1:n;

elseif i == 3
    v = n:-1:1;
elseif i == 4
    v = linspace(-10,10,n);
elseif i == 5
    v = [0,ones(1,n)*5];
elseif i == 6
    v = [3:29,31:100];
elseif i == 7
    v = (-1).^(0:n-1);
elseif i == 8
    v = 1:2:(2*n+1);
    v = v.^2;
elseif i == 9
    w = n:-1:0;
    x = 1:n;
    v = [w,x];
elseif i == 10
    v = [abs(-n:n)];
    
elseif i == 11
    v = 10.^(0:7) + 1;
    
elseif i == 12
    v = 5.^(2:2:20);
    
elseif i == 13
    v = 2:5:n;
    
elseif i == 14
    v = 2:5:2+5*(n-1);
    
elseif i == 15
   v = linspace(1,1+(n-1)*9,10);
elseif i == 16
   v = 1:n;
   v(4:4:end) = [];
elseif i == 17
   v = 1:4:89;
   v(2:2:end) = -1*v(2:2:end);
elseif i == 18
    v = zeros(1,3*n);
    v(3:3:end) = 1;
    
end
end
