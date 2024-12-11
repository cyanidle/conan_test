cmake_minimum_required(VERSION 3.16)

project(damn C CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(fmt REQUIRED)
find_package(LibDataChannel REQUIRED)

add_library(damn SHARED src/damn.cpp)
target_include_directories(damn PUBLIC include)
target_link_libraries(damn PUBLIC fmt::fmt)
set_target_properties(damn PROPERTIES PUBLIC_HEADER "include/damn.hpp")

add_library(damn-static STATIC src/damn.cpp)
target_include_directories(damn-static PUBLIC include)
target_link_libraries(damn-static PUBLIC fmt::fmt)
set_target_properties(damn-static PROPERTIES PUBLIC_HEADER "include/damn.hpp")

install(TARGETS damn damn-static)