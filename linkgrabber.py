""#line:8
import re #line:9
import urllib .request #line:10
import csv #line:11
from PyQt5 import QtCore ,QtGui ,QtWidgets #line:12
import sys #line:13
import os #line:14
'''
    DECLARE MAIN FILES AND OPEN FILES
    
'''#line:19
dir =''#line:23
url =''#line:25
key =''#line:27
list =[]#line:31
log =[]#line:32
def main ():#line:35
    import sys #line:40
    O00OO0O0O0OO00000 =QtWidgets .QApplication (sys .argv )#line:41
    OOO0O0000O00O00OO =QtWidgets .QMainWindow ()#line:42
    OOO0OOOO0000O0O00 =Ui_Linkgrabber ()#line:43
    OOO0OOOO0000O0O00 .setupUi (OOO0O0000O00O00OO )#line:44
    OOO0O0000O00O00OO .show ()#line:45
    sys .exit (O00OO0O0O0OO00000 .exec_ ())#line:46
def openfile ():#line:48
    ""#line:52
    O00OOO00000O00O00 =open (dir +"/links.txt",'w');#line:54
    print ("N "+dir )#line:56
    with open (dir +"/temp.txt",'r',encoding ='utf8')as OOOOO00O0OOOOO00O :#line:58
            print ("K")#line:60
            for OOOO00O0000O000O0 in OOOOO00O0OOOOO00O :#line:62
                OOOO00O0000O000O0 =OOOO00O0000O000O0 .strip ()#line:63
                OOOO0O00O0OO0OOO0 =re .findall (r'(https?://[^\s]+)',OOOO00O0000O000O0 )#line:64
                O0O00000O0OOO000O =str (OOOO0O00O0OO0OOO0 )#line:66
                print (O0O00000O0OOO000O )#line:67
                if key in O0O00000O0OOO000O :#line:69
                    if OOOO0O00O0OO0OOO0 :#line:70
                        list .append (O0O00000O0OOO000O )#line:71
                        log .append (OOOO0O00O0OO0OOO0 )#line:72
    O00OOO00000O00O00 .write (replace (list ))#line:74
    O00OOO00000O00O00 .close ()#line:75
'''

        REPLACE TRASH
    
'''#line:81
def replace (OOOO0O0O00000OOO0 ):#line:82
    OOOO0O0O00000OOO0 =str (OOOO0O0O00000OOO0 )#line:83
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace ('[','')#line:84
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace (']','')#line:85
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace (',','\n')#line:86
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace ('\'','')#line:87
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace ('"','')#line:88
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace ('\\','')#line:89
    OOOO0O0O00000OOO0 =OOOO0O0O00000OOO0 .replace ('></span>','')#line:90
    return OOOO0O0O00000OOO0 #line:91
