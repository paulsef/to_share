#!/bin/sh
"""
For loops in unix!? I had no idea! This simple script
uses some command substituations and aliases to extract
a product id and generate some amazon urls
"""

set -e

parse_products() 
{
	for name in $(cat $SPRINT_DIR/data/products/video_filenames.txt)
	do
		rm urls_list.txt	
		url="www.amazon.com/dp/$(grep 'ASIN: ' $SPRINT_DIR/data/products/$name  | cut -f 2 -d ' ')"

		echo $url >> urls_list.txt

	done

}

parse_products
