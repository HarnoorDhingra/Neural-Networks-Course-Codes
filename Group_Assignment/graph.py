# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import graphviz
import os, io
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import numpy as np
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
# from graphs import Ui_Dialog
 
 
# def merge_graphs(name):
#     os.chdir('cache')
#     png2merge = [(name + '_' + str(i) + '.png') for i in range(4)]
#     result = Image.new("RGB", (786, 266))
 
#     for index, file in enumerate(png2merge):
#       path = os.path.expanduser(file)
#       img = Image.open(path)
#       img.thumbnail((391, 131), Image.ANTIALIAS)
#       x = index // 2 * 391
#       y = index % 2 * 131
#       w, h = img.size
#       print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
#       result.paste(img, (x+1, y+1, x + w + 1, y + h+1))
 
#     result.save(os.path.expanduser(name+'.png'))

def get_output(w1,w2,x1,x2,th):
	if w1*x1 + w2*x2 >= th:
		return 1
	else :
		return 0

def get_outputHotandCold(w1,w2,w3,w4,w5,w6,x1,x2,th):
	z2=x2
	z1=get_output(w1,w2,z2,x2,th)
	y1=get_output(w3,w4,x1,z1,th)
	y2=get_output(w5,w6,x2,z2,th)
	return [y1,y2]

def draw_hotcoldgraph(y1, y2, x1, x2, name="hotcold"):
	g=graphviz.Digraph(format='png')
	g.graph_attr['rankdir'] = 'LR'
	# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
	#       so that Graphviz recognizes it as a special cluster subgraph

# 	x1 = [1,0]
# 	x2 = [0,1]
	# y_true = [0,0,0,1]
	# w = [1,1]
	theta = 2
# 	y_pred = []

# 	for i in range(2):
# 		y_pred.append(get_outputHotandCold(2,-1,2,2,1,1,x1[i],x2[i],theta))

	
	with g.subgraph(name='cluster_10') as c:
		c.attr(color='blue')
		with c.subgraph(name='cluster0_inp') as inp:
			inp.attr(rank='same', color='gray')
			inp.node('x01','hot_input = ' + str(x1), fillcolor="gray", style="filled", rank='same')
			inp.node('x02','cold_input = ' + str(x2), fillcolor="gray", style="filled", rank='same')
		c.node('z01','z01')
		c.node('z02','z02')
		# c.node('i0', '∑')
		c.edge('x02','z01',label='w = -1')
		c.edge('x02','z02',label='w = 2')
		c.edge('z02','z01',label='w = 2')
		with c.subgraph(name='cluster0_opt') as opt:
			opt.attr(rank='same', color='gray')
			if(y1==0):
				opt.node('y01','hot = ' + str(y1), fillcolor="red", style="filled")
			else: opt.node('y01','hot = ' + str(y1), fillcolor="green", style="filled")
			if(y2==0):
				opt.node('y02','cold = ' + str(y2), fillcolor="red", style="filled")
			else: opt.node('y02','cold = ' + str(y2), fillcolor="green", style="filled")
		c.edge('x01','y01',label='w = 2')
		c.edge('z01','y01',label='w = 2')
		c.edge('x02','y02',label='w = 1')
		c.edge('z02','y02',label='w = 1')
		
	
