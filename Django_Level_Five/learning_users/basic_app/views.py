from django.shortcuts import render
from basic_app.forms import PersonForm
from basic_app.models import Person
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json

g1=Person.objects.filter(question_1__endswith='g').count()
n1=Person.objects.filter(question_1__endswith='n').count()
ss1=Person.objects.filter(question_1__endswith='ss').count()
ns1=Person.objects.filter(question_1__endswith='ns').count()
e1=Person.objects.filter(question_1__endswith='e').count()
#return render(request,'basic_app/base.html',{'dat': dat })
#print(dat.question_1)
g2=Person.objects.filter(question_2__endswith='g').count()
n2=Person.objects.filter(question_2__endswith='n').count()
ss2=Person.objects.filter(question_2__endswith='ss').count()
ns2=Person.objects.filter(question_2__endswith='ns').count()
e2=Person.objects.filter(question_2__endswith='e').count()

g3=Person.objects.filter(question_3__endswith='g').count()
n3=Person.objects.filter(question_3__endswith='n').count()
ss3=Person.objects.filter(question_3__endswith='ss').count()
ns3=Person.objects.filter(question_3__endswith='ns').count()
e3=Person.objects.filter(question_3__endswith='e').count()

g4=Person.objects.filter(question_4__endswith='g').count()
n4=Person.objects.filter(question_4__endswith='n').count()
ss4=Person.objects.filter(question_4__endswith='ss').count()
ns4=Person.objects.filter(question_4__endswith='ns').count()
e4=Person.objects.filter(question_4__endswith='e').count()

g5=Person.objects.filter(question_5__endswith='g').count()
n5=Person.objects.filter(question_5__endswith='n').count()
ss5=Person.objects.filter(question_5__endswith='ss').count()
ns5=Person.objects.filter(question_5__endswith='ns').count()
e5=Person.objects.filter(question_5__endswith='e').count()

g6=Person.objects.filter(question_6__endswith='g').count()
n6=Person.objects.filter(question_6__endswith='n').count()
ss6=Person.objects.filter(question_6__endswith='ss').count()
ns6=Person.objects.filter(question_6__endswith='ns').count()
e6=Person.objects.filter(question_6__endswith='e').count()

g7=Person.objects.filter(question_7__endswith='g').count()
n7=Person.objects.filter(question_7__endswith='n').count()
ss7=Person.objects.filter(question_7__endswith='ss').count()
ns7=Person.objects.filter(question_7__endswith='ns').count()
e7=Person.objects.filter(question_7__endswith='e').count()

g8=Person.objects.filter(question_8__endswith='g').count()
n8=Person.objects.filter(question_8__endswith='n').count()
ss8=Person.objects.filter(question_8__endswith='ss').count()
ns8=Person.objects.filter(question_8__endswith='ns').count()
e8=Person.objects.filter(question_8__endswith='e').count()

g9=Person.objects.filter(question_9__endswith='g').count()
n9=Person.objects.filter(question_9__endswith='n').count()
ss9=Person.objects.filter(question_9__endswith='ss').count()
ns9=Person.objects.filter(question_9__endswith='ns').count()
e9=Person.objects.filter(question_9__endswith='e').count()

g10=Person.objects.filter(question_10__endswith='g').count()
n10=Person.objects.filter(question_10__endswith='n').count()
ss10=Person.objects.filter(question_10__endswith='ss').count()
ns10=Person.objects.filter(question_10__endswith='ns').count()
e10=Person.objects.filter(question_10__endswith='e').count()

g11=Person.objects.filter(question_11__endswith='g').count()
n11=Person.objects.filter(question_11__endswith='n').count()
ss11=Person.objects.filter(question_11__endswith='ss').count()
ns11=Person.objects.filter(question_11__endswith='ns').count()
e11=Person.objects.filter(question_11__endswith='e').count()

g12=Person.objects.filter(question_12__endswith='g').count()
n12=Person.objects.filter(question_12__endswith='n').count()
ss12=Person.objects.filter(question_12__endswith='ss').count()
ns12=Person.objects.filter(question_12__endswith='ns').count()
e12=Person.objects.filter(question_12__endswith='e').count()

g13=Person.objects.filter(question_13__endswith='g').count()
n13=Person.objects.filter(question_13__endswith='n').count()
ss13=Person.objects.filter(question_13__endswith='ss').count()
ns13=Person.objects.filter(question_13__endswith='ns').count()
e13=Person.objects.filter(question_13__endswith='e').count()

