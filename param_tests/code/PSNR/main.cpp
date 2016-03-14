/**
 * @file main.cpp
 * @author Amaury Louarn
 * @date 2016-03-04
 */
#include <iostream>
#include <string>
#include <thread>
#include <visp/vpImage.h>
#include <visp/vpImageIo.h>

void psnr(vpImage<vpRGBa> const& refImg, vpImage<vpRGBa> const& tstImg, double * psnrs, unsigned int const test_nbr);

double eqm(vpImage<vpRGBa> const& refImg, vpImage<vpRGBa> const& tstImg);

int main(int argc, char ** argv)
{
    unsigned int const nb_tests = 69;

    std::string const data_dir = "../data/";

    double psnrs[nb_tests];
    std::thread threadPool[nb_tests];

    vpImage<vpRGBa> refImg;
    vpImage<vpRGBa> tstImg;

    vpImageIo::read(refImg, data_dir+"cbox.png");

    for(unsigned int i = 0; i < nb_tests; ++i)
    {
        std::string filepath = data_dir;
        filepath += std::to_string(i+1) + ".png";
        vpImageIo::read(tstImg, filepath);
        threadPool[i] = std::thread(psnr, refImg, tstImg, psnrs, i);
    }

    for(unsigned int i = 0; i < nb_tests; ++i)
    {
        threadPool[i].join();
        std::cout << psnrs[i] << std::endl;
    }

    return EXIT_SUCCESS;
}

void psnr(vpImage<vpRGBa> const& refImg, vpImage<vpRGBa> const& tstImg, double * psnrs, unsigned int const test_nbr)
{
    unsigned int const dynamique = 255;

    psnrs[test_nbr] = 10*( log((dynamique*dynamique) / eqm(refImg, tstImg)) / log(10) );
}

double eqm(vpImage<vpRGBa> const& refImg, vpImage<vpRGBa> const& tstImg)
{
    unsigned int width = std::min(refImg.getWidth(), tstImg.getWidth());
    unsigned int height = std::min(refImg.getHeight(), tstImg.getHeight());

    double eqm_result = 0.0;

    for(unsigned int i = 0; i < height; ++i)
        for(unsigned int j = 0; j < width; ++j)
        {
            double I0 = (refImg[i][j].R + refImg[i][j].G + refImg[i][j].B) / 3;
            double Ir = (tstImg[i][j].R + tstImg[i][j].G + tstImg[i][j].B) / 3;
            double diff = I0 - Ir;
            eqm_result += diff*diff;
        }

    return eqm_result/(width*height);
}
