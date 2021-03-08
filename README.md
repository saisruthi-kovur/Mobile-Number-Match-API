# EpikAssignment1
## Mobile Number Match

The file demo.py has the final code.
1) Purpose: To Compare 2 input mobile numbers (passed to API) and respond with a match found or not.

	a) Exact Match: If the given two inputs are exactly same.
	
	b) Intelligent Match: If the given two inputs follow the rules of 'valid phone number' of that particular country and is intelligent matched irrespective of changes in country codes (ISD Codes).
2) The code solves the above listed Requirements.
3) Here, I considered two countries: India, Australia and applied regex of that particular countries to validate if the input phone number is valid.

	a) Based on this, it also differentiates if a number is of India or of Australia.
	
		i) India: Uses ten-digit local phone numbers with country code +91 (if needed) and in case calls to non-local mobile numbers (ten-digit number) need to be prefixed with 0.
		
		ii) Australia: Uses eight-digit local phone numbers preceded by a two-digit STD area code (02,03,04,07,08) and country code is +61/61. Calling from outside Australia, leave out the leading '0' from the STD area code (2,3,4,7,8).
4) Based on above cases, two inputs can be identified if they are exactly matched or intelligently matched.
5) Further work: If any country has to be added to the same, just add the regex of that particular country mobile number and phone number conversions to the above code.

The file demo1.py has the code only for Indian Numbers.
