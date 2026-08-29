# 📘 Assignment: Data Visualization with Pandas and Matplotlib

## 🎯 Objective

Analyze a real dataset and use Python libraries to summarize trends and create clear visualizations. This assignment helps students practice data cleaning, grouping, chart design, and explaining findings from graphs.

## 📝 Tasks

### 🛠️ Load and Explore a Dataset

#### Description
Read a CSV file into a pandas DataFrame and inspect its structure before creating any charts.

#### Requirements
Completed program should:

- Import `pandas` and load the provided dataset.
- View the first few rows using `.head()`.
- Print the number of rows and columns.
- Check the column names and data types.
- Identify at least one column that should be converted to a date or numeric type if needed.
- Example output:
  ```python
  print(df.head())
  print(df.shape)
  ```

### 🛠️ Summarize Trends in the Data

#### Description
Group or filter the dataset to calculate meaningful summary statistics.

#### Requirements
Completed program should:

- Use grouping, filtering, or sorting to answer a simple question about the dataset.
- Calculate totals, averages, or monthly trends.
- Display the result using a pandas DataFrame or printed summary.
- Example analysis questions:
  - Which month had the highest sales?
  - What is the average value for a category?
  - Which product or region performed best?

### 🛠️ Create Visualizations

#### Description
Use Matplotlib to create charts that communicate the story in the data.

#### Requirements
Completed program should:

- Create at least two different charts, such as a line chart, bar chart, or scatter plot.
- Add labels to the axes and a title to each chart.
- Use colors or styling that make the graph readable.
- Save one chart as a PNG file.
- Example:
  ```python
  plt.plot(months, sales)
  plt.title("Monthly Sales")
  plt.xlabel("Month")
  plt.ylabel("Revenue")
  plt.show()
  ```

### 🛠️ Explain What the Charts Show

#### Description
Write a short summary explaining the patterns visible in the graphs.

#### Requirements
Completed program should:

- Describe at least two insights from the visualizations.
- Explain what happened during a peak or drop in the data.
- Include a final paragraph summarizing what the chart suggests about the dataset.
- Example insight:
  - "Sales increased sharply during the summer months and declined in the fall."
