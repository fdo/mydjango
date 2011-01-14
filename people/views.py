from django.shortcuts import HttpResponse
from mydjango.people.models import Person

def index(request):
    response = HttpResponse()
    response.write("<center><H1>People</H1></center><HR>\n")
    lst = Person.objects.all()   # what we have in lst are the names
                                 # of all the people in the database
    for p in lst:
        link = "<a href=\"Info/%d/\">\n" % p.id
        response.write("<li>%s%s</a></li>\n" % (link,p.name)) 
    response.write("</body></html>\n")
    return response

def what(request):
    response = HttpResponse()
    response.write("<body><html>\n")
    response.write("<title>database programming is what this is</title>\n")
    response.write("<center><H3>some django code I whipped up to learn how to access a database from the web</H3></center><HR>\n")
    link = "<a href=\"/people/\">\n"
    response.write("<li>%slist of people</a></li>\n" % link) 
    link = "<a href=\"/fitness/weight/\">\n"
    response.write("<li>%srecordings of my weight</a></li>\n" % link) 
    link = "<a href=\"/fitness/running/\">\n"
    response.write("<li>%sskimpy running diary</a></li>\n" % link) 
    link = "<a href=\"/fitness/reps/\">\n"
    response.write("<li>%sexercise</a></li>\n" % link) 
    response.write("<p>coming soon I will let a SQL query be modified everso slightly (I am worried about SQL injection)<p>\n")
    response.write("</body></html>\n")
    return response
    
def details(request, pID='0'):
    myname = "everybody"
    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    if (pID == '0'):
        response.write("<center><H1>Details for %s</H1></center><HR>\n" % (myname))
    else:
        response.write("<center><H1>Details for Person%s</H1>\n" % pID)
    response.write("</BODY></HTML>\n")
    return response
    
def colors(request):
    colors = ("BLUE","RED","GREEN")
    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    response.write("<H1>Color Index</H1><HR>\n")
    for c in colors:
        response.write("<FONT COLOR=%s><LI>%s</LI></FONT>\n" % (c,c))
    response.write("</BODY></HTML>\n")
    return response