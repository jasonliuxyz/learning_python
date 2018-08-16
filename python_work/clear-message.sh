#!/bin/bash
# -----------------------------------------------------------------------------------------
# Usage: ./clear-old-message.sh
# Description: This script can be used to delete the older libmessage.so and umessage.desc
#		which are no longer used (the version is 20 older than the current version).
#		  For example, if the current version is 1.0.183, all the versions (no longer used)
#		older than 1.0.163 will be deleted.
# -----------------------------------------------------------------------------------------

# libmessage static white list
whitelist_file=/tmp/libmessage_static_whitelist
static_whitelist="
/root/wiwo/libs/libmessage.so.1.0.108
/root/wiwo/libs/libmessage.so.1.0.153
/root/wiwo/libs/libmessage.so.1.0.162
/root/wiwo/libs/libmessage.so.1.0.167
/root/wiwo/libs/libmessage.so.1.0.175
/root/wiwo/libs/libmessage.so.1.0.189
/root/wiwo/libs/libmessage.so.1.0.192
/root/wiwo/libs/libmessage.so.1.0.196
/root/wiwo/libs/libmessage.so.1.0.217
/root/wiwo/libs/libmessage.so.1.0.230
/root/wiwo/libs/libmessage.so.1.0.90
/root/wiwo/libs/libmessage.so.1.0.87
/root/wiwo/libs/libmessage.so.1.0.44
/root/wiwo/libs/libmessage.so.1.0.140
"

> /tmp/libmessage_static_whitelist
for x in $static_whitelist;
do
        echo $x >> $whitelist_file
done

# install lsof
LSOF_INSTALL=$(whereis lsof | cut -d':' -f2 | wc -w)
if [ $LSOF_INSTALL -eq 0 ]; then
	yum clean all
	yum makecache
	yum -y install lsof
fi
echo "lsof has been installed"

# generate the boundary messages to be deleted
VERSION=$(readlink -m /root/wiwo/libs/libmessage.so | cut -d'.' -f5)
BOUNDARY_VERSION=$[$VERSION - 20]

# clear old libmessage.so
BOUNDARY_MESSAGE=/root/wiwo/libs/libmessage.so.1.0.$BOUNDARY_VERSION
echo "the libmessage.so older than libmessage.so.1.0.$BOUNDARY_VERSION will be deleted"
for item in /root/wiwo/libs/libmessage.so.1.0.*
do
	echo $item
	item_version=$(eval echo $item | cut -d'.' -f5)
#	if [ $item_version -eq 87 ] || [ $item_version -eq 140 ] || [ $item_version -eq 44 ]; then	# for udisk/umem
	if grep $item  $whitelist_file; then	
		continue
	fi
	if [ $item_version -lt $BOUNDARY_VERSION ]; then
		USED=$(eval lsof $item | wc -l)
		if [ $USED -eq 0 ]; then
			rm -f $item
			echo "delete $item"
		fi
	fi
done

# clear old umessage.desc
BOUNDARY_DESC=/root/wiwo/libs/umessage.desc.1.0.$BOUNDARY_VERSION
echo "the umessage.desc older than umessage.desc.1.0.$BOUNDARY_VERSION will be deleted"
for item in /root/wiwo/libs/umessage.desc.1.0.*
do
	echo $item
	item_version=$(eval echo $item | cut -d'.' -f5)
	if [ $item_version -lt $BOUNDARY_VERSION ]; then
		USED=$(eval lsof $item | wc -l)
		if [ $USED -eq 0 ]; then
			rm -f $item
			echo "delete $item"
		fi
	fi
done


# 删除超过七天的库文件备份

find /root/wiwo/libs/  -maxdepth 1  -type d -name "201*" -mtime +1 -exec rm -rfv {} \;