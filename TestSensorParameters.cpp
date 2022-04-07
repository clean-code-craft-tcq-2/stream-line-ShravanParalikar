#define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do this in one cpp file

#include "test/catch.hpp"
#include "SensorParameters.h"

TEST_CASE("Test whether sensor inputs are in Range")
{
  int upper_limit = 25;
  int lower_limit = 0;

  int randomInteger = getRandomIntegerInRange(lower_limit, upper_limit);

  REQUIRE(randomInteger <= upper_limit);
  REQUIRE(randomInteger >= lower_limit);
}

