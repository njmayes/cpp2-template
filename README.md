# cpp2-template

Basic C++2 project template that uses cppfront and premake to automatically compile your cpp2 files to C++ and compile them.

## Description

This is a basic template for a C++2 project, using cppfront and premake as a build system. The template comes with basic premake template projects, and when the 
set up script is run premake will be built from source and project files will be generated if there have been any changes to the premake or source files.

The first time that the setup script is run, the user is prompted to supply the name for the workspace and starting template project. 
The repo directory will still need to be renamed manually as sometimes the permissions for this can be restricted.

## Getting Started

### Dependencies

* Python3
* [premake5](https://github.com/premake/premake-core) - Downloaded as a submodule and built from source when the setup script is run if it is not found.
* [cppfront](https://github.com/hsutter/cppfront) - Downloaded as a submodule and built from source.

### Installing

* Clone the repo recursively and run `setup.bat` for Windows or `setup.sh` for Linux. 
* Enter the name for the solution and the starting project.
* Project files will be generated for the target platform to use.
* Extend the project as desired!

## License

This project is licensed under the MIT License - see the LICENSE.md file for details