g14=Person.objects.filter(question_14__endswith='g').count()
n14=Person.objects.filter(question_14__endswith='n').count()
ss14=Person.objects.filter(question_14__endswith='ss').count()
ns14=Person.objects.filter(question_14__endswith='ns').count()
e14=Person.objects.filter(question_14__endswith='e').count()

g15=Person.objects.filter(question_15__endswith='g').count()
n15=Person.objects.filter(question_15__endswith='n').count()
ss15=Person.objects.filter(question_15__endswith='ss').count()
ns15=Person.objects.filter(question_15__endswith='ns').count()
e15=Person.objects.filter(question_15__endswith='e').count()

g16=Person.objects.filter(question_16__endswith='g').count()
n16=Person.objects.filter(question_16__endswith='n').count()
ss16=Person.objects.filter(question_16__endswith='ss').count()
ns16=Person.objects.filter(question_16__endswith='ns').count()
e16=Person.objects.filter(question_16__endswith='e').count()

g17=Person.objects.filter(question_17__endswith='g').count()
n17=Person.objects.filter(question_17__endswith='n').count()
ss17=Person.objects.filter(question_17__endswith='ss').count()
ns17=Person.objects.filter(question_17__endswith='ns').count()
e17=Person.objects.filter(question_17__endswith='e').count()

g18=Person.objects.filter(question_18__endswith='g').count()
n18=Person.objects.filter(question_18__endswith='n').count()
ss18=Person.objects.filter(question_18__endswith='ss').count()
ns18=Person.objects.filter(question_18__endswith='ns').count()
e18=Person.objects.filter(question_18__endswith='e').count()

g19=Person.objects.filter(question_19__endswith='g').count()
n19=Person.objects.filter(question_19__endswith='n').count()
ss19=Person.objects.filter(question_19__endswith='ss').count()
ns19=Person.objects.filter(question_19__endswith='ns').count()
e19=Person.objects.filter(question_19__endswith='e').count()

g20=Person.objects.filter(question_20__endswith='g').count()
n20=Person.objects.filter(question_20__endswith='n').count()
ss20=Person.objects.filter(question_20__endswith='ss').count()
ns20=Person.objects.filter(question_20__endswith='ns').count()
e20=Person.objects.filter(question_20__endswith='e').count()

g21=Person.objects.filter(question_21__endswith='g').count()
n21=Person.objects.filter(question_21__endswith='n').count()
ss21=Person.objects.filter(question_21__endswith='ss').count()
ns21=Person.objects.filter(question_21__endswith='ns').count()
e21=Person.objects.filter(question_21__endswith='e').count()

g22=Person.objects.filter(question_22__endswith='g').count()
n22=Person.objects.filter(question_22__endswith='n').count()
ss22=Person.objects.filter(question_22__endswith='ss').count()
ns22=Person.objects.filter(question_22__endswith='ns').count()
e22=Person.objects.filter(question_22__endswith='e').count()

g23=Person.objects.filter(question_23__endswith='g').count()
n23=Person.objects.filter(question_23__endswith='n').count()
ss23=Person.objects.filter(question_23__endswith='ss').count()
ns23=Person.objects.filter(question_23__endswith='ns').count()
e23=Person.objects.filter(question_23__endswith='e').count()

g24=Person.objects.filter(question_24__endswith='g').count()
n24=Person.objects.filter(question_24__endswith='n').count()
ss24=Person.objects.filter(question_24__endswith='ss').count()
ns24=Person.objects.filter(question_24__endswith='ns').count()
e24=Person.objects.filter(question_24__endswith='e').count()

g25=Person.objects.filter(question_25__endswith='g').count()
n25=Person.objects.filter(question_25__endswith='n').count()
ss25=Person.objects.filter(question_25__endswith='ss').count()
ns25=Person.objects.filter(question_25__endswith='ns').count()
e25=Person.objects.filter(question_25__endswith='e').count()

g26=Person.objects.filter(question_26__endswith='g').count()
n26=Person.objects.filter(question_26__endswith='n').count()
ss26=Person.objects.filter(question_26__endswith='ss').count()
ns26=Person.objects.filter(question_26__endswith='ns').count()
e26=Person.objects.filter(question_26__endswith='e').count()

g27=Person.objects.filter(question_27__endswith='g').count()
n27=Person.objects.filter(question_27__endswith='n').count()
ss27=Person.objects.filter(question_27__endswith='ss').count()
ns27=Person.objects.filter(question_27__endswith='ns').count()
e27=Person.objects.filter(question_27__endswith='e').count()

