from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import ast

from .models import User, Paper, Query, Section, Answers
from django import forms

# Create your views here.

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['identity','query']

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['name','questions', 'pdf_file','sections']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'students']

def index(request):
    if request.user.is_authenticated:
        if request.user.designation == "student":
            sections = request.user.my_section.all()
            papers = Paper.objects.filter(sections__in = sections).distinct()
        else:
            papers = Paper.objects.filter(professor = request.user)
    else:
        papers = []
    return render(request, "paper/index.html",{
        'papers':papers
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "paper/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "paper/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        designation = request.POST["designation"]
        if password != confirmation:
            return render(request, "paper/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.designation = designation
            user.save()
        except IntegrityError:
            return render(request, "paper/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "paper/register.html")

def upload(request):
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper1 = form.save(commit=False)
            paper1.professor = request.user
            paper1.save()
            sections = form.cleaned_data.get('sections')
            print(sections)
            if sections:
                paper1.sections.set(sections)
            return HttpResponseRedirect(reverse('upload_checked', args=[paper1.id]))
        else:
            print("Invalid form: ", form.errors)
            return render(request, 'paper/upload.html', {
                'form1': form,
                'sections': Section.objects.all(),
            })
    return render(request, 'paper/upload.html', {
        'form1': PaperForm(),
        'sections':Section.objects.all(),
    })

def upload_checked(request, paper_id):
    paper = Paper.objects.get(pk = paper_id)
    students = []
    for section in paper.sections.all():
        for student in section.students.all():
            if student not in students:
                students.append(student)
    if request.method == "POST":
        for student in students:
            pdf = request.FILES.get(f"{student.id}")
            if pdf:
                Answers.objects.create(
                    paper = paper,
                    student = student,
                    pdf = pdf
                )
            else:
                return HttpResponseRedirect(reverse('upload_checked',args=[paper.id]))
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'paper/upload_checked.html',{
        'paper':paper,
        'students':students,
    })

def allot(request):
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid Form!")
    return render(request, 'paper/allot.html',{
        'sections': Section.objects.all(),
        'students' : User.objects.filter(designation="student"),
        'form':SectionForm(),
    })

def edit_section(request, section_id):
    section = Section.objects.get(pk=section_id)
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == "delete":
            section.delete()
            return HttpResponseRedirect(reverse('allot'))
        else:        
            form = SectionForm(request.POST)
            if form.is_valid():
                section.name = form.cleaned_data['name']
                section.students.set(form.cleaned_data['students'])
                section.save()
                return HttpResponseRedirect(reverse('allot'))
    return render(request, 'paper/edit.html',{
        'section':section,
        'students':User.objects.filter(designation ="student"),
        'form':SectionForm()
    })

def view_student(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    def make_options(list1):
        options = []
        alphabets = list("abcdefghijklmnopqrstuvwxyz")
        list1 = ast.literal_eval(list1)
        for i in range(len(list1)):
            base_string = f"Q.{i+1}"
            obj = list1[i]
            stack = [(obj, base_string)]
            while stack:
                obj, string = stack.pop()
                if isinstance(obj, int):
                    options.append((obj, string))
                else:
                    for j in range(len(obj)):
                        stack.append((obj[j], string + '.' + alphabets[j%len(alphabets)]))
        return options
    
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            query1 = form.save(commit=False)
            query1.student = request.user
            query1.paper = paper
            query1.save()
        else:
            print("form invalid")
    
    return render(request, 'paper/view_stud.html',{
        'query_form': QueryForm(),
        'paper':paper,
        'options':make_options(paper.questions),
        'queries':Query.objects.filter(student = request.user, paper = paper),
        'response1': Answers.objects.filter(paper = paper, student = request.user).first()
    })

def view_prof(request, paper_id):
    paper1 = Paper.objects.get(pk=paper_id)
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        try:
            num = int(form_type)
            if type(num) == int:
                query = Query.objects.get(pk=form_type)
                query.response = request.POST.get('response')
                query.change_of_marks = request.POST.get('change_of_marks')
                query.resolved = True
                query.save()
            else:
                print("Type is not inetger1")
        except:
            if form_type == "stop":
                paper1.open = False
            elif form_type == "start":
                paper1.open = True
            elif form_type == "delete":
                paper1.delete()
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponseRedirect(reverse(index))
            paper1.save()

    queries_unres = Query.objects.filter(paper = paper1, resolved = False)
    query_res = Query.objects.filter(paper = paper1, resolved = True)
    return render(request, 'paper/view_prof.html',{
        'paper': Paper.objects.get(pk=paper_id),
        'queries_unres':queries_unres,
        'query_res':query_res,
    })