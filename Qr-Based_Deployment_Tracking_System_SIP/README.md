# QR-Based Deployment Tracking System

## About The Project
This project is an automated deployment tracking system developed to streamline large-scale IT device deployment operations. It replaces a manual, spreadsheet-based data entry workflow with a custom mobile application and a real-time analytics dashboard. This system was engineered as a Student Industrial Project (SIP) for CTC Global Sdn Bhd in collaboration with Universiti Teknologi PETRONAS (UTP).

**Tech Stack:** Microsoft Power Apps, Microsoft Power BI, Microsoft Excel Online (OneDrive), Power Fx, Power Query.

## The Challenge
The previous IT deployment workflow relied heavily on engineers manually entering device information into Excel spreadsheets. This created several critical operational bottlenecks:
* **Lack of Real-Time Visibility:** Management could not immediately track deployment progress or team productivity.
* **Data Inaccuracy Risks:** Manual data input increased the likelihood of human errors, resulting in duplicate or inconsistent records.
* **Inefficient Reporting:** Generating actionable reports required time-consuming manual data cleaning and consolidation.
* **Limited Scalability:** The manual workflow could not effectively support large-scale enterprise operations.

## System Architecture

![System Architecture Diagram](System%20Architecture%20Diagram.png)

To address these challenges, I developed a three-tier architecture utilizing the Microsoft Power Platform:
* **Application Layer:** A mobile application built with Microsoft Power Apps allows engineers to scan device QR codes directly using their mobile camera.
* **Data Management Layer:** Microsoft Excel hosted on OneDrive serves as a centralized cloud database to securely log and store deployment records.
* **Analytics Layer:** Microsoft Power BI connects directly to the database to transform raw data into interactive, real-time visual dashboards.

## Key Features & User Interface

### 1. Automated Data Capture
![QR Scanner Interface](QR%20Scanner%20Interface.png)

A built-in Barcode Scanner control extracts the device Hostname and Serial Number instantly from the QR code, eliminating manual typing.

### 2. Streamlined Data Entry
![Data Entry Interface](Data%20Entry%20Interface.jpg)

Engineers simply select their name from a predefined dropdown list and submit the record directly to the centralized cloud database.

### 3. Duplicate Record Validation
![Duplicate Validation Error](Duplicate%20Validation%20Error.jpg)

The application uses Power Fx (specifically the `LookUp` function) to check the database for existing hostnames or serial numbers, instantly alerting the user and preventing duplicate entries.

### 4. Interactive Power BI Dashboard
![Power BI Dashboard](Power%20BI%20Dashboard.jpg)

Power Query is used to clean and transform the data, feeding Power BI visualizations that provide actionable insights into daily deployment trends, monthly summaries, and individual engineer performance through dynamic cross-filtering.

## Project Impact
* **Increased Efficiency:** Eliminated manual spreadsheet logging, allowing engineers to deploy devices faster and focus on technical tasks.
* **Enhanced Data Integrity:** Eradicated typographical errors and ensured every deployment record in the database is unique.
* **Data-Driven Decision Making:** Provided supervisors with near real-time operational visibility to monitor daily trends and resource allocation without waiting for manual reports.
* **Digital Transformation:** Successfully modernized a traditional paper-based process into a scalable, sustainable digital workflow.

## Repository Contents
* `SIP Presentation Slidee.pdf`: A visual overview of the system architecture, UI designs, and project goals.
* `22012086_IrfanAimanBinMohdYussuf_SIPReport.pdf`: The comprehensive technical report detailing the project methodology, data pipeline flow, and operational findings.
