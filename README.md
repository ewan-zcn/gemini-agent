# BigQuery Insights Agent (ADK)

This project implements an AI agent using the [Google Agent Development Kit (ADK)](https://github.com/google/google-adk) to query and analyze data from the `kg_demo` dataset in BigQuery.

## Prerequisites

- Python 3.10+
- Google Cloud Project with BigQuery enabled.
- Application Default Credentials (ADC) configured.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install google-adk google-auth google-cloud-bigquery
    ```
    *Note: If you are in a Google-managed environment, you may need to authenticate (e.g., `gcert`) before running `pip` if it's using an internal mirror.*

3.  **Configure Authentication:**
    Ensure you have authenticated to Google Cloud:
    ```bash
    gcloud auth application-default login
    ```

## Usage

Run the agent with the example query:
```bash
python3 main.py
```

The agent is configured to:
- Access the `ewans-demo-project.kg_demo` dataset.
- Query tables like `customers`, `products`, and `purchase_orders`.
- Provide natural language insights based on the data.

## Example Questions to Ask
- "What are the top 3 most expensive products and which customers have ordered them?"
- "Which regions (cities/countries) have the most purchase orders?"
- "Is there any correlation between product category and total order amounts?"
