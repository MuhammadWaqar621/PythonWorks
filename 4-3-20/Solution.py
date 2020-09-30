import datetime as dt


def daysToReview(text):
    # Splitting the text and storing in array
    splitted_string = text.split(" ")
    print(splitted_string)
    # Extracting name
    name = splitted_string[1] + " " + splitted_string[2]

    # Extracting assigned date and month
    # d means date and b is used for abrivated month name
    assigned_date = dt.datetime.strptime(splitted_string[6] + " " + splitted_string[7], "%b %d")
    submitted_date = dt.datetime.strptime(splitted_string[11] + " " + splitted_string[12], "%b %d")
    days_difference = submitted_date-assigned_date

    # Showing Output
    if days_difference.days == 0:
        print(name, "submited this review on the day it was assigned")
    else:
        print(name, "completed this review in", days_difference.days, " days")
    
    
def main():
    text = "Reviewer Jean Sharlow / Review assigned jan 23 / Review submitted feb 19"
    daysToReview(text)
    # Remove all spaces and store each word in a list
    # Output must be like
    # Jean Sharlow completed this review on the day it was assigned


if __name__ == '__main__':
    main()