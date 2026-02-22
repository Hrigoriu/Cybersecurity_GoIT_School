use reqwest;
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11";

    let response = reqwest::get(url).await?;
    let exchange_rate: Value = response.json().await?;

    println!("{:#}", exchange_rate);

    Ok(())
}
