# VulcanDC

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-NONE-blue.svg)
![Roll](https://img.shields.io/badge/Rick-Astley-green.svg)

A Python script that uses the Vulcan API to fetch lesson schedules and sends reminders to Discord users 20 minutes before a lesson starts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Initial onfiguration](#initial-onfiguration)
- [Contributing](#contributing)
- [Liecnse](#license)
- [Files](#files)

- [Documentation](#documentation)
- [Other links](#other-links)

## Introduction

Sends discord message to users about their next lesson

- Lesson start hour
- Lesson end hour
- Lesson class
- Lesson group
- Lesson subject

## Features

- Sends a reminder message to a given discord channel

## Requirements

- Python 3.8+
- Required Python libraries (install using `pip`):
  - `vulcan-api`
  - `discord-webhook

## Initial onfiguration

- Copy repo to your local mashine
- run `register.py` file
- log in to your Vulcan account
- go to `Uczeń` tab
- select `Dostęp mobilny` tab
- press `Wygeneruj kod dostępu` button
- copy-pasta `Token`, `Symbol` and `PIN` texts
- make a discord Webhook and paste it

#### NOTE

Never relase your `Token` or `PIN` to anyone. This will give them full acces to your account. If you do then press `Wyrejestruj Użądzenie` button immediately!

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

## License

This project has no license, which means that you can do anything with this code.

## Files

This code does not make or edit any files except `secrets.json`, which contains all your API keys

## Documentation

TODO

## Other links

[Vulcan API repo](https://github.com/kapi2289/vulcan-api)
