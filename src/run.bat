@ECHO OFF
REM LOCATION OF THE RUN.BAT AND INITIALIZER
REM CHANGE THIS TO WHEREVER YOU'VE PUT THE FILES
REM DON'T FORGET TO ADD IT TO THE PATH ENVIRONMENT VARIABLE AS WELL
SET DIR=C:\Users\haegg\Desktop\Code\Python\GithubInitializer\src
SET PROJECT=%CD%
PUSHD %DIR%
PYTHON INITIALIZER.PY %PROJECT%
POPD
