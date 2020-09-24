#!/bin/bash
# Get the latest migration from the file received as a parameter and print it with 
set -e;


migration_file=$1

if [ ! -z ${migration_file} ]; then 
    down_revision=$(grep -Po "(?<=^down_revision = ').*(?=')" $migration_file );
    revision=$(grep -Po "(?<=^revision = ').*(?=')" $migration_file );
    echo "Showing SQL script for migrations: $down_revision -> $revision";
    sql_command=$(flask db upgrade --sql ${down_revision}:${revision});
    echo $sql_command;
else 
    exit 0;
fi