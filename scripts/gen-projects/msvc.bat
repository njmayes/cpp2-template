@echo off

pushd %~dp0\..\..\
call dependencies\premake\bin\premake5.exe vs2022
popd

if "%1"=="nopause" goto end
pause

:end