g28=Person.objects.filter(question_28__endswith='g').count()
n28=Person.objects.filter(question_28__endswith='n').count()
ss28=Person.objects.filter(question_28__endswith='ss').count()
ns28=Person.objects.filter(question_28__endswith='ns').count()
e28=Person.objects.filter(question_28__endswith='e').count()

g29=Person.objects.filter(question_29__endswith='g').count()
n29=Person.objects.filter(question_29__endswith='n').count()
ss29=Person.objects.filter(question_29__endswith='ss').count()
ns29=Person.objects.filter(question_29__endswith='ns').count()
e29=Person.objects.filter(question_29__endswith='e').count()

g30=Person.objects.filter(question_30__endswith='g').count()
n30=Person.objects.filter(question_30__endswith='n').count()
ss30=Person.objects.filter(question_30__endswith='ss').count()
ns30=Person.objects.filter(question_30__endswith='ns').count()
e30=Person.objects.filter(question_30__endswith='e').count()

g31=Person.objects.filter(question_31__endswith='g').count()
n31=Person.objects.filter(question_31__endswith='n').count()
ss31=Person.objects.filter(question_31__endswith='ss').count()
ns31=Person.objects.filter(question_31__endswith='ns').count()
e31=Person.objects.filter(question_31__endswith='e').count()

c=Person.objects.all().count()

good1=(g1*100)/c
neutral1=(n1*100)/c
satisfied1=(ss1*100)/c
not_satisfied1=(ns1*100)/c
excellent1=(e1*100)/c

good2=(g2*100)/c
neutral2=(n2*100)/c
satisfied2=(ss2*100)/c
not_satisfied2=(ns2*100)/c
excellent2=(e2*100)/c

good3=(g3*100)/c
neutral3=(n3*100)/c
satisfied3=(ss3*100)/c
not_satisfied3=(ns3*100)/c
excellent3=(e3*100)/c


good4=(g4*100)/c
neutral4=(n4*100)/c
satisfied4=(ss4*100)/c
not_satisfied4=(ns4*100)/c
excellent4=(e4*100)/c

good5=(g5*100)/c
neutral5=(n5*100)/c
satisfied5=(ss5*100)/c
not_satisfied5=(ns5*100)/c
excellent5=(e5*100)/c

good6=(g6*100)/c
neutral6=(n6*100)/c
satisfied6=(ss6*100)/c
not_satisfied6=(ns6*100)/c
excellent6=(e6*100)/c

good7=(g7*100)/c
neutral7=(n7*100)/c
satisfied7=(ss7*100)/c
not_satisfied7=(ns7*100)/c
excellent7=(e7*100)/c

good8=(g8*100)/c
neutral8=(n8*100)/c
satisfied8=(ss8*100)/c
not_satisfied8=(ns8*100)/c
excellent8=(e8*100)/c

good9=(g9*100)/c
neutral9=(n9*100)/c
satisfied9=(ss9*100)/c
not_satisfied9=(ns9*100)/c
excellent9=(e9*100)/c

good10=(g10*100)/c
neutral10=(n10*100)/c
satisfied10=(ss10*100)/c
not_satisfied10=(ns10*100)/c
excellent10=(e10*100)/c

good11=(g11*100)/c
neutral11=(n11*100)/c
satisfied11=(ss11*100)/c
not_satisfied11=(ns11*100)/c
excellent11=(e11*100)/c

good12=(g12*100)/c
neutral12=(n12*100)/c
satisfied12=(ss12*100)/c
not_satisfied12=(ns12*100)/c
excellent12=(e12*100)/c

good13=(g13*100)/c
neutral13=(n13*100)/c
satisfied13=(ss13*100)/c
not_satisfied13=(ns13*100)/c
excellent13=(e13*100)/c

good14=(g14*100)/c
neutral14=(n14*100)/c
satisfied14=(ss14*100)/c
not_satisfied14=(ns14*100)/c
excellent14=(e14*100)/c

good15=(g15*100)/c
neutral15=(n15*100)/c
satisfied15=(ss15*100)/c
not_satisfied15=(ns15*100)/c
excellent15=(e15*100)/c

good16=(g16*100)/c
neutral16=(n16*100)/c
satisfied16=(ss16*100)/c
not_satisfied16=(ns16*100)/c
excellent16=(e16*100)/c

good17=(g17*100)/c
neutral17=(n17*100)/c
satisfied17=(ss17*100)/c
not_satisfied17=(ns17*100)/c
excellent17=(e17*100)/c

