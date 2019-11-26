# CleanDesktop

Simple python3 script, that moves all your Desktop folder contents to ~/Documents/Desktop/dd.mm.yyyy

Works on linux and mac os

## How to use it

### Manual usage:

```
$ python3 clean.py
```

### Schedule task with Cron Job

```
$ sudo crontab -e
```
Then write and save
```
00 * * * * path/to/python path/to/clean.py
```
This means that the script will be executed every hour at 00 minute
For more examples visit [this site](https://www.adminschoice.com/crontab-quick-reference).

### Set as launch agent

- #### On linux:

1) copy this script to /bin:

```
$ sudo cp -i /path/to/clean.py /bin
```

2) add new Cron Job:

```
$ sudo crontab -e
```

3) scroll down, write and save

```
@reboot path/to/python /bin/clean.py &
```

- #### On mac OS

1) Go to ~/Library/LaunchAgents

2) create plist file com.gregoryandruschak.clean

3) open it and paste this code:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.gregoryandruschak.clean</string>
	<key>ProgramArguments</key>
	<array>
		<string>path/to/python</string> 
		<string>path/to/clean.py</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
```

#####  DON`T FORGET TO CHANGE PATH TO PYTHON AND CLEAN.PY

4) run terminal and type

```
$ launchctl load -w ~/Library/LaunchAgents/com.gregoryandruschak.clean.plist
```