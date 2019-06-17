#print ("Hello Oleg!")
import os
import datetime
import time
import html
#print(os.getcwd())
#print(os.getenv('HOME'))
#print(datetime.date.isoformat(datetime.date.today()))
print(time.strftime("%H:%M %A %p"))

#Преобразование разметки html и экранированный текст и обратно
print(html.escape("this html fragment contains <script>script</script> tag."))
print(html.unescape("I &hearts; Pyton &lt;standats&gt;."))