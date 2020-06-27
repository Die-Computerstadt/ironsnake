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
