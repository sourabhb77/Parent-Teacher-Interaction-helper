# not used all models
class StudentInfo(db.Model):
    id=db.Column(db.String(7),primary_key=True)
    parent_id=db.Column
    year_of_admission=db.Column(db.String(15),nullable=False)
    branch=db.Column(db.String(5),nullable=False)
    year=db.Column(db.String(5),nullable=False)
    division=db.Column(db.String(1),nullable=False)
    mobile_number=db.Column(db.String(10),nullable=False)
    name_of_student=db.Column(db.String(30),nullable=False) 
    name_of_parent_guardian=db.Column(db.String(30),nullable=False)

    pre_add_loc_add_hos_add=db.Column(db.String(150),nullable=False)
    nav_place_permt_add=db.Column(db.String(150),nullable=False)
    stu_email_id=db.Column(db.String(25),nullable=False)
    blood_group=db.Column(db.String(4),nullable=False)
    any_disease_disability=db.Column(db.String(70),nullable=False)
    date_of_birth=db.Column(db.String(15),nullable=False)
    place_of_birth=db.Column(db.String(70),nullable=False)
    mother_tongue=db.Column(db.String(20),nullable=False)
    religion=db.Column(db.String(20),nullable=False)
    exam=db.Column(db.String(10),nullable=False)
    score=db.Column(db.String(5),nullable=False)
    per_ssc_marks=db.Column(db.String(3),nullable=False)
    per_hsc_marks=db.Column(db.String(3),nullable=False)

    discipline=db.Column(db.String(50),nullable=False)
    date=db.Column(db.String(15),nullable=False)
    photo=db.Column(db.LargeBinary)

    # for StudentInfo and ProctorInfo(M:1)

    proctor_id=db.Column(db.String(7),db.ForeignKey('proctorinfo.id'))
    
    # for StudentInfo and ParentInfo (1:1)

    parent=db.relationship('ParentInfo',backref='studentinfo',uselist=False)
    
    # for studentinfo and internship(1:M)
    internship=db.relationship('IntForm',backref='intern')

 



class ParentInfo(db.Model):
    id=db.Column(db.String(7),primary_key=True)
    name_of_parent_guardian=db.Column(db.String(30),nullable=False)
    parent_pre_add_loc_add_hos_add=db.Column(db.String(150),nullable=False)
    office=db.Column(db.String(150),nullable=False)
    ptr_mobile_number=db.Column(db.String(10),nullable=False)
    prt_email_id=db.Column(db.String(25),nullable=False)
    photo=db.Column(db.LargeBinary)


    # for StudentInfo and ParentInfo (1:1)
    student_id=db.Column(db.String(7),db.ForeignKey('studentinfo.id'))


class ProctorInfo(db.Model):
    id=db.Column(db.String(7),primary_key=True)
    name_of_proctor=db.Column(db.String(30),nullable=False)
    email_of_proctor=db.Column(db.String(25),nullable=False)
    mobile_number_of_proctor=db.Column(db.String(10),nullable=False)
    photo=db.Column(db.LargeBinary)

    # for StudentInfo and ProctorInfo(M:1)
    student=db.relationship('StudentInfo',backref='stu')





class IntForm(db.Model):
    semester= db.Column(db.String(13),nullable=False)
    internship_announcement_number=db.Column(db.String(15))
    type_of_internship= db.Column(db.String(10),nullable=False)
    year=db.Column(db.String(5),nullable=False)
    course=db.Column(db.String(8),nullable=False)
    period=db.Column(db.String(10),nullable=False)
    year_of_internship=db.Column(db.String(5),nullable=False)
    duration=db.Column(db.String(10),nullable=False)
    from_time=db.Column(db.String(10),nullable=False)
    to_time=db.Column(db.String(10),nullable=False)
    location=db.Column(db.String(20),nullable=False)
    name_of_institute=db.Column(db.String(50),nullable=False)
    work_profile=db.Column(db.String(50),nullable=False)
    name_of_supervisor=db.Column(db.String(20),nullable=False)
    stipend=db.Column(db.String(10))
    days_missed=db.Column(db.String(10))
    todays_date=db.Column(db.String(10),nullable=False)
    # for studentinfo and internship(1:M)
    stu_id=db.Column(db.String(7),db.ForeignKey('studentinfo.id'))



















    
