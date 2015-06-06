#Boa:Frame:piramida_penduduk

import wx
from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics

def create(parent):
    return piramida_penduduk(parent)

[wxID_PIRAMIDA_PENDUDUK] = [wx.NewId() for _init_ctrls in range(1)]

class piramida_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PIRAMIDA_PENDUDUK,
              name=u'piramida_penduduk', parent=prnt, pos=wx.Point(341, 167),
              size=wx.Size(911, 445), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Perbandingan Penduduk')
        self.SetClientSize(wx.Size(911, 445))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.drawBarGraph()
        
    def drawBarGraph():
        self.canvas = PlotCanvas(panel)
        self.canvas.Draw(drawBarGraph())
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
        toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Show Legend")
        toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)
        
        points1=[(1,0), (1,10)]
        line1 = PolyLine(points1, colour='green', legend='Feb.', width=10)
        points1g=[(2,0), (2,4)]
        line1g = PolyLine(points1g, colour='red', legend='Mar.', width=10)
        points1b=[(3,0), (3,100)]
        line1b = PolyLine(points1b, colour='blue', legend='Apr.', width=10)
 
        points2=[(4,0), (4,12)]
        line2 = PolyLine(points2, colour='Yellow', legend='May', width=10)
        points2g=[(5,0), (5,8)]
        line2g = PolyLine(points2g, colour='orange', legend='June', width=10)
        points2b=[(6,0), (6,4)]
        line2b = PolyLine(points2b, colour='brown', legend='July', width=10)
 
        return PlotGraphics([line1, line1g, line1b, line2, line2g, line2b],
                        "Bar Graph - (Turn on Grid, Legend)", "Months", 
                        "Number of Students")
 
    def onToggleGrid(self, event):
        """"""
        self.canvas.SetEnableGrid(event.IsChecked())
 
    #----------------------------------------------------------------------
    def onToggleLegend(self, event):
        """"""
        self.canvas.SetEnableLegend(event.IsChecked())
 
