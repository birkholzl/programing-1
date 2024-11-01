import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(66, 352)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(85, 49)
        self._button1.TabIndex = 0
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(251, 352)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(88, 51)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(440, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(97, 49)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(36, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 3
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(36, 53)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 4
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(36, 76)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(36, 99)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 6
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(36, 122)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 7
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(36, 145)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 8
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(36, 168)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 9
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(36, 191)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 10
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(622, 458)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "myschedule"
        self.ResumeLayout(False)


   

    def Button1Click(self, sender, e):
        self._label1.Text="biology"

    def Button2Click(self, sender, e):
        slef._label1.Text=""

    def Button3Click(self, sender, e):
        application.Exit()