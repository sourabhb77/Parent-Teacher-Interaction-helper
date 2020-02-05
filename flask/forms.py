from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,SelectField,BooleanField
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegistrationForm(FlaskForm):
    id= StringField('Username',validators=[DataRequired(),Length(min=2,max=7)])
    password =PasswordField('Password',validators=[DataRequired()])
    confirm_password =PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    id= StringField('Username',validators=[DataRequired(),Length(min=2,max=7)])
    password =PasswordField('Password',validators=[DataRequired()])
    submit =SubmitField('Log In')
    # po=RadioField('khjf')

class InternshipForm(FlaskForm):
    internship_announcement_number= StringField('Internship Applied As per College Intership announcement number:',validators=[DataRequired(),Length(min=1,max=7)])
    
    student_name= StringField('Name of student',validators=[DataRequired(),Length(min=2,max=30)])

    id= StringField('Roll number',validators=[DataRequired(),Length(min=2,max=7)])

    student_address= StringField('Student\'s address',validators=[DataRequired(),Length(min=2,max=40)])

    student_email= StringField('Email ID',validators=[DataRequired(),Email()])

    student_mobile= StringField('Mobile number',validators=[DataRequired()])

    parent_name= StringField('Name of parent/guardian',validators=[DataRequired()])

    parent_address= StringField('Parent\'s address',validators=[DataRequired()])

    parent_email= StringField('Parent\'s Email ID',validators=[DataRequired(),Email()])

    parent_mobile= StringField('Parent\'s Mobile number',validators=[DataRequired()])

    location= StringField('Location',validators=[DataRequired()])

    name_of_institute= StringField('Name of organization/institute:',validators=[DataRequired()])

    work_profile= StringField('Title/Work profile',validators=[DataRequired()])

    name_of_supervisor= StringField('Name of supervisor with contact details(Email/Address/Mob number)',validators=[DataRequired()])

    stipend= StringField('Stipend if any(per month)')

    days_missed= StringField('Total no of working instructional days may be missed as per academic calender',validators=[DataRequired()])

    semester= SelectField('Semester',choices=[(1,"June-November"),(2,"Jan-April")])

    type_of_internship= RadioField('Type of internship',choices=[(1,"Internal"),(2,"External")])

    year= SelectField('Year',choices=[(1,'F.Y.'),(2,'S.Y.'),(3,'T.Y.'),(4,'L.Y.')])

    course= SelectField('Course',choices=[(1,"B.Tech"),(2,"M.Tech")])

    branch= SelectField('Branch',choices=[(1,'Comp'),(2,'IT'),(3,'EXTC'),(4,'MECH')])

    division= SelectField('Division',choices=[(1,'A'),(2,'B')])

    # same_as_student= BooleanField('Same as student',validators=[DataRequired()])

    period= SelectField('Period',choices=[(1,"Summer"),(2,"Winter")])

    year_of_internship= SelectField('Year',choices=[(1,"2019"),(2,"2020"),(3,"2021"),(4,"2022")])
    # year_admission= SelectField('Year',choices=[(1,"2019"),(2,"2020"),(3,"2021"),(4,"2022")])

    # year_admission=SelectField('Year of admission',choices=[(1,'2016-2017'),(2,'2017-2018'),(3,'2018-2019'),(4,'2019-2020')])

    duration= StringField('Duration',validators=[DataRequired()])

    from_time= DateField('From',validators=[DataRequired()],format="'%m/%d/%Y'")

    to_time= DateField('To',validators=[DataRequired()],format="'%m/%d/%Y'")

    todays_date= DateField('Today\'s date',validators=[DataRequired()],format="'%m/%d/%Y'")
    # delete_photo =SubmitField('Delete photo')s

    submit_form= SubmitField('Send Email to confirm')



