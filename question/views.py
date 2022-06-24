from django.contrib.auth.decorators import login_required
from itertools import count
from django.shortcuts import render
from question.models import Question
from django.http import JsonResponse

def home(request):
    context={
        "great":"i would be great one day"
    }
    return render(request,"home.html",context)



def questions_view(request,dyna_visible_questions):
     
    visible = 5
    upper = dyna_visible_questions
    lower = upper-visible
    questions=Question.objects.all()
    data=[]
     
    for question in questions:
        item={
          
        "id":question.id,
        "question":question.question,
        "imageA":question.imageA.url,
        "imageB":question.imageB.url,
        "countA":question.countA.all().count(),
        "countB":question.countB.all().count(),
        "timestamp":question.timestamp,
        "is_votedA":True if request.user in question.countA.all() else False,
        "is_votedB":True if request.user in question.countB.all() else False


        }
    
        data.append(item)
   
    return JsonResponse({"data":data[lower:upper],"size":Question.objects.all().count()})

@login_required(login_url='/accounts/login/')
def vote_view(request):
    print("mini-max")
    
    if request.is_ajax():
        btnId = request.POST.get('btnId')
        ques_obj = Question.objects.get(id=btnId)
        btnType = request.POST.get('btnType')
        
        if btnType =="A":

            if request.user  in ques_obj.countA.all():
                voteA = False
                ques_obj.countA.remove(request.user)
            else:
                voteA = True
                ques_obj.countA.add(request.user)

            

            return JsonResponse({"voteA":voteA,
            "is_votedB":True if request.user in ques_obj.countB.all() else False,
            "otherCount":ques_obj.countB.all().count(),
            "countA":ques_obj.countA.all().count()})


        
        if btnType =="B":

            if request.user  in ques_obj.countB.all():
                voteB = False
                ques_obj.countB.remove(request.user)
            else:
                voteB = True
                ques_obj.countB.add(request.user)

            

            return JsonResponse({"voteB":voteB,
            "otherCount":ques_obj.countA.all().count(),
            "is_votedA":True if request.user in ques_obj.countA.all() else False,
            "countB":ques_obj.countB.all().count()})

            
    return redirect('posts:feed-data')