 %%
 figure(1);
 colormap('jet');
 [theta, r] = meshgrid (linspace(0,2*pi,128), linspace(0,1,128));
 [X, Y] = pol2cart(theta, r);
 sigma_range = linspace(0,1000,100000000);
 for sigma = 0:0.05:1000
     clf(1);
     Z = sin(2*pi*(X.*Y + sigma));
     contourf(X, Y, abs (Z), 10);
     drawnow
 end
 %title ({'contour() plot'; 'polar fcn: Z = sin (2*theta) * (1-r)'});
 %%