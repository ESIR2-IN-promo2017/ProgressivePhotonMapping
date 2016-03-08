close all;
clear;
clc;

refImg = imread('../data/cbox.png');

nbImg = 69;

ssims = zeros(nbImg,1);

for i = 1:nbImg
    i
    testImg = imread(['../data/' num2str(i)], 'png');
    ssims(i) = ssim(testImg, nbImg);
end

ssims