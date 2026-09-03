from flask import*
import sqlite3
import json
import os
import base64
# from login import*
# from reg_std import*
from package import login,reg_std,reg_std_no_img,admin_login_pck,staff_prfile,staf_profile_no_img,filter_std,update_std_rcd
# import package
app = Flask(__name__)
# app.secret_key='school'
std_reg_no=""

# @app.after_request
# def add_header(response):
#     """
#     Direct the browser to never cache pages.
#     Forces a fresh server request on back-button navigation.
#     """
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Pragma"] = "no-cache"
#     response.headers["Expires"] = "0"
#     return response
    
@app.route('/')
def home():    
    # if 'user' in session:        
        return render_template('home_page.html')
    # else:           
        # return render_template('login_page.html')   
@app.route('/teacher_login')
def teacher_login():
    return render_template('login_page.html')

@app.route('/admin_login_page')
def admin_login_page():
    return render_template('admin_login_page.html')


@app.route('/add_teacher')
def add_teacher():
    return render_template('teacher_form.html')


@app.route('/login_user',methods=['POST','GET'])
def login_user():  
   
    if request.method=='POST':                
             user1=request.form.get('user')            
             password1=request.form.get('password')
             obj=login.new_login.show()
             if user1==obj['user'] and password1==obj['password']:    
                return jsonify({
                    "status":"Logged in successfully ",
                    "redirect_url":url_for('dashboard')
                }),200  
                # return "login successfull"  
             else:
                return jsonify({
                         "status": "user Id and Password incorrect !...", 
                         "message": "Invalid credentials"
                 }), 401
                                       
    return render_template('login_page.html')
    
@app.route('/dashboard')
def dashboard():    
     return render_template('dashboard_teacher.html')

@app.route('/admin_dashboard')
def admin_dashboard():    
     return render_template('admin_dashboard.html')  

@app.route('/logout')
def logout():    
        global user  
        user=""             
        return render_template('home_page.html')
        
            
@app.route('/back_page')
def back_page():  
 return render_template('dashboard_teacher.html')


@app.route('/new_reg',methods=['POST','GET'])
def new_reg():    
    if request.method=='POST':  

        std_file=request.files['file']    
        print(std_file.filename)
        first_name=request.form.get('first_name') 
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        mobile_no=request.form.get('mobile_no')
        dob=request.form.get('dob')
        gender=request.form.get('gender')
        admission_in_Class=request.form.get('admission_in_Class')
        admission_date=request.form.get('admission_date')
        father_name=request.form.get('father_name')
        mother_name=request.form.get('mother_name')
        parent_contact=request.form.get('parent_contact')
        whats_no=request.form.get('whats_no')
        address=request.form.get('address')
        mode=request.form.get('mode')
        height=request.form.get('height')
        weight=request.form.get('weight')
        cls_obj=reg_std.reg_std_class(std_file,first_name,last_name,email,mobile_no,dob,gender,admission_in_Class,admission_date,father_name,mother_name,parent_contact,whats_no,address,mode,height,weight)
        ret=cls_obj.insert_record()           
        return ret          
    return render_template('login_page.html')



# student regitratio with no file/photo
@app.route('/new_reg_no_file',methods=['POST','GET'])
def new_reg_no_file():    
    if request.method=='POST':  
       
            first_name=request.form.get('first_name') 
            last_name=request.form.get('last_name')
            email=request.form.get('email')
            mobile_no=request.form.get('mobile_no')
            dob=request.form.get('dob')
            gender=request.form.get('gender')
            admission_in_Class=request.form.get('admission_in_Class')
            admission_date=request.form.get('admission_date')
            father_name=request.form.get('father_name')
            mother_name=request.form.get('mother_name')
            parent_contact=request.form.get('parent_contact')
            whats_no=request.form.get('whats_no')
            address=request.form.get('address')
            mode=request.form.get('mode')
            height=request.form.get('height')
            weight=request.form.get('weight')
            cls_obj1=reg_std.reg_std_class_no_file(first_name,last_name,email,mobile_no,dob,gender,admission_in_Class,admission_date,father_name,mother_name,parent_contact,whats_no,address,mode,height,weight)
            ret=cls_obj1.insert_record()
            return ret       
              
    return render_template('login_page.html')

#end of no file 
 

# staff profile  staff_profile
@app.route('/staff_profile1',methods=['POST','GET'])
def staff_profile1():    
    if request.method=='POST':   
        if 'my_file' not in request.files:  
            
            first_name=request.form.get('first_name') 
            slct_gender=request.form.get('slct_gender')
            dob=request.form.get('dob')
            sltc_blood=request.form.get('sltc_blood')
            email=request.form.get('email')
            mobile=request.form.get('mobile')
            txt_address=request.form.get('txt_address')
            slct_qualification=request.form.get('slct_qualification')
            sltc_department=request.form.get('sltc_department')
            join_date=request.form.get('join_date')
            txt_emp_id=request.form.get('txt_emp_id')
            password=request.form.get('password')           
            cls_obj=staf_profile_no_img.staff_prfile_class (first_name,slct_gender,dob,sltc_blood,email,mobile,txt_address,slct_qualification,sltc_department,join_date,txt_emp_id,password)
            ret=cls_obj.insert_record_no_photo()
            return ret       

        else:          
            std_file=request.files['file']    
            first_name=request.form.get('first_name') 
            slct_gender=request.form.get('slct_gender')
            dob=request.form.get('dob')
            sltc_blood=request.form.get('sltc_blood')
            email=request.form.get('email')
            mobile=request.form.get('mobile')
            txt_address=request.form.get('txt_address')
            slct_qualification=request.form.get('slct_qualification')
            sltc_department=request.form.get('sltc_department')
            join_date=request.form.get('join_date')
            txt_emp_id=request.form.get('txt_emp_id')
            password=request.form.get('password')           
            cls_obj=staff_prfile.staff_prfile_class(std_file,first_name,slct_gender,dob,sltc_blood,email,mobile,txt_address,slct_qualification,sltc_department,join_date,txt_emp_id,password)
            ret=cls_obj.insert_record() 
            return ret          
    return render_template('login_page.html')
 
# admin login
@app.route('/admin_login',methods=['POST','GET'])
def admin_login():  
   
    if request.method=='POST':                
             user1=request.form.get('username')            
             password1=request.form.get('password')             
             date_time=request.form.get('date_time')
             obj=admin_login_pck.cls_login_admin(user1,password1)
            #  ret=obj.admin_login_fun()                                 
    return obj.admin_login_fun()

# student dashboard redirect page

@app.route('/load_page',methods=['POST','GET'])
def load_page():     
    if request.method=='POST':  
        page=request.form.get('sltc_value')        
        if page=='Add Student':            
             return jsonify({
                    "status":"Logged in successfully ",
                    "redirect_url":url_for('add_student')
                }),200
        if page=='Filter/Update':
         return jsonify({
                    "status":"Logged in successfully ",
                    "redirect_url":url_for('filter_student')
                }),200
    return "msg"


@app.route('/add_student')
def add_student():    
     return render_template('Reg_form.html')

@app.route('/filter_student')
def filter_student():    
     return render_template('filter_std.html')
# end of 
# filter page

@app.route('/filter_rcd',methods=['POST','GET'])
def filter_rcd():
    if request.method=='POST':
        std_id=request.form.get('search_id')
        std_class=request.form.get('std_class')       
        con=sqlite3.connect('test.db')
        cur=con.cursor()
        con.row_factory = sqlite3.Row          
        # query='select *from student_record where admission_in_Class=?',(self.std_class))        
        cur.execute('select *from student_record where admission_in_Class=? OR reg_no=?',(std_class,std_id,))
        rows=cur.fetchall()    
        data = []       
        for row in rows:
            std_photo=base64.b64encode(row[16]).decode('utf-8')
            data.append({
                'image':f"data:image/jpeg;base64,{std_photo}",
               'first_name':row[0],
                'last_name':row[1],
                "email":row[2],
                "dob":row[3],
                "gender":row[4],       
                "admission_in_Class":row[5],
                "admission_date":row[6],
                "father_name":row[7],
                "mother_name":row[8],
                "parent_contact":row[9],
                "whats_no":row[10],
                "address":row[11],
                "mode":row[12],
                "weight":row[13],
                "height":row[14],
                "reg_no":row[15],                  
                "session":row[17],
                "admission_no":row[18],
                "pre_school":row[19],
                "roll_no":row[20]
                               
            })
        con.close()
        return jsonify(data)
    return "error message"

