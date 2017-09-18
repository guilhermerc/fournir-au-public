all: trainer solver

trainer: train_net.o
	gcc -O3 $< -o $@ -lfann -lm

solver: solve.o
	gcc -O3 $< -o $@ -lfloatfann -lm -lfann

%.o: %.c
	gcc -O3 -c $< -o $@

