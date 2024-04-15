import pandas as pd

def calculate_demographic_data(file_path):
    # Read data from CSV file
    df = pd.read_csv(file_path)
    
    # 1. How many people of each race are represented in this dataset? 
    race_counts = df['race'].value_counts()
    
    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    
    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich_percentage = (len(higher_education_rich) / len(higher_education)) * 100
    
    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    lower_education_rich_percentage = (len(lower_education_rich) / len(lower_education)) * 100
    
    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = (len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers) * 100
    
    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').mean() * 100
    
    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Return results as a dictionary
    return {
        "race_count": race_counts.to_dict(),
        "average_age_men": round(average_age_men, 1),
        "percentage_bachelors": round(percentage_bachelors, 1),
        "higher_education_rich_percentage": round(higher_education_rich_percentage, 1),
        "lower_education_rich_percentage": round(lower_education_rich_percentage, 1),
        "min_work_hours": min_work_hours,
        "rich_percentage": round(rich_percentage, 1),
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": round(highest_earning_country_percentage, 1),
        "top_IN_occupation": top_IN_occupation
    }

# Test the function
result = calculate_demographic_data("adult.data.csv")
for key, value in result.items():
    print(f"{key}: {value}")
