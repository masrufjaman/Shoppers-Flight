from django.shortcuts import render
import mysql.connector as sql
fd=''
ad=''
dc=''
oc=''
pn=''
tn=''
an=''
email=''
phone=''
def land_page(request):
    return render(request, 'index.html')
def post_request(request):
    global fd, ad, dc, oc, pn, tn, an, email, phone
    if request.method =="POST":
    x=sql.connect(host="localhost", user="root",password="chayon",database='website')
    cursor=x.cursor()
    d=request.POST
    for key,value in d.items():
        if key=="Flight_Date":
            fd=value
        if key=="Arrival_date":
            ad=value
        if key=="Destination_country":
            dc=value
        if key=="Origin_country":
            oc=value
        if key=="Passport_no":
            pn=value
        if key=="ticket_no":
            tn=value
        if key=="Airlines_name":
            an=value
        if key=="email":
            email=value
        if key=="phone":
            phone=value
    c="insert into detail Values('{}','{}','{}''{}','{}','{}','{}','{}','{}')".format(fd,ad,dc,oc,pn,tn,an,email,phone)
    cursor.execute(c)
    x.commit()

    return render(request, 'flightDetails.html')