# 	with g.subgraph(name='cluster_1') as c:
# 		c.attr(color='blue')
# 		with c.subgraph(name='cluster1_inp') as inp:
# 			inp.attr(rank='same', color='gray')
# 			inp.node('x11','hot = ' + str(x1[1]), fillcolor="gray", style="filled", rank='same')
# 			inp.node('x12','cold = ' + str(x2[1]), fillcolor="gray", style="filled", rank='same')
# 		c.node('z11','z1')
# 		c.node('z12','z2')
# 		# c.node('i0', '∑')
# 		c.edge('x12','z11',label='w = -1')
# 		c.edge('x12','z12',label='w = 2')
# 		c.edge('z12','z11',label='w = 2')
# 		with c.subgraph(name='cluster1_opt') as opt:
# 			opt.attr(rank='same', color='gray')
# 			if(y_pred[1][0]==0):
# 				opt.node('y11','hot = ' + str(y_pred[1][0]), fillcolor="red", style="filled")
# 			else: opt.node('y11','hot = ' + str(y_pred[1][0]), fillcolor="green", style="filled")
# 			if(y_pred[1][1]==0):
# 				opt.node('y12','cold = ' + str(y_pred[1][1]), fillcolor="red", style="filled")
# 			else: opt.node('y12','cold = ' + str(y_pred[1][1]), fillcolor="green", style="filled")
# 		c.edge('x11','y11',label='w = 2')
# 		c.edge('z11','y11',label='w = 2')
# 		c.edge('x12','y12',label='w = 1')
# 		c.edge('z12','y12',label='w = 1')
		

	g.render(name,'cache',view=False)
	img = Image.open(os.path.expanduser('cache/'+name+'.png'))
	img = img.resize((750,400),Image.ANTIALIAS)
	img.save(os.path.expanduser('cache/'+name+'.png'))

