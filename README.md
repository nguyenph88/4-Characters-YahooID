4-chars-yahoo-id
================

Automatic process in finding available 4 chars yahoo ID: eg: vn0s@yahoo.com which im having.

Not only 4 chars, you can ask the problem to check for as many chars as you want. I've also provided a generator to generate the combination which satisfies your condition.

Pretty much i'm still having those 4-chars yahoo ID: <b>vn0s (most favorite, as I call it: Viet Nam Zero Second), jkre, pnps, mhiw, mgin etc...</b>

I have 2 version of the file (PHP/Python) so you can try out:
- PHP: I wrote it like 2-3 years ago:
    http://nguyenphuoc.net/tools/4char/index.php

- Python: I run with 1 dyno so it's slow: 
    http://check4char.herokuapp.com/

E.g: checking with string "concobe" and total char = 8

![Image](/imgs/img1.png?raw=true)

Note - 02/21/2013
-----
I was working on the multi-threading to check more IDs at once but problem occurs as following:
- All of my connections are denied, I worked around by using sock5 and it works again but takes so long.
- All of the check in JSON returns "FAILURE" even though it's valid.
- Speed drops down a lot and things get so cocky :(
 
Problem is maybe I left my computer to check for prolly 10-20k IDs last night so it is flagged somehow :( Until I get it fixed or find another better way, feel free to try out the program on my website (may/may not work).

Introduction
----------------
Yahoo was very famous in Asia couple years ago (especially yahoo messenger). So having a unique yahoo ID like "abc2" or "cool", isn't it cool? I was so curious in how to find and register for those unique ID so I did some researchs back in the time and came up with some methods of find unique ID.

Also, at that time, there were 2 kinds of unique yahoo ID that people were so interested in: the 4 chars ID (which is the lowest # of digits that are allowed), or the number digits ID (like mine: 0907216712@yahoo.com). Yahoo no longer allows people to register for numberID but there the method for exploiting 4 chars is still there.

How The List is Generated?
------------
Based on the information that user inputs, i'm going to keep their original string and randomly choose from [0..9] and [a..z] to fill in the remaining chars. It's easy to calculate the result base on the remaining char, total combination = 36 * remaining chars

How The ID is Checked?
-----------
Even though your info POST to yahoo server is encrypted, sometimes when we send raw data it is still acceptable. After some researches in the past I came up with a link (URL) where you can put your desired ID as raw data and you will get raw json as result.

E.g: I want to check for ID: "awer" , the ID is passed as arguement as below: (part of the URL is removed)

![Image](/imgs/img2.png?raw=true)

I will get the result like above, since that ID is already taken, as a json file.

Otherwise, if i'm parsing an ID which I surely know is valid: "thiswillneverbetaken12" , the result is:

![Image](/imgs/img3.png?raw=true)

Likewise, in the JSON response I will see the success message.

As part of the program, I'm using urllib2 to connect to the link that I've explored, read the response from the JSON and compare whether or not it contains "SUCCESS". Based on the result then I will be able to know the validity of the ID.

Well, everything is normal, code is simple it's just how I came up with the URL. It is being used in another file called checkyahoo.py which contains that class for checking, i'm not uploading the file up on here anyway :)
