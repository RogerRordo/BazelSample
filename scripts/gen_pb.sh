#!/bin/bash

readonly PROTO_FILES=$(find ./proto/ -name "*.proto" -type f)
mkdir -p ./.protobuf_output
for proto_file in $PROTO_FILES; do
    protoc -I /usr/local/include -I ./ --pyi_out ./.protobuf_output $proto_file
done
