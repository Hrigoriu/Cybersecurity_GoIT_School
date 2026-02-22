use serde::Deserialize;
use thiserror::Error;

#[derive(Debug, Deserialize)]
struct ExchangeRate {
    ccy: String,
    base_ccy: String,
    buy: String,
    sale: String,
}

#[derive(Error, Debug)]
enum AppError {
    #[error("HTTP request failed: {0}")]
    Request(#[from] reqwest::Error),

    #[error("Invalid response format: {0}")]
    Parse(#[from] serde_json::Error),
}

async fn fetch_rates() -> Result<Vec<ExchangeRate>, AppError> {
    let url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11";

    let response = reqwest::Client::new()
        .get(url)
        .timeout(std::time::Duration::from_secs(10))
        .send()
        .await?
        .error_for_status()?; // перевірка HTTP статусу

    let rates = response.json::<Vec<ExchangeRate>>().await?;

    Ok(rates)
}

#[tokio::main]
async fn main() {
    env_logger::init();

    match fetch_rates().await {
        Ok(rates) => {
            println!("Exchange rates:");
            for rate in rates {
                println!(
                    "{} / {} | buy: {} | sale: {}",
                    rate.ccy, rate.base_ccy, rate.buy, rate.sale
                );
            }
        }
        Err(e) => {
            eprintln!("Application error: {}", e);
        }
    }
}
