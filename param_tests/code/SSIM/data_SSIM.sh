#!/bin/sh

echo "SSIM R,SSIM G,SSIM B" > SSIM.results

for IMG in $(ls ../../data/ | grep -v cbox.png)
do
    echo $IMG
    ./ssim_test.out ../../data/cbox.png ../../data/$IMG >> SSIM.results
done
