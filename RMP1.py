class Student {
  String name;
  int math;
  int physics;
  int chemistry;

  Student(this.name, this.math, this.physics, this.chemistry);

  double average() {
    return (math + physics + chemistry) / 3;
  }

  void showDetails() {
    print('Name: $name');
    print('Total score: ${math + physics + chemistry}');
  }
}

void main() {
  var student = Student('John Doe', 85, 90, 80);
  print('Average score: ${student.average()}');
  student.showDetails();
}

