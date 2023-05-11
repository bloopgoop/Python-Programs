def AcceptOrReject(gpa, testScore):
    if gpa < 3:
        if testScore > 80:
            return "Accepted"
        else:
            return "Rejected"
    else:
        if testScore > 60:
            return "Accepted"
        else:
            return "Rejected"

def main():
    student_name = input("What is your name?\n")
    gpa = float(input("What is your gpa?\n"))
    testScore = float(input("What is your test score?\n"))
    print(AcceptOrReject(gpa, testScore))

main()