def draw_graph(w, theta, name):
	g=graphviz.Digraph(format='png')
	g.graph_attr['rankdir'] = 'LR'
	# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
	#       so that Graphviz recognizes it as a special cluster subgraph

	x1 = [0,0,1,1]
	x2 = [0,1,0,1]
	# y_true = [0,0,0,1]
	# w = [1,1]
	# theta = 2
	y_pred = [0, 0, 0, 0]


	for i in range(4):
	    y_pred[i] = get_output(w[0],w[1],x1[i],x2[i],theta)


	
	with g.subgraph(name='cluster_0') as c:
	    c.attr(color='blue')
	    c.node('x01','x1 = ' + str(x1[0]), fillcolor="gray", style="filled")
	    c.node('x02','x2 = ' + str(x2[0]), fillcolor="gray", style="filled")
	    c.node('i0', '∑')
	    c.edge('x01','i0',label=('w1 = ' + str(w[0])))
	    c.edge('x02','i0',label=('w2 = ' + str(w[1])))
	    if(y_pred[0]==0):
	        c.node('y0',str(y_pred[0]), fillcolor="red", style="filled")
	    else:
	        c.node('y0',str(y_pred[0]), fillcolor="green", style="filled")
	    c.edge('i0','y0', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_1') as c:
	    c.attr(color='blue')
	    c.node('x11','x1 = ' + str(x1[1]), fillcolor="gray", style="filled")
	    c.node('x12','x2 = ' + str(x2[1]), fillcolor="gray", style="filled")
	    c.node('i1', '∑')
	    c.edge('x11','i1',label=('w1 = ' + str(w[0])))
	    c.edge('x12','i1',label=('w2 = ' + str(w[1])))
	    if(y_pred[1]==0):
	        c.node('y1',str(y_pred[1]), fillcolor="red", style="filled")
	    else:
	        c.node('y1',str(y_pred[1]), fillcolor="green", style="filled")
	    c.edge('i1','y1', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_2') as c:
	    c.attr(color='blue')
	    c.node('x21','x1 = ' + str(x1[2]), fillcolor="gray", style="filled")
	    c.node('x22','x2 = ' + str(x2[2]), fillcolor="gray", style="filled")
	    c.node('i2', '∑')
	    c.edge('x21','i2',label=('w1 = ' + str(w[0])))
	    c.edge('x22','i2',label=('w2 = ' + str(w[1])))
	    if(y_pred[2]==0):
	        c.node('y2',str(y_pred[2]), fillcolor="red", style="filled")
	    else:
	        c.node('y2',str(y_pred[2]), fillcolor="green", style="filled")
	    c.edge('i2','y2', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_3') as c:
	    c.attr(color='blue')
	    c.node('x31','x1 = ' + str(x1[3]), fillcolor="gray", style="filled")
	    c.node('x32','x2 = ' + str(x2[3]), fillcolor="gray", style="filled")
	    c.node('i3', '∑')
	    c.edge('x31','i3',label=('w1 = ' + str(w[0])))
	    c.edge('x32','i3',label=('w2 = ' + str(w[1])))
	    if(y_pred[3]==0):
	        c.node('y3',str(y_pred[3]), fillcolor="red", style="filled")
	    else:
	        c.node('y3',str(y_pred[3]), fillcolor="green", style="filled")
	    c.edge('i3','y3', label=('θ = ' + str(theta)))
	    

	g.render(name,'cache',view=False)
	img = Image.open(os.path.expanduser('cache/'+name+'.png'))
	img = img.resize((500,590),Image.ANTIALIAS)
	img.save(os.path.expanduser('cache/'+name+'.png'))
    
def draw_xorgraph(name="xor", theta=2):
	g=graphviz.Digraph(format='png')
	g.graph_attr['rankdir'] = 'LR'
	# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
	#       so that Graphviz recognizes it as a special cluster subgraph

	x1 = [0,0,1,1]
	x2 = [0,1,0,1]
	# y_true = [0,0,0,1]
	# w = [1,1]
	# theta = 2
	y_pred = [0, 1, 1, 0]

	
	with g.subgraph(name='cluster_0') as c:
	    c.attr(color='blue')
	    c.node('x01','x1 = ' + str(x1[0]), fillcolor="gray", style="filled")
	    c.node('x02','x2 = ' + str(x2[0]), fillcolor="gray", style="filled")
	    c.node('z01','z1', fillcolor="gray", style="filled")
	    c.node('z02','z2', fillcolor="gray", style="filled")
	    c.node('i0', '∑')
	    c.edge('x01','z01',label='w1 = 2')
	    c.edge('x01','z02',label='w2 = -1')
	    c.edge('x02','z01',label='w3 = -1')
	    c.edge('x02','z02',label='w4 = 2')
	    c.edge('z01','i0',label='w5 = 2')
	    c.edge('z02','i0',label='w6 = 2')
	    if(y_pred[0]==0):
	        c.node('y0',str(y_pred[0]), fillcolor="red", style="filled")
	    else:
	        c.node('y0',str(y_pred[0]), fillcolor="green", style="filled")
	    c.edge('i0','y0', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_1') as c:
	    c.attr(color='blue')
	    c.node('x11','x1 = ' + str(x1[1]), fillcolor="gray", style="filled")
	    c.node('x12','x2 = ' + str(x2[1]), fillcolor="gray", style="filled")
	    c.node('z11','z1', fillcolor="gray", style="filled")
	    c.node('z12','z2', fillcolor="gray", style="filled")
	    c.node('i1', '∑')
	    c.edge('x11','z11',label='w1 = 2')
	    c.edge('x11','z12',label='w2 = -1')
	    c.edge('x12','z11',label='w3 = -1')
	    c.edge('x12','z12',label='w4 = 2')
	    c.edge('z11','i1',label='w5 = 2')
	    c.edge('z12','i1',label='w6 = 2')
	    if(y_pred[1]==0):
	        c.node('y1',str(y_pred[1]), fillcolor="red", style="filled")
	    else:
	        c.node('y1',str(y_pred[1]), fillcolor="green", style="filled")
	    c.edge('i1','y1', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_2') as c:
	    c.attr(color='blue')
	    c.node('x21','x1 = ' + str(x1[2]), fillcolor="gray", style="filled")
	    c.node('x22','x2 = ' + str(x2[2]), fillcolor="gray", style="filled")
	    c.node('z21','z1', fillcolor="gray", style="filled")
	    c.node('z22','z2', fillcolor="gray", style="filled")
	    c.node('i2', '∑')
	    c.edge('x21','z21',label='w1 = 2')
	    c.edge('x21','z22',label='w2 = -1')
	    c.edge('x22','z21',label='w3 = -1')
	    c.edge('x22','z22',label='w4 = 2')
	    c.edge('z21','i2',label='w5 = 2')
	    c.edge('z22','i2',label='w6 = 2')
	    if(y_pred[2]==0):
	        c.node('y2',str(y_pred[2]), fillcolor="red", style="filled")
	    else:
	        c.node('y2',str(y_pred[2]), fillcolor="green", style="filled")
	    c.edge('i2','y2', label=('θ = ' + str(theta)))
	    
	
	with g.subgraph(name='cluster_3') as c:
	    c.attr(color='blue')
	    c.node('x31','x1 = ' + str(x1[3]), fillcolor="gray", style="filled")
	    c.node('x32','x2 = ' + str(x2[3]), fillcolor="gray", style="filled")
	    c.node('z31','z1', fillcolor="gray", style="filled")
	    c.node('z32','z2', fillcolor="gray", style="filled")
	    c.node('i3', '∑')
	    c.edge('x31','z31',label='w1 = 2')
	    c.edge('x31','z32',label='w2 = -1')
	    c.edge('x32','z31',label='w3 = -1')
	    c.edge('x32','z32',label='w4 = 2')
	    c.edge('z31','i3',label='w5 = 2')
	    c.edge('z32','i3',label='w6 = 2')
	    if(y_pred[3]==0):
	        c.node('y3',str(y_pred[3]), fillcolor="red", style="filled")
	    else:
	        c.node('y3',str(y_pred[3]), fillcolor="green", style="filled")
	    c.edge('i3','y3', label=('θ = ' + str(theta)))
	    

	g.render(name,'cache',view=False)
	img = Image.open(os.path.expanduser('cache/'+name+'.png'))
	img = img.resize((500,590),Image.ANTIALIAS)
	img.save(os.path.expanduser('cache/'+name+'.png'))
 

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        self.centralwidget = QtWidgets.QWidget(Dialog)
        draw_graph(w=[1,1], theta=2, name="and")
        draw_graph(w=[2,2], theta=2, name="or")
        draw_graph(w=[2,-1], theta=2, name="andnot")
        draw_xorgraph(name="xor")
#         draw_hotcoldgraph(name="hotcold")
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 750)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setGeometry(QtCore.QRect(170, 30, 431, 481))
#         self.label.setText("")
#         self.label.setPixmap(QtGui.QPixmap("cache/and_0.png"))
#         self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 430, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.label = QtWidgets.QLabel(Dialog)
#         self.label.setPixmap(QtGui.QPixmap("cache/and_1.png"))
        pixmap = QPixmap("welcome.png")
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(170, 30, 431, 481))
        self.label.setObjectName("label")
        self.pushButton.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_2.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_3.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_4.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_5.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        self.pushButton_6.setStyleSheet("QPushButton { background-color: gray }"
                      "QPushButton:pressed { background-color: red }" )
        
#         Dialog.setCentralWidget(self.centralwidget)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    
        
       
    def testand(self,Dialog):
#         draw_graphs(w=[1,1], theta=2,name="and")
        #self.label.setText("")
        pixmap = QPixmap("cache/and.png")
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(170, 30, 500, 600))

    def testor(self,Dialog):
#         draw_graphs(w=[2,2], theta=2,name="or")
        #self.label.setText("")
        pixmap = QPixmap("cache/or.png")
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(170, 30, 500, 600))
        
    def testandnot(self,Dialog):
#         draw_graphs(w=[2,-1], theta=2,name="andnot")
        #self.label.setText("")
        pixmap = QPixmap("cache/andnot.png")  #change image accordingly
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(170, 30, 500, 600))   
        
    def testxor(self,Dialog):
