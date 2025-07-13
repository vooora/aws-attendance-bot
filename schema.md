Tables:

Users(StudentID, Name, BatchNumber, Branch, FingerprintURL)
Professor(ProfessorID, Name)
Course(CourseID, CourseName, ProfessorID)
Exam(ExamID, StartTime, EndTime, CourseID)
ExamAttendance(EntryID, CourseID, StudentID, StudentInTime, StudentOutTime)
CourseRegistrations(RegistrationID, CourseID, StudentID)

Relationships:

- Exam.CourseID -> Course.CourseID
- ExamAttendance.CourseID -> Course.CourseID
- ExamAttendance.StudentID -> Users.StudentID
- CourseRegistrations.CourseID -> Course.CourseID
- CourseRegistrations.StudentID -> Users.StudentID
- Course.ProfessorID -> Professor.ProfessorID
