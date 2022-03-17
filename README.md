# SilentScreenshotFtp + Add to Startup

1:
pip install -r requirements.txt

![image](https://user-images.githubusercontent.com/63863060/158911580-2258fde3-0126-4adc-a6d4-76d4764b1ab5.png)

2:
Edit your ftp logs line 59-61.

![image](https://user-images.githubusercontent.com/63863060/158911675-7491280f-b7ce-40ce-9f8b-ef5d5a4c7440.png)

3:
Edit line 69 the interval time between every screnshot took on the victim machine.

![image](https://user-images.githubusercontent.com/63863060/158911737-d0f25f47-f640-442f-a95c-ab27a8acfcc6.png)

4:
pyinstaller --onefile filename.pyw

![image](https://user-images.githubusercontent.com/63863060/158911977-8be2237a-9fee-4196-8670-d8a626d5abd1.png)

Once done, the file will be saved in /dist/ :

![image](https://user-images.githubusercontent.com/63863060/158912135-cd0e5a08-040a-4e37-bab2-7a5daacb9ad6.png)

Now let's get a look to the reaction of Antiviruses :

Virustotal :
(atleast 2 false positives)

![image](https://user-images.githubusercontent.com/63863060/158912203-92b7424a-ae94-4846-84f8-7ec093ef7f65.png)

Bypass runtime all famous antiviruses.