#         draw_xorgraphs()
        #self.label.setText("")
        pixmap = QPixmap("cache/xor.png")  #change image accordingly
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(170, 30, 500, 600)) 
        
    def testhotcold(self):
        #draw_graphs([2,2], 2,"or")
        #self.label.setText("")
        x1_array = []
        x2_array = []
        
        th = 2
        w1 = 2
        w2 = -1
        w3 = 2
        w4 = 2
        w5 = 1
        w6 = 1

        # Take inputs
#         x1_array, x2_array = takex1x2(x1_array, x2_array)
        x1, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter value for first timestep: (H/C)')
#         x2, done2 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter value for first timestep x2:')
        
        if x1=="H":
            x1_array.append(1)
            x2_array.append(0)
        else:
            x1_array.append(0)
            x2_array.append(1)

        z2 = x2_array[0]
        z1 = get_output(w1, w2, z2, x2_array[0], th)

        current_iter = 0
    
        while(1):

            current_iter+=1

            # Take new input
            x2, done2 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter value for new timestep: (H/C)')
#             x2, done2 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter value for new timestep x2:')
            
            if done2:
                if x2=="H":
                    x1_array.append(1)
                    x2_array.append(0)
                else:
                    x1_array.append(0)
                    x2_array.append(1)

                if x1_array[current_iter-1]==1:
                    y1=1
                else:
                    y1 = get_output(w3, w4, x1_array[current_iter], z1,th)

                y2 = get_output(w5, w6, x2_array[current_iter], z2,th)

                # Print outputs
    #             print("Hot output: (y1)", y1)
    #             print("Cold output: (y2)", y2)
                draw_hotcoldgraph(y1, y2, x1_array[current_iter], x2_array[current_iter], name="hotcold")
                pixmap = QPixmap("cache/hotcold.png")  #change image accordingly
                self.label.setPixmap(pixmap)
                self.label.setGeometry(QtCore.QRect(170, 30, 750, 400))
