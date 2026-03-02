# hello_pkg
This is a simple example to show how to setup Pixi to create a package that executes an OpenMDAO component that depends on external C code. The C code is built upon first execution using the Makefile in the `src` folder.


Show Pixi tasks:

```console
pixi task list
```

To run the Python code that executes the C code:

```console
pixi run hello-py
```

To run the C code directly

```console
pixi run hello-c
```