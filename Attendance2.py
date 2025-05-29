def main():
    # Step 1: Input total number of students
    total_students = int(input("Enter the total number of students in the class: "))
    
    # Step 2: Input total number of periods
    while True:
        total_periods = int(input("Enter total number of periods of the class held in the week (between 1 and 5): "))
        if 1 <= total_periods <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
            
    # Step 3: Initialise student data list
    students = []
    
    # Step 4: Gather data for each student
    for i in range(total_students):
        print()
        name = input(f"Enter name for student {i + 1}: ")
        attendance = []
        for j in range(total_periods):
            while True:
                status = input(f"Enter attendance for {name} (P/A) for period {j + 1}: ").upper()
                if status in ['P', 'A']:
                    attendance.append(status)
                    break
                else:
                    print("Invalid input. Enter 'P' for Present or 'A' for Absent.")
        students.append({'name': name, 'attendance': attendance})
        
    print("\nAttendance Report:")
    report_lines = []
    
    # Step 5: Process and display attendance data
    for student in students:
        name = student['name']
        attendance = student['attendance']
        total_present = attendance.count('P')
        percentage = (total_present / total_periods) * 100
        line = f"{name}: {total_present} periods present ({percentage:.0f}%)"
        if percentage < 75:
            line += "- Warning: Low attendance"
        print(line)
        report_lines.append(line)
        
    # Step 6: Write data to file
    with open("attendance.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']}: {''.join(student['attendance'])}\n")
            
    print("\nData written to file.")
    
    
if __name__ == '__main__':
    main()
        
        
        
    
    
                
