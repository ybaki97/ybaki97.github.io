function [] = random_image_sol()
v = VideoWriter('myIndexed.mp4','MPEG-4');
v.FrameRate = 10;
open(v)
my_colors = [207, 255, 179;173, 226, 93;252, 236, 82;59, 112, 128;58, 87, 67]./255;
for i = 1:100
image(randi(5,10,10));
colormap(my_colors);
frame = getframe;
writeVideo(v,frame);
end
close(v)
end 


