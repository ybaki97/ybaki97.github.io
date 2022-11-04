function [s] = randsuit()
x = randi([-1,1]);
  if x < .25
      s = "clubs";
  elseif (.25 <= x) && (x < .5)
      s = "diamonds";
  elseif (.5 <= x) && (x < .75)
      s = "hearts";
  else
      s = "spades";
  end
end