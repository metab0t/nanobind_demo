cmake_minimum_required(VERSION 3.15...3.27)

project(nbtest)

set(PROJ_INSTALL_DIR nbtest)

# Build Python extensions
find_package(Python ${PYTHON_VERSION}
  REQUIRED COMPONENTS Interpreter Development.Module
  OPTIONAL_COMPONENTS Development.SABIModule)

# Import nanobind through CMake's find_package mechanism
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(
  ext

  STABLE_ABI NB_STATIC

  src/x.cpp
)
install(TARGETS ext LIBRARY DESTINATION ${PROJ_INSTALL_DIR})
