#importing module
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="quiz_comp")
mycursor=mydb.cursor()

#introduction
print(''' "QUIZ SOFTWARE"

The following program lets you input data for your QUIZ COMPETITION into TABLES

We are providing you with the following tables:
''')
print('''Table 1.Questions

Table 2.Participants

Table 3.Scores Update

Table 4.Display

Table 5.HOTS Questions, Rapid Fire Questions and Multiple Correct Questions


''')
choice=int(input("Enter the respective table number of your choice :"))

#mycursor.execute("create table questions1(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table maths(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table science_GK(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table astronomy(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table rapid_fire(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table tourism(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table sports(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table entertain(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
#mycursor.execute("create table mul_crct(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")

#Choice of Quiz Category and Entering of Data 
if choice==1:
    f=int(input('''To Select the Category of Quiz Questions
i)Enter 10 for General knowlege
ii)11 for Mental Maths
iii)12 for Science GK
iv)13 for Astronomy
v)14 for Tourism
vi)15 for Sports
vii)16 for Entertainment'''))
    
    if f==10:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into questions1 values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==11:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into maths values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==12:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into science_GK values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==13:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into astronomy values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==14:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into tourism values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==15:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into sports values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")

    elif f==16:
        sql=int(input("Enter the index_no of the Question:"))
        sql1=input("Enter the question :")
        sql2=input("Enter the option A:")
        sql3=input("Enter the option B:")
        sql4=input("Enter the option C:")
        sql5=input("Enter the option D:")
        sql6=input("The Answer is:")
        sql_in= "insert into entertain values(" + str(sql) + ",'"+ (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+(sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
        mycursor.execute(sql_in)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")
    else:
        print("INVALID ENTRY")
    
#mycursor.execute("create table participants(reg_no int(5) primary key, pname varchar(50) ,age_group int(10),city varchar(50),no_of_appearances_made int(10))")

#Entering of Participants name
elif choice==2:
    sql6=int(input("Enter the participant reg_no:"))
    sql7=input("Enter the participant name:")
    sql8=int(input("Enter the age group:"))
    sql9=input("Enter the city:")
    sql10=int(input("Enter the no.of.appearances made:"))
    sql_int="insert into participants values("+ str(sql6)+ ",'"+ (sql7) + "'" + ",'"+str(sql8) + "'" + ",'"+(sql9) +"'"+",'"+str(sql10)+"'"")"
    print(sql_int)
    mycursor.execute(sql_int)
    print("participants are all updated")
    mydb.commit()

#mycursor.execute("create table scores(reg_no int(5) primary key , participant_name varchar(50),total_correct int(50),total_wrong int(50),total_attempted int(50))")
#mycursor.execute("create table ranking(reg_no int(5) primary key,participant_name varchar(50),score int(3))")

#Score update of participants 
if choice==3:
    a=int(input("Enter the partipants reg_no"))
    b=input("Enter the participants name")
    d=int(input("Enter the total no.of.correct answers"))
    e=int(input("Enter the no.of.incorrect answer"))
    f=int(input("Enter the no_of_attempted_questions"))
    sql_insert="insert into scores values("+ str(a) +",'"+ (b)+"'"+ ",'"+str(d) +"'"+ ",'"+str(e) +"'"+",'"+str(f)+ "'"")"
    print(sql_insert)
    mycursor.execute(sql_insert)
   
    scoreyn=input(print('''do you wish to see the score of the participant?
    enter Y for yes and N for no'''))
    if scoreyn=='Y' or 'y':
        print("the participant is awarded +4 for every correct answer and -1 for every incorrect answer")
        x=(d*4)-(e)
        print("the participant named",b,"has scored a total of ",x)
        print("total marks scored without negative marking:",d*4)
    elif scoreyn=='N' or 'n':
        print('you request has been processed')
    else:
        print("please enter a valid input")    
    
    mydb.commit()
     

#Displaying of Data of specific data
elif choice==4:
    print("You have choosen to display the tables")
    print('''
Which table do you want to display ?
''')
    print('''Enter: 
1 for Questions table
2 for HOTS or Rapid Fire questions table or Multiple correct questions
3 for Participants table
4 for Scores table ''')
    g=int(input("Enter your choice : "))
    
    if g==1:
        p=int(input('''To select the Subject Table Choice i)Enter 9 for General Knowledge
ii)10 for maths
iii)11 for Science GK
iv)12 for Astronomy
v)13 for Tourism
vi)14 for Sports
vii) 15 for Entertainment'''))
        
        if p==9:
            mycursor.execute("select * from questions1")
            data=mycursor.fetchall()
            print(data)
        elif p==10:
           mycursor.execute("select * from maths")
           data=mycursor.fetchall()
           print(data)
        elif p==11:
            mycursor.execute("select * from science_GK")
            data=mycursor.fetchall()
            print(data)
        elif p==12:
            mycursor.execute("select * from astronomy")
            data=mycursor.fetchall()
            print(data)
        elif p==13:
            mycursor.execute("select * from tourism")
            data=mycursor.fetchall()
            print(data)
        elif p==14:
            mycursor.execute("select * from sports")
            data=mycursor.fetchall()
            print(data)
        elif p==15:
            mycursor.execute("select * from entertain")
            data=mycursor.fetchall()
            print(data)
        
        else:
            print("INVALID ENTRY")
            
               
    elif g==2:
        q=int(input('''To select the table choice Enter: 1 for HOTS
                        2 for Rapid Fire Questions
                        3 for Multi Correct Questions'''))
                    
        if q==1:
            mycursor.execute("select * from questions2")
            data=mycursor.fetchall()
            print(data)
        elif q==2:
            mycursor.execute("select * from rapid_fire")
            data=mycursor.fetchall()
            print(data)
        elif q==3:
            mycursor.execute("select * from mul_crct")
            data=mycursor.fetchall()
            print(data)            
        else:
            print("INVALID ENTRY")
            
    elif g==3:
        mycursor.execute("select * from participants")
        data=mycursor.fetchall()
        print(data)

    elif g==4:
        mycursor.execute("select * from scores")
        data=mycursor.fetchall()
        print(data)
              
    else:
        print("INVALID ENTRY")

#mycursor.execute("create table questions2(qno_no int(3) primary key , qno varchar(10000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")

#Entering of Second level Quiz questions
elif choice==5:
    o=int(input('''To Select the Category of type of Questions Enter: 99 for HOTS Questions
100 for Rapid Fire Questions
101 for Multiple Correct Questions'''))
    
    if o==99:
        sql11=int(input("Enter the index_no of the Question:"))
        sql12=input("Enter the question :")
        sql13=input("Enter the option A:")
        sql14=input("Enter the option B:")
        sql15=input("Enter the option C:")
        sql16=input("Enter the option D:")
        sql17=input("The Answer is:")
        sql_ins= "insert into questions2 values(" + str(sql11) + ",'"+ (sql12)+ "'"+",'" + (sql13) + "'"+",'" + (sql14) +"'" +",'"+(sql15) +"'"+",'" + (sql16) +"'"+ ",'"+(sql17) +"'"")"
        mycursor.execute(sql_ins)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")
    
    elif o==100:
        sql11=int(input("Enter the index_no of the Question:"))
        sql12=input("Enter the question :")
        sql13=input("Enter the option A:")
        sql14=input("Enter the option B:")
        sql15=input("Enter the option C:")
        sql16=input("Enter the option D:")
        sql17=input("The Answer is:")
        sql_ins= "insert into rapid_fire values(" + str(sql11) + ",'"+ (sql12)+ "'"+",'" + (sql13) + "'"+",'" + (sql14) +"'" +",'"+(sql15) +"'"+",'" + (sql16) +"'"+ ",'"+(sql17) +"'"")"
        mycursor.execute(sql_ins)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")
        
    elif o==101:
        sql11=int(input("Enter the index_no of the Question:"))
        sql12=input("Enter the question :")
        sql13=input("Enter the option A:")
        sql14=input("Enter the option B:")
        sql15=input("Enter the option C:")
        sql16=input("Enter the option D:")
        sql17=input("Enter both correct answer is:")
        sql_ins= "insert into rapid_fire values(" + str(sql11) + ",'"+ (sql12)+ "'"+",'" + (sql13) + "'"+",'" + (sql14) +"'" +",'"+(sql15) +"'"+",'" + (sql16) +"'"+ ",'"+(sql17) +"'"")"
        mycursor.execute(sql_ins)
        mydb.commit()
        print("Your request has been processed. Thank you for making us as a part of your project")


    else:
        print("INVALID ENTRY")



#Input of feedback
feed=int(input(''' Hope You Liked the quiz software management system. Please give your feedback.
Do you want to give the feedback ?
Enter 1 for yes and 2 for no.'''))


if feed==1:
    input("Enter your feedback")

print('''
THANK YOU FOR CHOOSING US
''')

print("         ***             ")













