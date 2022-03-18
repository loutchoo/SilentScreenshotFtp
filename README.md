# Introduction

SilentScreenshotFtp is a program in Python that will give you the opportunity to spy a person by sending screenshots of the screen every wanted seconds, once compiled as a .exe file and opened by the victim, the file will copy itself into the startup directory of the machine and run it, starting to send screenshots without the victim and antiviruses being aware of it or maybe yes but an AV is an AV.


# :bulb: To do list :

:bug: 1: Reduce file size after compilation.

:rocket: 2: Create automatically on the ftp server a directory named by the windows username of the victim.

:pencil: 3: Edit and refresh my code from all the shit variables names i did put in the past yes i regret.

✨ 4: Create a builder that will make everything easier, no need to edit the file and maybe a few ideas will born.

999: @loutchoesport on Twitter, give me ideas :bulb:


# Installation :

1:
:hammer: pip install -r requirements.txt

![image](https://user-images.githubusercontent.com/63863060/158911580-2258fde3-0126-4adc-a6d4-76d4764b1ab5.png)

2:
:lock: Edit your ftp logs line 59-61.

![image](https://user-images.githubusercontent.com/63863060/158911675-7491280f-b7ce-40ce-9f8b-ef5d5a4c7440.png)

3:
Edit line 69 the interval time between every screnshot took on the victim machine.

![image](https://user-images.githubusercontent.com/63863060/158911737-d0f25f47-f640-442f-a95c-ab27a8acfcc6.png)

4:
:hammer: pyinstaller --onefile filename.pyw

![image](https://user-images.githubusercontent.com/63863060/158911977-8be2237a-9fee-4196-8670-d8a626d5abd1.png)

Once done, the file will be saved in /dist/ :

![image](https://user-images.githubusercontent.com/63863060/158912135-cd0e5a08-040a-4e37-bab2-7a5daacb9ad6.png)


# Victim side :hankey:

File paste in startup and automatically launching, victim sees nothing.

![image](https://user-images.githubusercontent.com/63863060/158913727-b58eb58d-2166-4347-8e60-cd19359e1ea3.png)



# Attacker side 🏴

Amazing screenshots 😎


![image](https://user-images.githubusercontent.com/63863060/158913593-e56c77b0-dcba-4749-8c0c-e0923ae4e5eb.png)


# Antiviruses test :zap:

Now let's take a look to the reaction of Antiviruses :

:white_check_mark: Virustotal :
3/64 (all 3 are false positives)

![image](https://user-images.githubusercontent.com/63863060/158912203-92b7424a-ae94-4846-84f8-7ec093ef7f65.png)

Bypass runtime all famous antiviruses lol no socket no detection or maybe because that's just fucking screenshots lol wtf ofc it's not detected ?? will know more about that soon thx

# Builder developpement ongoing

![image](https://user-images.githubusercontent.com/63863060/158914789-e8cbc1f3-f48b-4f14-8eee-8a80cffe2984.png)
![image](https://user-images.githubusercontent.com/63863060/158914818-12772c86-abf5-4d0f-8bd8-a28f08359e88.png)
