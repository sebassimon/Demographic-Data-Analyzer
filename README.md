<h1>Demographic Data Analysis</h1>

### Insights ###
<li>race_count: {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271} </li>
<li>average_age_men: 39.4 </li>
<li>percentage_bachelors: 16.4</li>
<li>higher_education_rich_percentage: 46.5</li>
<li>lower_education_rich_percentage: 17.4</li>
<li>min_work_hours: 1</li>
<li>rich_percentage: 10.0 </li>
<li>highest_earning_country: Iran </li>
<li>highest_earning_country_percentage: 41.9 </li>
<li>top_IN_occupation: Prof-specialty</li>

<h2>Description</h2>
<p>This project analyzes demographic data from the 1994 Census to explore employment and income trends across different demographics using Pandas.</p>

<h2>Environments & Libraries Used</h2>
<ul>
  <li><b>Python</b></li>
  <li><b>Pandas</b></li>
</ul>

<h2>Program Walk-through:</h2>

<h3>1. Race Distribution</h3>
<pre><code>race_counts = df['race'].value_counts()</code></pre>
<br />

<h3>2. Average Age of Men</h3>
<pre><code>average_age_men = df[df['sex'] == 'Male']['age'].mean()</code></pre>
<br />

<h3>3. Bachelors Degree Holders Percentage</h3>
<pre><code>percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100</code></pre>
<br />

<h3>4. Higher Education Impact on Salary >50K</h3>
<pre><code>higher_education_rich_percentage = (higher_education[higher_education['salary'] == '>50K'].size / higher_education.size) * 100</code></pre>
<br />

<h3>5. Non-Higher Education Impact on Salary >50K</h3>
<pre><code>lower_education_rich_percentage = (lower_education[lower_education['salary'] == '>50K'].size / lower_education.size) * 100</code></pre>
<br />

<h3>6. Minimum Working Hours</h3>
<pre><code>min_work_hours = df['hours-per-week'].min()</code></pre>
<br />

<h3>7. Analysis of Min Work Hours and High Salary</h3>
<pre><code>rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].size / df[df['hours-per-week'] == min_work_hours].size) * 100</code></pre>
<br />

<h3>8. Top Earning Country and Its Percentage</h3>
<pre><code>highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
highest_earning_country_percentage = (df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].size / df[df['native-country'] == highest_earning_country].size) * 100</code></pre>
<br />

<h3>9. Most Popular Occupation in India for High Earners</h3>
<pre><code>top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()</code></pre>
<br />

<h2>Conclusion</h2>
<p>This analysis provides crucial insights into how different demographic factors affect employment and income, highlighting the impact of education on salary and the distribution of working hours.</p>
