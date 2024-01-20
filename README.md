# AirBnB Clone Project

![Project Preview](./images/obolo_and_adich_console.png)

## Table of Contents

- [Project Description](#project-description)
- [Command Interpreter Description](#command-interpreter-description)
- [How to Start](#how-to-start)
- [How to Use](#how-to-use)
- [Example](#example)
- [Authors](#authors)

## Project Description

This is an AirBnB clone project that aims to replicate some functionalities of the AirBnB website. The project will include a command-line interface for managing various objects within the application.

## Command Interpreter Description

The command interpreter serves as the primary interface for users to interact with the AirBnB clone. It allows users to perform actions such as creating new objects, retrieving information, updating attributes, and more.

### How to Start

To start the command interpreter, follow these steps:

```bash
$ ./console.py
```

### How to Use

The command interpreter supports various commands. Here are some examples:

- Create a new user:

  ```bash
  (hbnb) create User
  ```

- Retrieve objects:

  ```bash
  (hbnb) show User 1234-5678
  ```

- Update attributes:

  ```bash
  (hbnb) update User 1234-5678 first_name "Emmanuel"
  ```

- Exit the interpreter:
  ```bash
  (hbnb) quit
  ```

### Example

Here is an example illustrating the usage of the command interpreter:

```bash
$ ./console.py
(hbnb) create User
1234-5678
(hbnb) show User 1234-5678
[User] (1234-5678) {'id': '1234-5678', 'created_at': '2022-01-20T12:00:00', 'updated_at': '2022-01-20T12:00:00'}
(hbnb) update User 1234-5678 first_name "John"
(hbnb) show User 1234-5678
[User] (1234-5678) {'id': '1234-5678', 'created_at': '2022-01-20T12:00:00', 'updated_at': '2022-01-20T12:05:00', 'first_name': 'John'}
(hbnb) quit
```

## Authors

See list [here](./AUTHORS)
