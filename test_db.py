#!/usr/bin/python
# -*- coding:UTF-8 -*-

import psycopg2

conn = psycopg2.connect(database="test", user="test", password="test", host="localhost", port = "5432")

print "Opened database successfully!"
