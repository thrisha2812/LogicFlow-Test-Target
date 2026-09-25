import java.util.*;

class Student {
    private int id;
    private String name;
    private double marks;

    public Student(int id, String name, double marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getMarks() {
        return marks;
    }

    public void display() {
        System.out.println(
            id + " | " + name + " | " + marks
        );
    }
}

class StudentManager {
    private List<Student> students;

    public StudentManager() {
        students = new ArrayList<>();
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public Student findStudent(int id) {
        for (Student student : students) {
            if (student.getId() == id) {
                return student;
            }
        }
        return null;
    }

    public double calculateAverage() {
        if (students.isEmpty()) {
            return 0;
        }

        double total = 0;

        for (Student student : students) {
            total += student.getMarks();
        }

        return total / students.size();
    }

    public void displayStudents() {
        System.out.println("\n--- Student List ---");

        for (Student student : students) {
            student.display();
        }
    }
}

class GradeService {

    public String calculateGrade(double marks) {

        if (marks >= 90) {
            return "A";
        } else if (marks >= 75) {
            return "B";
        } else if (marks >= 60) {
            return "C";
        } else if (marks >= 50) {
            return "D";
        }

        return "F";
    }

    public void displayGrade(Student student) {

        String grade =
            calculateGrade(student.getMarks());

        System.out.println(
            student.getName() +
            " -> Grade: " + grade
        );
    }
}

class ReportService {

    private StudentManager manager;
    private GradeService gradeService;

    public ReportService(
        StudentManager manager,
        GradeService gradeService
    ) {
        this.manager = manager;
        this.gradeService = gradeService;
    }

    public void generateReport() {

        manager.displayStudents();

        System.out.println(
            "\nAverage Marks: " +
            manager.calculateAverage()
        );
    }

    public void displayStudentGrade(int id) {

        Student student =
            manager.findStudent(student);

        if (student == null) {
            System.out.println("Student not found");
            return;
        }

        gradeService.displayGrade(student);
    }
}

public class StudentManagement {

    public static void main(String[] args) {

        StudentManager manager =
            new StudentManager();

        Student s1 =
            new Student(101, "Rahul", 85);

        Student s2 =
            new Student(102, "Ananya", 92);

        Student s3 =
            new Student(103, "Arjun", 68);

        manager.addStudent(s1);
        manager.addStudent(s2);
        manager.addStudent(s3);

        GradeService gradeService =
            new GradeService();

        ReportService report =
            new ReportService(
                manager,
                gradeService
            );

        report.generateReport();

        report.displayStudentGrade(101);
        report.displayStudentGrade(102);
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> 5f8f9a762e2bde4a980afb2b784f36e9fca0ea76
