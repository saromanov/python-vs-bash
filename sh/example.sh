#!/bin/bash

ls -l | sed -E  -e '1d; s/^([^ ]+ +){8}//'