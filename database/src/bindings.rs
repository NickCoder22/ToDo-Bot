use super::*;

#[pymodule]
fn database(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(connect, m)?)?;
    Ok(())
}

#[pyclass]
struct DataBase {
    db: Surreal<Client>,
}

#[pyfunction]
fn connect(
    py: Python,
    address: String,
    user: String,
    pass: String,
    ns: String,
    db: String,
) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async move {
        let db = rconnect(address, user, pass, ns, db).await?;
        Ok(DataBase { db })
    })
}

#[pymethods]
impl DataBase {}
