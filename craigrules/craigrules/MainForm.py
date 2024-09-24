import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(21, 23)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(127, 35)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(941, 394)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "craigrules"
        self.ResumeLayout(False)

