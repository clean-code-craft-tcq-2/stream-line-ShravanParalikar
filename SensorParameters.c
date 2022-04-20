#include "SensorParameters.h"

int randomreadingsgen(int lower_limit, int upper_limit) {
    
    return (rand() % (upper_limit - lower_limit + 1)) + lower_limit;
}

int *generate_readings(int lower_limit, int upper_limit, int arraySize, int *readings) {

    srand(time(0));
    for (int i = 0; i < arraySize; i++)
    {
        readings[i] = randomreadingsgen(lower_limit, upper_limit);
    }
    return readings;
}

void Console_Output(char *data, int *values, int size) {

    printf("%s:", data);
    for (int i = 0; i < size; i++)
    {
        printf("%d ", values[i]);
    }
    printf("\n");
}

void Get_Sensor_Data() {

    int *temperature_readings = (int *)malloc(DATA_SAMPLES * sizeof(int));
    generate_readings(MIN_TEMPERATURE, MAX_TEMPERATURE, DATA_SAMPLES, temperature_readings);

    int *soc_readings = (int *)malloc(DATA_SAMPLES * sizeof(int));
    generate_readings(MIN_STATE_OF_CHARGE, MAX_STATE_OF_CHARGE, DATA_SAMPLES, soc_readings);

    Console_Output((char *)"TEMPERATURE", temperature_readings, DATA_SAMPLES);
    Console_Output((char *)"STATE_OF_CHARGE", soc_readings, DATA_SAMPLES);

    free(temperature_readings);
    free(soc_readings);
}