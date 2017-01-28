# cppstyle

A style checker for C/C++ based on clang Edit

## Usage

### Local

First, you need a proper version of libclang and it's python bindings.

- Arch: `yaourt -S python-clang`
- Ubuntu Xenial: `apt-get install python-pip python-clang-3.8 libclang-3.8-dev`

Then just install it using pip:

`pip install cppstyle`

Run it!

`cppstyle --config /path/to/.cppstyle -i /path/to/[YourCFile]`

### Docker

Run it!

`docker run -v /path/to/code:/code gfelbing/cppstyle cppstyle --config /code/.cppstyle -i /code/[YourCFile]`

## Configuration

cppstyle is configured using a yaml file. By default, it uses the .cppstyle in your current directory.

You can specify another path using the `--config` option.

For a full example, see `.cppstyle` in this repository.
Every configuration is optional, a missing configuration means no checks on it.