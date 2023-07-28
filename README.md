# ImmoEliza: Property Price Predictor

## Description
**This repository is contains Data Analysis for a fictional real estate company called "ImmoEliza". I created it as part of my [BeCode](https://www.becode.org) AI Bootcamp training in 2023.**

This repo can be used to predict property prices in Belgium.  

The data used in this project was sourced from the repository [ImmoEliza: Collecting Data](https://github.com/DeFre/ImmoEliza-collecting-data) which was used to collect data on 10.000 properties from Immoweb.

## Installation
Clone the repo. It can than be opened using a program such a VS code or import it in [Google Colab](https://colab.research.google.com/) if you prefer to run it in browser.

To use the API, the following Python libraries need to be installed: 
* Pandas
* XG Boost
* FastAPI
* Pydantic
* Typing

If you want to explore the data or change the models you will also need the following Python libraries:
* Numpy
* Re (Regex)
* Matplotlib.pyplot
* seaborn
* Pandas
* Time

## Using the API
1. Open a terminal (such as command prompt (win+R, cmd, enter)) and go to the folder where you cloned the repo.
2. Type the command ´´´uvicorn app:app --reload´´´ and press enter
3. open this link: (http://127.0.0.1:8000/docs/)
4. In "POST Price Predictor" fill out all fields and press execute.

## Delving deeper
If you want to explore the data or create a new model based on recent data, you can use these guidelines.
Open the Jupyter Notebook called data-analysis.ipynb.
Without modifcation, the code will import scraped_data_10.csv as a dataframe.
When you "Run All", all code blocks will run in sequence and create the visuals which can be found in the section Graphs of the notebook.

## Models
Three models where explored for this price predictor: Linear Regression, Decision Tree (with Grid Search) and XG Boost. XG Boost produced the best results, hence it was incorporated in the price predictor.

## Timeline
This project was created in July 2023 in two in-class coding challenge. 
* Data Analysis: between 05/07/2023 & 11/07/2023
* Implementing Machine Learning Models: between 17/07/2023 & 20/07/2023.
* Creating an API: between 26/07/2023 & 28/07/2023

## Contributors
This project was individual challenge and was fully written by the author Fré Van Oers with some help from the coaches at BeCode and fellow students.

## Acknowledgment
Learning a new skill is challenging. Therefore I would like to thank my fellow students and our coaches Vanessa & Sam for all the support they provided.

Created by [Fré Van Oers](https://www.linkedin.com/in/frevanoers/)
