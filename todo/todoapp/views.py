from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        # todo = Todo.objects.all() # modelden almak ıstedıgın yapıları ceker 
        todo = Todo.objects.filter(user=request.user)
        if request.method == 'POST':
            form = TodoForm(request.POST)    #htmlden admin tarafına veri göndereceğimiz zaman
            if form.is_valid():             #bu methodu kullanırız

                userTodo =form.save(commit=False)
                userTodo.user =request.user
                userTodo.save()
                #form.save()                 #! html tarafında ilgili yapı formun icinde ve submit olmalıdır 
                return redirect('index')
        else:
            form = TodoForm #göruntulenecek olan formu esıtletıp asagıda yansıtıyoruz context sayesınde
        
        context = {  #kolaylık olsun dıye bır tuple actık
        
        'todo':todo,
        
        'form':form,
        
        }
        return render(request,'index.html',context)
    
    else:
        return render(request,'index.html',)
        
        
        
    

def todoDetay(request,d_slug):
    todo = get_object_or_404(Todo,slug= d_slug)
    context = {
        'todo':todo
    }
    return render(request,'todoDetay.html',context)

def sil(request):
    if request.method == 'POST':
        todoId = request.POST['sil']
        sil = Todo.objects.get(id = todoId)  #ilk deger database den gelir
        sil.delete()
        return redirect ('index')



