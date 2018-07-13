import wx
import sys
import time

class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()
        self.parent = parent
        
        mmi = wx.MenuItem(self, wx.NewId(), "Minimize")
        self.AppendItem(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)
        
        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)
    
    def OnMinimize(self, e):
        self.parent.Iconize()
    
    def OnClose(self, e):
        self.parent.Close()

class MyFrame(wx.Frame):
    APP_EXIT = 1
    
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.InitUI()
     
    def InitUI(self):
        self.example2()
    
    def example1(self):
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()
        
        quitMenu = wx.MenuItem(fileMenu, self.APP_EXIT, 'Quit\tCtrl+Q')
        quitMenu.SetBitmap( wx.Bitmap('img\\exit.png') )
        
        subMenu = wx.Menu()
        subMenu.Append(wx.ID_ANY, "Some 1")
        subMenu.Append(wx.ID_ANY, "Some 2")
        subMenu.AppendSeparator()
        subMenu.Append(wx.ID_ANY, "Some 3")
        subMenu.Append(wx.ID_ANY, "Some 4")
        
        fileMenu.Append(wx.ID_OPEN, "Open")
        fileMenu.Append(wx.ID_SAVE, "Save")
        fileMenu.AppendSeparator()
        fileMenu.AppendMenu(wx.ID_ANY, "Other", subMenu)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(quitMenu)
        
        self.shsb = viewMenu.Append(wx.ID_ANY, 'Show status bar', 'Show the status bar', kind=wx.ITEM_CHECK)
        self.shtb = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show the toolbar', kind=wx.ITEM_CHECK) 
        
        viewMenu.Check(self.shsb.GetId(), True)
        viewMenu.Check(self.shtb.GetId(), True)
        
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(viewMenu, "&View")
        self.SetMenuBar(menuBar)
        
        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('img\\frog.png'))
        self.toolbar.Realize()
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready!')
        
        self.Bind(wx.EVT_MENU, self.OnQuit, id=self.APP_EXIT)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shsb)
        self.Bind(wx.EVT_MENU, self.ToggleToolbar, self.shtb)
        
        self.SetSize( (600,480) )
        self.SetTitle("Hello friends")
        self.Centre()
        self.Show(True)
    
    def example2(self):
        tb = self.CreateToolBar()
        quitTool = tb.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('img\\exit.png'))
        tb.AddSeparator()
        minTool = tb.AddLabelTool(wx.ID_ANY, 'Minimize', wx.Bitmap('img\\down.png'))
        tb.Realize()
        
        self.Bind( wx.EVT_RIGHT_DOWN, self.OnRightDown )
        self.Bind( wx.EVT_TOOL, self.OnQuit, quitTool)
        self.Bind(wx.EVT_TOOL, self.OnMinimize, minTool)
        
        self.SetSize( (400, 300) )
        self.SetTitle( "Context Menu" )
        self.Centre()
        self.Show(True)
    
    def OnRightDown(self, e):
        self.PopupMenu( MyPopupMenu(self), e.GetPosition() )
    
    def OnQuit(self, e):
        self.Close()
    
    def OnMinimize(self, e):
        self.Iconize()
    
    def ToggleStatusBar(self, e):
        if self.shsb.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()
    
    def ToggleToolbar(self, e):
        if self.shtb.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

def main():
    app = wx.App()
    MyFrame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()