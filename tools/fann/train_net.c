#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fann.h>

struct fann *create_network(unsigned int inputs, unsigned int hidden_layers, unsigned int neurons_hidden, unsigned int outputs)
{
	unsigned int *layers = malloc((hidden_layers + 2)*(sizeof(unsigned int)));
	layers[0] = inputs;
	layers[hidden_layers + 1] = outputs;
	for (int i = 1; i < (hidden_layers + 1); i++)
	{
		layers[i] = neurons_hidden;
	}
	fann_create_standard_array(hidden_layers + 2, layers);
	//free(layers);
}

int main(int argc, char *argv[])
{
	if (argc != 10)
	{
		printf("Usage: %s train_db.data inputs hidden_layers neurons_per_hidden outputs max_epochs epochs_per_report max_error result.net\n", argv[0]);
		return 1;
	}

	const unsigned int num_input = atoi(argv[2]);
	const unsigned int num_output = atoi(argv[5]);
	const unsigned int num_hidden_layers = atoi(argv[3]);
	const unsigned int num_neurons_hidden = atoi(argv[4]);
	const float desired_error = (const float) atof(argv[8]);
	const unsigned int max_epochs = atoi(argv[6]);
	const unsigned int epochs_between_reports = atoi(argv[7]);

	struct fann *ann = create_network(num_input, num_hidden_layers,
											num_neurons_hidden, num_output);

	fann_set_activation_function_hidden(ann, FANN_SIGMOID_SYMMETRIC);
	fann_set_activation_function_output(ann, FANN_SIGMOID_SYMMETRIC);

    fann_train_on_file(ann, argv[1], max_epochs, epochs_between_reports, desired_error);

    fann_save(ann, argv[9]);
	printf("Neural network saved to %s\n", argv[9]);

    fann_destroy(ann);

    return 0;
}
