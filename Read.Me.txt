Titanic Survival Analysis



Description

This is my first data analysis project. I explored the famous Titanic dataset from Kaggle to understand which factors helped passengers survive the disaster.

Main questions I tried to answer:
- What was the overall survival rate?
- Did gender affect survival chances?
- How did passenger class (1st, 2nd, 3rd) influence survival?
- Was age an important factor in survival?

Tools & Technologies

Language: Python 3
Libraries:
  - pandas → data cleaning and analysis
  - numpy → numerical operations
  - matplotlib & seaborn → data visualization

Environment: Jupyter Notebook
Dataset: [Titanic – Machine Learning from Disaster](https://www.kaggle.com/c/titanic) (train.csv)

Key Findings

Overall survival rate: **~38.4%** of passengers in the training set survived.
Gender had a massive impact:
  - Women: ~74% survival rate
  - Men: ~19% survival rate
Passenger class strongly influenced survival:
  - 1st class: ~63% survived
  - 2nd class: ~47% survived
  - 3rd class: ~24% survived

Children (age < 15) had a higher survival rate than adults in most classes.
Most expensive tickets (highest fares) were strongly associated with 1st class and better survival odds.



How to Run the Project

1. Clone or download this repository
2. Make sure you have Python installed (3.8 or higher recommended)
3. Install required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter