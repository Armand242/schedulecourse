from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Courses(db.Model):
    id = db.Column('course_id', db.Integer, primary_key=True)
    course_num = db.Column(db.String(100))
    semester = db.Column(db.String(50))
    time = db.Column(db.String(20))
    course_name = db.Column(db.String(100))
    course_level = db.Column(db.String(100))
    course_des = db.Column(db.String(100))
    course_prereq = db.Column(db.String(100))
    instructor_num = db.Column(db.String(100))
    instructor_name = db.Column(db.String(100))
    instructor_BD = db.Column(db.String(100))
    instructor_gender = db.Column(db.String(100))
    instructor_nationality = db.Column(db.String(100))
    instructor_edu = db.Column(db.String(100))
    instructor_degree = db.Column(db.String(100))
    instructor_bio = db.Column(db.String(100))



    def __init__(self, course_num, semester, time, course_name,
                 course_level, course_des, course_prereq, instructor_num,
                 instructor_name, instructor_BD, instructor_gender,
                 instructor_nationality, instructor_edu,
                 instructor_degree, instructor_bio):
        self.course_num = course_num
        self.semester = semester
        self.time = time
        self.course_name = course_name
        self.course_level = course_level
        self.course_des = course_des
        self.course_prereq = course_prereq
        self.instructor_num = instructor_num
        self.instructor_name = instructor_name
        self.instructor_BD = instructor_BD
        self.instructor_gender = instructor_gender
        self.instructor_nationality = instructor_nationality
        self.instructor_edu = instructor_edu
        self.instructor_degree = instructor_degree
        self.instructor_bio = instructor_bio

class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    course_num = db.Column(db.String(100))
    student_name = db.Column(db.String(50))
    studentid = db.Column(db.String(50))



    def __init__(self, course_num,student_name, studentid):
        self.course_num = course_num
        self.student_name = student_name
        self.studentid = studentid






@app.route('/mainpage')
def Schedule():
    return render_template('Schedule.html')

@app.route('/')
def show_all():
    return render_template('show_all.html', Courses=Courses.query.all() , Student = Student.query.all())



@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['course_num'] \
        or not request.form['semester'] \
        or not request.form['time'] \
        or not request.form['course_name']\
        or not request.form['course_level'] \
        or not request.form['course_des']\
        or not request.form['course_prereq']\
        or not request.form['instructor_num'] \
        or not request.form['instructor_name']\
        or not request.form['instructor_BD'] \
        or not request.form['instructor_gender']\
        or not request.form['instructor_nationality'] \
        or not request.form['instructor_edu']\
        or not request.form['instructor_degree'] \
        or not request.form['instructor_bio']:
            flash('Please enter all the fields', 'error')
        else:
            course = Courses(request.form['course_num'],
            request.form['semester'], request.form['time'],
            request.form['course_name'], request.form['course_level'],
            request.form['course_des'], request.form['course_prereq'],
            request.form['instructor_num'], request.form['instructor_name'],
            request.form['instructor_BD'], request.form['instructor_gender'],
            request.form['instructor_nationality'], request.form['instructor_edu'],
            request.form['instructor_degree'], request.form['instructor_bio'])
            db.session.add(course)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/student1', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        if not request.form['course_num']\
        or not request.form['student_name'] \
        or not request.form['studentid']:
            flash('Please enter all the fields', 'error')
        else:
            student = Student(request.form['course_num'], request.form['student_name'], request.form['studentid'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('students.html')



@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)