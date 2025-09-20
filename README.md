# GitLab
Brute-force decryption
Based on what I've done, I've chosen two forms of code to do the job. 
The first form is very basic.
Image 1
<img width="729" height="706" alt="image" src="https://github.com/user-attachments/assets/7b3bfdb5-755d-4a69-b495-350a2f590100" />

We observe how the code takes letter by letter and compares to get the result.
Image 2
<img width="890" height="876" alt="image" src="https://github.com/user-attachments/assets/84ea2c0e-40c8-4be5-9b36-07debeff45a9" />

This image shows how much time and attempts it took to crack each password with different characters.
The reason why it only contained three characters was that the code failed to distinguish four characters and couldn't find each password.
Observations:
Using this method, it was observed that numeric characters took longer than combined alphabetic and symbolic characters.

Second, the second form already contains complexity but has problems.
Image 3
<img width="718" height="983" alt="image" src="https://github.com/user-attachments/assets/8c192715-9c1f-4366-bcd5-1e324fe06f86" />

It is observed that if you can decipher a password of 4 characters and with difficulty of 5
Image 4
<img width="891" height="714" alt="image" src="https://github.com/user-attachments/assets/59dd555c-0f8b-4b0a-889f-4a3997b4ccfb" />
Image 4
<img width="893" height="680" alt="image" src="https://github.com/user-attachments/assets/98d8dc58-b96f-4146-b69a-7d095f1781df" />


In the image, we can see the same problem as in the first code attempts, since it took the longest time
for purely numeric data and exceeding 4 characters.
Then, a more normal but basic password was attempted. The time is indefinite, as it took more than 6 hours and no way was found.

Concluding, the code should have a better structure based on the alphabet used for greater optimization, since the
first observation would be that the use of a single array and the numeric characters were at the end, whether that is why the prolonged brute-force time
