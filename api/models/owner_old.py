#!/usr/bin/env python3

import os.path
# model wraps around the database, one class per table. Will control schema, column types, etc

# do as I say, not as I do. This will eventually be a db
# model/wrapper, but files are easier (kinda), so do this atm

dbFile = "mock_db.txt"

class Owner():
	def get(self, lineNumber):
		if lineNumber:
			with open(dbFile, "r+") as f:
				lines = f.readlines()
				return lines[lineNumber - 1]

		else:
			with open(dbFile, "r+") as f:
				return f.readlines()

	def write(self, username):
		with open(dbFile, "a+") as f:
			return f.write("%s\n" % username)

model = Owner()