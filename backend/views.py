from django.http import  Http404
from backend.models import Project, Persona, Metadata, Category
from django.shortcuts import render_to_response
from django.template import RequestContext
       
def index(request):
    #import pdb; pdb.set_trace()
    return render_to_response('index.html',{
        'projects': Project.objects.filter(status = 1), 
        'alistair':Persona.objects.all()[:1].get(),
        'filters': Category.objects.filter(project__status=1).distinct(),
        'metadata': Metadata.objects.all(), },
        RequestContext(request) 
        )

def project_detail(request, name):
    try:
        project = Project.objects.get(name = name.replace('-',' '))
        details = project.projectdetail_set.all()
        #import pdb; pdb.set_trace()
    except Exception,e:
        raise Http404,e
    return render_to_response('details.html',{'project': project,
        'alistair':Persona.objects.all()[:1].get(),
        'details': details, 
        'metadata': Metadata.objects.all(),},
        RequestContext(request) 
        )

def bio(request):
    return render_to_response('bio.html',{'alistair':Persona.objects.all()[:1].get(),
        'metadata': Metadata.objects.all(), },
        RequestContext(request) )

def info(request):
    return render_to_response('info.html',{'alistair':Persona.objects.all()[:1].get(),
        'metadata': Metadata.objects.all(),},
        RequestContext(request) )

def test(request):
    return render_to_response('only-filter.html', RequestContext(request) )

def convert_collection_to_matrix(collection, cols):
    matrix = []
    while collection:
        matrix.append(collection[:cols])
        collection = collection[cols:]
    return matrix