# dna-api

[![Build Status](https://api.travis-ci.com/affonsobrian/dna-api.svg?branch=main)](https://app.travis-ci.com/github/affonsobrian/dna-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

An API that stores genes and show stats of it. Check out the project's [documentation](http://ec2-18-221-62-23.us-east-2.compute.amazonaws.com:8001/).

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
