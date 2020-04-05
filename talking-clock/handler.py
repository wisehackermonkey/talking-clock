"""
talking clock
returns word version of 24hour time

wisemonkey
oranbusiness@gmail.com
20181219
github.com/wisehackermonkey

run tests with command
python -m nose	
"""

hour_names = ["twelve","one","two","three","four","five","six","seven",
"eight","nine","ten","eleven","twelve","thirteen","fourteen",
"fifteen","sixteen","seventeen","eighteen","nineteen"]

tens = ["XX","ten", "twenty", "thirty", "fourty", "fifty"]

def talking_clock(time_str):
	hour,minute = time_str.split(":")

	return [int(hour[0:2]),int(minute[0:2])]
def time_in_words(time_str):
	hour,minute = talking_clock(time_str)
		# 24:32
		# thirty two
	daycycle = ""
	hour_word = ""
	min_word = ""
	if  hour < 13 and hour >=0:
			daycycle = "am"
	if hour > 12 and hour <= 24:
		hour -= 12
		daycycle = "pm"
	 

	if hour == 0 and minute == 0 :
		return f"{hour_names[hour]} {daycycle}"
	elif minute == 0 :
		return f"{hour_names[hour]} {daycycle}"
	elif minute <=9:
		min_word = f"oh {hour_names[minute]}"
	elif minute > 19:
		digit_one = int(str(minute)[0])
		digit_two = minute - (digit_one * 10)
		if digit_two == 0:
			min_word = f"{tens[digit_one]}"
		else:
			min_word = f"{tens[digit_one]} {hour_names[digit_two]}"

	else:
		min_word = hour_names[minute]
	return f"{hour_names[hour]} {min_word} {daycycle}"
	

def time_sentense(time_str):
	return time_in_words(time_str)


# print(time_in_words("15:30"))
# if 
# 		print("pm")
# elif x < 13 and x >=0:
# 		print("am")

# if x < 60 and x >= 0:
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return time_in_words(req)
