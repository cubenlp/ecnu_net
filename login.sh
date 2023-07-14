#!/bin/bash

# 若 .env 存在，则读取
if [ -f .env ]; then
  source .env
fi

python ecnu_net.py -u $USERNAME -p $PASSWORD -m login