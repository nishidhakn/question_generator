from django.shortcuts import render
from app1.models import Question

# Create your views here.
def func1(request):
    if request.method=='POST':
        obj=Question()
        obj.class1=request.POST.get('class1')
        obj.subject=request.POST.get('subject')
        obj.twomark=request.POST.get('twomark')
        obj.threemark=request.POST.get('threemark')
        obj.fivemark=request.POST.get('fivemark')
        obj.save()
    return render(request,'form.html')

def func2(request):
    obj=Question.objects.all()
    return render(request,'table.html',{'a':obj})



def func3(request):
      if request.method == 'POST':
          class1 = request.POST.get('class1', '')
          subject = request.POST.get('subject', '')
          twomark = request.POST.get('twomark', '')
          threemark = request.POST.get('threemark', '')
          fivemark = request.POST.get('fivemark', '')
          context = {
             'class1': class1,
              'subject': subject,
              'twomark': twomark,
              'threemark': threemark,
              'fivemark': fivemark,
          }
          questions = Question.objects.filter(class1=class1, subject=subject)
          context['questions'] = questions
          return render(request, 'paper.html', context)
      return render(request, 'form.html') 

