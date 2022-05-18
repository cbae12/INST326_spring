# Exercise: Exploring Olympic speed skating data
<hr/>

## Table of Contents
[Problem statement](#problem-statement)<br/>
[Data](#data)<br/>
&emsp;[Dealing with NaN values](#dealing-with-nan-values)<br/>
&emsp;&emsp;[.dropna()](#dropna)<br/>
&emsp;&emsp;[.fillna(VALUE)](#fillnavalue)<br/>
[Instructions](#instructions)<br/>
[Submission](#submission)<br/>
<hr/>

## Problem statement
Create a Jupyter notebook in which you use a variety of Pandas features to explore a data set consisting of men’s 1500m speed skating results from the 2006, 2010, 2014, 2018, and 2022 Winter Olympics.
<hr/>

## Data
The files mens1500_2006.csv, mens1500_2010.csv, mens1500_2014.csv, mens1500_2018.csv, and mens1500_2022.csv all have the following columns:

- Rank: the order in which the athlete finished (1 represents a first-place finish)

- Athlete: the name of the athlete

- Country: a three-letter abbreviation of the country the athlete represents

- Result: the time in which the athlete completed the event

- Finished: 1 if the athlete finished the race; 0 otherwise

- Year: the year in which the competition took place

The file *speed_skaters.csv* has the following columns:

- Name: the name of the athlete

- Birth year: the year the athlete was born

- Height: the athlete’s height in meters

- Weight: the athlete’s weight in kilograms

    * Note: a *NaN* ("not a number") value indicates the athlete’s weight is unknown; see [Dealing with NaN values](#dealing-with-nan-values) below
<hr/>

### Dealing with NaN values
If your analysis does not involves a column that contains *NaN* values, you can just ignore them. If your analysis depends on a column with *NaN* values, Pandas gives you at least two ways to deal with them:

#### .dropna()
*.dropna()* throws out all rows that contain *NaN*. This is a method of DataFrame objects and by default it returns a new DataFrame object containing all the rows from the original DataFrame that have no *NaN* values. Below is an example.

&emsp;*df1 = read_csv("mydata.csv")*<br/>
&emsp;*df2 = df1.dropna()*<br/>

#### .fillna(VALUE)
*.fillna(VALUE)* replaces *NaN* values with some other value you specify. This is a method of DataFrame objects and by default it returns a new DataFrame object containing all the rows from the original DataFrame, but with *NaN* values replaced with the value you specify. Below is an example.

&emsp;*df1 = read_csv("mydata.csv")*<br/>
&emsp;*df2 = df1.fillna(0)*<br/>
<hr/>

## Instructions
Create a Jupyter notebook in which you do the following:

Import Pandas.

Read in all the CSV files. Concatenate all of the result files (*mens1500_**) into a single DataFrame. Merge the results with the athlete information (from *speed_skaters.csv*) into a single DataFrame.

Use boolean indexing with two criteria to filter the DataFrame. Explain in a Markdown cell what data you selected.

Use the split-apply-combine methodology to analyze the DataFrame in some way. In a Markdown cell, explain what you did.

Please do different analyses than the ones in the lecture videos.
<hr/>

## Submission
Submit your Jupyter notebook on Gradescope.
<hr/>