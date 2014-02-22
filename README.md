4-chars-yahoo-id
================

Automatic process in finding available 4 chars yahoo ID: eg: vn0s@yahoo.com which im having.

Not only 4 chars, you can ask the problem to check for as much char as possible. I've also provided a generator to generate the combination which satisfies your condition.

Pretty much i'm still having those 4-chars yahoo ID: vn0s (most favorite, as I call it: Viet Nam Zero Second), jkre, pnps, mhiw, mgin etc...

![Image](/img/img1.png?raw=true)

Introduction
----------------
Yahoo was very famous in Asia couple years ago (especially yahoo messenger). So having a unique yahoo ID, isn't it cool? I was so curious in how to find and register for those unique ID so I did some researchs back in the time and came up with some method of find unique ID.

Also, at that time, there are 2 kinds of unique yahoo ID that people are so interested: the 4 chars ID (which is the lowest # of digits that are allowed), or the number digits ID (like me: 0907216712@yahoo.com). Yahoo no longer allows people to register for numberID but there the method for exploiting 4 chars is still there.

How The List is Generated?
------------
Based on the information that user inputs, i'm going to keep their original string and randomly choose from [0..9] and [a..z] to fill in the remaining chars. It's easy to calculate the result base on the remaining char, total combination = 36 * remaining chars

How The ID is Checked?
-----------
Even though your info POST to yahoo server is encrypted, sometimes when we send raw data it is still acceptable. After some researches in the past I came up with a link (URL) where you can put your desired ID as raw data and you will get raw json as result.

E.g: I want to check for ID: awer , the ID is passed as arguement as below: (part of the URL is removed)

![Image](/img/img2.png?raw=true)

I will get the result like above, since that ID is already taken, as a json file.

Otherwise, if i'm parsing an ID which I surely know is valid: thiswillneverbetaken12 , the result is:

![Image](/img/img3.png?raw=true)

Likewise, in the JSON response I will see the success message.

As part of the program, I'm using urllib2 to connect to the link that I've explored, read the response from the JSON and compare whether or not it contains "SUCCESS". Based on the result then I will be able to know the validity of the ID.

Well, everything is normal, code is simple it's just how I came up with the URL. It is being used in another file called checkyahoo.py which contains that class for checking, i'm not uploading the file up on here anyway :)