good18=(g18*100)/c
neutral18=(n18*100)/c
satisfied18=(ss18*100)/c
not_satisfied18=(ns18*100)/c
excellent18=(e18*100)/c


good19=(g19*100)/c
neutral19=(n19*100)/c
satisfied19=(ss19*100)/c
not_satisfied19=(ns19*100)/c
excellent19=(e19*100)/c

good20=(g20*100)/c
neutral20=(n20*100)/c
satisfied20=(ss20*100)/c
not_satisfied20=(ns20*100)/c
excellent20=(e20*100)/c

good21=(g21*100)/c
neutral21=(n21*100)/c
satisfied21=(ss21*100)/c
not_satisfied21=(ns21*100)/c
excellent21=(e21*100)/c

good22=(g22*100)/c
neutral22=(n22*100)/c
satisfied22=(ss22*100)/c
not_satisfied22=(ns22*100)/c
excellent22=(e22*100)/c

good23=(g23*100)/c
neutral23=(n23*100)/c
satisfied23=(ss23*100)/c
not_satisfied23=(ns23*100)/c
excellent23=(e23*100)/c


good24=(g24*100)/c
neutral24=(n24*100)/c
satisfied24=(ss24*100)/c
not_satisfied24=(ns24*100)/c
excellent24=(e24*100)/c

good25=(g25*100)/c
neutral25=(n25*100)/c
satisfied25=(ss25*100)/c
not_satisfied25=(ns25*100)/c
excellent25=(e25*100)/c

good26=(g26*100)/c
neutral26=(n26*100)/c
satisfied26=(ss26*100)/c
not_satisfied26=(ns26*100)/c
excellent26=(e26*100)/c

good27=(g27*100)/c
neutral27=(n27*100)/c
satisfied27=(ss27*100)/c
not_satisfied27=(ns27*100)/c
excellent27=(e27*100)/c

good28=(g28*100)/c
neutral28=(n28*100)/c
satisfied28=(ss28*100)/c
not_satisfied28=(ns28*100)/c
excellent28=(e28*100)/c

good29=(g29*100)/c
neutral29=(n29*100)/c
satisfied29=(ss29*100)/c
not_satisfied29=(ns29*100)/c
excellent29=(e29*100)/c

good30=(g30*100)/c
neutral30=(n30*100)/c
satisfied30=(ss30*100)/c
not_satisfied30=(ns30*100)/c
excellent30=(e30*100)/c

