# Rust+Python=IronSnake

This is just a really simple example of using [pyO3](https://pyo3.rs)
to make a python module in rust. Really just a cut down version
of any tutorial that you'd find, so I can remember how to do it.

# The rust side of things
We define a python module called `rusty_bits` with a single
function `hello` - it looks like this

```rust
// src/lib.rs

use pyo3::prelude::*;

#[pymodule]
fn rusty_bits(_py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "hello")]
    fn hello_wrap(_py: Python, s: String) -> PyResult<()> {
        println!("Hello {}", s);
        Ok(())
    }

    Ok(())
}
```

Our `Cargo.toml` looks "normal" with these special bits:

```toml
[lib]
name = "rusty_bits"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.10.1", features = ["extension-module"] }
```

# The python side of things
I use [poetry](https://python-poetry.org/) for dependency
management and virtual enving. The only special thing I
need here is 

```toml
[tool.poetry.dependencies]
setuptools-rust = "^0.10.6"
```

To build the rust extension we need some special things 
in `setup.py`

```python
# setup.py

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="snake",
    version="0.1.0",
    rust_extensions=[RustExtension("snake.rusty_bits", binding=Binding.PyO3)],
    packages=["snake"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "hello=snake:say_hello"
        ]
    }
)
```

Note that my rust-defined python module was called `rusty_bits`
so it's being defined there as `snake.rusty_bits` where `snake`
is the name of the python module/package.

We'll also need to make sure we package the rust code with
the python if we want to sdist or bdist or whatever

```
# MANIFEST.in

include Cargo.toml
recursive-include src *
```

Then the actual python just looks like I'm importing a 
sibling module:

```python
# snake/__init__.py

from .rusty_bits import hello
import sys

def say_hello():
    name = sys.argv[1]
    hello(name)
```

# Building
All you need to build is to run

```
> poetry install
```

Then you can run it

```
> poetry run hello World
Hello World
```

Boring, but fun?
