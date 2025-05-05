#define CATCH_CONFIG_MAIN
#include "../src/math_functions.h"
#include "catch.hpp"

TEST_CASE("Testing add function") {
    REQUIRE(add(1, 2) == 3);
    REQUIRE(add(-1, 1) == 0);
}

TEST_CASE("Testing subtract function") {
    REQUIRE(subtract(5, 3) == 2);
    REQUIRE(subtract(3, 5) == -2);
}

TEST_CASE("Testing square function") {
    REQUIRE(square(4) == 16);
    REQUIRE(square(-3) == 9);
}
