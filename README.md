# NFL QB Pass Distribution (2024 Season)

This project looks at NFL quarterback passing data from the 2024 season. I used Python to explore how different QBs performed in terms of total passing yards and to visualize how passing stats are distributed across the league.

## Data Source
The data comes from the `nfl_data_py` package, which provides official NFL play-by-play data. I focused on the 2024 regular season.

## Tools and Libraries
- pandas
- matplotlib
- seaborn
- nfl_data_py

## What the Project Does
1. Downloads 2024 NFL play-by-play data  
2. Filters for quarterback passing plays  
3. Calculates total passing yards per QB  
4. Creates visualizations including:
   - A histogram of total passing yards
   - A box plot showing passing yard distribution
   - A bar chart showing the top 10 QBs by total passing yards

## Results
The graphs help show how most QBs fall within a similar yardage range, while a few top players clearly stand out as outliers with much higher totals.

## How to Run
1. Make sure you have Python installed  
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn nfl_data_py
