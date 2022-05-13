#include <stdlib.h>
#include "clog.h"
#include <unistd.h>
#include <stdio.h>

#define population_pct 15
#define city_name "Bogota"

int main(int argc, char* argv[])
{
	//char* city_name  = "Bogota";
	//int population_pct = 15;
	logf_("%d%% of Columbia lives in %s.\n", population_pct, city_name);

	logf_red("%s\n", "RED");
	logf_green("%s\n", "GREEN");
	logf_yellow("%s\n", "YELLOW");
	logf_blue("%s\n", "BLUE");
	logf_magenta("%s\n", "MAGENTA");
	logf_cyan("%s\n", "CYAN");

	log_int(3 + 4);
	log_int(population_pct);
	log_char('A');
	log_char(65);
	log_char(city_name[0]);

	log_str(city_name);
	log_addr(city_name);
	log_float(1.0 / 8.0);

	log_bool(3 > 5);
	log_bool(3 > 1);

	return EXIT_SUCCESS;
}
