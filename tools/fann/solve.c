#include <stdio.h>
#include <string.h>
#include <floatfann.h>
#include <argp.h>

const char *argp_program_version =
	"FANN Network Solver V0.1";
const char *argp_program_bug_address =
	"<augustofg96@gmail.com>";

static char doc[] =
	"Solver -- a program that computes the answer of a neural network based on the provided inputs";

static char args_doc[] = "-n netfile";

struct arguments
{
	char *args[2];
	int shellmode, msemode;
	char *netfile, *input_db;
};

static struct argp_option options[] = {
	{"netfile", 'n', "FILE", 0,
	 "Neural network file"},
	{"shellmode", 's', 0, 0,
	 "Requests inputs displays outputs interactively to the user"},
	{"input-db", 'i', "FILE", 0,
	 "Use a database with the inputs and expected outputs to compute the mean square error"},
	{0}
};

static error_t parse_opt(int key, char *arg, struct argp_state *state)
{
	struct arguments *arguments = state->input;

	switch (key)
	{
	case 's':
		arguments->shellmode = 1;
		break;
	case 'n':
		if (arguments->netfile != NULL)
		{
			printf("Only one neural network file should be specified\n");
			argp_usage (state);
		}
		else arguments->netfile = arg;
		break;
	case 'i':
		arguments->input_db = arg;
		arguments->msemode = 1;
		break;

	case ARGP_KEY_ARG:
		if (state->arg_num >= 2)
			/* Too many arguments. */
			argp_usage (state);

		/* arguments->args[state->arg_num] = arg; */

		break;

	case ARGP_KEY_END:
		if (arguments->netfile == NULL)
		{
			printf("The neural network file must be specified\n");
			argp_usage (state);
		}
		/* if (state->arg_num < 2) */
		/* 	  /\* Not enough arguments. *\/ */
		/* 	  argp_usage (state); */
		break;

	default:
		return ARGP_ERR_UNKNOWN;
	}
	return 0;
}

static struct argp argp = {options, parse_opt, args_doc, doc};

int main(int argc, char *argv[])
{
	struct arguments inarg;
	inarg.msemode = 0;
	inarg.shellmode = 0;
	inarg.netfile = NULL;
	argp_parse (&argp, argc, argv, 0, 0, &inarg);
	int interactive = inarg.shellmode;
	
	fann_type *calc_out;
	char *netfilename = inarg.netfile;
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

	if (inarg.msemode)
	{
		struct fann_train_data *valdata = fann_read_train_from_file(
			inarg.input_db);
		float res = fann_test_data(ann, valdata);
		printf("%f\n", res);
		return 0;
	}
	else if (interactive)
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
