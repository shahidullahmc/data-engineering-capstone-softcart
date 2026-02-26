# data-engineering-capstone-softcart
End‑to‑end Data Engineering Capstone Project for an e‑commerce company. Includes OLTP design, data warehousing, ETL pipelines, Airflow DAGs, analytics dashboards, and Spark‑based big data processing. Covers full data lifecycle from ingestion to reporting and machine learning.

>A complete, production‑style data engineering workflow for a modern e‑commerce platform.


---
### **SoftCart Data Engineering Capstone — OLTP, Warehousing, ETL, Airflow, Analytics & Spark ML**
---
#### Project Overview  
This repository contains the full implementation of the **SoftCart Data Engineering Capstone Project**, completed across multiple modules covering OLTP systems, data warehousing, ETL pipelines, workflow orchestration, analytics dashboards, and big data processing with Apache Spark. The project simulates the data platform of an e‑commerce company and demonstrates the complete lifecycle of data from ingestion to reporting and machine learning.

### Module 1 — OLTP Database Design  
Designed a transactional database schema for SoftCart’s sales operations.  
Key tasks included:

- Creating an OLTP schema with fields such as ProductID, CustomerID, Price, Quantity, and Timestamp.
- Importing operational data into MySQL.
- Verifying data integrity and record counts.
- Preparing the OLTP layer for downstream ETL processes.

### 🏛️ Module 3 — Data Warehousing & Reporting  
Built a full data warehouse using PostgreSQL and pgAdmin ERD tools.

#### **Data Warehousing**
- Designed a **Star Schema** with:
  - `softcartDimDate`
  - `softcartDimCategory`
  - `softcartDimCountry`
  - `softcartFactSales`
- Modeled relationships (1–many, many–1) using pgAdmin ERD.
- Restored staging data from provided dump files.
- Loaded CSV data into dimension and fact tables.
- Implemented **GROUPING SETS**, **ROLLUP**, **CUBE**, and created an **MQT** for total sales per country.

#### **Data Warehousing Reporting**
- Loaded reporting data into PostgreSQL.
- Built dashboards using **IBM Cognos Analytics** or **Google Looker Studio**:
  - Quarterly mobile phone sales (bar chart)
  - Category‑wise electronic goods sales (pie chart)
  - Month‑wise total sales (line chart)

### Module 4 — Data Analytics  
- Created a reporting data source.
- Designed interactive dashboards for business KPIs.
- Automated administrative tasks:
  - Created index on timestamp
  - Listed all indexes
  - Wrote a Bash script to export table records

### Module 5 — ETL & Data Pipelines  
#### **Part 1 — ETL using Python**
- Connected MySQL (OLTP) → PostgreSQL (Data Warehouse).
- Loaded `sales.sql` into MySQL and `sales.csv` into PostgreSQL.
- Implemented incremental ETL:
  - Extract yesterday’s data
  - Transform fields
  - Load into warehouse
- Automated the workflow using a Python ETL script.

#### **Part 2 — Apache Airflow Pipeline**
- Created a daily DAG to process web server logs.
- Tasks included:
  - Extract IP addresses
  - Filter out specific IPs
  - Archive processed logs into TAR files
- Deployed, unpaused, and monitored DAG runs in Airflow UI.

### Module 6 — Big Data Analytics with Spark  
- Processed large‑scale search term data using PySpark.
- Built a Spark ML regression model for sales forecasting.
- Loaded and applied the model to predict **2023 sales**.
- Implemented a clean `predict_sales_2023()` function using `model.predict()`.
=============================================================================

### Skills Demonstrated  
- OLTP & relational modeling  
- Data warehouse design (Star Schema)  
- SQL analytics (GROUPING SETS, ROLLUP, CUBE, MQT)  
- ETL development (Python, SQL, Bash)  
- Workflow orchestration (Apache Airflow)  
- Big data processing (Apache Spark)  
- Machine learning pipelines (Spark ML)  
- Dashboarding (Cognos / Looker Studio)  
- End‑to‑end data engineering lifecycle  



Would you like those added?
