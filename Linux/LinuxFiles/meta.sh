# WiiX Meta.xml generator

read -p 'Name of your homebrew : ' nhbc
read -p 'Your author name :  ' ahbc
read -p 'Version : ' vhbc
read -p 'Description : ' dhbc

echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' >> meta.xml
echo '<app version="1">' >> meta.xml
echo '    <name>'$nhbc'</name>' >> meta.xml
echo '    <version>'$vhbc'</name>' >> meta.xml
echo '    <release_date>20210427150308</release_date>' >> meta.xml
echo '    <coder>'$ahbc'</coder>' >> meta.xml
echo '    <short_description>'$dhbc'</short_description>' >> meta.xml
echo '<long_description>'$nhbc' by '$ahbc'' >> meta.xml
echo '</long_description>' >> meta.xml
echo '<ahb_access/>' >> meta.xml
echo '</app>' >> meta.xml
echo "return with code 1"
 
