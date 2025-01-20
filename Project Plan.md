## Step 0: Create a Git Repository named housing-firstname-lastname

## Step 1: Implement the API with PostgreSQL

- Create a sub-project named `housing-api` and initialize a Python environment and dependency manager (by using Poetry and/or pyenv for example).
- Implement an API with the following routes:
  - `GET /houses`: Fetch houses as JSON.
  - `POST /houses`: Add a new house.
- Create a migration that create `houses` table with columns:
  - `longitude`: **float** -> A measure of how far west a house is; a higher value is farther west
  - `latitude`: **float** -> A measure of how far north a house is; a higher value is farther north
  - `housing_median_age`: **int** -> Median age of a house within a block; a lower number is a newer building
  - `total_rooms`: **int** -> Total number of rooms within a block
  - `total_bedrooms`: **int** -> Total number of bedrooms within a block
  - `population`: **int** -> Total number of people residing within a block
  - `households`: **int** -> Total number of households, a group of people residing within a home unit, for a block
  - `median_income`: **float** -> Median income for households within a block of houses (measured in tens of thousands of US Dollars)
  - `median_house_value`: **float** -> Median house value for households within a block (measured in US Dollars)
  - `ocean_proximity`: **string** (possible values: ["NEAR BAY","<1H OCEAN","INLAND","ISLAND","NEAR OCEAN"]) -> Location of the house w.r.t ocean/sea
- At least the API database connection `host` should be configurable.

```csv
longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value,ocean_proximity
-122.23,37.88,41,880,129,322,126,8.3252,452600.0,NEAR BAY
```

```json
{
  "longitude": -122,
  "latitude": 23,
  "housing_median_age": 37.88,
  "total_rooms": 41,
  "total_bedrooms": 880,
  "population": 129,
  "households": 322,
  "median_income": 126,
  "longitude": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}
```

- At the end of the step you should be able create houses and fetching them.

