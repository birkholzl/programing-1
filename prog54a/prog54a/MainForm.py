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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "pick a car"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 297)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "miles"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 320)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "gallons"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(12, 343)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "mpg"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(118, 297)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(118, 320)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 5
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(118, 343)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 6
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 179)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(89, 51)
        self._button1.TabIndex = 7
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(158, 182)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(114, 48)
        self._button2.TabIndex = 8
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(316, 175)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(93, 53)
        self._button3.TabIndex = 9
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["1970 vw bug",
            "1979 firebird",
            "1980 subaru",
            "1975 cutlas"]))
        self._comboBox1.Location = System.Drawing.Point(97, 6)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(121, 21)
        self._comboBox1.TabIndex = 10
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(461, 422)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        miles = 1
        gallons = 1
        car = self._comboBox.Text
        
        # todo: repeat for all 4 cars
        if car == "1970 VW Bug":
            miles = 286
            gallons = 9
        elif car == "1979 firebird":
            miles = 
        else:
            MessageBox.Show("invalid car!")
            
            mpg = miles / float(gallons)
            mpg = round(mpg, 1)
            
            slef._label7.Text = str(mpg)