@app.route('/back__filter_page')
def back__filter_page():  
 return render_template('dashboard_teacher.html')


# redirect update_html page

@app.route('/update_form_link',methods=['POST','GET'])
def update_form_link():    
    if request.method=='POST': 
        global std_reg_no
        std_id=request.form.get('std_reg')        
        std_reg_no=std_id
        return jsonify({
                    "status":"divert successfully successfully ",
                    "redirect_url":url_for('update_html_page')
                }),200
    return "diversion problme"

@app.route('/update_html_page')
def update_html_page():  
 return render_template('update_std_rcd.html')

# end of redirect html page
 

@app.route('/load_std_rcd',methods=['POST','GET'])
def load_std_rcd():    
    if request.method=='POST':   
        #  session=request.form.get('session')
         obj=update_std_rcd.update_cls(std_reg_no)
         ret=obj.get_std_rcd()          
         return ret            
    return "network error"  
 
# back  page of update
@app.route('/back_page_update')
def back_page_update():
     return render_template('filter_std.html')
# end of this 
@app.route('/update_reg_form',methods=['POST','GET'])
def update_reg_form():    
    if request.method=='POST':   
                
        std_file=request.files['file']         
        first_name=request.form.get('first_name') 
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        # mobile_no=request.form.get('mobile_no')
        dob=request.form.get('dob')
        gender=request.form.get('gender')
        admission_in_Class=request.form.get('admission_in_Class')
        admission_date=request.form.get('admission_date')
      
        father_name=request.form.get('father_name')
        mother_name=request.form.get('mother_name')
        parent_contact=request.form.get('parent_contact')
        whats_no=request.form.get('whats_no')
        address=request.form.get('address')
        mode=request.form.get('mode')

        height=request.form.get('height')
        weight=request.form.get('weight')
        session=request.form.get('session')
        adm_no=request.form.get('adm_no')
        pre_school=request.form.get('pre_school') 
        roll_no=request.form.get('roll_no') 
        cls_obj_update=update_std_rcd.update_recd_with_file_class(std_file,std_reg_no,first_name,last_name,email,dob,gender,admission_in_Class,admission_date,father_name,mother_name,parent_contact,whats_no,address,mode,height,weight,session,adm_no,pre_school,roll_no)
        # cls_obj_update=update_std_rcd.update_recd_with_file_class(std_reg_no,first_name,last_name,email,dob,gender,admission_in_Class,admission_date,father_name,mother_name,parent_contact,whats_no,address,mode)
        ret=cls_obj_update.update_data_with_file()
        return jsonify({"msg":ret,
                        "redirect":url_for('back_page_update')
                            })  
    return "network error"  

@app.route('/update_reg_form_no_img',methods=['POST','GET'])
def update_reg_form_no_img():    
    if request.method=='POST':                   
              
        first_name=request.form.get('first_name') 
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        # mobile_no=request.form.get('mobile_no')
        dob=request.form.get('dob')
        gender=request.form.get('gender')
        admission_in_Class=request.form.get('admission_in_Class')
        admission_date=request.form.get('admission_date')      
        father_name=request.form.get('father_name')
        mother_name=request.form.get('mother_name')
        parent_contact=request.form.get('parent_contact')
        whats_no=request.form.get('whats_no')
        address=request.form.get('address')
        mode=request.form.get('mode')
        height=request.form.get('height')
        weight=request.form.get('weight')
        session=request.form.get('session')
        adm_no=request.form.get('adm_no')
        pre_school=request.form.get('pre_school') 
        roll_no=request.form.get('roll_no') 
        cls_obj_update=update_std_rcd.update_recd_with_no_file_class(std_reg_no,first_name,last_name,email,dob,gender,admission_in_Class,admission_date,father_name,mother_name,parent_contact,whats_no,address,mode,height,weight,session,adm_no,pre_school,roll_no)
        ret=cls_obj_update.update_data_with_no_file()
        return jsonify({"msg":ret,"redirect":url_for('back_page_update')})  
    return "network error"  

if __name__ == '__main__':
    app.run(debug=True)
    # # app.run(debug=True)
    # import os
    # HOST = os.environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(os.environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    # app.run(HOST, PORT)