'''
    MAIN 
    
'''#line:96
def getHtml ():#line:97
    OOOOO0O00O0O000OO ={}#line:101
    OOOOO0O00O0O000OO ['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"#line:102
    OO0O00O00O0OO00O0 =urllib .request .Request (url ,headers =OOOOO0O00O0O000OO )#line:103
    OO0O0000OO0O0O0OO =urllib .request .urlopen (OO0O00O00O0OO00O0 )#line:104
    OO00000O0OOO000O0 =OO0O0000OO0O0O0OO .read ()#line:105
    OOOOO0O0O0OOOO0OO =open (dir +"/temp.txt",'wb')#line:110
    print (OOOOO0O0O0OOOO0OO )#line:112
    OOOOO0O0O0OOOO0OO .write ((OO00000O0OOO000O0 ))#line:114
    OOOOO0O0O0OOOO0OO .close ()#line:116
class Ui_Linkgrabber (object ):#line:120
    def setupUi (OOO00OOO00OO0OOO0 ,O00OO0000OOOO0000 ):#line:121
        O00OO0000OOOO0000 .setObjectName ("Linkgrabber")#line:122
        O00OO0000OOOO0000 .setWindowModality (QtCore .Qt .NonModal )#line:123
        O00OO0000OOOO0000 .resize (580 ,332 )#line:124
        O00OO0000OOOO0000 .setAutoFillBackground (False )#line:125
        O00OO0000OOOO0000 .setStyleSheet ("*{\n" "    background-color: rgb(0, 0, 0);\n" "}\n" "\n" "#textDir{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "#textDir_2{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "#textDir_3{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "\n" "#keyBox{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "\n" "#urlBox{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "\n" "#logBox{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "\n" "#dirBox{\n" "    background-color: rgb(0, 0, 0);\n" "    color: green;\n" "}\n" "")#line:162
        O00OO0000OOOO0000 .setDocumentMode (False )#line:163
        O00OO0000OOOO0000 .setTabShape (QtWidgets .QTabWidget .Rounded )#line:164
        OOO00OOO00OO0OOO0 .centralwidget =QtWidgets .QWidget (O00OO0000OOOO0000 )#line:165
        OOO00OOO00OO0OOO0 .centralwidget .setObjectName ("centralwidget")#line:166
        OOO00OOO00OO0OOO0 .dirBox =QtWidgets .QPlainTextEdit (OOO00OOO00OO0OOO0 .centralwidget )#line:167
        OOO00OOO00OO0OOO0 .dirBox .setGeometry (QtCore .QRect (20 ,20 ,361 ,31 ))#line:168
        OOO00OOO00OO0OOO0 .dirBox .setObjectName ("dirBox")#line:169
        OOO00OOO00OO0OOO0 .urlBox =QtWidgets .QPlainTextEdit (OOO00OOO00OO0OOO0 .centralwidget )#line:170
        OOO00OOO00OO0OOO0 .urlBox .setGeometry (QtCore .QRect (20 ,80 ,361 ,31 ))#line:171
        OOO00OOO00OO0OOO0 .urlBox .setDocumentTitle ("")#line:172
        OOO00OOO00OO0OOO0 .urlBox .setObjectName ("urlBox")#line:173
        OOO00OOO00OO0OOO0 .textDir =QtWidgets .QLabel (OOO00OOO00OO0OOO0 .centralwidget )#line:174
        OOO00OOO00OO0OOO0 .textDir .setGeometry (QtCore .QRect (390 ,20 ,141 ,31 ))#line:175
        OOO00OOO00OO0OOO0 .textDir .setObjectName ("textDir")#line:176
        OOO00OOO00OO0OOO0 .textDir_2 =QtWidgets .QLabel (OOO00OOO00OO0OOO0 .centralwidget )#line:177
        OOO00OOO00OO0OOO0 .textDir_2 .setGeometry (QtCore .QRect (390 ,80 ,131 ,31 ))#line:178
        OOO00OOO00OO0OOO0 .textDir_2 .setObjectName ("textDir_2")#line:179
        OOO00OOO00OO0OOO0 .keyBox =QtWidgets .QPlainTextEdit (OOO00OOO00OO0OOO0 .centralwidget )#line:180
        OOO00OOO00OO0OOO0 .keyBox .setGeometry (QtCore .QRect (20 ,130 ,361 ,31 ))#line:181
        OOO00OOO00OO0OOO0 .keyBox .setObjectName ("keyBox")#line:182
        OOO00OOO00OO0OOO0 .textDir_3 =QtWidgets .QLabel (OOO00OOO00OO0OOO0 .centralwidget )#line:183
        OOO00OOO00OO0OOO0 .textDir_3 .setGeometry (QtCore .QRect (390 ,130 ,131 ,31 ))#line:184
        OOO00OOO00OO0OOO0 .textDir_3 .setObjectName ("textDir_3")#line:185
        OOO00OOO00OO0OOO0 .logBox =QtWidgets .QTextEdit (OOO00OOO00OO0OOO0 .centralwidget )#line:186
        OOO00OOO00OO0OOO0 .logBox .setGeometry (QtCore .QRect (20 ,170 ,361 ,91 ))#line:187
        OOO00OOO00OO0OOO0 .logBox .setReadOnly (True )#line:188
        OOO00OOO00OO0OOO0 .logBox .setObjectName ("logBox")#line:189
        OOO00OOO00OO0OOO0 .goButton =QtWidgets .QPushButton (OOO00OOO00OO0OOO0 .centralwidget )#line:190
        OOO00OOO00OO0OOO0 .goButton .setGeometry (QtCore .QRect (420 ,200 ,101 ,61 ))#line:191
        OOO00OOO00OO0OOO0 .goButton .setStyleSheet ("#goButton{\n" "    background-color:#44c767;\n" "    -moz-border-radius:28px;\n" "    -webkit-border-radius:28px;\n" "    border-radius:28px;\n" "    border:1px solid #18ab29;\n" "    display:inline-block;\n" "    cursor:pointer;\n" "    color:#ffffff;\n" "    font-family:Arial;\n" "    font-size:35px;\n" "    padding:4px 4px;\n" "    text-decoration:none;\n" "    text-shadow:0px 1px 0px #2f6627;\n" "}")#line:206
        OOO00OOO00OO0OOO0 .goButton .setObjectName ("goButton")#line:207
        OOO00OOO00OO0OOO0 .goButton .clicked .connect (OOO00OOO00OO0OOO0 .open )#line:210
        O00OO0000OOOO0000 .setCentralWidget (OOO00OOO00OO0OOO0 .centralwidget )#line:214
        OOO00OOO00OO0OOO0 .menubar =QtWidgets .QMenuBar (O00OO0000OOOO0000 )#line:215
        OOO00OOO00OO0OOO0 .menubar .setGeometry (QtCore .QRect (0 ,0 ,580 ,21 ))#line:216
        OOO00OOO00OO0OOO0 .menubar .setObjectName ("menubar")#line:217
        O00OO0000OOOO0000 .setMenuBar (OOO00OOO00OO0OOO0 .menubar )#line:218
        OOO00OOO00OO0OOO0 .statusbar =QtWidgets .QStatusBar (O00OO0000OOOO0000 )#line:219
        OOO00OOO00OO0OOO0 .statusbar .setObjectName ("statusbar")#line:220
        O00OO0000OOOO0000 .setStatusBar (OOO00OOO00OO0OOO0 .statusbar )#line:221
        OOO00OOO00OO0OOO0 .retranslateUi (O00OO0000OOOO0000 )#line:223
        QtCore .QMetaObject .connectSlotsByName (O00OO0000OOOO0000 )#line:224
    def open (O0O0OOO00OOO0O00O ):#line:226
        OOO0O000000O00OOO =str (O0O0OOO00OOO0O00O .dirBox .toPlainText ())#line:231
        OOO0O000000O00OOO =OOO0O000000O00OOO .replace ('\\','/')#line:232
        print ('D> '+OOO0O000000O00OOO )#line:233
        OOOOOOOO00OO0O000 =open (OOO0O000000O00OOO +'/links.txt','w');#line:238
        OOOOOOOO00OO0O000 .close ()#line:239
        OOOO0O0O0O0O0O00O =open (OOO0O000000O00OOO +"/temp.txt",'w')#line:240
        OOOO0O0O0O0O0O00O .close ()#line:241
        main .dir =OOO0O000000O00OOO #line:243
        main .url =str (O0O0OOO00OOO0O00O .urlBox .toPlainText ())#line:244
        main .key =str (O0O0OOO00OOO0O00O .keyBox .toPlainText ())#line:245
        main .getHtml ()#line:247
        main .openfile ()#line:248
        _OOO0OO0O000OOOOO0 =QtCore .QCoreApplication .translate #line:250
        print (main .log )#line:251
        O0O0OOO00OOO0O00O .logBox .setText (str (main .log ))#line:252
        os .remove (OOO0O000000O00OOO +"/temp.txt")#line:253
    def retranslateUi (O0OOOOO0O00OO0OO0 ,OO00000O0OOO0OOO0 ):#line:257
        _O0OO00O00OO00OOO0 =QtCore .QCoreApplication .translate #line:258
        OO00000O0OOO0OOO0 .setWindowTitle (_O0OO00O00OO00OOO0 ("Linkgrabber","Link Grabber v1.0 - Elitcody"))#line:259
        O0OOOOO0O00OO0OO0 .dirBox .setPlainText (_O0OO00O00OO00OOO0 ("Linkgrabber","C:/Users/<Name>/Desktop"))#line:260
        O0OOOOO0O00OO0OO0 .urlBox .setPlainText (_O0OO00O00OO00OOO0 ("Linkgrabber","https://google.com"))#line:261
        O0OOOOO0O00OO0OO0 .textDir .setText (_O0OO00O00OO00OOO0 ("Linkgrabber","Directory with / instead of \\"))#line:262
        O0OOOOO0O00OO0OO0 .textDir_2 .setText (_O0OO00O00OO00OOO0 ("Linkgrabber","Site link"))#line:263
        O0OOOOO0O00OO0OO0 .keyBox .setPlainText (_O0OO00O00OO00OOO0 ("Linkgrabber","speed"))#line:264
        O0OOOOO0O00OO0OO0 .textDir_3 .setText (_O0OO00O00OO00OOO0 ("Linkgrabber","Key to find"))#line:265
        O0OOOOO0O00OO0OO0 .goButton .setText (_O0OO00O00OO00OOO0 ("Linkgrabber","GO"))#line:266
if __name__ =='__main__':#line:269
    main ()