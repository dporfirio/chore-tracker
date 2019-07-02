# Chore Tracker 0.1.0

For all of your chore-tracking needs. Currently maintains a category of chores to be completed, and the set of chores corresponding to that category. This code is intended to be run on a Raspberry Pi with an 800x480 touch screen.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Currently all that is required are the following Python3 libraries

1. PyQT5
2. csv

### Installing

No installation required.

## Running the tests

```
python3 main <chore csv file>
```

### Sample input data

A sample CSV file is provided in the io folder.

```
python3 main io/sample_chorelist.csv
```
