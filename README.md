# @pgodschalk/obey-the-testing-goat

Working code for Harry Percival's Obey the Testing Goat

## Table of contents

- [@pgodschalk/obey-the-testing-goat](#pgodschalkobey-the-testing-goat)
  - [Table of contents](#table-of-contents)
  - [About this project](#about-this-project)
  - [Getting started](#getting-started)
    - [Dependencies](#dependencies)
    - [Install](#install)
    - [Running tests](#running-tests)
      - [Functional tests](#functional-tests)
      - [Unit tests](#unit-tests)
  - [Deployment](#deployment)
    - [Build for production](#build-for-production)
  - [Authors](#authors)

## About this project

Working code for Harry Percival's Obey the Testing Goat

## Getting started

### Dependencies

- NodeJS >= 16
- NPM
- Poetry >= 1.4
- Python == 3.6

### Install

Clone this git repository:

```sh
git clone https://github.com/pgodschalk/obey-the-testing-goat.git
```

Install node modules:

```sh
npm install
```

Install poetry dependencies:

```sh
poetry install
```

Activate virtualenv:

```sh
poetry shell
```

Start the dev server:

```sh
python manage.py runserver
```

### Running tests

#### Functional tests

```sh
python manage.py test functional_tests
```

#### Unit tests

```sh
python manage.py test lists
open lists/static/tests/tests.html
```

## Deployment

### Build for production

See `deploy_tools/provisioning_notes.md`

```sh
fab deploy:host=foo@example.org
```

## Authors

- **Patrick Godschalk** - _Developer_ - [pgodschalk](https://github.com/pgodschalk)

[SPDX](https://spdx.org/licenses/) license: `UNLICENSED`

Copyright (c) 2023 Patrick Godschalk
