# CSV = CSV stand for Comma Separated Value.
# Using the CSV building the students marks reader.
import csv
# Opening the marks.csv.
with open('marks.csv', 'r', newline='') as csv_file:
    # Reading the file DictReader, so that each row is Dictionary.    
    csv_reader = csv.DictReader(csv_file)
    topper_name = ""
    topper_total = 0
    for row in csv_reader:
        # convert each subject mark from text to a number
        science = int(row['science'])
        mathematics = int(row['mathematics'])
        english = int(row['english'])
        hindi = int(row['hindi'])
        computer_science = int(row['computer-science'])
        # add the 5 marks → student's total
        total_marks = science + mathematics + english + hindi + computer_science
        # percentage = total ÷ 500 × 100
        percentage = total_marks/500 * 100
        # finding topper according to marks
        if total_marks > topper_total:
            topper_name = row['names']
            topper_total = total_marks
        # show name, total, percentage
        print(f"{row['names']}: total marks:{total_marks} percentage:{round(percentage, 2)} %")
    print(f"Topper: {topper_name} with {topper_total} marks")