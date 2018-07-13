import wx

'''
    How to create multiple toolbars
'''

class MyFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.InitUI()
    
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        toolbar1 = wx.ToolBar(self)
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\car1.png') )
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\car2.png') )
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\car3.png') )
        toolbar1.Realize()
        
        toolbar2 = wx.ToolBar(self)
        toolbar2.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\cat.png') )
        toolbar2.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\dog.png') )
        toolbar2.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\rabbit.png') )
        toolbar2.Realize()
        
        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.AddSpacer(4)
        vbox.Add(toolbar2, 0, wx.EXPAND)
        
        self.SetSizer(vbox)
        
        self.SetSize( (400,300) )
        self.SetTitle('Toolbars')
        self.Centre()
        self.Show(True)
    
def main():
    app = wx.App()
    MyFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()