CC=g++
LIBS=-lvisp
FLAGS=-std=c++14 -Wall -pedantic -g -Og
PROJECT_NAME=psnr_test.out

objects=main.o

all: $(objects)
	$(CC) -o $(PROJECT_NAME) $^ $(LIBS)

%.o: %.cpp
	$(CC) -c $< $(FLAGS)

.PHONY: clean

clean:
	rm -rf $(objects) $(PROJECT_NAME)
