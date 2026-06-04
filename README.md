# Client Server Project

## Team

Dawid Gburczyk
- server
- client
- tests
- multithreading
- documentation

Mikołaj Kostrzewa
- tests
- documentation

Dawid Stępień
-Models
-Repository initialization and data management
-Object serialization support
-tests

## Description

Client-server application using:

- TCP sockets
- multithreading
- object serialization
- automated tests

Three data models:

- Cat
- Dog
- Parrot

Server stores four objects of each type in a map.

Clients request collections of objects and process them using stream-like operations.

---

## Running

Start server:

```bash
python server.py
```
or
```bash
python3 server.py
```

Start client:

```bash
python client.py
```
or
```bash
python3 client.py
```

Run tests:

```bash
python -m unittest discover tests
```
or
```bash
python3 -m unittest discover tests
```

---

## AI Usage Declaration

The following AI tools were used:

- ChatGPT GPT-5.5
- GitHub Copilot
- Claude Sonnet

Applications:

- project architecture
- socket communication examples
- multithreading support
- test generation
- documentation generation

Example prompts:

1. Create a TCP client-server application in Python using pickle serialization.
2. Generate unit tests for Python dataclasses.
3. Explain how to limit concurrent clients in a multithreaded server.
4. Create integration tests for object serialization.
5. Suggest E2E test scenarios for a socket-based application.

All generated code was reviewed, modified and tested by project authors.
