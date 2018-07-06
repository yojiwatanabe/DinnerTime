# DINNERTIME
### Written by Yoji Watanabe - Fall 2017
_DinnerTime_ is a script that helps users to find the optimal meeting ('dinner') times for people with varying availabilities.
***

#### Current Features
* Randomly assign dinner times for a week of dinners and check availability of guests
* Evaluate how good these dinner times are based on guest availability and variability
* Pack information about guest availability & variability at dinners and the dinner times in a 64-bit string of bits
* Retrieve all of a week's dinners information from a 64-bit string

#### Inputting data

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
