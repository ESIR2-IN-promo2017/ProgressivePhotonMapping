#!/bin/sh

echo "SSIM R,SSIM G,SSIM B" > SSIM.results

for IMG in $(ls png_results_30mn | grep ".png")
do
    echo $IMG >> SSIM.results
    ../tests/parameters/code/SSIM/ssim_test.out rendererResult_VPL.png png_results_30mn/$IMG >> SSIM.results
done
