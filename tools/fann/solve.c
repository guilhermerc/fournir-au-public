#include <stdio.h>
#include <string.h>
#include "floatfann.h"

int main(int argc, char *argv[])
{
	int interactive = 1;
	if (argc != 2 && argc != 3)
	{
		printf("Usage: %s netfile.net [optional --non-interactive]\n", argv[0]);
		return 1;
	}
	
	if (argc == 3)
	{
		if (strcmp(argv[2], "--non-interactive") == 0)
		{
			interactive = 0;
		}
	}
	
	fann_type *calc_out;
	char *netfilename = argv[1];
	struct fann *ann = fann_create_from_file(netfilename);
	if (ann == NULL)
	{
		printf("Error when loading the neural network file.");
		return 2;
	}
	unsigned int num_outputs = fann_get_num_output(ann);
	unsigned int num_inputs = fann_get_num_input(ann);
	unsigned int num_layers = fann_get_num_layers(ann);
	fann_type *inputs = malloc(num_inputs*sizeof(fann_type));

	if (interactive)
	{
		printf("Loaded %s network\n", netfilename);
		printf("Inputs: %d Outputs: %d Hidden layers: %d\n", num_inputs,
			   num_outputs, num_layers - 2);
	}

	while (1)
	{
		int i;
		float inval;
		if (interactive) printf("Inputs: ");
		for (i = 0; i < num_inputs; i++)
		{
			if (scanf("%f", &inval) == EOF)
				break;

			inputs[i] = inval;
		}

		if (i != num_inputs)
			break;

		calc_out = fann_run(ann, inputs);
		if (interactive) printf("Result:\n");
		
		for (i = 0; i < num_outputs; i++)
		{
			printf("%f ", calc_out[i]);
		}
		printf("\n");
		
	}

	free(inputs);
	fann_destroy(ann);
	return 0;
}
