import os
import google.auth

# Force Vertex AI backend to use ADC instead of an API Key
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

credentials, project_id = google.auth.default()
if project_id:
    os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
else:
    # Fallback to the known demo project if ADC doesn't provide one
    os.environ["GOOGLE_CLOUD_PROJECT"] = "ewans-demo-project"

# Optional: Set location if needed
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from google.adk.agents.llm_agent import Agent
from google.adk.tools.bigquery.bigquery_toolset import BigQueryToolset
from google.adk.tools.bigquery.bigquery_credentials import BigQueryCredentialsConfig
from google.adk.tools.bigquery.config import BigQueryToolConfig, WriteMode

# 1. Setup BigQuery Tools
credentials, project_id = google.auth.default()
# project_id = "ewans-demo-project"

creds_config = BigQueryCredentialsConfig(credentials=credentials)
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

bq_toolset = BigQueryToolset(
    credentials_config=creds_config,
    bigquery_tool_config=tool_config
)

# 2. Define the Agent
# Note: For ADK discovery, this is often named 'root_agent' or 'agent'
root_agent = Agent(
    name="bigquery_analyst",
    model="gemini-3-pro-preview",
    instruction="""

    You are a data analyst specializing in supply chain and manufacturing knowledge graphs.
    Use the BigQuery tools to query the `kg_demo` dataset in the project `ewans-demo-project`.
    
    The dataset contains tables such as:
    - `customers`: Customer information.
    - `products`: Product details.
    - `purchase_orders`: Orders placed by customers.
    - `part_nodes`, `material_nodes`: Components of the manufacturing graph.
    - `edges_...`: Relationships between different entities.

    Your goal is to answer user questions by:
    1. Listing tables if you are unsure of the schema.
    2. Getting table information for the relevant tables.
    3. Executing SQL queries to retrieve data.
    4. Providing clear insights based on the query results.
    
    Always ensure your SQL queries use the fully qualified table name: `ewans-demo-project.kg_demo.<table_name>`.
    """,
    tools=[bq_toolset]
)
