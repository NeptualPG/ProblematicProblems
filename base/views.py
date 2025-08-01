from django.shortcuts import get_object_or_404, render,  redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Problem, Solution, Topic, Message
from .forms import SolutionForm

# recien me doy cuenta de que no estoy dejando documentación demonios


def loginPage(request):
    page = 'login';
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = (request.POST.get('username') or '').lower()
        password = (request.POST.get('password') or '')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, "Username OR password does not exist.")

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occurrend during registration')
    context = {'form':form }
    return render(request, 'base/login_register.html', context)


# home es home
def home(request):    
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    problems = Problem.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )

    # Annotate topics with number of related problems
    topics = Topic.objects.annotate(num_problems=Count('problem'))

    problem_count = problems.count()

    problem_messages = Message.objects.filter(
        Q(problem__topic__name__icontains=q)
    ).order_by('-created')[:5]  # Ajustado también aquí

    context = {
        'problems': problems,
        'topics': topics,
        'problem_count': problem_count,
        'problem_messages': problem_messages
    }

    return render(request, 'base/home.html', context)

# dentro de los problemas tendremos las soluciones
def problem(request, pk):
    problem = Problem.objects.get(id=pk)
    problem_messages = Message.objects.filter(problem=problem).order_by('-created')
    solvers = problem.solvers.all()

    if request.method == 'POST':
        messages = Message.objects.create(
            user = request.user,
            problem = problem,
            body = request.POST.get('body')
        )
        problem.solvers.add(request.user)
        return redirect('problem', pk=problem.id)

    solutions = Solution.objects.filter(problem=problem)
    context = {'problem': problem, 'solutions': solutions,'m_messages': problem_messages,'solvers': solvers} 
    return render(request, 'base/problem.html', context)

# ya esta está creada falta que veamos formas para 
# ingresar la información desde un tipo visual para 
# que sea intuitivo
def solution(request, pk):
    solution = Solution.objects.get(id=pk)
    context = {'solution': solution}
    return render(request, 'base/solution.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    solutions = user.solution_set.all()  
    messages = user.message_set.all()  
    topics = Topic.objects.all()
    context = {'user':user, 'solutions': solutions, 'm_messages': messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def createSolution(request, pk):
    problem = Problem.objects.get(id=pk)
    form = SolutionForm()
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            # Crea el objeto pero no lo guardes en la base de datos todavía
            solution = form.save(commit=False)
            solution.user = request.user 
            solution.problem = problem


            # Asigna el problema y el autor (el usuario logueado)

            solution.save()
            problem.solvers.add(request.user)
            return redirect('problem', pk=problem.id)
    context = {'form': form, 'problem': problem}
    return render(request, 'base/solution_form.html', context)

@login_required(login_url='/login')
def updateSolution(request, pk):
    solution = Solution.objects.get(id=pk)
    problem = solution.problem
    form = SolutionForm(instance=solution)

    if request.user != solution.user:
        return HttpResponse('Your are not alllowed here')
    
    if request.method == 'POST':
        form = SolutionForm(request.POST, instance = solution)
        if form.is_valid():
            form.save()
            return redirect('problem', pk=problem.id)

    context = {'form':form, 'problem': problem}
    return render(request, 'base/solution_form.html', context)

@login_required(login_url='/login')
def deleteSolution(request, pk):
    solution = get_object_or_404(Solution, id=pk)
    problem = solution.problem
    
    if request.user != solution.user:
        return HttpResponse('Your are not alllowed here')
    
    if request.method == 'POST':
        solution.delete()
        return redirect('problem', pk=problem.id) # or wherever you want to redirect to
    
    context = {'obj': solution}
    return render(request, 'base/delete.html', context)


@login_required(login_url='/login')
def deleteMessage(request, pk):
    messages = get_object_or_404(Message, id=pk)
    problem = messages.problem


    if request.user != messages.user:
        return HttpResponse('Your are not zalllowed here')
    
    if request.method == 'POST':
        messages.delete()
        return redirect('problem', pk=problem.id) # or wherever you want to redirect to
    
    context = {'obj': messages}
    return render(request, 'base/delete.html', context)




