import smtpd
import asyncore
 
d=smtpd.DebuggingServer(('0.0.0.0', 25), None)
  
try:
    asyncore.loop()
except KeyboardInterrupt:
    pass
