from num2words import num2words #line:1
class BasisRechnungen :#line:4
    def __init__ (O00OOOO0000O0O00O ,O00O0O00OOOO0OO0O ,O0000OO0000OOOOO0 ,OOO0O0O0O0OOOO000 ):#line:5
        O00OOOO0000O0O00O .length =O00O0O00OOOO0OO0O #line:6
        O00OOOO0000O0O00O .width =O0000OO0000OOOOO0 #line:7
        O00OOOO0000O0O00O .depth =OOO0O0O0O0OOOO000 #line:8
    def volume (O0OO0000000O0O0O0 ):#line:10
        return O0OO0000000O0O0O0 .length *O0OO0000000O0O0O0 .width *O0OO0000000O0O0O0 .depth #line:11
    def area (O00O00OO000OO0000 ):#line:13
        return O00O00OO000OO0000 .length *O00O00OO000OO0000 .width #line:14
calculate =BasisRechnungen (int (input ("Länge ")),int (input ("Breite ")),int (input ("Höhe ")))#line:22
print ("Fläche: ",calculate .area (),"cm²\n" "In Worten: ",num2words (calculate .area (),lang ='de'))#line:24
print ("")#line:25
print ("Volumen: ",calculate .volume (),"cm³\n" "In Worten: ",num2words (calculate .volume (),lang ='de'))#line:26
