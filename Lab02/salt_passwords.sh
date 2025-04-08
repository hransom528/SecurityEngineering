#!/bin/sh

cat sample_passwords.txt | while read line
do
	SALT=$(openssl rand -base64 16)
	HASH=$(echo -n "$line$SALT" | openssl dgst -sha256 -binary | base64)
	echo "$SALT,$HASH" >> hashed_passwords.csv
	echo "$SALT,$HASH"
done
