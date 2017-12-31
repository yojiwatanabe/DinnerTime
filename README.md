# DINNER TIME
#### Written by Yoji Watanabe - Fall 2017
_Dinner Time_ is a small application that allows users to find the optimal dinner time for people with varying availabilities.
***

*Inputting data*

Open the file called _data.dinner_, and input each piece of data for each person as follows, followed by a new line:
* Name
* Availability, in binary format
	* 0-1 if available at the following time periods for each of the 5 days, so the result is a word with 20 booleans for a week with four dinners with five possible times:
	* 6:00-6:29, 6:30-6:59, 7:00-7:29, 7:30-7:59, 8:00-8:29

Example, for a person Yoji who is available from 6:00-6:59 and 8:00-8:29 on days one and three, and available at all five times on days two and four:
* Yoji 11001111111100111111

*Example _data.dinner_:*
```
Yoji 11001011010011111111
Mauri 00101111001100000011
Jake 11100100111100111101
Aidan 01111110011111011111
```
