# Surfs Up!

## Overview of Analysis
The purpose of this analysis was to review weather data for an investor to determine if opening up a Surf n' Shake (ice cream and surf shop) would be a smart decision. The weather data that was focused on was the temperature statistics for the months of June and December in Oahu, Hawaii. 

The data was analyzed using SQLite in Jupyter Notebook, using SQLAlchemy to connect the SQLite to JN.

## Results 
**June Stats**
- The average tempertature for June was 74.9 degrees
- The highest temperature for June was 85.0 degrees
- The lowest temperature for June was 64.0 degrees
**December Stats**
- The average temperature for December was 71.0 degrees
- The highest temperature for December was 83.0 degrees
- The lowest temperature for December was 56.0 degrees

*Full statistics for each month can be seen below*
### June Temps
![June_temps](https://user-images.githubusercontent.com/102814578/175187689-4539e9f7-e2eb-4b9c-989c-4c8b05e025de.png)

### December Temps
![Dec_temps](https://user-images.githubusercontent.com/102814578/175187678-d80714d9-09a7-4a74-962f-8a9c5a950e2e.png)

## Summary
The temperatures in Oahu stay pretty coinsistent throughout the year. Through the summer month of June and the winter month of December ther average temperature only varied byh 3.9 degrees. The high temperatures only differed by 2 degrees, and the low temperatures differed by 6 degrees. Even though the low temperature in December is 56 degrees, I would say the ranges of these temperatures are well within "ice cream-weather" range (since daily lows often occur in the middle of the night).

Additonal queries I would run would be the preciptiaion statisitcs for June and December. Rain often plays a part into quality of the surf, but more importantly, how many people are likely to go out to the beach in general. The precipitaion statistics are as follows:

### June Precip
![june_precip](https://user-images.githubusercontent.com/102814578/175194179-f9aaaab9-b023-45a1-9591-7cdbf6c2e738.png)


### December Precip
![Dec_precip](https://user-images.githubusercontent.com/102814578/175194151-d786e08a-8d4c-4847-826b-239f52d9dd1c.png)
