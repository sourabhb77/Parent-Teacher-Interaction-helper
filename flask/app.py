from flask import Flask,render_template,url_for,request,redirect,session,flash,send_file,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm,ProctorForm,InternshipForm
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_login import LoginManager,login_user,current_user,logout_user,login_required,UserMixin
from flask_mail import Mail,Message
from itsdangerous import URLSafeTimedSerializer , SignatureExpired
from io import BytesIO
import os
from werkzeug.utils import secure_filename
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app=Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\SOURABH\\Desktop\\py_project\\flask\\certificates'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','pdf','docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='abcde'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
bcrypt=Bcrypt(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='proctorsoft@gmail.com',
    MAIL_PASSWORD='dsmddsmd'
)
mail=Mail(app)
s=URLSafeTimedSerializer('abcde')
db = SQLAlchemy(app)

admin=Admin(app)

login_manager = LoginManager()
login_manager.login_view='login'
login_manager.session_protection = 'strong'
login_manager.login_message_category='info'
login_manager.init_app(app)

class User(db.Model,UserMixin):
    id=db.Column(db.String(7),primary_key=True)
    password=db.Column(db.String(50),nullable=False)
    def __repr__(self):
        return f"(User('{self.id}','{self.password}'))"


class IntForm(db.Model,UserMixin):
    id= db.Column(db.String(7),primary_key=True)
    semester= db.Column(db.String(13),nullable=False)
    internship_announcement_number=db.Column(db.String(15))
    type_of_internship= db.Column(db.String(10),nullable=False)
    student_name= db.Column(db.String(30),nullable=False)
    student_address= db.Column(db.String(150),nullable=False)
    student_email= db.Column(db.String(25),nullable=False)
    student_mobile=db.Column(db.String(10),nullable=False)
    year=db.Column(db.String(5),nullable=False)
    course=db.Column(db.String(8),nullable=False)
    branch=db.Column(db.String(8),nullable=False)
    division=db.Column(db.String(2),nullable=False)
    parent_name=db.Column(db.String(25),nullable=False)
    parent_address=db.Column(db.String(150),nullable=False)
    parent_email=db.Column(db.String(25),nullable=False)
    parent_mobile=db.Column(db.String(13),nullable=False)
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
    def __repr__(self):
        return f"IntForm('{self.id}','{self.name_of_supervisor}')"



class PtrForm(db.Model,UserMixin):
    id=db.Column(db.String(7),primary_key=True)
    
    year_of_admission=db.Column(db.String(15),nullable=False)
    branch=db.Column(db.String(5),nullable=False)
    year=db.Column(db.String(5),nullable=False)
    division=db.Column(db.String(1),nullable=False)
    mobile_number=db.Column(db.String(10),nullable=False)
    name_of_proctor=db.Column(db.String(30),nullable=False)
    email_of_proctor=db.Column(db.String(25),nullable=False)
    mobile_number_of_proctor=db.Column(db.String(10),nullable=False)
    name_of_student=db.Column(db.String(30),nullable=False)
    name_of_parent_guardian=db.Column(db.String(30),nullable=False)

    pre_add_loc_add_hos_add=db.Column(db.String(150),nullable=False)
    parent_pre_add_loc_add_hos_add=db.Column(db.String(150),nullable=False)
    nav_place_permt_add=db.Column(db.String(150),nullable=False)
    residential=db.Column(db.String(150),nullable=False)
    office=db.Column(db.String(150),nullable=False)
    ptr_mobile_number=db.Column(db.String(10),nullable=False)
    stu_email_id=db.Column(db.String(25),nullable=False)
    prt_email_id=db.Column(db.String(25),nullable=False)

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
    # photo=db.Column(db.LargeBinary)
    photo=db.Column(db.String(12),nullable=False)
    def __repr__(self):
        return f"PtrForm('{self.id}')"



admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(IntForm,db.session))
admin.add_view(ModelView(PtrForm,db.session))





