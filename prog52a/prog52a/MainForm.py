import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(65, 48)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "length:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(247, 48)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(102, 20)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(247, 110)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 2
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(53, 107)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 3
        self._label2.Text = "width:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(38, 177)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "area:"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(44, 244)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "perimeter:"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(247, 177)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 6
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(247, 232)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 7
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(38, 329)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(100, 51)
        self._button1.TabIndex = 8
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(267, 329)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 45)
        self._button2.TabIndex = 9
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(473, 322)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(86, 44)
        self._button3.TabIndex = 10
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(871, 419)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        length=int(self._textbox1.Text)
        width=int(self._textbox2.Text)
        area=length*width
        perimeter=2*length+2*width
        self._label5.Text=str(area)
        self._label6.Text=str(perimeter)
        # + - * / % **pow //divide & round down
        #int (integer): a whole number, pos/neg
        # float (floating-point number): any number with decimal
        # str (string): a string of text

    def Button2Click(self, sender, e):
        self._textbox1.Text=""
        self._textbox2.Text=""
        self._label5.Text=""
        self._label6.Text=""