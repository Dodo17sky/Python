import wx

'''
    A typical application consists of various widgets.
    Those widgets are placed inside container widgets. 
    A programmer must manage the layout of the application. 
    This is not an easy task. 
    In wxPython it is possible to lay out widgets using absolute positioning or using sizers.
    
    Absolute Positioning:
        The programmer specifies the position and the size of each widget in pixels. Absolute positioning has several disadvantages:
            -> The size and the position of a widget do not change if we resize a window.
            -> Applications look different on various platforms.
            -> Changing fonts in the application might spoil the layout.
            -> If we decide to change our layout, we must completely redo our layout, which is tedious and time consuming.
        
        There might be situations where we can possibly use absolute positioning.
        For instance, small test examples. But mostly, in real world programs, programmers use sizers.
        In our example we have a simple skeleton of a text editor.
        If we resize the window, the size of out wx.TextCtrl does not change as we would expect. 
'''

class MyFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.InitUI()
    
    def InitUI(self):
#         self.builtInSizer()
#         self.absolutePositioning()
#         self.wx_BoxSizer()
        self.another_Layout()
    
    def builtInSizer(self):
        menuBar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()
        
        menuBar.Append(filem, "File")
        menuBar.Append(editm, "Edit")
        menuBar.Append(helpm, "Help")
        
        self.SetMenuBar(menuBar)        
        
        wx.TextCtrl(self)
        '''
            In this example, there is no sizer visible. We placed a wx.TextCtrl inside the wx.Frame widget. 
            The wx.Frame widget has a special built-in sizer. We can put only one widget inside the wx.Frame container.
            The child widget occupies all the space, which is not given to the borders, menu, toolbar and the statusbar. 
        '''
        
        self.SetTitle('Layouts')
        self.Centre()
        self.Show(True)
    
    def absolutePositioning(self):
        panel = wx.Panel(self, -1)
        menuBar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()
        
        menuBar.Append(filem, "File")
        menuBar.Append(editm, "Edit")
        menuBar.Append(helpm, "Help")
        
        self.SetMenuBar(menuBar)        
        
        wx.TextCtrl(panel, pos=(10,10), size=(300,200))
                
        self.SetSize((400,300))
        self.SetTitle('Layouts')
        self.Centre()
        self.Show(True)
    
    def wx_BoxSizer(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4fad49')
        
        midPan = wx.wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        
        panel.SetSizer(vbox)
        
        self.SetSize((400,300))
        self.SetTitle('Layout BoxSizer')
        self.Centre()
        self.Show(True)
    
    def another_Layout(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
 
        vbox = wx.BoxSizer(wx.VERTICAL)
 
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Class Name')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
 
        vbox.Add((-1, 10))
 
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
 
        vbox.Add((-1, 10))
 
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)
 
        vbox.Add((-1, 25))
 
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)
 
        vbox.Add((-1, 25))
 
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)
        
        self.SetSize((400,300))
        self.SetTitle('Many layouts')
        self.Centre()
        self.Show(True)

def main():
    app = wx.App()
    MyFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()