#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN_TEMPERATURE     0
#define MAX_TEMPERATURE     45
#define MIN_STATE_OF_CHARGE 20
#define MAX_STATE_OF_CHARGE 80
#define DATA_SAMPLES        25

int randomreadingsgen(int lower_limit, int upper_limit);
int *generate_readings(int lower_limit, int upper_limit, int arraySize, int *readings);

void Console_Output(char *data, int *values, int size);
void Get_Sensor_Data();