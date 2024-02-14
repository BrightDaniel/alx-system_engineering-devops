#!/usr/bin/env bash
# Generates a compressed archive of a MySQL dump.
mysqldump -uroot -p"$1" --all-databases > backup.sql
tar -cvzf "$(date +%d-%m-%Y)".tar.gz backup.sql
