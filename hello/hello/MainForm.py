﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._clear = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(49, 51)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(711, 254)
        self._label1.TabIndex = 0
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(87, 362)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(94, 46)
        self._button1.TabIndex = 1
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # clear
        # 
        self._clear.Location = System.Drawing.Point(297, 371)
        self._clear.Name = "clear"
        self._clear.Size = System.Drawing.Size(87, 50)
        self._clear.TabIndex = 2
        self._clear.Text = "clear"
        self._clear.UseVisualStyleBackColor = True
        self._clear.Click += self.ClearClick
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(572, 371)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(86, 37)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(886, 441)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._clear)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "hello"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text="hello, world"

    def ClearClick(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        application.Exit()