good31=(g31*100)/c
neutral31=(n31*100)/c
satisfied31=(ss31*100)/c
not_satisfied31=(ns31*100)/c
excellent31=(e31*100)/c
# Create your views here.
def data(request):
   


    html = """<html>
    <body>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <div class="container">
    <div class="jumbotron">
    <h2> details for question 1</h2>
    <p>who marked not satisfied for question 1 =  {0}.</p>
    <p>who marked  satisfied for question 1 =  {1}.
    </p><p>who marked neutral for question 1 = {2}.</p>
    <p>who marked good for question 1 =  {3}.</p>
    <p>who marked excelent for question 1 =  {4}.</p>
    </br>
    </br>
    <h2> details for question 2</h2>
    <p>who marked not satisfied for question 2 =  {5}.</p>
    <p>who marked  satisfied for question 2 =  {6}.
    </p><p>who marked neutral for question 2 = {7}.</p>
    <p>who marked good for question 2 =  {8}.</p>
    <p>who marked excelent for question 2 =  {9}.</p>
    </br>
    </br>

    <h2> details for question 3</h2>
    <p>who marked not satisfied for question 3 =  {10}.</p>
    <p>who marked  satisfied for question 3 =  {11}.
    </p><p>who marked neutral for question 3 = {12}.</p>
    <p>who marked good for question 3 =  {13}.</p>
    <p>who marked excelent for question 3 =  {14}.</p>
    </br>
    </br>

    <h2> details for question 4</h2>
    <p>who marked not satisfied for question 4 =  {15}.</p>
    <p>who marked  satisfied for question 4 =  {16}.
    </p><p>who marked neutral for question 4 = {17}.</p>
    <p>who marked good for question 4 =  {18}.</p>
    <p>who marked excelent for question 4 =  {19}.</p>
    </br>
    </br>

    <h2> details for question 5 </h2>
    <p>who marked not satisfied for question 5 =  {20}.</p>
    <p>who marked  satisfied for question 5 =  {21}.
    </p><p>who marked neutral for question 5 = {22}.</p>
    <p>who marked good for question 5 =  {23}.</p>
    <p>who marked excelent for question 5 =  {24}.</p>
    </br>
    </br>
    <h2> details for question 6</h2>
    <p>who marked not satisfied for question 6 =  {25}.</p>
    <p>who marked  satisfied for question 6 =  {26}.
    </p><p>who marked neutral for question 6 = {27}.</p>
    <p>who marked good for question 6 =  {28}.</p>
    <p>who marked excelent for question 6 =  {29}.</p>
    </br>
    </br>


    <h2> details for question 7</h2>
    <p>who marked not satisfied for question 7 =  {30}.</p>
    <p>who marked  satisfied for question 7 =  {31}.
    </p><p>who marked neutral for question 7 = {32}.</p>
    <p>who marked good for question 7 =  {33}.</p>
    <p>who marked excelent for question 7 =  {34}.</p>
    </br>
    </br>

    <h2> details for question 8</h2>
    <p>who marked not satisfied for question 8 =  {35}.</p>
    <p>who marked  satisfied for question 8 =  {36}.
    </p><p>who marked neutral for question 8 = {37}.</p>
    <p>who marked good for question 8 =  {38}.</p>
    <p>who marked excelent for question 8 =  {39}.</p>
    </br>
    </br>

    <h2> details for question 9</h2>
    <p>who marked not satisfied for question 9 =  {40}.</p>
    <p>who marked  satisfied for question 9 =  {41}.
    </p><p>who marked neutral for question 9 = {42}.</p>
    <p>who marked good for question 9 =  {43}.</p>
    <p>who marked excelent for question 9 =  {44}.</p>
    </br>
    </br>

    <h2> details for question 10</h2>
    <p>who marked not satisfied for question 10 =  {45}.</p>
    <p>who marked  satisfied for question 10 =  {46}.
    </p><p>who marked neutral for question 10 = {47}.</p>
    <p>who marked good for question 10 =  {48}.</p>
    <p>who marked excelent for question 10 =  {49}.</p>
    </br>
    </br>

    <h2> details for question 11</h2>
    <p>who marked not satisfied for question 11 =  {50}.</p>
    <p>who marked  satisfied for question 11 =  {51}.
    </p><p>who marked neutral for question 11 = {52}.</p>
    <p>who marked good for question 11 =  {53}.</p>
    <p>who marked excelent for question 11 =  {54}.</p>
    </br>
    </br>

    <h2> details for question 12</h2>
    <p>who marked not satisfied for question 12 =  {55}.</p>
    <p>who marked  satisfied for question 12 =  {56}.
    </p><p>who marked neutral for question 12 = {57}.</p>
    <p>who marked good for question 12 =  {58}.</p>
    <p>who marked excelent for question 12 =  {59}.</p>
    </br>
    </br>

    <h2> details for question 13</h2>
    <p>who marked not satisfied for question 13 =  {60}.</p>
    <p>who marked  satisfied for question 13 =  {61}.
    </p><p>who marked neutral for question 13 = {62}.</p>
    <p>who marked good for question 13 =  {63}.</p>
    <p>who marked excelent for question 13 =  {64}.</p>
    </br>
    </br>

    <h2> details for question 14</h2>
    <p>who marked not satisfied for question 14 =  {65}.</p>
    <p>who marked  satisfied for question 14 =  {66}.
    </p><p>who marked neutral for question 14 = {67}.</p>
    <p>who marked good for question 14 =  {68}.</p>
    <p>who marked excelent for question 14 =  {69}.</p>
    </br>
    </br>

    <h2> details for question 15</h2>
    <p>who marked not satisfied for question 15 =  {70}.</p>
    <p>who marked  satisfied for question 15 =  {71}.
    </p><p>who marked neutral for question 15 = {72}.</p>
    <p>who marked good for question 15 =  {73}.</p>
    <p>who marked excelent for question 15 =  {74}.</p>
    </br>
    </br>

    <h2> details for question 16</h2>
    <p>who marked not satisfied for question 16 =  {75}.</p>
    <p>who marked  satisfied for question 16 =  {76}.
    </p><p>who marked neutral for question 16 = {77}.</p>
    <p>who marked good for question 16 =  {78}.</p>
    <p>who marked excelent for question 16 =  {79}.</p>
    </br>
    </br>

    <h2> details for question 17</h2>
    <p>who marked not satisfied for question 17 :-  '{80}'.</p>
    <p>who marked  satisfied for question 17 :-  '{81}'.
    </p><p>who marked neutral for question 17 :- '{82}'.</p>
    <p>who marked good for question 17 :-  '{83}'.</p>
    <p>who marked excelent for question 17 :-  '{84}'.</p>
    </br>
    </br>

    <h2> details for question 18</h2>
    <p>who marked not satisfied for question 18 =  {85}.</p>
    <p>who marked  satisfied for question 18 =  {86}.
    </p><p>who marked neutral for question 18 = {87}.</p>
    <p>who marked good for question 18 =  {88}.</p>
    <p>who marked excelent for question 18 =  {89}.</p>
    </br>
    </br>

    <h2> details for question 19</h2>
    <p>who marked not satisfied for question 19 =  {90}.</p>
    <p>who marked  satisfied for question 19 =  {91}.
    </p><p>who marked neutral for question 19 = {92}.</p>
    <p>who marked good for question 19 =  {93}.</p>
    <p>who marked excelent for question 19 =  {94}.</p>
    </br>
    </br>

    <h2> details for question 20</h2>
    <p>who marked not satisfied for question 20 =  {95}.</p>
    <p>who marked  satisfied for question 20 =  {96}.
    </p><p>who marked neutral for question 20 = {97}.</p>
    <p>who marked good for question 20 =  {98}.</p>
    <p>who marked excelent for question 20 =  {99}.</p>
    </br>
    </br>

    <h2> details for question 21</h2>
    <p>who marked not satisfied for question 21 =  {100}.</p>
    <p>who marked  satisfied for question 21 =  {101}.
    </p><p>who marked neutral for question 21 = {102}.</p>
    <p>who marked good for question 21 =  {103}.</p>
    <p>who marked excelent for question 21 =  {104}.</p>
    </br>
    </br>

    <h2> details for question 22</h2>
    <p>who marked not satisfied for question 22 =  {105}.</p>
    <p>who marked  satisfied for question 22 =  {106}.
    </p><p>who marked neutral for question 22 = {107}.</p>
    <p>who marked good for question 22 =  {108}.</p>
    <p>who marked excelent for question 22 =  {109}.</p>
    </br>
    </br>

    <h2> details for question 23</h2>
    <p>who marked not satisfied for question 23 =  {110}.</p>
    <p>who marked  satisfied for question 23 =  {111}.
    </p><p>who marked neutral for question 23 = {112}.</p>
    <p>who marked good for question 23 =  {113}.</p>
    <p>who marked excelent for question 23 =  {114}.</p>
    </br>
    </br>

    <h2> details for question 24</h2>
    <p>who marked not satisfied for question 24 =  {115}.</p>
    <p>who marked  satisfied for question 24 =  {116}.
    </p><p>who marked neutral for question 24 = {117}.</p>
    <p>who marked good for question 24 =  {118}.</p>
    <p>who marked excelent for question 24 =  {119}.</p>
    </br>
    </br>

    <h2> details for question 25</h2>
    <p>who marked not satisfied for question 25 =  {120}.</p>
    <p>who marked  satisfied for question 25 =  {121}.
    </p><p>who marked neutral for question 25 = {122}.</p>
    <p>who marked good for question 25 =  {123}.</p>
    <p>who marked excelent for question 25 =  {124}.</p>
    </br>
    </br>

    <h2> details for question 26</h2>
    <p>who marked not satisfied for question 26 =  {125}.</p>
    <p>who marked  satisfied for question 26 =  {126}.
    </p><p>who marked neutral for question 26 = {127}.</p>
    <p>who marked good for question 26 =  {128}.</p>
    <p>who marked excelent for question 26 =  {129}.</p>
    </br>
    </br>

    <h2> details for question 27</h2>
    <p>who marked not satisfied for question 27 =  {130}.</p>
    <p>who marked  satisfied for question 27 =  {131}.
    </p><p>who marked neutral for question 27 = {132}.</p>
    <p>who marked good for question 27 =  {133}.</p>
    <p>who marked excelent for question 27 =  {134}.</p>
    </br>
    </br>

    <h2> details for question 28</h2>
    <p>who marked not satisfied for question 28 =  {135}.</p>
    <p>who marked  satisfied for question 28 =  {136}.
    </p><p>who marked neutral for question 28 = {137}.</p>
    <p>who marked good for question 28 =  {138}.</p>
    <p>who marked excelent for question 28 =  {139}.</p>
    </br>
    </br>

    <h2> details for question 29</h2>
    <p>who marked not satisfied for question 29 =  {140}.</p>
    <p>who marked  satisfied for question 29 =  {141}.
    </p><p>who marked neutral for question 29 = {142}.</p>
    <p>who marked good for question 29 =  {143}.</p>
    <p>who marked excelent for question 29 =  {144}.</p>
    </br>
    </br>

    <h2> details for question 30</h2>
    <p>who marked not satisfied for question 30 =  {145}.</p>
    <p>who marked  satisfied for question 30 =  {146}.
    </p><p>who marked neutral for question 30 = {147}.</p>
    <p>who marked good for question 30 =  {148}.</p>
    <p>who marked excelent for question 30 =  {149}.</p>
    </br>
    </br>

    <h2> details for question 31</h2>
    <p>who marked not satisfied for question 31 =  {150}.</p>
    <p>who marked  satisfied for question 31 =  {151}.
    </p><p>who marked neutral for question 31 = {152}.</p>
    <p>who marked good for question 31 =  {153}.</p>
    <p>who marked excelent for question 31 =  {154}.</p>

    
    </br>
    </br>
    </div>
    </div>

    </body>
    </html>""" .format(ns1, ss1, n1, g1, e1,ns2, ss2, n2, g2, e2,ns3, ss3, n3, g3, e3,ns4, ss4, n4, g4, e4,ns5, ss5, n5, g5, e5,ns6, ss6, n6, g6, e6,ns7, ss7, n7, g7, e7,ns8, ss8, n8, g8, e8,ns9, ss9, n9, g9, e9,ns10, ss10, n10, g10, e10,ns11, ss11, n11, g11, e11,ns12, ss12, n12, g12, e12,ns13, ss13, n13, g13, e13,ns14, ss14, n14, g14, e14,ns15, ss15, n15, g15, e15,ns16, ss16, n16, g16, e16,ns17, ss17, n17, g17, e17,ns18, ss18, n18, g18, e18,ns19, ss19, n19, g19, e19,ns20, ss20, n20, g20, e20,ns21, ss21, n21, g21, e21,ns22, ss22, n22, g22, e22,ns23, ss23, n23, g23, e23,ns24, ss24, n24, g24, e24,ns25, ss25, n25, g25, e25,ns26, ss26, n26, g26, e26,ns27, ss27, n27, g27, e27,ns28, ss28, n28, g28, e28,ns29, ss29, n29, g29, e29,ns30, ss30, n30, g30, e30,ns31, ss31, n31, g31, e31)
    return HttpResponse(html)

