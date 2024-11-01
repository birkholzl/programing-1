import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(3, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(96, 35)
        self._label1.TabIndex = 0
        self._label1.Text = "num1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(3, 44)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(96, 35)
        self._label2.TabIndex = 1
        self._label2.Text = "num2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(3, 79)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(96, 35)
        self._label3.TabIndex = 2
        self._label3.Text = "sum"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(3, 114)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(96, 35)
        self._label4.TabIndex = 3
        self._label4.Text = "difference"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(3, 149)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(96, 35)
        self._label5.TabIndex = 4
        self._label5.Text = "product"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(3, 188)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(96, 35)
        self._label6.TabIndex = 5
        self._label6.Text = "average"
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(3, 223)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(96, 35)
        self._label7.TabIndex = 6
        self._label7.Text = "distance"
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(3, 258)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(96, 35)
        self._label8.TabIndex = 7
        self._label8.Text = "max"
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(3, 293)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(96, 35)
        self._label9.TabIndex = 8
        self._label9.Text = "min"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(89, 6)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(89, 41)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 10
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(13, 362)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(86, 52)
        self._button1.TabIndex = 11
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(132, 362)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(86, 52)
        self._button2.TabIndex = 12
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(269, 361)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(102, 55)
        self._button3.TabIndex = 13
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(93, 79)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(96, 35)
        self._label10.TabIndex = 14
        # 
        # label11
        # 
        self._label11.Location = System.Drawing.Point(89, 114)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(96, 35)
        self._label11.TabIndex = 15
        # 
        # label12
        # 
        self._label12.Location = System.Drawing.Point(89, 149)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(96, 35)
        self._label12.TabIndex = 16
        # 
        # label13
        # 
        self._label13.Location = System.Drawing.Point(89, 188)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(96, 35)
        self._label13.TabIndex = 17
        # 
        # label14
        # 
        self._label14.Location = System.Drawing.Point(89, 219)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(96, 35)
        self._label14.TabIndex = 18
        # 
        # label15
        # 
        self._label15.Location = System.Drawing.Point(89, 258)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(96, 35)
        self._label15.TabIndex = 19
        # 
        # label16
        # 
        self._label16.Location = System.Drawing.Point(89, 293)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(96, 35)
        self._label16.TabIndex = 20
        self._label16.Click += self.Label16Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(383, 446)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog88a"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        num1=int(self._textbox1.Text)
        num2=int(self._textbox2.Text)
        Sum=num1+num2
        dif=num1-num2
        #TODO:finish product and average
        Abs=abs(Dif)
        Max=0
        Min=0
        if num1 >=num2:
            Max=num1
        else:#otherwise...
            Max=num2
        
        if Max==num1: #if Max has the same value as num1(==)
            Min=num1
        else:
            Min=num1
            
        self._label15.Text=str(Max)
        self._label16.Text=str(Min)

    def Button2Click(self, sender, e):
        self._textbox1.Text=""
        self._textbox2.Text=""

    def Button3Click(self, sender, e):
        application.Exit()