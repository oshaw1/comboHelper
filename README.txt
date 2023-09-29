comboHelper is two tools that work together to help you use combo lists for load testing / account creation needs, comboFixer standardises your combo list into username:password format, comboUser will enter in the username:password combos and you can pause and log the previous entry whenever you would like. 

*********************************************************************
*       (                    )       ( /(       (                   *  
*   )\           )    ( /(       )\())   (  )\          (   (       *
* (((_)   (     (     )\())  (  ((_)\   ))\((_)`  )    ))\  )(      *
* )\___   )\    )\  '((_)\   )\  _((_) /((_)_  /(/(   /((_)(()\     *
*((/ __| ((_) _((_)) | |(_) ((_)| || |(_)) | |((_)_\ (_))   ((_)    *
* | (__ / _ \| '  \()| '_ \/ _ \| __ |/ -_)| || '_ \)/ -_) | '_|    *
*  \___|\___/|_|_|_| |_.__/\___/|_||_|\___||_|| .__/ \___| |_|      *
*                                             |_|                   *
*********************************************************************

Clone the comboHelper repo and extract to chosen directory. Inside are two python scripts executable by commandline.
Directions for both tools follows:

<----------------------------------------------------------------------comboFixer------------------------------------------------------------------------------------------------------>
1. Download chosen combolist with "username:password" format and insert into the inputs folder

2. Open cmd / gitbash in the comboFixer folder and run the following command python combo-fixer.py input/{original.txt} output/fixedCombo.txt

3. Check combo list is fixed in fixedCombo.txt

Note: NOW WORKS WITH FORMATS INCLUDING username : password AND 1. username : password

<---------------------------------------------------------------------comboUser-------------------------------------------------------------------------------------------------------->
1. Insert fixedCombo.txt into the input folder

2. Open cmd / gitbash in the comboUser folder and run the following command python combo-enter.py input/fixedCombo.txt and click on the username input box of your application

3. IF THERE IS A SUCCESSFUL LOGIN CLICK Home TO PAUSE THE SCRIPT AND AGAIN TO UNPAUSE

IMPORTANT: The keys to control the combo user are: 
							Home - pause/unpause
							End - kill
							Insert - Log last inputted username:password
HOLD DOWN INPUT KEYS FOR A FEW SECONDS 

Currently only one configureation of the tool is available and that is for league of legends other configurations for web apps/sites will be added in the future.

