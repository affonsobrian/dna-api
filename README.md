# dna-api

[![Build Status](https://travis-ci.org/affonsobrian/dna-api.svg?branch=master)](https://travis-ci.org/affonsobrian/dna-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

An API that stores genes and show stats of it. Check out the project's [documentation](http://affonsobrian.github.io/dna-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
