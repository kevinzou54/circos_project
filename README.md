#Circos Plot Generation Web App

##Description
This project provides an intuitive web interface for generating and visualizing genome data using Circos, an open-source genome visualization tool. The application is built with Flask and Nginx and is containerized with Docker for easy deployment. It allows users to configure Circos plots, submit data for visualization, and interact with the generated plots. The project was deployed using Azure Container Apps, improving cost efficiency and scalability.

##Features
Web-based UI: Users can interactively configure and generate Circos plots.
Seamless Integration: The web app integrates with the Circos command-line tool to handle configuration and data visualization.
Dockerized Deployment: The entire app, including Nginx, Flask, and Circos, is packaged into a Docker container for easy deployment.
Cloud Deployment: Deployed on Azure Container Apps, making it scalable and cost-effective compared to traditional VM hosting.

##Prerequisites
Docker installed on your machine.
Azure account (if you plan to deploy on Azure).
Basic knowledge of using the command line.

##Configuring Circos Plots
Access the web app and input your genome data through the UI.
Use the provided forms to configure Circos plot options, including:
Data file selection
Plot type (e.g., histogram, scatter, etc.)
Custom annotations
Submit the form to generate your plot.
##Viewing and Downloading Plots
After submitting your configuration, the app will generate a Circos plot and display it on the results page.
You can download the generated plot in PNG or SVG format.
