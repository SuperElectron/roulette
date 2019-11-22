# Coding Challenges
Book: Building Skills in Object-Oriented Design
Author: Steven F. Lott
pdf name: oodesign-python-2.1.pdf

## Casino Example
======
1. Outcome.py

Deliverables
	1. the Outcome class
	2. testing class for Outcome class.
	- unit test should create three instances of Outcome, two of which have the same name.
		- It should use a number of individual tests to establish that two Outcome with the same name will test true for equality, have the same hash code, and establish that the winAmount method works correctly.

### Notes
- ensure that project name and source folder name (roulette) are the same so that test discovery functions.

```bash
$ python -m unittest discover -v
```