class ProctorForm(FlaskForm):
    #zero block
    year_of_admission=SelectField('Year of admission',choices=[(1,'2016-2017'),(2,'2017-2018'),(3,'2018-2019'),(4,'2019-2020')])
    # branch=SelectField('Branch',choices=['C.S','I.T.','EXTC','MECH','ETRX'])
    branch= SelectField('Branch',choices=[(1,'Comp'),(2,'IT'),(3,'EXTC'),(4,'MECH')])
    # year=RadioField('Year',choices=['F.Y','S.Y','T.Y','B.E'])
    year= SelectField('Year',choices=[(1,'F.Y.'),(2,'S.Y.'),(3,'T.Y.'),(4,'L.Y.')])

    # division= StringField('Division',validators=[ DataRequired(),Length(1)])
    division= SelectField('Division',choices=[(1,'A'),(2,'B')])

    id= StringField('Roll number',validators=[ DataRequired(),Length(7)])
    mobile_number= StringField('Mobile number',validators=[ DataRequired(),Length(10)])


    # first block
    name_of_proctor=StringField('Name of Proctor',validators=[DataRequired(),Length(min=10,max=50)])
    email_of_proctor=StringField('Email of Proctor',validators=[DataRequired(),Email()])
    mobile_number_of_proctor = StringField('Mobile number of proctor',validators=[DataRequired(),Length(min=2,max=10)])
    name_of_student=StringField('Name of student',validators=[DataRequired(),Length(max=50)])
    name_of_parent_guardian=StringField('Name of parent/guardian',validators=[DataRequired(),Length(min=10,max=50)])

    # second block
    pre_add_loc_add_hos_add=StringField('Present Address/Local Address/Hostel Address',validators=[DataRequired(),Length(min=50,max=150)])
    parent_pre_add_loc_add_hos_add=StringField('Present Address/Local Address/Hostel Address of parents',validators=[DataRequired(),Length(min=50,max=150)])
    # same_as_student=BooleanField('Same as student',validators=[DataRequired()])
    nav_place_permt_add=StringField('Native Place/Permanent Address',validators=[DataRequired(),Length(min=50,max=300)])
    residential=StringField('Residential',validators=[DataRequired(),Length(min=2,max=10)])
    office=StringField('Office',validators=[DataRequired(),Length(min=2,max=10)])
    ptr_mobile_number=StringField('Mobile Number',validators=[DataRequired(),Length(min=2,max=10)])
    stu_email_id=StringField('Student Email ID',validators=[DataRequired(),Email()])
    prt_email_id=StringField('Parent Email ID',validators=[DataRequired(),Email()])
    
    #third block
    blood_group=SelectField('Blood Group',choices=[(1,'A+'),(2,'B+'),(3,'AB+'),(4,'O+'),(5,'A-'),(6,'B-'),(7,'AB-'),(8,'O-')])
    any_disease_disability=RadioField('Any disease/disability',choices=[(1,'YES'),(2,'NO')])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()], format="'%m-%d-%y'")
    place_of_birth=StringField('Place of birth',validators=[DataRequired(),Length(min=2,max=20)])
    mother_tongue=StringField('Mother tongue',validators=[DataRequired(),Length(min=2,max=20)])
    religion=StringField('Religion',validators=[DataRequired(),Length(min=2,max=20)])
    exam=RadioField(''' Score at the competative exam based on which admission to KJSCE is taken: 
    Name of that exam''',choices=[(1,'JEE'),(2,'CET'),(3,'DIPLOMA')])
    score=StringField('Score',validators=[DataRequired(),Length(min=2,max=5)])
    per_ssc_marks=StringField('%SSC marks',validators=[DataRequired(),Length(min=2,max=5)])
    per_hsc_marks=StringField('%HSC/Diploma marks',validators=[DataRequired(),Length(min=2,max=5)])

    #fourth block
    discipline=BooleanField('''The information given above is true to the best of my knowledge and I will adhere to the rules
     and regulations of the college/campus specifically behaviour discipline, attendance, ragging and intellectual property 
     rights during the tenure of completion of the undergraduate/postgraduate programme.''',validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], format="'%m-%d-%y'")

    # photo section
    # photo=FileField(validators=[FileRequired()])
    photo=StringField('photo',validators=[DataRequired(),Length(min=2,max=20)])
    #submit button
    submit=SubmitField('Submit Form')





