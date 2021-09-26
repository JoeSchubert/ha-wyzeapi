# Change Log

- - -
## 0.1.0 - 2021-09-26


### Bug Fixes

4beb03 - bump version of wyzeapy to fix logging error - Joshua Mulliken

f4a6ad - Update light.py (#259) - reidprichard

2f3fa4 - 250 incorrect color temp (#258) - Joe Schubert

f5788f - reuse workflow and update packages - Josh Mulliken

e0deeb - reuse lint on  and scripts - Josh Mulliken

2608dc - remove broken import - Joshua Mulliken

cea856 - Fix Permission denied wyze_config.ini (#242) - Leonardo Ledesma Maguilla

559351 - Stop loading binary sensors - Joshua Mulliken

46867c - fixes config_path problem on some installs and removes camera subscription on removal from hass - Joshua Mulliken

912aba - resolves issue where locks will never update from the server - Joshua Mulliken

1a6050 - Fix exception where content type is not json on updating sensors sometimes. - Joshua Mulliken

098d3a - Update to catch certain types of network errors and recover. - Joshua Mulliken

de1844 - Assign client correctly on unload - Joshua Mulliken

0706f8 - Undo removal of devices - Joshua Mulliken

d309f2 - Remove preset mode from thermostat due to a bugFixes: #207Signed-off-by: Joshua Mulliken <joshua@mulliken.net> - Joshua Mulliken

f476a8 - wait for the notifications endpoint to update before checking - Joshua Mulliken

216e00 - Combine notification switches into one - Joshua Mulliken

6b97aa - change to schedule_update_ha_state - Joshua Mulliken

44dc7e - make the switch turn itself off after a period of time - Joshua Mulliken

0ed64e - Add new unique id for notification switch - Joshua Mulliken

32cbba - Update the name of the device - Joshua Mulliken

3d24f9 - change to using phone id - Joshua Mulliken

5fd6c1 - Update to use latest wyzeapy that fixes some access token problems - Joshua Mulliken

8a555d - Update to fix errors and fix linting problems - Joshua Mulliken

68e19b - available now exists - Joshua Mulliken

67d30c - increase scan interval - Joshua Mulliken

7e71dd - Update to lock update method. - Joshua Mulliken

d805ec - Update set temp code - Joshua Mulliken

aab21c - Update device_state_attributes to return the same as the state attribute - Joshua Mulliken

9b4d8c - Hotfix: Push the scan interval for the lock higher - Joshua Mulliken

24b060 - Fix to inform HA that the switch is off. - Joshua Mulliken

e5a1ac - Except errors to prevent new devices from (#137) - Joshua Mulliken

499dc1 - Outdoor Plug: remove unnecessary third switch (#120) - Brian Hanifin

bc47fb - Add version to manifest (required since HA 2021.3) (#118) - davidlang42

e220ce - Syntax and warning fixes - Joshua Mulliken

8287d3 - Quick fix to show the right state value when the plug is turned off - Joshua Mulliken

43c1e4 - Patch to prevent switch from displaying as off just after it is turned on. This happens because home assistant calls the update function of the switch just after sending the command and the wyze servers are a bit slow to update their knowledge of the switch's state. - Joshua Mulliken

05fad4 - On second login would hash the password again. This made the password incorrect and therefore might lock a users account. - Joshua Mulliken

c02e08 - Access token error bug reborn (#84) - Joshua Mulliken

9e95f5 - Remove the reference to RefreshToken. It doesn't seem to work. (#83) - Joshua Mulliken

271d72 - Revert speed of polling. And increment version number - Joshua Mulliken

f96821 - Revert speed of polling. - Joshua Mulliken

35ef9e - Fix for bad logic in client.update() - Joshua Mulliken

a6cefb - Fix misspellings in several places. It is still unknown why sensors are not updating. - Joshua Mulliken

a4ebfd - Fix additional available typos. - Joshua Mulliken

a06257 - Update to fix typo causing switch errors. - Joshua Mulliken

a3d4c0 - Fix for motion_sensor.py error - Joshua Mulliken

357a19 - Fix for lock status being reversed. - Joshua Mulliken

3eecfb - Fix for the manifest.json that prevented the UI from restarting Home Assistant. - Joshua Mulliken

7b9950 - The logging in token would never have been reset - Joshua Mulliken

cad21b - Fix initialization to ensure there are no doubles - Joshua Mulliken

57f228 - Add new link to fix bad call on the switch this time. - Joshua Mulliken

37e4bf - Add new link to fix bad call. Again... ugh - Joshua Mulliken

ea0fb1 - Add new link to fix bad call - Joshua Mulliken

d286c2 - Remove erroneous check - Joshua Mulliken

702530 - Forgot that the values in the json are strings in __post_and_recover - Joshua Mulliken

9a472f - Fix some more bad logic in __post_and_recover - Joshua Mulliken

fe2b65 - Remove bad logic in __post_and_recover - Joshua Mulliken

050a96 - Added actual lists. All devices are available immediately - Joshua Mulliken

e364ff - Added actual lists. Ooops - Joshua Mulliken

ed39f4 - Added check with hasattr - Joshua Mulliken

9ef73e - Added check for none - Joshua Mulliken

c1a238 - Updated constants file - Joshua Mulliken

0e333e - Added logging to post to server. swap logic on get_devices - Joshua Mulliken

1139ed - Adding logging to most operations in client.py. Plus small logic change - Joshua Mulliken

a8e674 - Did not add required dep - Joshua Mulliken

c71c08 - Forgot to add the md5_md5 method back into the refactor - Joshua Mulliken

aa617f - Update to handle locked accounts - Joshua Mulliken

dd2fe4 - Let's try to get this working! More logging. One small change - Joshua Mulliken

93dd2e - Let's try to get this working! - Joshua Mulliken

1c1688 - Even more bug fixes! Types cannot save me - Joshua Mulliken

3b9fe1 - Another bug fix - Joshua Mulliken

b3eb4d - Small bug fix - Joshua Mulliken

54861f - Update __init__.py - Joshua Mulliken

fd8611 - Fix indentation - Joshua Mulliken

794448 - Update because refresh tokens doesn't work - Joshua Mulliken

89ed3b - Fix for bug in logging code - Joshua Mulliken

cc81b6 - indention fix - Joshua Mulliken

a7838a - Update to solve update issues - Joshua Mulliken

247387 - Remove await from turn on and turn off to see if it speeds up requests - Joshua Mulliken

8d59e3 - Update to correctly update state - Joshua Mulliken

1cb123 - update to actually await the turnon - Joshua Mulliken

bc9cbf - Small fix - Joshua Mulliken

e55be0 - Async fixes - Joshua Mulliken

b93130 - Fix for small annoying error - Joshua Mulliken

d1279b - Fix to reset error state to false - Joshua Mulliken

c916ca - Fix import of exceptions - Joshua Mulliken

bde4c4 - made changes to login to run in single thread. - Joshua Mulliken

021afc - Updated to fix additonal error in #18 - Joshua Mulliken

973045 - updated switch.py to fix #18 - Joshua Mulliken

e61033 - Fix to change brightness and color temperature at the same time. - Quantum-cross

09080c - I believe that I have fixed the access_token error - Joshua Mulliken

d8da3b - Keep color temp set - Joshua Mulliken

d9c394 - Reset brightness value to old value on color temp change - Joshua Mulliken

063478 - Changed method for setting color temp and brightness to fix brightness going to 100 - Joshua Mulliken

5f677b - Changed to none to avoid errors - Joshua Mulliken

d718f5 - Update translate field - Joshua Mulliken

15086a - Testing - Joshua Mulliken

bf3408 - Trying to fix stuff - Joshua Mulliken

9c32a5 - code changes to address bug - Joshua Mulliken

32138f - Attempt to fix brightness resetting to 100% - Joshua Mulliken

783256 - Changing to debug - Joshua Mulliken

fd95d3 - Changed turn_on to hopefully maintain state - Joshua Mulliken

ef7869 - attempt to fix brightness + color temperature change problems - Joshua Mulliken

723769 - Actually fixed the error - Joshua Mulliken

5f04b1 - Fixed a bug if there is no brightness set the turn_on function will fail - Joshua Mulliken

883212 - There appears to be a delay in the wyze api updating the state so I am handling it here for one request - Joshua Mulliken

b84cc5 - Update state information in this method - Joshua Mulliken

18514b - Updated state understanding - Joshua Mulliken

9f3ea7 - Generating a guid did not work so I am hardcoding one used in other examples - Joshua Mulliken

5e1717 - Updated to fix bug preventing the api from loading - Joshua Mulliken


### Performance Improvements

cfa129 - Remove get info. It is redundant and not efficient for multiple cameras - Joshua Mulliken


### Tests

58a450 - Updated tests and intro debug message - Joshua Mulliken

240411 - add switches to tests - Joseph Yancey

fe4696 - Updated test - Joshua Mulliken


### Continuous Integration

c2956f - reuse linter to github workflow - Josh Mulliken

1501ef - Remove broken linting - Joshua Mulliken

86d413 - pin the wyzeapy version - Joshua Mulliken

c3a9ef - Update linting action - Joshua Mulliken

0eaf93 - Update linting action - Joshua Mulliken

7d47ba - Update PythonLinting.yml - Joshua Mulliken

8422e1 - Update PythonLinting.yml - Joshua Mulliken

845a07 - Rename main.yml to PythonLinting.yml - Joshua Mulliken

518904 - Create main.yml - Joshua Mulliken

19ed27 - Create HASAction.yml - Joshua Mulliken

494323 - update stale bot config - Joshua Mulliken

431443 - add stale bot - Joshua Mulliken


### Miscellaneous Chores

f18328 - bump wyzeapy & version number - Joshua Mulliken

9f5e9c - bump version - Joshua Mulliken

18490c - bump versions - Joshua Mulliken

3ccfb3 - bump version - Joshua Mulliken

5b8755 - update version number - Joshua Mulliken

5edb48 - bump versions - Joshua Mulliken

90ff22 - bump version number - Joshua Mulliken

39fb6d - bump version number - Joshua Mulliken

47fe00 - bump wyzeapy version number - Joshua Mulliken

8d8b51 - bump version of wyzeapy - Joshua Mulliken

c5e94e - gitignore to ignore .test folders - Joshua Mulliken

0a48fe - bump version number to 2021.9.1Includes fix: 3d9ba688da0e0aa9086142b81fbe2a54a2cdd93bThis fixes issues where users who were not on docker/supervised installs were unable to write the wyzeconfig.ini file to the filesystem - Joshua Mulliken

cf791a - bump version number - Joshua Mulliken

832630 - Update wyzeapy to 0.2.9 - Joshua Mulliken

71dc42 - update version number - Joshua Mulliken

bc27a9 - bump version number - Joshua Mulliken

fe2e09 - Bump version number - Joshua Mulliken

3aa0a6 - bump version - Joshua Mulliken

c1e26b - update version number - Joshua Mulliken

e51733 - Require at least wyzeapy 0.2.2 - Joshua Mulliken

1d17a1 - update version number - Joshua Mulliken

732df0 - Bump wyzeapy - Joshua Mulliken

d295cc - bump version number - Joshua Mulliken

c2a634 - Bump version number - Joshua Mulliken

99c365 - bump version number - Joshua Mulliken

56ee92 - bump version number - Joshua Mulliken

1460fd - Increment version number - Joshua Mulliken

c0e145 - Update version number - Joshua Mulliken

52f56b - Increment version number - Joshua Mulliken

4e2568 - Increment version number - Joshua Mulliken

fb395f - Update version number - Joshua Mulliken

4110d7 - Update version number again - Joshua Mulliken

91bfbe - Update the version number - Joshua Mulliken

46acb3 - Update version number - Joshua Mulliken

d1992f - Bump version number - Joshua Mulliken

b1092b - Bumped the version number (#58) - Joshua Mulliken

9c32b9 - Set version number - Joshua Mulliken

847b4c - Update version number - Joshua Mulliken

9692cd - Remove tests - Joshua Mulliken

bc9aaa - Update version number in preperation for release - Joshua Mulliken

254d57 - Updated version number - Joshua Mulliken

5834c5 - Removed tests as they are no longer neccessary - Joshua Mulliken

14efc9 - Changed debug version error - Joshua Mulliken

071d90 - Changed version number - Joshua Mulliken

38c131 - Update my username - Joshua Mulliken

20ef70 - Updated the domain - Joshua Mulliken

a956f6 - Removed untracked files - Joshua Mulliken

d3d018 - ignore the wyzeconfig.ini file - Joshua Mulliken

c10097 - git remove untracked files - Joshua Mulliken

adb5fa - Added .DS_Store to ignore - Joshua Mulliken


### Style

f96794 - Ignore pycharm errors - Joshua Mulliken

f136a2 - Update to fix linter errors - Joshua Mulliken

636337 - Removed unused import - Joshua Mulliken

d82ee3 - Additional style fixes. - Joshua Mulliken

243316 - Major update to improve style and fix some small issues. - Joshua Mulliken

503ec5 - Removes readme from internal file structure. - Mark Rickert

a73992 - Updated message to look better - Joshua Mulliken


### Documentation

b033e2 - fix CHANGELOG.md formatting - Joshua Mulliken

e577b6 - add changelog - Joshua Mulliken

76b129 - Update README.md - Joshua Mulliken

ddca35 - Update readme to remove the 2fa disabled requirement (#252) - Joe Schubert

97a082 - become compliant with REUSE 3.0 spec - Joshua Mulliken

cf53be - Update README.md - Joshua Mulliken

1a9727 - Update README.md - Joshua Mulliken

0566ee - Update README.md - Joshua Mulliken

f176e2 - Update bug_report.md - Joshua Mulliken

905e69 - Update README.md - Joshua Mulliken

24d6cb - Update README.md - Joshua Mulliken

cf831a - Update FUNDING.yml - Joshua Mulliken

57a0c8 - Create hassfest.yml - Joshua Mulliken

ab4d60 - Update README.md - Joshua Mulliken

ee6dcd - Update issue templates - Joshua Mulliken

800a4b - Update SECURITY.md - Joshua Mulliken

38051b - Update issue templates - Joshua Mulliken

19f34d - Create config.yml - Joshua Mulliken

1c3708 - Update info.md - Joshua Mulliken

b4776e - Update hacs.json - Joshua Mulliken

34f702 - Update README.md - Joshua Mulliken

a82ba4 - Update README.md - Joshua Mulliken

edd81d - Update README.md - Joshua Mulliken

1f0d72 - Update README.md - Joshua Mulliken

5dc47a - Create FUNDING.yml - Joshua Mulliken

034fb5 - Update README.md - Joshua Mulliken

3b45ce - Update to make it more clear that 2FA is not supported - Joshua Mulliken

e9c852 - Update SECURITY.md - Joshua Mulliken

c7ecb3 - Update SECURITY.md - Joshua Mulliken

d5ba25 - Create SECURITY.md - Joshua Mulliken

0be055 - Update info.md - Joshua Mulliken

737ec4 - Update README.md - Joshua Mulliken

5e1fea - Update README.md - Joshua Mulliken

a07cdd - Update README.md - Joshua Mulliken

918176 - Update README.md - Joshua Mulliken

15bb1c - Update info.md - Joshua Mulliken

8eab90 - Update README.md - Joshua Mulliken

506ed4 - Update README.md - Joshua Mulliken

bae1f5 - Update README.md - Joshua Mulliken

a82438 - Delete feature_request.md - Joshua Mulliken

5397bf - Update hacs.json - Joshua Mulliken

b24a6c - Update issue templates (#45) - Joshua Mulliken

f96805 - Update README.md (#36) - davidking4411

8d9bbd - Update README.md - Joshua Mulliken

b471c6 - updated readme to add additional information - Joshua Mulliken

6fe837 - Add issue templates - Joshua Mulliken

b1c52c - Add how to report an issue information - Joshua Mulliken

38497e - Update readme for new confiruration instructions. - Mark Rickert

b2e4cf - Updated title - Joshua Mulliken

ef58b9 - Changed title in hacs.json - Joshua Mulliken

6b741e - Changed hacs.json - Joshua Mulliken

e65d5d - Added hacs.json - Joshua Mulliken

b3fbd8 - Added info.md so a description will show up in HACS - Joshua Mulliken

1bc728 - Update README.md - Joshua Mulliken

6ec619 - Updated README.md to reflect the new repo name - Joshua Mulliken

acb223 - Updated readme to inform of future coming changes - Joshua Mulliken

42b736 - Updated the readme - Joshua Mulliken

156170 - Updated readme and manifest to cover new addition of the wyze switch - Joshua Mulliken

16ccc3 - Update README.md - Joshua Mulliken

a2e7e9 - Update README.md - Joshua Mulliken

09bc8f - Update README.md - Joshua Mulliken

4eaece - Update README.md - Joshua Mulliken

d75419 - Update README.md - Joshua Mulliken

e6cf80 - Update README.md - Joshua Mulliken

ca324a - Update README.md - Joshua Mulliken


### Refactoring

48ca0b - Small changes - Joshua Mulliken

992983 - eefactor to reduce the amount of duplicate code and increase ability to fix bugs. - Joshua Mulliken

8d32e2 - Refactor (#74) - Joshua Mulliken

f695a6 - Update to remove deprecated references to Light and Switch - Joshua Mulliken

f4ad91 - Beginning work to convert the integration to async - Joshua Mulliken

2445b9 - Drop down to single threaded and begin work on implementing async - Joshua Mulliken

8d493a - Stripped authentication out of the individual platforms and into the init file for domain use. - Mark Rickert

d3b9f7 - Removed unneeded __init__.py file - Joshua Mulliken

a33ca3 - Added exceptions and testing as well as changed the application structure - Joshua Mulliken

a468cf - updated to remove the need to include a guid - Joshua Mulliken


### Features

d0be22 - Switch - Show extended params so that Wyze Cam Outdoor will have them - Yoinx

8dde1a - Lock - Display keypad battery if it is available - Yoinx

6d012d - Lock - Change the term "battery" to "lock battery" for clarity - Yoinx

b41089 - Lock Entity - Support showing battery status - Yoinx

4786c2 - Switch - Add battery status to the device info - Yoinx

f77a89 - scripts to allow for quick testing of ha-wyzeapi changes - Joshua Mulliken

58c38b - 2fa (#244)* Remove client.async_close as it is unnecessaryThis is unnecessary and throws errors after https://github.com/JoshuaMulliken/wyzeapy/pull/18/commits/ae6aaa196db5a7921c5172bef9ef304144d0ecd7* Initial 2fa supportThis is preliminary 2fa support. It depends on some of the changes in PR: https://github.com/JoshuaMulliken/wyzeapy/pull/18It still needs to implement a token callback so that it can save the changes when the token is refreshed. It also should have a title on the 2fa input screen.* 2fa: Enable storing an updated token via callbackGiven that Wyzeapy updates the token as necessary internally, we need to feed it a callback in order to store the updated tokens as it renews them so that we can actually login using the token when 2fa is enabled after a reboot/restart.* TokenManager: carry forward the username/passwordWe should probably go ahead and keep the existing username/password combination when we update the entry. Previously, it was clearing these values out during the token updates.* TokenManager: Add exception handle decorator to remove entryThis decorator should allow us to remove the wyzeapi entry when an AccessToken Error or LoginError occurs during a wyzeapy call.* Wrap wyzeapy calls with TokenManager exception decorator.This should wrap all the relevant calls with the decorator to catch errors with the token/login info.* TokenManager: Fix Error handler logicThis did not work as intended, now it does.However, this completely removes the entry for the integration so it will need to be re-installed after this happens. I'm not 100% sure that this is the most graceful way to handle this... but it also should never really happen.* Rework re-authentication to properly notify the user and reauthenticateThis should allow for users to be notified when something goes wrong and allow them re-authenticate.* chore: update version number, include latest beta wyzeapyCo-authored-by: Joshua Mulliken <joshua@mulliken.net> - Joe Schubert

59b7ef - Remove all devices that are not discovered on startup. - Joshua Mulliken

f1f2a6 - remove orphaned devices on startup - Joshua Mulliken

740a3e - Shorten the time to 200 milliseconds - Joshua Mulliken

f94810 - adds the ability to toggle global notifications - Joshua Mulliken

5c6482 - Wyzeapy upgrade (#206)* Refactored to use v0.1.0 of wyzeapy* Improve performance* Fix for all devices refresh the token* Fixes: #191* Fixes: #181* Fixes: #182* Fixes: #186* Wyze Rules are temporarily unavailable - Joshua Mulliken

2242ce - Update the dependency to stable and to include speedups - Joshua Mulliken

49f391 - Asyncify (#203) - Joshua Mulliken

0427d5 - Update to hopefully improve camera responsiveness - Joshua Mulliken

3d2124 - added_HVAC_ACTION (#193) - mlhfb

04f65e - Wyze home monitoring (#183) - Joshua Mulliken

47eae8 - Feature: Implements the Wyze Thermostat (#171)* feat: Implements the Wyze ThermostatImplements: [Feature Request] Wyze Thermostat issue #87Signed-off-by: Joshua Mulliken <joshua@mulliken.net> - Joshua Mulliken

d654db - Add russian translation (#169) - Sergey Morozik

1af3af - Added support for Wyze Rules to be available as Home Assistant Scenes. (#163) - faanskit

f8e2bc - Group entities by device and turn off and on cameras (#155)Implements the following user story:As a resident in the house, I want to be able to use a physical switchto turn on and turn off the cameras when I enter or leave the house sothat I can easily turn on and turn off camera supervision and feel safewhen I am away and private when I am homeSee Github Pull Request #153Signed-off-by: Joshua Mulliken <joshua@mulliken.net> - Joshua Mulliken

30901e - Add support for Wyze Locks with the ability to lock and unlock (#146) - Joshua Mulliken

206079 - Add per-platform scan interval. - Joshua Mulliken

dad184 - Add support for using cameras as motion sensors (#138) - Joshua Mulliken

06c3b9 - Merge pull request #129 - Joshua Mulliken

0f9d79 - Update client.py to add outdoor plug!! (#111) - Joshua Mulliken

2109e4 - Add logging for issue i've been dealing with - Joshua Mulliken

775ccf - Adding more logging - Joshua Mulliken

099d26 - Add default values to brightness and color temp - Joshua Mulliken

87efb0 - Add logging to failed post and recover commands - Joshua Mulliken

7e82d0 - Made change to explain to the user the issues with locks - Joshua Mulliken

f63bb3 - This adds support to see the Wyze Lock Status and the door status (#51)* Support for Contacts* Added support for Contacts and motion also added support for RSSI in Switch and Light* Added support for sensors to be an option* Optional Config for Sensors.Now you choose what you want to have. By default Sensors are False and Light and Switch are True. Also These are optional.Sample Configwyzeapi:  username: name@me.com  password: somepassword  sensors: true  light: true  switch: trueCo-authored-by: Allen Farmer <james.farmer@dormakaba.com> - jfarmer08

502245 - Support for Sensor polling (#47)* Support for ContactsAddded support for Contacts and motion also added support for RSSI in Switch and Light* Sync with main branch* Sync* Added support for sensors to be an optionAdded support for sensors to be an option* Add files via upload* Optional Config for Sensors.Now you choose what you want to have. By default Sensors are False and Light and Switch are True. Also These are optional.Sample Configwyzeapi:  username: name@me.com  password: somepassword  sensors: true  light: true  switch: true* Wrong Place* Add Support for OptionsNow you choose what you want to have. By default Sensors are False and Light and Switch are true. Also These are optional.Sample Configwyzeapi:  username: name@me.com  password: somepassword  sensors: true  light: true  switch: true* Polling updateSetting polling down to 10 secounds.* Update Readme* Code Clean up and Support for Sensor PollingAdded support for Sensor Polling at 5 secounds. Clean up logging. Add option to disable any device from showing in HA.* Added Support open Close State TimeAdded Support open Close State Time* Clean Up* Code Clean up* Code Clean up* Code Clean Up* Update wyze_sensor.py* Change Line EndingsCo-authored-by: Allen Farmer <james.farmer@dormakaba.com> - jfarmer08

5b7d94 - Support for Contacts (#46) - jfarmer08

d97dd5 - Update to use refresh token (#44) - Joshua Mulliken

92cacc - Updates to add more logging - Joshua Mulliken

752728 - More changes to add async more places - Joshua Mulliken

fe3ccd - Significant update to move everything into async world - Joshua Mulliken

41db33 - create the task instead of awaiting - Joshua Mulliken

907427 - Update for async - Joshua Mulliken

cd60ee - Added funtionality to check if a switch is online - Joshua Mulliken

77de4e - Made changes to light to attempt to detect if a bulb has lost connection to the server - Joshua Mulliken

a4647c - Made changes to log messages and set logging to debug for some messages - Joshua Mulliken

a834fc - Update debug log message and changed AccessToken error message to warning - Joshua Mulliken

cba22b - Changed request structure to improve performace and gracefully recover from errors - Joshua Mulliken

8e4e0e - No longer save to config file - Joshua Mulliken

189d58 - Added additional logging and interated the version number in the log to a stable - Joshua Mulliken

6b8c35 - Added logging to inform of AccessTokenErrors - Joshua Mulliken

5ba42b - Add integration for Wyze Plug as a swtich in HA - Joseph Yancey

49e94b - Updated to work better with alexas color temp range - Joshua Mulliken

c50d14 - Update to logging - Joshua Mulliken

f39a5b - Adding debug to main element - Joshua Mulliken

0af8f9 - Setting up logging to debug brightness and color temp - Joshua Mulliken

157f1d - Added multithreading to requests to speed up turning on and off bulbs - Joshua Mulliken

6acfbe - Added component - Joshua Mulliken


- - -
## 2021.9.6..2021.9.7b1 - 2021-09-26


### Miscellaneous Chores

f18328 - bump wyzeapy & version number - Joshua Mulliken