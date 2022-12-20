from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Riddle, Option, Kits
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html", {"list_kits": Kits.objects.order_by('id')})


def detail(request, kits_id):
    dl = []
    det_lst = Riddle.objects.order_by('id')
    for i in range(kits_id*3-3, kits_id*3):
        dl.append(det_lst[i])
    ki = kits_id*3-2
    context = {"detail_list": dl,
               "num_kits": kits_id,
               "ki": ki}

    return render(request, 'detail.html', context=context)


count_v = 0
count_n = 0


def answer(request, riddle_id, kits_id):
    global count_v, count_n
    # count_riddle = Riddle.objects.all().count()

    if riddle_id <= kits_id*3:
        riddle = get_object_or_404(Riddle, pk=riddle_id)
        kits = get_object_or_404(Kits, pk=kits_id)
        try:
            option = riddle.option_set.get(pk=request.POST['option'])
            
        except (KeyError, Option.DoesNotExist):
            return render(request, 'answer.html', {'kits': kits, 'riddle': riddle})
           
        else:
            if option.correct:
                count_v += 1
                # return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('id'),
                #                                       "message": "Прекрасно! Правильный ответ!"})
                return HttpResponseRedirect(f"/answer/{kits_id}/{riddle_id + 1}")
            else:
                count_n += 1
                # return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Неправильный ответ!'})
                return HttpResponseRedirect(f"/answer/{kits_id}/{riddle_id + 1}")

    if count_n != 0:
        perc = round((count_v/(count_v+count_n))*100, 2)
    else:
        perc = 100
    context = {'message_v': count_v, 'message_n': count_n, 'perc': perc}
    count_v = 0
    count_n = 0
    return render(request, "result.html", context=context)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
        
    def get(self, request):
        context = {
            'form' : self.form_class
        }
        return render(request, self.template_name, context)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    