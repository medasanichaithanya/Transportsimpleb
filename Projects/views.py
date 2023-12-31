from django.shortcuts import render
from Projects.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import bcrypt
from datetime import datetime, timedelta
import pytz





# This is the default view
@csrf_exempt
def default(request):
    return JsonResponse({'message': 'Welcome to the Django Welcome API!'})

@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            check_email  = UserInformation.objects.filter(username=email)
            if check_email:
                return JsonResponse({'status': 'SUCCESS'})
            else:
                add_user = UserInformation()
                add_user.username = body['email']
                add_user.firstname = body['firstName']
                add_user.lastname = body['lastName']
                if 'password' in body:
                    hashed_password = bcrypt.hashpw( body['password'].encode('utf-8'), bcrypt.gensalt())
                    add_user.password = hashed_password
                else:
                    add_user.password = ''
                if 'token' in body:
                    add_user.token = body['token']
                else:
                    add_user.token = ''

                add_user.mobile = body['phone']
                add_user.save()
                return JsonResponse({'status':'SUCCESS','message':'no error'})
            
        except Exception as e:
            return JsonResponse({'Status': 'Error occured'})
    else:
        return JsonResponse({'Status': 'UNKNOWN ERROR'})
    
@csrf_exempt
def loginuser(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            password = body['password'].encode('utf-8')
            user_check = UserInformation.objects.filter(username=email).values()
            encoded_string = user_check[0]['password'].encode('utf-8')
            if bcrypt.checkpw(password, encoded_string):
                return JsonResponse({'status':'SUCCESS','message':user_check[0]['username']})
            else:
                return JsonResponse({'status':'FAILED','message':'Password Incorrect'})

        except Exception as e:
            return JsonResponse({'Status': 'Error occured'})
    else:
        return JsonResponse({'Status': 'UNKNOWN ERROR'})
    
    
@csrf_exempt
def addquestion(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            questiondata = body['question']
            userdata = body['user']
            get_user_data = UserInformation.objects.filter(username=userdata).values()
            add_question = QuestionDetails()
            add_question.userid = get_user_data[0]['id']
            add_question.question = questiondata
            get_last_id = QuestionDetails.objects.order_by('-userid').last()
            add_question.questionid = get_last_id.id + 1
            add_question.description  = "no description"
            add_question.save()
            return JsonResponse({'status': 'SUCCESS'})

        except Exception as e:
            return JsonResponse({'Status': 'Error occured'})
    else:
        return JsonResponse({'Status': 'UNKNOWN ERROR'})
    
@csrf_exempt
def fetchposts(request):
    if request.method == 'GET':
        try:
            posts_data = UserInformation.objects.filter().all()
            end_datetime = datetime.now(pytz.UTC)
            data=[]
            for users in posts_data:
                get_questions = QuestionDetails.objects.filter(userid=users.id).distinct()
                for questions in get_questions:
                    obj={}
                    obj['questionid'] = questions.questionid
                    obj['question'] = questions.question
                    duration = end_datetime - questions.dateCreated
                    days = duration.days
                    hours = duration.seconds // 3600  # 3600 seconds in an hour
                    weeks = days // 7
                    if weeks >= 1:
                        obj['qtime']= f"{weeks}w"
                    elif days >= 1:
                        obj['qtime'] = f"{days}d"
                    else:
                        obj['qtime']= f"{hours}h"
                    check_user = UserInformation.objects.filter(id=questions.userid)
                    obj['user'] = check_user[0].firstname +" " +check_user[0].lastname
                    obj['imgurl'] = check_user[0].profileImgUrl
                    answerdata = []
                    fetch_answers = AnswerDetails.objects.filter(questionid=questions.questionid)
                    for answer in fetch_answers:
                        answers={}
                        check_user = UserInformation.objects.filter(id=answer.userid)
                        answers['user'] = check_user[0].firstname +" " +check_user[0].lastname
                        answers['imgurls'] = check_user[0].profileImgUrl
                        answers['answer'] = answer.answer
                        duration = end_datetime - answer.dateCreated
                        days = duration.days
                        hours = duration.seconds // 3600  # 3600 seconds in an hour
                        weeks = days // 7
                        if weeks >= 1:
                            answers['atime']= f"{weeks}w"
                        elif days >= 1:
                            answers['atime'] = f"{days}d"
                        else:
                            answers['atime']= f"{hours}h"
                        
                        answerdata.append(answers)

                    obj['answers'] = answerdata

            
                    data.append(obj)
            return JsonResponse({'status': 'SUCCESS','data':data})

           
        except Exception as e:
            return JsonResponse({'Status': str(e)})
    else:
        return JsonResponse({'Status': 'UNKNOWN ERROR'})

    
@csrf_exempt
def addanswer(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            questionid = body['questionid']
            answer = body['postanswer']
            get_userid = UserInformation.objects.filter(username=body['userid']).values()
            addanswer = AnswerDetails()
            addanswer.questionid = questionid
            addanswer.answer = answer
            addanswer.userid = get_userid[0]['id']
            get_last_id = AnswerDetails.objects.order_by('-answerid').last()
            addanswer.answerid = get_last_id.answerid  + 1
            addanswer.save()
            return JsonResponse({'Status': 'SUCCESS'})

        except Exception as e:
            return JsonResponse({'Status': 'Error occured'})
    else:
        return JsonResponse({'Status': 'UNKNOWN ERROR'})

