from snowflake.core import Root
from snowflake.snowpark import Session

session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

root = Root(session)                         
svc = root.databases[CORTEX_SEARCH_DATABASE].schemas[CORTEX_SEARCH_SCHEMA].cortex_search_services[CORTEX_SEARCH_SERVICE]