@app.route('/register' , methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return "you are already authiticated"
    form = RegistrationForm()
    # if form.validate_on_submit():
    if request.method == "POST":
        # if form.validate_on_submit():
        id=request.form.get('id')
        if id[0]=='s' or id[0]=='p' or id[0]=='g':
            password=request.form.get('password')
            confirm_password=request.form.get('confirm_password')
            if User.query.filter_by(id=id).first():
                # already in use
                flash("Username already exist",'danger')
                return redirect("/register")
            elif password !=confirm_password:
                #password missmatch
                flash("Password missmatch",'danger')
                return redirect("/register")
            else:
                hash_pass=bcrypt.generate_password_hash(password).decode('utf-8')
                db.session.add(User(id=id,password=hash_pass))
                db.session.commit()
                flash(f"Registerd for {id}",'success')
                return redirect(url_for('login'))
        else:
            flash("invalid username",'danger')
            return redirect("/register")

    return render_template('register.html',form=form)


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return "you are already authiticated"
    form = LoginForm()
    if request.method=='POST':
        id=request.form.get('id')
        password=request.form.get('password')
        x=User.query.filter_by(id=id).first()
        if x==None:
            flash("Username not exist",'danger')
            return redirect(url_for("login"))
        else:
            if bcrypt.check_password_hash(x.password,password):
                login_user(x)
                if id[0]=="s":
                    return redirect(url_for('studentpanel'))
                elif id[0]=='p':
                    return redirect(url_for('proctorpanel'))
                elif id[0]=='g':
                    return redirect(url_for('parentpanel'))
            else:
                flash("Incorrect password",'danger')
                return redirect(url_for("login"))
    return render_template('login.html',form=form)



@app.route("/internshipForm" , methods=['GET','POST'])
@login_required
def internshipForm():
    form=InternshipForm()

    already_existed_user=IntForm.query.filter_by(id=current_user.id).first()
    if already_existed_user != None:
        # pform=PtrForm.query.filter_by(id=current_user.id).first()
        # iform=already_existed_user
        # return render_template('display_internship_form.html',iform=iform,form=form,pform=pform) 
        return redirect(url_for("displayiform"))
    form=InternshipForm()
    form.todays_date = datetime.now().strftime("%x")
    pform=PtrForm.query.filter_by(id=current_user.id).first()


    if request.method == "POST":
        id=pform.id
        internship_announcement_number=request.form.get('internship_announcement_number')
        student_name= pform.name_of_student
        student_address=pform.pre_add_loc_add_hos_add
        student_email=pform.stu_email_id

        student_mobile=pform.mobile_number
        parent_name=pform.name_of_parent_guardian
        parent_address=pform.parent_pre_add_loc_add_hos_add
        parent_email=pform.prt_email_id
        parent_mobile=pform.ptr_mobile_number
        location=request.form.get('location')
        name_of_institute=request.form.get('name_of_institute')
        work_profile=request.form.get('work_profile')
        name_of_supervisor=request.form.get('name_of_supervisor')
        stipend=request.form.get('stipend')
        semester=dict(form.semester.choices)[int(request.form.get('semester'))]
        type_of_internship=dict(form.type_of_internship.choices)[int(request.form.get('type_of_internship'))]
        course=dict(form.course.choices)[int(request.form.get('course'))]
        year=pform.year
        course=dict(form.course.choices)[int(request.form.get('course'))]
        branch=pform.branch
        division=pform.division
        period=dict(form.period.choices)[int(request.form.get('period'))]
        year_of_internship=dict(form.year_of_internship.choices)[int(request.form.get('year_of_internship'))]
        duration=request.form.get('duration')
        from_time=request.form.get('from_time')
        to_time=request.form.get('to_time')
        days_missed=request.form.get('days_missed')

        todays_date=datetime.now().strftime("%x")
        db.session.add(IntForm(id=id,internship_announcement_number=internship_announcement_number,student_name=student_name,student_address=student_address,student_email=student_email,student_mobile=student_mobile,parent_name=parent_name,parent_address=parent_address,parent_email=parent_email,parent_mobile=parent_mobile,location=location,name_of_institute=name_of_institute,work_profile=work_profile,name_of_supervisor=name_of_supervisor,stipend=stipend,semester=semester,type_of_internship=type_of_internship,year=year,course=course,branch=branch,division=division,period=period,year_of_internship=year_of_internship,duration=duration,from_time=from_time,to_time=to_time,todays_date=todays_date,days_missed=days_missed))
        db.session.commit()
        flash(f"{id} submited internship form",'success')
        return redirect(url_for('sMail'))
    return render_template('internship_form.html',form=form,pform=pform) 


@app.route("/proctorForm" , methods=['GET','POST'])
@login_required
def proctorForm():
    form=ProctorForm()
    already_existed_user=PtrForm.query.filter_by(id=current_user.id).first()
    if already_existed_user != None:
        return redirect(url_for("displaypform"))
    form.date = datetime.now().strftime("%x")
    form.id=current_user.id
    if request.method == "POST":
        id=current_user.id
        year_of_admission=dict(form.year_of_admission.choices)[int(request.form.get('year_of_admission'))]
        branch=dict(form.branch.choices)[int(request.form.get('branch'))]
        year=dict(form.year.choices)[int(request.form.get('year'))]
        division=dict(form.division.choices)[int(request.form.get('division'))]
        mobile_number=request.form.get('mobile_number')
        name_of_proctor=request.form.get('name_of_proctor')
        email_of_proctor=request.form.get('email_of_proctor')
        mobile_number_of_proctor=request.form.get('mobile_number_of_proctor')
        name_of_student=request.form.get('name_of_student')
        name_of_parent_guardian=request.form.get('name_of_parent_guardian')
        pre_add_loc_add_hos_add=request.form.get('pre_add_loc_add_hos_add')
        parent_pre_add_loc_add_hos_add=request.form.get('parent_pre_add_loc_add_hos_add')
        nav_place_permt_add=request.form.get('nav_place_permt_add')
        residential=request.form.get('residential')
        office=request.form.get('office')
        ptr_mobile_number=request.form.get('ptr_mobile_number')
        stu_email_id=request.form.get('stu_email_id')
        prt_email_id=request.form.get('prt_email_id')
        blood_group=dict(form.blood_group.choices)[int(request.form.get('blood_group'))]
        any_disease_disability=dict(form.any_disease_disability.choices)[int(request.form.get('any_disease_disability'))]
        date_of_birth=request.form.get('date_of_birth')
        place_of_birth=request.form.get('place_of_birth')
        mother_tongue=request.form.get('mother_tongue')
        religion=request.form.get('religion')
        exam=dict(form.exam.choices)[int(request.form.get('exam'))]
        score=request.form.get('score')
        per_ssc_marks=request.form.get('per_ssc_marks')
        per_hsc_marks=request.form.get('per_hsc_marks')
        discipline=request.form.get('discipline')
        date=datetime.now().strftime("%x")
        photo= current_user.id +".png"
        # photo=request.files['photo'].read()
        db.session.add(PtrForm(id=id,year_of_admission=year_of_admission,branch=branch,year=year,division=division,mobile_number=mobile_number,name_of_proctor=name_of_proctor,email_of_proctor=email_of_proctor,mobile_number_of_proctor=mobile_number_of_proctor,name_of_student=name_of_student,name_of_parent_guardian=name_of_parent_guardian,pre_add_loc_add_hos_add=pre_add_loc_add_hos_add,parent_pre_add_loc_add_hos_add=parent_pre_add_loc_add_hos_add,nav_place_permt_add=nav_place_permt_add,residential=residential,office=office,ptr_mobile_number=ptr_mobile_number,stu_email_id=stu_email_id,prt_email_id=prt_email_id,blood_group=blood_group,any_disease_disability=any_disease_disability,date_of_birth=date_of_birth,place_of_birth=place_of_birth,mother_tongue=mother_tongue,religion=religion,exam=exam,score=score,per_ssc_marks=per_ssc_marks,per_hsc_marks=per_hsc_marks,discipline=discipline,date=date,photo=photo))
        db.session.commit()
        flash(f"{id} submited proctorform",'success')
        return redirect(url_for('displaypform'))
    return render_template('proctor_form.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/display")
def display():
    # logout_user()
    form=IntForm.query.filter_by(id='1814013').first()

    return render_template('display_internship_form.html',form=form)

@app.route("/displayForProctor")
def displayForProctor():
    x=PtrForm.query.all()
    imgdict={}
    for i in x:
        imgdict[i.id]= BytesIO(PtrForm.query.filter_by(id=i.id).first().photo)
    return render_template('display_for_proctor.html',imgdict=imgdict,x=x)


@app.route("/drop")
def drop():
    db.drop_all()
    return "you dropped everything"

@app.route("/dbcreate")
def dbcreate():
    db.create_all()
    return "your database created"

@app.route("/test")
def test():
    return "this is testing page"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@app.route('/sMail', methods=['POST','GET'])
def sMail():
    pform=PtrForm.query.filter_by(id=current_user.id).first()
    if request.method == 'GET' :
        email = pform.prt_email_id
        token = s.dumps(email, salt='email-confirm')

        msg = Message('Confirm Email', sender='proctorsoft@gmail.com', recipients=[email])

        link = url_for('confirmEmail', token=token, _external=True)

        msg.body = 'Your link is {}'.format(link)

        mail.send(msg)

        return '<h1>The email you entered is {}. The token is {}</h1>'.format(email, token)



@app.route('/confirmEmail/<token>')
def confirmEmail(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=60)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    return '<h1>The token works!</h1>'




@app.route("/displaypform")
@login_required
def displaypform():
    form=ProctorForm()

    already_existed_user=PtrForm.query.filter_by(id=current_user.id).first()
    if already_existed_user != None:
        pform=already_existed_user
        return render_template('display_proctor_form.html',form=form,pform=pform) 
    return redirect(url_for("proctorForm"))

@app.route("/displayiform")
@login_required
def displayiform():
    form=InternshipForm()
    pform=PtrForm.query.filter_by(id=current_user.id).first()    
    already_existed_user=IntForm.query.filter_by(id=current_user.id).first()
    if already_existed_user != None:
        pform=PtrForm.query.filter_by(id=current_user.id).first()
        iform=already_existed_user
        return render_template('display_internship_form.html',iform=iform,form=form,pform=pform) 
    return redirect(url_for("internshipForm"))


@app.route("/StudentPanel",methods=['POST','GET'])
@login_required
def studentpanel():
    pform=PtrForm.query.filter_by(id=current_user.id).first()
    iform=IntForm.query.filter_by(id=current_user.id).first()
    if current_user.id[0]=='s':
        if request.method=='POST':
            email=pform.email_of_proctor
            message=request.form.get('message')
            mail.send_message('New message from'+ pform.id,
                                sender='proctorsoft@gmail.com',
                                recipients=[email],
                                body=message)
            flash("mail send",'success')
        return render_template("student_panel.html",pform=pform,iform=iform)
    elif current_user.id[0]=='p':
        flash("you can\'t go there",'danger')
        return redirect(url_for("proctorpanel"))
    else:
        flash("you can\'t go there",'danger')
        return redirect(url_for("parentpanel"))



@app.route("/deleteiform")
@login_required
def deleteiform():
    IntForm.query.filter_by(id=current_user.id).delete()
    db.session.commit()
    return redirect(url_for("internshipForm"))



@app.route("/deletepform")
@login_required
def deletepform():
    PtrForm.query.filter_by(id=current_user.id).delete()
    db.session.commit()
    return redirect(url_for("proctorForm"))

@app.route("/ProctorPanel")
@login_required
def proctorpanel():
    pform=PtrForm.query.all()
    if current_user.id[0]=='p':
        return render_template("proctor_panel.html",pform=pform)
    elif current_user.id[0]=='s':
        flash("you can\'t go there",'danger')
        return redirect(url_for("studentpanel"))
    else:
        flash("you can\'t go there",'danger')
        return redirect(url_for("parentpanel"))


@app.route("/ParentPanel")
@login_required
def parentpanel():
    if current_user.id[0]=='g':
        student_mail ="s"+current_user.id[1:]
        pform=PtrForm.query.filter_by(id=student_mail).first()
        iform=IntForm.query.filter_by(id=student_mail).first()
        if request.method=='POST':
            email=pform.email_of_proctor
            message=request.form.get('message')
            mail.send_message('New message from'+ current_user.id,
                                sender='proctorsoft@gmail.com',
                                recipients=[email],
                                body=message)
            flash("mail send",'success')
            return render_template("parent_panel.html",pform=pform,iform=iform)
        return render_template("parent_panel.html",pform=pform,iform=iform)
    elif current_user.id[0]=='s':
        flash("you can\'t go there",'danger')
        return redirect(url_for("studentpanel"))
    else:
        flash("you can\'t go there",'danger')
        return redirect(url_for("proctorpanel"))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Choose your files</h1>
    <hr>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <hr>

    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)





if __name__=="__main__":
    app.run(debug=True)

