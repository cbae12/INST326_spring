1. Choose one of the following options and write the corresponding regular expression:
	- A regular expression to match any complete English word that starts with "t" and doesn't contain the letter "e" (e.g., "top", "tawny", "tarmac", but not "terp", "tree", "tower"); you can ignore hyphenated words and words with apostrophes
	- A regular expression to match any complete integer that is a multiple of four (hint: if the tens digit is even, or if the number has only a ones digit, the ones digit will be 0, 4, or 8; if the tens digit is odd, the ones digit will be 2 or 6)
	- A regular expression to match any complete English word that consists of all capital letters OR all lowercase letters (the expression should handle both capitalized ("GIRAFFE") and lower-case ("giraffe") words, but it should reject mixed-case words ("Giraffe", "GiRaFfE")); you can ignore hyphenated words and words with apostrophes
2. Use the re.search() function to apply your regular expression to a string; print the matching string.
3. Bonus: choose one of the following options; write the corresponding regular expression; apply it to a string using re.search() and print the value captured by one of the capturing groups in your expression:
	- A regular expression to match any nutrient line on the FDA-mandated Nutrition Facts label (Links to an external site.) (e.g., "Total Fat 8g 10%", "Sodium 160mg 7%", "Protein 3g"); assume there are spaces between the nutrient label, the measurement, and the percent daily value. Capture each of the following in separate capturing groups: the nutrient label, the measurement, and the percent daily value.
	- A regular expression to match any eyeglass prescription of the form EYE SPHERE CYL AXIS where
		- EYE is "OD" (right eye) or "OS" (left eye)
		- SPHERE is a number starting with a "+" or "-", a single digit, a decimal point, and two more digits (e.g., "+1.00", "-3.50"); negative values indicate nearsightedness, while positive values indicate farsightedness
		- CYL (a measurement of astigmatism) is either a number in the same format as SPHERE, or the abbreviation "SPH" (indicating no astigmatism)
		- AXIS is a one-to-three digit number (the axis of the astigmatism in degrees), but it is omitted if CYL has a value of "SPH"
		- Here are some examples: "OD -1.50 -2.25 34", "OS +4.75 SPH"
		- Only match strings that follow the specified format (so, don't match strings like "RE 1.2 -4 12")
		- Capture the values for EYE, SPHERE, CYL, and AXIS in separate capturing groups.
	- A regular expression to match any rank / book title / author / publication year line from this Guardian article (Links to an external site.) (e.g., "3. Gulliver’s Travels by Jonathan Swift (1726)", "34. Kim by Rudyard Kipling (1901)", "93. Money: A Suicide Note by Martin Amis (1984)"). Create separate capturing groups for the rank, the book title, the author's name, and the year of publication (but don't capture the parentheses).