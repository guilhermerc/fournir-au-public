#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fann.h>
#include <stdint.h>

struct fann *create_network(uint32_t inputs, uint32_t hidden_layers, uint32_t neurons_hidden, uint32_t outputs)
{
	uint32_t *layers = malloc((hidden_layers + 2)*(sizeof(uint32_t)));
	layers[0] = inputs;
	layers[hidden_layers + 1] = outputs;
	for (uint32_t i = 1; i < (hidden_layers + 1); i++)
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

	const uint32_t num_input = atoi(argv[2]);
	const uint32_t num_output = atoi(argv[5]);
	const uint32_t num_hidden_layers = atoi(argv[3]);
	const uint32_t num_neurons_hidden = atoi(argv[4]);
	const float desired_error = (const float) atof(argv[8]);
	const uint64_t max_epochs = atoi(argv[6]);
	const uint64_t epochs_between_reports = atoi(argv[7]);
	const char *outnetfile = argv[9];

	struct fann *ann = create_network(num_input, num_hidden_layers,
											num_neurons_hidden, num_output);

	fann_set_activation_function_hidden(ann, FANN_SIGMOID_SYMMETRIC);
	fann_set_activation_function_output(ann, FANN_SIGMOID_SYMMETRIC);

	struct fann_train_data *tdata = fann_read_train_from_file(argv[1]);

	float lastmin = 1;
	struct fann *bestnet = fann_copy(ann);
	float mse = fann_train_epoch(ann, tdata);
	uint32_t bitfail = fann_get_bit_fail(ann);
	uint64_t epoch;
	printf("Epoch: 1 Error: %.8f Bit fail: %d\n", mse, bitfail);
	for (epoch = 1; epoch < max_epochs; epoch++)
	{
		mse = fann_train_epoch(ann, tdata);
		if (mse < lastmin)
		{
			fann_destroy(bestnet);
			bestnet = fann_copy(ann);
			lastmin = mse;
		}
		if (mse <= desired_error)
		{
			break;
		}
		if ((epoch % epochs_between_reports) == 0)
		{
			bitfail = fann_get_bit_fail(ann);
			printf("Epoch: %d Error: %.8f Bit fail: %d\n", epoch, mse, bitfail);
		}
	}

	fann_save(bestnet, outnetfile);
	printf("Finished after %d epochs\n", epoch);
	printf("Best error: %.8f Bit fail: %d\n", mse, fann_get_bit_fail(bestnet));
	printf("Neural network saved to %s\n", outnetfile);

	fann_destroy_train(tdata);
	fann_destroy(ann);
	fann_destroy(bestnet);

	return 0;
}