#                 if y1==1:
#                     self.label.setText("Output is: HOT")
#                 else:
#                     self.label.setText("Output is: COLD")

                # Update z1 and z2 in anticipation of next iteration
                z2 = x2_array[current_iter]
                z1 = get_output(w1, w2, z2, x2_array[current_iter], th)

    #             continue_check = input("Do you wish to continue? (Y/N)")
                
                continue_check, done3 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Do you wish to continue? (Y/N)')
                
                if done3:
                    if continue_check=="N":
                        break
#             x1, done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for w1:')
#             x2, done2 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for w2:')
#             theta, done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for theta:')
#             if done1 and done2 and done3:
# #                 draw_graph(w=[w1,w2], theta=theta, name="custom")
#                 pixmap = QPixmap("cache/custom.png")  #change image accordingly
#                 self.label.setPixmap(pixmap)
#                 self.label.setGeometry(QtCore.QRect(170, 30, 500, 600))
            else:
                break
    
    def testCustomInput(self,Dialog):
        w1, done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for w1:')
        w2, done2 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for w2:')
        theta, done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter value for theta:')
        if done1 and done2 and done3:
            draw_graph(w=[w1,w2], theta=theta, name="custom")
            pixmap = QPixmap("cache/custom.png")  #change image accordingly
            self.label.setPixmap(pixmap)
            self.label.setGeometry(QtCore.QRect(170, 30, 500, 600))
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "AND"))
  
        self.pushButton_2.setText(_translate("Dialog", "OR"))
        self.pushButton_3.setText(_translate("Dialog", "AND-NOT"))
        self.pushButton_4.setText(_translate("Dialog", "XOR"))
        self.pushButton_5.setText(_translate("Dialog", "HOT-COLD"))
        self.pushButton_6.setText(_translate("Dialog", "CUSTOM"))
        
        self.label.setText("")
   
        self.pushButton.clicked.connect(self.testand)
        self.pushButton_2.clicked.connect(self.testor)
        self.pushButton_3.clicked.connect(self.testandnot)
        self.pushButton_4.clicked.connect(self.testxor)
        self.pushButton_5.clicked.connect(self.testhotcold)
        self.pushButton_6.clicked.connect(self.testCustomInput)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv) 
	Dialog = QtWidgets.QDialog() 
	ui = Ui_Dialog() 
	ui.setupUi(Dialog) 
	Dialog.show()
	sys.exit(app.exec_())
