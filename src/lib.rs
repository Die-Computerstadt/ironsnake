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
