# все прекрасно, но гугл банит письма отсюда
import smtplib
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login('https.dev@gmail.com', '*******')
smtp_obj.sendmail(from_addr=["https.ki@gmail.com","https.ki@gmail.com"], to_addrs="el.piankova@gmail.com", msg="I did it!")
smtp_obj.quit()