if [ $# -lt 1 ]; then
	echo 1>&2 "$0 [app.py]"
	exit 2
fi

export FLASK_ENV=development
export FLASK_DEBUG=1
python $1
