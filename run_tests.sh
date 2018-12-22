#!/bin/bash

ALL_TESTS="tests/"
### RUN TESTS AND STORE COMSOLE RESULTS IN LOG FILE ####
pytest -s $ALL_TESTS > test_result.log #--junitxml=test_result.xml