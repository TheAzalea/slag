#!/usr/bin/env bash

cd output
git add . -f
git commit -m "slag deployment"
git push -f
