#!/bin/bash
DIR=""
FILE=""
COMPIL=""
RUN=""
FLAG=""
while [ -n "$1" ]
do
case "$1" in
-d) param="$2"
DIR=$param
shift ;;
-f) param="$2"
FILE=$param
shift ;;
-c) COMPIL="true" ;;
-r) RUN="true" ;;
*) echo "$1 is not an option" ;;
esac
shift ;done
if [[ "$DIR" != "" ]]; then
	ls $DIR
	fi
if [[ "$FILE" != "" ]]; then
  cat $FILE
	if [[ "$COMPIL" == "true" ]]; then
	  gcc -Wall -o $FILE.o $FILE ;
	if [[ "$?" -ne 0 ]] ;
		then
	echo "No comp"
	exit 0
	fi

	if [[ "$RUN" == "true" ]]; then
		 [ -f "$FILE" ] && ./$FILE.o ;
	fi
fi
else cat ~/.bashrc ;
fi
