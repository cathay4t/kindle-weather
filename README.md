Kindle Weather

# STOP, THIS WILL BRICK YOUR KINDLE, ONLY FOR LINUX GEEK.
# ~~UNLESS YOU KNOW ALL THE FOLLOWING LINUX COMMANDS, GO AWAY, THIS IS NOT FOR YOU.~~

# Big Thanks to Matthew Petroff for his sharing.

This project is fully based on the project shared by Matthew Petroff:
http://mpetroff.net/2012/09/kindle-weather-display/

Without his kind share of this great work, my kindle 3 might still sleep in the
dust.

The changes I made:
 * Use `crontab` instead of `kite` or stop `powerd` by changing the
   `suspend_levels`.

 * Reorganized the `weather_script.py` by spliting weather API out.

 * Change `weather-script-preprocess.svg` to fit the weather API.

 * I tried to change `weather-script-preprocess.svg` to use `<image>` tag
   for external image which allow me to easily change the icon, but I failed to
   at the rsvg-convert point. So still in embedded way.

# License

* The code is in MIT license.
* The `weather_script.py` file is based on the work of Matthew Petroff 2012, MIT
  license.
* The `weather-script-preprocess.svg` and its embedded icon are under
  [CC0 Public Domain Dedication][4] license by Matthew Petroff also. I(Gris Ge)
  did small change to fit the [weather.com][1] API.

# Pre-requirements

 * Kindle 3 wireless (Only tested on this one).
 * The API key from [weather.com][1]
 * [Kindle Jailbreak][2] and [USB network][3].
 * A kindle WIFI accessible Linux server with `python2 pngcrush librsvg2-tools`.

# HowTo
## Kindle Side

### Jailbreak your Kindle and install USB network.
 * The above wiki pages works on me. The tips would be disable wifi at the
   initial login, then change root password, change ssh config to allow wifi
   login, set as auto start, reboot.

### Allow cron running in suspend mode.
**Skip this if you have USB cable always connected to your kindle.**

 * Execute `mntroot rw`
 * Execute `vi /etc/kdb.src/luigi/system/daemon/powerd/suspend_levels`
 * Change the number at the last line to look like(no trailing \n):

    ```
    RG002
    40
     0x4C0 (fw at 10, cmd 7, wan/wifi 6)
    <DATA>
    1152
    ```

 * The `1152` here means the 7th bit(start from 0) as 0 which allows crontab
   in suspend mode. This is purely based on my guess, but it works. :)

### Install weather display script
 * Edit the `URL` in `display-weather.sh` by pointing to your own http server.
 * Create folder `mkdir /mnt/base-us/weather`.
 * Make sure kindle root mount point is writeable `mntroot rw`
 * `scp display-weather.sh root@k3w:/usr/bin/`
 * Make sure `display-weather.sh` is executable via `chmod +x` on kindle.

### Setup crontab
 * Execute `mntroot rw`.
 * Add this line into `/etc/crontab/root`

    ```
*/60 6-22 * * * /usr/bin/display-weather.sh
    ```
 * This means weather report will be refreshed hourly during 6AM to 10PM.

### Reboot your kindle via `reboot` command.

## Server Side
### Install httpd daemon.
 * `sudo yum install httpd pngcrush librsvg2-tools python2 -y`
 * `sudo systemctl enable httpd`
 * `sudo systemctl start httpd`

### Create weather output folder with correct permission.
 * `sudo mkdir /var/www/html/weather`
 * `sudo chmod 777 /var/www/html/weather/` or use `chown`.

### Setup crontab
 * Add this line to `crontab -e` to refresh weather every 29 minutes during
   6AM to 10PM:
```
*/29 6-22 * * * <PATH>/weather_script.py <API_KEY> <LAT> <LON>
```
 * Change `<PATH>` as the folder of source code.
 * Change `<API_KEY>` as the [weather.com][1] API key strin.
 * Change `<LAT>` and `<LON>` as latitude and lontitude of your city.

### Create initial weather PNG
 * Invoke `<PATH>/weather_script.py <API_KEY> <LAT> <LON>`.
 * Check whether you can get the weather png via:
    `http://<your_server_hostname>/weather/weather.png`

# TODO
 * Include AQI(air quality index)

# Contact
 * https://github.com/cathay4t/kindle-weather/issues

[1]: http://www.wunderground.com/weather/api/d/login.html
[2]: http://wiki.mobileread.com/wiki/Kindle_Hacks_Information
[3]: https://blitiri.com.ar/p/other/kindle/#usb-networking
[4]: http://creativecommons.org/publicdomain/zero/1.0/
