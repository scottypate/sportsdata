#!/bin/bash

for FILE in $(ls -1 ./swagger);
do
    API=$(echo ${FILE} | sed 's/v[2|3]-//' | sed 's/-/_/g' | sed 's/.json//')
    swagger-codegen generate \
        -i ./swagger/${FILE} \
        -c ./swagger_config.json \
        --api-package ${API} \
        --model-name-prefix ${API} \
        -D packageName=sportsdata.${API} \
        -l python \
        -o .
done
