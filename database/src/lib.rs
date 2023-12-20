use pyo3::prelude::*;
use surrealdb::{
    engine::remote::ws::{Client, Ws},
    opt::auth::Root,
    Surreal,
};

mod bindings;

async fn rconnect(
    address: String,
    user: String,
    pass: String,
    ns: String,
    db: String,
) -> anyhow::Result<Surreal<Client>> {
    let data_base = Surreal::new::<Ws>(address).await?;
    data_base
        .signin(Root {
            username: &user,
            password: &pass,
        })
        .await?;
    data_base.use_ns(ns).use_db(db).await?;

    Ok(data_base)
}
