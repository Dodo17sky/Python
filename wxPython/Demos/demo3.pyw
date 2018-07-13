import wx

'''
    In the following example, we will show, how we can enable and disable toolbar buttons. 
    We will also see a separator line.
'''

class MyFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.InitUI()
    
    def InitUI(self):
        self.count = 5
        
        self.toolbar = self.CreateToolBar()
        toolUndo = self.toolbar.AddLabelTool(wx.ID_UNDO, '', wx.Bitmap('img\\undo.png'))
        toolRedo = self.toolbar.AddLabelTool(wx.ID_REDO, '', wx.Bitmap('img\\redo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        toolExit = self.toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('img\\exit.png'))
        self.toolbar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.OnExit, toolExit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, toolUndo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, toolRedo)
        
        self.SetSize( (400,300) )
        self.SetTitle('Toolbars')
        self.Centre()
        self.Show(True)
    
    def OnUndo(self, e):
        if self.count > 0 and self.count <= 5:
            self.count -= 1
        
        if self.count == 0:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
        
        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)
        
    def OnRedo(self, e):
        if self.count < 5 and self.count >= 0:
            self.count += 1
        
        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        
        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, True)
        
    def OnExit(self, e):
        self.Close()
    
def main():
    app = wx.App()
    MyFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()