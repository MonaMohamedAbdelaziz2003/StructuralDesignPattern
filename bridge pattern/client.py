from button import button
from operatingSystem import windows, linux
os = linux()
Button = button(os)
Button.click()
