#define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do this in one cpp file

#include "test/catch.hpp"
#include "SensorParameters.h"

TEST_CASE("Test whether sensor inputs are in Range")
{
  int upper_limit = 25;
  int lower_limit = 0;

  int sensor_data = Get_Sensor_Data(lower_limit, upper_limit);

  REQUIRE(sensor_data <= upper_limit);
  REQUIRE(sensor_data >= lower_limit);
}

