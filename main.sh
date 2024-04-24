#!/bin/bash

# Function to create a new student record
create_student() {
    echo "Enter student email:"
    read email
    echo "Enter student age:"
    read age
    echo "Enter student ID:"
    read student_id

    # Append student record to the file
    echo "$email, $age, $student_id" >> students-list_1023.txt
    echo "Student record created successfully."
}

# Function to view all students
view_students() {
    echo "List of students:"
    cat students-list_1023.txt
}

# Function to delete a student record by ID
delete_student() {
    echo "Enter student ID to delete:"
    read delete_id
    # Use sed to delete the line with the matching student ID
    sed -i "/^$delete_id,/d" students-list_1023.txt
    echo "Student record deleted successfully."
}

# Function to update a student record by ID
update_student() {
    echo "Enter student ID to update:"
    read update_id
    echo "Enter new email:"
    read new_email
    echo "Enter new age:"
    read new_age

    # Use sed to find and replace the student record with the new information
    sed -i "s/^$update_id,.*/$new_email, $new_age, $update_id/" students-list_1023.txt
    echo "Student record updated successfully."
}

# Function to select emails of students and save them to student-emails.txt
select_emails() {
    cut -d ',' -f 1 students-list_1023.txt > student-emails.txt
    echo "Emails of students have been saved to student-emails.txt"
}

# Main menu loop
while true; do
    echo "1. Create student record"
    echo "2. View all students"
    echo "3. Delete student record"
    echo "4. Update student record"
    echo "5. Select emails of students"
    echo "6. Exit"
    read choice

    case $choice in
        1) create_student ;;
        2) view_students ;;
        3) delete_student ;;
        4) update_student ;;
        5) select_emails ;;
        6) echo "Exiting program."; exit ;;
        *) echo "Invalid choice. Please select a valid option." ;;
    esac
done

