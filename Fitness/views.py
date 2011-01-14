# Crete your views here.
from django.shortcuts import HttpResponse
from mydjango.Fitness.models import Reps, Weight, Running

def index(request):
    response = HttpResponse()
    response.write("<html><body><center><H1> INDEX</H1></center><HR>")
    replist = Reps.objects.all()
    for p in replist:
        junk = "I did %d %s on %s" % (p.reps,p.exercise,p.timeenter)
        response.write("%s--%s<br>" % (junk,p.more)) 
    response.write("</body></html>")
    return response


def replist(request):
    response = HttpResponse()
    response.write("<html><body><center><H1>all my exercise that's fit to print</H1></center><HR>")
    replist = Reps.objects.all()
    for p in replist:
        junk = "I did %d %s on %s" % (p.reps,p.exercise,p.timeenter)
        response.write("%s--%s.<br>" % (junk,p.more)) 
    return response

def weightlist(request):
    response = HttpResponse()
    response.write("<html><body><center><H2>Obsessing on my weight</H2></center><HR>")
    wlist = Weight.objects.all()
    for p in wlist:
        junk = "I weighed %s on %s" % (p.damage,p.timeenter)
        response.write("%s--%s.<br>" % (junk,p.data)) 
    response.write("</body></html>")
    return response

def runlist(request):
    response = HttpResponse()
    response.write("<html><body><center><H1>my running log</H1></center><HR>")
    runlist = Running.objects.all()
    for p in runlist:
        junk = "I ran %d minutes on %s" % (p.minutes,p.timeenter)
        response.write("%s--%s.<br>" % (junk,p.data)) 
    response.write("</body></html>")
    return response
