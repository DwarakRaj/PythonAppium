def Test2():
  text = 'cell'
  Browsers.Item[btChrome].Navigate("https://services.smartbear.com/samples/TestComplete15/smartstore/")
  browser = Aliases.browser
  browserWindow = browser.BrowserWindow
  browserWindow.Maximize()
  textbox = browser.pageShop.header.formSearch
  textbox2 = textbox.textboxInstasearch
  textbox2.Click()
  textbox2.SetText(text)
  textbox.buttonSearch.ClickButton()
  if textbox2.Text == text:
     Log.Checkpoint(f'{text} is presented')
  else:
    Log.Warning(f'{text} is presented')