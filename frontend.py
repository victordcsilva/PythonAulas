import backend
import wx

def press_button(event): #Função para indicar o que fazer ao precionar o botão
    metros = float(input_box.GetValue()) 

    result.SetLabel(str(backend.metro_pes(metros)))

app = wx.App() # Objeto APP
frame = wx.Frame(parent = None, title="Metros para pés") #O bjeto frame
panel = wx.Panel(frame) # Objeto panel
sizer = wx.GridBagSizer() # Objeto sizer

# Objetos Widget
input_label = wx.StaticText(panel, label = "Metros: ")
input_box = wx.TextCtrl(panel)
result_label = wx.StaticText(panel, label = "Pés: ")
result = wx.StaticText(panel, label = "")
button = wx.Button(panel, label = "Converter")
button.Bind(wx.EVT_BUTTON, press_button)

# Adiciona os objetos widget ao sizer 
sizer.Add(input_label, (0,0))
sizer.Add(input_box, (0,1))
sizer.Add(result_label, (1,0))
sizer.Add(result, (1,1))
sizer.Add(button, (2,2))


# Conecta o sizer ao panel e ao frame
panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)
frame.Show() #Mostra o frame
app.MainLoop() #Mostrando constantemente a interface