def index(request):
    form=PersonForm()

    if request.method=="POST":
        form=PersonForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
        else:
            form=PersonForm()


    return render(request,'basic_app/index.html',{'form': form })





#for chart views
#user=get_user_model()

# class homeview(View):
    
    
#     def get(self,request,*args,**kwargs):
#         return render(request, 'basic_app/chart.html',{})

def get_data(request, *args, **kwargs):
    data={
       "good1": good1,
       "satisfied1": satisfied1,
       "not_satisfied1": not_satisfied1,
       "neutral1": neutral1,
       "excellent1": excellent1,

       "good2": good2,
       "satisfied2": satisfied2,
       "not_satisfied2": not_satisfied2,
       "neutral2": neutral2,
       "excellent2": excellent2,

       "good3": good3,
       "satisfied3": satisfied3,
       "not_satisfied3": not_satisfied3,
       "neutral3": neutral3,
       "excellent3": excellent3,

       "good4": good4,
       "satisfied4": satisfied4,
       "not_satisfied4": not_satisfied4,
       "neutral4": neutral4,
       "excellent4": excellent4,
       
        "good5": good5,
       "satisfied5": satisfied5,
       "not_satisfied5": not_satisfied5,
       "neutral5": neutral5,
       "excellent5": excellent5,

         "good6": good6,
       "satisfied6": satisfied6,
       "not_satisfied6": not_satisfied6,
       "neutral6": neutral6,
       "excellent6": excellent6, 

        "good7": good7,
       "satisfied7": satisfied7,
       "not_satisfied7": not_satisfied7,
       "neutral7": neutral7,
       "excellent7": excellent7,

        "good8": good8,
       "satisfied8": satisfied8,
       "not_satisfied8": not_satisfied8,
       "neutral8": neutral8,
       "excellent8": excellent8,  

         "good9": good9,
       "satisfied9": satisfied9,
       "not_satisfied9": not_satisfied9,
       "neutral9": neutral9,
       "excellent9": excellent9, 

         "good10": good10,
       "satisfied10": satisfied10,
       "not_satisfied10": not_satisfied10,
       "neutral10": neutral10,
       "excellent10": excellent10, 

         "good11": good11,
       "satisfied11": satisfied11,
       "not_satisfied11": not_satisfied11,
       "neutral11": neutral11,
       "excellent11": excellent11, 

         "good12": good12,
       "satisfied12": satisfied12,
       "not_satisfied12": not_satisfied12,
       "neutral12": neutral12,
       "excellent12": excellent12, 

         "good13": good13,
       "satisfied13": satisfied13,
       "not_satisfied13": not_satisfied13,
       "neutral13": neutral3,
       "excellent13": excellent13,

         "good14": good14,
       "satisfied14": satisfied14,
       "not_satisfied14": not_satisfied14,
       "neutral14": neutral14,
       "excellent14": excellent14,

         "good15": good15,
       "satisfied15": satisfied15,
       "not_satisfied15": not_satisfied15,
       "neutral15": neutral15,
       "excellent15": excellent15,

         "good16": good16,
       "satisfied16": satisfied16,
       "not_satisfied16": not_satisfied16,
       "neutral16": neutral16,
       "excellent16": excellent16,

         "good17": good17,
       "satisfied17": satisfied17,
       "not_satisfied17": not_satisfied17,
       "neutral17": neutral17,
       "excellent17": excellent17,

        "good18": good18,
       "satisfied18": satisfied18,
       "not_satisfied18": not_satisfied18,
       "neutral18": neutral18,
       "excellent18": excellent18,
        
         "good19": good19,
       "satisfied19": satisfied19,
       "not_satisfied19": not_satisfied19,
       "neutral19": neutral19,
       "excellent19": excellent19,
         
          "good20": good20,
       "satisfied20": satisfied20,
       "not_satisfied20": not_satisfied20,
       "neutral20": neutral20,
       "excellent20": excellent20,
        
        "good21": good21,
       "satisfied21": satisfied21,
       "not_satisfied21": not_satisfied21,
       "neutral21": neutral21,
       "excellent21": excellent21,

       "good22": good22,
       "satisfied22": satisfied22,
       "not_satisfied22": not_satisfied22,
       "neutral22": neutral22,
       "excellent22": excellent22,

       "good23": good23,
       "satisfied23": satisfied23,
       "not_satisfied23": not_satisfied23,
       "neutral23": neutral23,
       "excellent23": excellent23,

       "good24": good24,
       "satisfied24": satisfied24,
       "not_satisfied24": not_satisfied24,
       "neutral24": neutral24,
       "excellent24": excellent24,

       "good25": good25,
       "satisfied25": satisfied25,
       "not_satisfied25": not_satisfied25,
       "neutral25": neutral25,
       "excellent25": excellent25,

       "good26": good26,
       "satisfied26": satisfied26,
       "not_satisfied26": not_satisfied26,
       "neutral26": neutral26,
       "excellent26": excellent26,

       "good27": good27,
       "satisfied27": satisfied27,
       "not_satisfied27": not_satisfied27,
       "neutral27": neutral27,
       "excellent27": excellent27,

       "good28": good28,
       "satisfied28": satisfied28,
       "not_satisfied28": not_satisfied28,
       "neutral28": neutral28,
       "excellent28": excellent28,

       "good29": good29,
       "satisfied29": satisfied29,
       "not_satisfied29": not_satisfied29,
       "neutral29": neutral29,
       "excellent29": excellent29,

       "good30": good30,
       "satisfied30": satisfied30,
       "not_satisfied30": not_satisfied30,
       "neutral30": neutral30,
       "excellent30": excellent30,

       "good31": good31,
       "satisfied31": satisfied31,
       "not_satisfied31": not_satisfied31,
       "neutral31": neutral31,
       "excellent31": excellent31,

    }
    return render(request, 'basic_app/chart.html',{'data': data})


# class chartdata(APIView):

#     authentication_classes = []
#     permission_classes = []
    
#     def get(self, request, format=None):
#         qs_count=Person.objects.all().count()
#         labels=['users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
#         default_items=[qs_count,10,20,5,7,8]

#         data={
#         "labels":labels,
#         "default":default_items,
#         }
#         return Response(data)

def thankyou(request):
   
    return render(request, 'basic_app/thankyou.html', {})




User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'basic_app/charts.html', {"customers": 10})



def get_data2(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Not satisfied', 'Satisfied', 'Neutral', 'Good', 'Excellent']
        # default_items=[good1,good2,9,3,4,5,6]
        default_items = ( not_satisfied1,satisfied1,neutral1,good1, excellent1,  not_satisfied2,satisfied2,neutral2,good2,excellent2)
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)



