#!/bin/bash

accum_value=`gbase -Uuser _Ppwd -Dsid -H 10.10.10.1 -h -s -e "select count(*) from tab;"`

accum_value=`hive -S -e"set hive.cli.print.header=false;select * from accum_value limit 1;"|awk '{print $4}'`

echo ${accum_value}
