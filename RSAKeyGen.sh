#!/bin/bash

# Code from https://rietta.com/blog/openssl-generating-rsa-key-from-command/

openssl genrsa -des3 -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
openssl rsa -in private.pem -out unsafe_private.pem -outform PEM
