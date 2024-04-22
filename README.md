# ckanext-datapackage

[![Build](https://img.shields.io/github/actions/workflow/status/frictionlessdata/ckanext-datapackage/general.yaml?branch=main)](https://github.com/frictionlessdata/ckanext-datapackage/actions)
[![Coverage](https://img.shields.io/codecov/c/github/frictionlessdata/ckanext-datapackage/main)](https://codecov.io/gh/frictionlessdata/ckanext-datapackage)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/ckanext-datapackage)
[![Release](https://img.shields.io/pypi/v/ckanext-datapackage.svg)](https://pypi.python.org/pypi/ckanext-datapackage)

Data Package integreation for CKAN.

## Purpose

This lightweight CKAN plugin adds a `dataset/<id>/datapackage.json` endpoint to every dataset in the data catalog. Read more about the [Data Package Standard](https://datapackage.org/).

## Requirements

The extension requires Python 3.8+. It is being developed and tested with CKAN 2.10. Please fill an issue if it doesn't work as expected with other versions.

## Installation

1.  Install the extension:

```bash
$ pip install ckanext-datapackage
```

2.  Enable the plugin in your ini file:

```text
ckan.plugins = ... datapackage
```

## Endpoint

Data Package representations of a particular dataset can be accessed using the following endpoint:

```
https://{ckan-instance-host}/dataset/{dataset-id}/datapackage.json
```

Read more about [Data Package Standard](https://datapackage.org/) specifications and `datapackage.json` metadata format.

## Example

TODO: x

## Development

Please follow the [Contribution Guide][CONTRIBUTING.md].

## Funding

This project is funded through [NGI0 Entrust](https://nlnet.nl/entrust), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) program. Learn more at the [NLnet project page](https://nlnet.nl/project/FrictionlessStandards/).

[<img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" width="20%" />](https://nlnet.nl)
[<img src="https://nlnet.nl/image/logos/NGI0_tag.svg" alt="NGI Zero Logo" width="20%" />](https://nlnet.nl/entrust)
